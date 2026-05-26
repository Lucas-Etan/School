## 飞书 Channel 验证

- OC-DeepSeek-<STUDENT_ID> 应用名称与 App ID 后四位：OC-DeepSeek-2410311401 / cli_aa...9cc5

- OC-Qwen-<STUDENT_ID> 应用名称与 App ID 后四位：OC-Qwen-2410311401 / cli_aa...9cc3

- Hermes-DeepSeek-<STUDENT_ID> 应用名称与 App ID 后四位：Hermes-DeepSeek-2410311401 / cli_aa...dcc6

- Hermes-Qwen-<STUDENT_ID> 应用名称与 App ID 后四位：Hermes-Qwen-2410311401 / cli_aa...85cb6

- OpenClaw Channel 名称：feishu

- Hermes Gateway 名称或状态：exp4deepseek / exp4qwen，状态 running

- 连接模式：websocket

- 已申请权限：im:message:send_as_bot, im:message.p2p_msg:readonly, im:message.group_at_msg:readonly

- 是否完成版本发布：是

- 测试群 chat_id 来源：Gateway 日志 / 群链接提取

- OC-DeepSeek-<STUDENT_ID> 私聊用户 open_id 是否已加入对应 allowFrom：是

- OC-Qwen-<STUDENT_ID> 私聊用户 open_id 是否已加入对应 allowFrom：是

- OpenClaw 测试群 groups 是否设置 requireMention 与群内 allowFrom：是

- OpenClaw 如出现 not in groupAllowFrom，测试群 chat_id 是否也已写入 groupAllowFrom：是

- Hermes-DeepSeek-<STUDENT_ID> pairing 是否已批准或写入 FEISHU_ALLOWED_USERS：是

- Hermes-Qwen-<STUDENT_ID> pairing 是否已批准或写入 FEISHU_ALLOWED_USERS：是

- Hermes 是否设置 FEISHU_GROUP_POLICY=disabled 或等价 default_group_policy: disabled：是

- 测试群外是否默认不响应：是（groupPolicy: allowlist，仅白名单群可响应）

- OpenClaw 测试消息是否抵达网关：是（日志显示 received message 和 dispatch complete）

- Hermes 测试消息是否抵达 Gateway：是（日志显示 Connected 并处理消息）

- 日志中的连接状态：feishu connected / Lark: connected to wss://msg-frontier.feishu.cn/ws/v2

- 是否使用四个机器人：是（OC-DeepSeek、OC-Qwen、Hermes-DeepSeek、Hermes-Qwen）

- 敏感字段来源与占位符处理说明：App ID/App Secret 来自飞书开放平台「凭证与基础信息」，已写入本机 .env 文件；共享配置中使用 <FEISHU_OC_DEEPSEEK_APP_ID> 等占位符；open_id 和 chat_id 从 Gateway 日志中获取，配置中使用真实值；API Key 已写入本机环境变量，共享配置中使用 <DEEPSEEK_API_KEY> 占位符
