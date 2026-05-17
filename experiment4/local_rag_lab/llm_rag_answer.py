import json
import os
import urllib.error
import urllib.request

from chroma_vector_db import search_chroma_db
from governed_rag import detect_conflicts, format_citation


SYSTEM_PROMPT = """你是一个严格基于资料回答的 RAG 助手。
你只能依据 <context> 中的资料回答。
如果资料不足，请明确说“资料中没有足够依据”。
回答必须保留方括号中的引用编号，例如 [genshin_basics_v1#c002]。
如果系统提示存在过期或冲突资料，不要给出唯一确定结论。
回答应简洁，最多 5 条要点，每条不要超过 60 字。"""


def build_context(chunks: list[dict]) -> str:
    """把已通过权限和时效过滤的检索片段整理成模型上下文。"""
    lines = []
    for chunk in chunks:
        meta = chunk["metadata"]
        status = "已过期" if chunk["expired"] else "有效"
        lines.append(
            f"[{chunk['chunk_id']}] "
            f"标题：{meta['title']}；来源：{meta['source']}；"
            f"更新时间：{meta['updated_at']}；状态：{status}；"
            f"内容：{chunk['text']}"
        )
    return "\n".join(lines)


def build_warnings(chunks: list[dict]) -> list[str]:
    """根据检索结果生成工程告警，提醒模型不要忽略过期或冲突资料。"""
    warnings = []
    if any(chunk["expired"] for chunk in chunks):
        warnings.append("检索结果包含过期资料，请优先参考未过期来源。")

    conflicts = detect_conflicts(chunks)
    if conflicts:
        warnings.append(f"检测到冲突内容：{conflicts}，需要人工确认。")

    return warnings


def qwen_config() -> dict:
    """读取本地 Qwen 的连接参数，模型名称可通过环境变量切换。"""
    return {
        "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        "model": os.getenv("QWEN_MODEL", "qwen3.6:35b-a3b"),
        "max_tokens": int(os.getenv("QWEN_MAX_TOKENS", "1024")),
    }


def ollama_chat_url(base_url: str) -> str:
    """把可能带 /v1 的地址统一转换成 Ollama 原生 chat 地址。"""
    root = base_url.rstrip("/")
    if root.endswith("/v1"):
        root = root[:-3]
    return f"{root}/api/chat"


def call_qwen(messages: list[dict]) -> str:
    """通过 Ollama 原生 chat 接口调用本地 Qwen，并关闭隐藏思考模式。"""
    config = qwen_config()
    payload = {
        "model": config["model"],
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0.2,
            "num_predict": config["max_tokens"],
        },
    }
    request = urllib.request.Request(
        ollama_chat_url(config["base_url"]),
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"无法连接 Ollama：{exc}") from exc

    if data.get("done_reason") == "length":
        raise RuntimeError(
            "Qwen 输出被 token 上限截断。"
            "请调大 QWEN_MAX_TOKENS，例如设置为 2048 或 4096。"
        )

    message = data.get("message", {})
    answer = (message.get("content") or "").strip()
    if answer:
        return answer

    raise RuntimeError("Qwen 返回了空答案，请检查模型状态和提示词。")


def answer_with_qwen(
    question: str,
    role: str = "student",
    include_expired: bool = False,
) -> dict:
    """先执行 RAG 检索治理，再把可访问上下文交给本地 Qwen 生成。"""
    # 检索层先完成权限、过期过滤和 Top-K 召回，模型不会看到未授权片段。
    chunks = search_chroma_db(
        question=question,
        role=role,
        top_k=5,
        include_expired=include_expired,
    )

    if not chunks:
        return {
            "answer": "资料中没有找到足够依据，无法回答该问题。",
            "citations": [],
            "warnings": [],
            "grounded": False,
        }

    warnings = build_warnings(chunks)
    context = build_context(chunks)
    # 模型输入只包含已经筛选过的上下文和告警，不把整个资料库塞给模型。
    user_prompt = (
        f"<context>\n{context}\n</context>\n\n"
        f"系统提示：{'；'.join(warnings) if warnings else '无'}\n"
        f"用户问题：{question}"
    )

    answer = call_qwen(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    return {
        "answer": answer,
        "citations": [format_citation(chunk) for chunk in chunks],
        "warnings": warnings,
        "grounded": True,
    }