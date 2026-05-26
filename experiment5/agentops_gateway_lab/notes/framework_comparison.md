## OpenClaw 与 Hermes 优缺点对比

### 多模型路由网关的课堂样例：OpenClaw 更合适

OpenClaw 采用单一配置文件（openclaw.json），Provider、Agent、Channel、bindings 结构清晰直观。学生可以通过修改 JSON 文件直接观察路由规则如何将不同飞书账号的消息分发到不同 Agent。配置即代码的理念便于课堂讲解和版本对比。而 Hermes 的 profile 隔离机制虽然更强大，但学习曲线较陡，不适合作为入门路由样例。

### 长期运行 Agent、记忆、Skill 和 MCP：Hermes 更合适

Hermes 原生支持长期记忆（memories/ 目录）、Skill 文件系统、MCP 工具扩展和跨会话上下文保持。Agent 可以记住历史对话并持续改进。OpenClaw 更侧重消息路由和模型调用，记忆能力较弱。对于需要演示“Agent 如何成长”的场景，Hermes 更有优势。

### 规则 Router vs LLM Router

规则 Router 基于固定规则（如飞书账号绑定、前缀匹配），稳定可解释，适合权限收敛和稳定分流。LLM Router 根据自然语言意图输出结构化编排计划，适合复合指令和多 Agent 协作。本章在 OpenClaw bindings 中观察规则 Router，在 Hermes-DeepSeek 的 JSON 输出中观察 LLM Router。

### 避免双响应

使用四个不同飞书机器人，每个框架接入不同机器人。OpenClaw 接入 OC-DeepSeek 和 OC-Qwen，Hermes 接入 Hermes-DeepSeek 和 Hermes-Qwen。同一消息只被一个机器人接收，从根本上避免双响应。

### 保留建议

我会保留 OpenClaw。理由：配置结构更清晰，路由机制直观，适合作为 AgentOps 入门框架。后续章节可在其基础上扩展工具和记忆能力，或引入 Hermes 作为对比。