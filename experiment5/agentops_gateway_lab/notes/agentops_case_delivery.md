## 实验 4 作业初筛与风险检查助手

- 回放日期：2026-05-26
- 临时输出目录：/tmp/exp4-agentops-case.Q6Mqrk
- LLM Router 输出文件：router.json（已成功生成完整 JSON）
- OC-DeepSeek-2410311401 检查结果摘要：生成了包含 10 项通过项、6 项风险项、7 项建议补证项的检查清单
- OC-Qwen-2410311401 反馈结果摘要：生成了学生补交作业反馈模板
- Hermes-Qwen-2410311401 安全复核摘要：生成了包含 6 项检查的安全复核清单
- 最终报告文件：final_report.md
- 是否发现真实密钥、chat_id、open_id 或 <think> 标签：未发现

| 步骤 | 智能体               | 框架     | 模型              | Skill              | 结果 | 耗时 | 备注                |
| ---- | -------------------- | -------- | ----------------- | ------------------ | ---- | ---- | ------------------- |
| 1    | hermes-exp4-deepseek | Hermes   | deepseek-v4-flash | exp4-task-planning | 成功 | ~5s  | JSON 编排计划已生成 |
| 2    | exp4-deepseek        | OpenClaw | deepseek-v4-flash | exp4-code-review   | 成功 | ~42s | 生成完整检查清单    |
| 3    | exp4-qwen            | OpenClaw | qwen2.5:7b-64k    | exp4-local-explain | 成功 | ~67s | 生成学生反馈模板    |
| 4    | hermes-exp4-qwen     | Hermes   | qwen2.5:7b-64k    | exp4-safety-review | 成功 | ~62s | 生成安全复核清单    |
| 5    | hermes-exp4-deepseek | Hermes   | deepseek-v4-flash | exp4-task-planning | 成功 | -    | 最终报告汇总        |

## 最终报告结构

- 提交完整性：四个智能体均已输出角色化内容
- 双 Gateway 检查：OpenClaw Gateway running，Hermes Gateway running
- 四机器人与飞书检查：四个飞书机器人均已接入测试群，群聊@测试通过
- 本地 Qwen/no-thinking 检查：使用 qwen2.5:7b-64k，已配置 /no_think 前缀
- Router/LLM Router 编排证据：Hermes-DeepSeek 输出 JSON 编排计划
- 安全与隐私风险：已配置 allowlist、groupPolicy，未发现敏感信息泄露
- 需要补交的问题：无
- 授课老师验收摘要：
