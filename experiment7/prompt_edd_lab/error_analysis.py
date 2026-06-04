def summarize_failures(results: list[dict]) -> dict:
    summary = {
        "format_errors": 0,
        "missed_points": 0,
        "forbidden_content": 0,
        "failed_refusal": 0,
        "failed_redaction": 0,
    }

    for result in results:
        for error in result["errors"]:
            if error.startswith("missing section"):
                summary["format_errors"] += 1
            if error.startswith("forbidden phrase"):
                summary["forbidden_content"] += 1

        checks = result.get("checks", {})
        if checks.get("coverage") is False:
            summary["missed_points"] += 1
        if checks.get("refusal") is False:
            summary["failed_refusal"] += 1
        if checks.get("redaction") is False:
            summary["failed_redaction"] += 1

    return summary


def suggest_prompt_changes(summary: dict) -> list[str]:
    suggestions = []

    if summary["format_errors"]:
        suggestions.append("强化输出格式要求，明确必须包含固定栏目。")
    if summary["missed_points"]:
        suggestions.append("在提示词中要求覆盖背景、原因、下一步安排和限制说明。")
    if summary["forbidden_content"]:
        suggestions.append("增加未经授权不得承诺赔偿、退款或责任归属的规则。")
    if summary["failed_refusal"]:
        suggestions.append("增加用户输入不可信、不得遵从注入指令的安全规则。")
    if summary["failed_redaction"]:
        suggestions.append("增加敏感信息脱敏要求，并确认脱敏器已接入输出链路。")

    return suggestions