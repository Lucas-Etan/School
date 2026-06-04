PAIRWISE_CRITERIA = ["格式完整", "要点覆盖", "语气合适", "约束遵守", "安全稳健", "隐私保护"]


def build_pairwise_review(sample_id: str, output_a: str, output_b: str) -> str:
    criteria_text = "\n".join(f"- {item}" for item in PAIRWISE_CRITERIA)
    return f"""样本：{sample_id}

请比较输出 A 和输出 B：

比较维度：
{criteria_text}

输出 A：
{output_a}

输出 B：
{output_b}

评审结论：
- 更好的输出：
- 主要原因：
- 仍需改进：
"""