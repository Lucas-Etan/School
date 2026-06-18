import json
import tools
from datetime import datetime
from pathlib import Path
from typing import Any

from policy import ALLOWED_EXTENSIONS, ALLOWED_TOOLS, AUDIT_LOG, LOG_DIR, MAX_WRITE_CHARS, WORKSPACE_DIR


class HarnessError(Exception):
    """Harness 校验失败时抛出的自定义异常。"""

    pass


def resolve_workspace_path(path_str: str) -> Path:
    """将 Agent 提供的相对路径解析为 workspace 内的安全绝对路径。"""

    candidate = (WORKSPACE_DIR / path_str).resolve()

    try:
        candidate.relative_to(WORKSPACE_DIR)
    except ValueError:
        raise HarnessError(f"路径越界：{path_str}")

    if candidate.suffix and candidate.suffix not in ALLOWED_EXTENSIONS:
        raise HarnessError(f"不允许的文件类型：{candidate.suffix}")

    return candidate

def audit(event: dict[str, Any]) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    event["time"] = datetime.now().isoformat(timespec="seconds")
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def validate_request(request: dict[str, Any]) -> None:
    if not isinstance(request, dict):
        raise HarnessError("工具请求必须是字典")

    tool_name = request.get("tool")
    if tool_name not in ALLOWED_TOOLS:
        raise HarnessError(f"工具未授权：{tool_name}")

    path = request.get("path")
    if not isinstance(path, str) or not path.strip():
        raise HarnessError("path 参数必须是非空字符串")

    content = request.get("content", "")

    if tool_name in {"write_text", "append_text"}:
        if "content" not in request:
            raise HarnessError(f"{tool_name} 缺少 content 参数")
        if not isinstance(content, str):
            raise HarnessError("content 参数必须是字符串")

    if tool_name in {"read_text", "list_files"} and content:
        raise HarnessError(f"{tool_name} 不应包含 content 参数")

    if content and len(content) > MAX_WRITE_CHARS:
        raise HarnessError("写入内容过长")


def run_tool(request: dict[str, Any]) -> dict[str, Any]:
    try:
        validate_request(request)
        tool_name = request["tool"]
        path = resolve_workspace_path(request["path"])
        content = request.get("content", "")

        if tool_name == "read_text":
            result = tools.read_text(path)
        elif tool_name == "write_text":
            result = tools.write_text(path, content)
        elif tool_name == "append_text":
            result = tools.append_text(path, content)
        elif tool_name == "list_files":
            result = tools.list_files(path)
        else:
            raise HarnessError(f"工具未实现：{tool_name}")

        response = {"ok": True, "result": result, "error": None}
        audit({"request": request, "response": response})
        return response

    except Exception as e:
        response = {"ok": False, "result": None, "error": str(e)}
        audit({"request": request, "response": response})
        return response


def build_feedback(response: dict[str, Any]) -> str:
    if response["ok"]:
        return f"工具执行成功，结果为：{response['result']}"
    return f"工具执行失败，原因：{response['error']}。请修改工具名或参数后重试。"