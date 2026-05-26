## Hermes 基础检查

- 安装方式：Linux
- Hermes 版本：v0.14.0 (2026.5.16)
- `hermes doctor` 结果：Found 1 issue(s) to address:

1. Run 'hermes setup' to configure missing API keys for full tool access

- 模型 Provider：custom
- 模型名或 Custom endpoint：http://localhost:11434/v1
- CLI 对话是否成功：是
- 配置目录或数据目录：/home/lucas/.hermes
- 遇到的问题：无

## Hermes Gateway 与安全观察

- Gateway 向导中看到的平台：feishu（飞书）、discord、telegram、slack、whatsapp、teams 等，本章仅启用 feishu

- 飞书是否已配置成功：是，两个 profile（exp4deepseek 和 exp4qwen）均已成功连接飞书 WebSocket，群聊 @ 机器人能正常回复

- hermes-exp4-deepseek CLI 验证：
  命令：exp4deepseek chat -q "只回复一句：Hermes 命名 provider exp4-deepseek 已经跑通。" -Q --provider custom -m deepseek-v4-flash --max-turns 2 --ignore-rules
  结果：成功，输出 "Hermes 命名 provider exp4-deepseek 已经跑通。"

- hermes-exp4-qwen CLI 验证：
  命令：exp4qwen chat -q "/no_think\n 只回复一句：Hermes 命名 provider exp4-ollama-qwen36 已经跑通。" -Q --provider custom -m qwen2.5:7b-64k --max-turns 2 --ignore-rules
  结果：成功，输出 "Hermes 命名 provider exp4-ollama-qwen36 已经跑通。"

- hermes-exp4-deepseek 飞书验证：
  测试消息：@Hermes-DeepSeek-2410311401 请只回复一句：hermes-exp4-deepseek 飞书入口已跑通。
  结果：成功收到回复

- hermes-exp4-qwen 飞书验证：
  测试消息：@Hermes-Qwen-2410311401 /no_think 请不要展开推理，只回复一句：hermes-exp4-qwen 飞书入口已跑通。
  结果：成功收到回复，无推理过程输出

- 工具配置入口：hermes tools 可查看当前启用的工具集，包括 hermes-cli、文件操作、代码执行等

- 是否看到命令审批或安全提示：是，当 Agent 尝试执行敏感操作（如写文件到其他 profile 目录）时，Hermes 会显示安全警告。例如：Cross-profile write blocked by soft guard。需要用户确认或修改配置才能继续。

- Router/Orchestrator 观察：Hermes 通过不同 profile 实现入口分离，exp4deepseek 负责任务规划与编排，exp4qwen 负责安全复核。复合指令可以先由 exp4deepseek 输出 JSON 编排计划，再由人工或自动化工具调用其他 profile 执行。相比 OpenClaw 的 bindings 路由，Hermes 的 profile 更强调独立运行入口。

- 复合指令如何拆给两个 profile：

  1. exp4deepseek 接收复合指令，输出结构化 JSON 编排计划
  2. 计划中包含需要安全复核的子任务，标记 review_agent: exp4qwen
  3. 人工或脚本调用 exp4qwen 执行安全复核
  4. 结果返回 exp4deepseek 进行最终汇总

- 记忆/Skill/配置目录：

  - 记忆文件：~/.hermes/profiles/exp4deepseek/memories/、~/.hermes/profiles/exp4qwen/memories/
  - Skill 文件：~/.hermes/profiles/exp4deepseek/skills/domain/exp4-task-planning/SKILL.md
  - 配置目录：~/.hermes/profiles/exp4deepseek/config.yaml、~/.hermes/profiles/exp4qwen/config.yaml
  - .env 文件：~/.hermes/profiles/exp4deepseek/.env、~/.hermes/profiles/exp4qwen/.env

- 与 OpenClaw 最大的体验差异：

  - OpenClaw：单一配置文件（openclaw.json），通过 bindings 实现路由，适合显式配置和批量管理
  - Hermes：profile 隔离，每个 profile 有独立配置、环境变量、记忆和 Skill，适合多租户或多种角色隔离
  - Hermes 内置安全审批机制（如跨 profile 写入拦截），OpenClaw 主要依赖 allowlist 和 groupPolicy

- 当前课堂环境下不适合启用的能力：
  - 子 Agent 并行执行（delegation）：需要更复杂的任务队列和状态管理
  - MCP 外部工具扩展：本章未配置 MCP 服务，留待后续章节
  - Gateway 多平台同时接入（Telegram、Slack 等）：避免配置混乱，集中验证飞书
  - 长期运行的生产级 Agent：本章仅验证基础链路，不涉及高可用部署
