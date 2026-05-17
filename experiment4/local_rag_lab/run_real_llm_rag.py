from chroma_vector_db import build_chroma_store
from llm_rag_answer import answer_with_qwen
from student_info import print_student_id

print_student_id()

QUESTIONS = [
    "原石、祈愿和角色养成有什么关系？",
    "课堂讲角色养成时有什么建议？",
    "原粹树脂应该优先做什么？",
]


def run_case(question: str, include_expired: bool = False) -> None:
    """运行一次真实模型 RAG 问答，并打印回答、引用和告警。"""
    print("=" * 80)
    print("question:", question)
    try:
        result = answer_with_qwen(
            question=question,
            role="student",
            include_expired=include_expired,
        )
    except Exception as exc:
        print("qwen_skipped_or_failed:", exc)
        return

    print(result["answer"])
    print("citations:", result["citations"])
    print("warnings:", result["warnings"])


build_chroma_store()

run_case(QUESTIONS[0])
run_case(QUESTIONS[1])
run_case(QUESTIONS[2], include_expired=True)