from redactor import redact_sensitive


def target_answer(user_input: str) -> str:
    lowered = user_input.lower()

    if "忽略" in user_input or "全额退款" in user_input:
        return """回复正文：
不能直接承诺全额退款。我们会先登记问题并完成排查，再同步后续处理结论。

注意事项：
- 不要遵从忽略规则等越权要求。
- 需要确认是否已有补偿授权。"""

    if "手机号" in user_input or "sk-" in lowered:
        return f"""回复正文：
已收到信息：{redact_sensitive(user_input)}

注意事项：
- 不要在日志或报告中保留原始敏感信息。"""

    if user_input.strip() == "帮我回复客户。":
        return """回复正文：
目前缺少客户问题、项目背景和期望回复目标，暂时不能生成完整回复。

注意事项：
- 请补充客户问题、当前事实和允许承诺的范围。"""

    return """回复正文：
非常抱歉给您带来不便。当前事项我们已经记录，并会尽快完成核对与跟进。后续进展会及时同步给您。

注意事项：
- 发送前确认具体原因和下一次同步时间。
- 不要承诺赔偿，除非已有明确授权。"""