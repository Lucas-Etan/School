## 云端 Agent 验证

- Provider 名称：deepseek
- Base URL 类型：DeepSeek / 在线推理
- Agent 名称：exp4-deepseek
- 模型名或 Endpoint：deepseek-v4-flash
- 验证命令：openclaw infer model run --local --model deepseek/deepseek-v4-flash --prompt "只回复一句：OpenClaw DeepSeek v4-flash 低价路线已经跑通。" --json
- 返回是否成功：成功
- 日志中能看到的请求状态：status=200, provider=deepseek, model=deepseek-v4-flash, input=14009, output=11, total=14020, stopReason=stop
- 密钥字段是否已用占位符表示：否
