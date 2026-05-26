## Router 端到端验收

| 测试消息 | 预期 Agent | 是否命中 | 是否回复 | 观察到的日志 | 备注 |
| --- | --- | --- | --- | --- | --- |
| @OC-DeepSeek-2410311401 /code 用 Java 写一个线程安全的单例模式 | exp4-deepseek | 是 | 是 | 日志显示 dispatching to agent，provider=deepseek，model=deepseek-v4-flash | 云端 Agent 响应，输出了完整的代码示例和适用场景说明 |
| @OC-Qwen-2410311401 /chat 用 30 个字解释为什么 RAG 系统需要资料外拒答 | exp4-qwen | 是 | 是 | 日志显示 provider=ollama，model=qwen2.5:7b-64k，/no_think 已生效 | 本地 Agent 响应，输出简洁（30字左右） |
| 复合指令：规划 + 权限复核 + 配置复盘 | LLM Router -> 多 Agent | 是 | 是 | hermes-exp4-deepseek 输出 JSON 编排计划，包含 intent、execution_mode、agents、safety_gate | LLM Router 成功输出结构化计划，包含安全复核门禁 |

## 对比观察

- 云端 Agent 响应特点：
  - 响应速度快（约 3-5 秒）
  - 输出内容丰富详细（代码示例 + 表格说明 + 适用场景）
  - 使用 deepseek-v4-flash 模型
  - 能够完整回答技术问题

- 本地 Agent 响应特点：
  - 响应速度较慢（约 60-90 秒）
  - 输出简洁（严格控制在 30 字左右）
  - 使用 qwen2.5:7b-64k 本地模型
  - 响应符合指令要求，无多余推理过程

- LLM Router 输出的 Agent 顺序：
  1. hermes-exp4-deepseek（双 gateway 审查）
  2. exp4-deepseek（DeepSeek 与本地 Qwen 部署核查）
  3. exp4-qwen（Router/LLM Router 证据收集）
  4. hermes-exp4-qwen（权限与脱敏证据审查）

- LLM Router 是否需要人工确认：是，当 confidence 低于阈值或缺少关键信息时应反问

- 路由误配或未命中的表现：
  - 日志中出现 "not in allowFrom" 或 "not in groupAllowFrom"
  - 机器人无回复或回复错误内容
  - 可通过检查 bindings 配置和 allowlist 修复

- 需要改进的地方：
  - allowInsecureAuth=true 建议关闭
  - BOOTSTRAP.md 等模板文件建议清理