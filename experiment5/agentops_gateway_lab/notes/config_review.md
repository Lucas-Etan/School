## 配置复盘

1. 本机实际配置文件路径是什么？
   - OpenClaw 主配置：~/.openclaw/openclaw.json
   - OpenClaw 工作区：~/.openclaw/workspace/、~/.openclaw/workspace-exp4-deepseek/、~/.openclaw/workspace-exp4-qwen/
   - Hermes exp4deepseek 配置：~/.hermes/profiles/exp4deepseek/config.yaml
   - Hermes exp4deepseek 环境变量：~/.hermes/profiles/exp4deepseek/.env
   - Hermes exp4qwen 配置：~/.hermes/profiles/exp4qwen/config.yaml
   - Hermes exp4qwen 环境变量：~/.hermes/profiles/exp4qwen/.env
   - 系统服务文件：~/.config/systemd/user/openclaw-gateway.service

2. OpenClaw 中 Provider、Agent、Channel、Router 分别出现在配置文件的哪个位置？
   - Provider：位于 models.providers 对象中，例如 deepseek 和 ollama provider
   - Agent：位于 agents.list 数组中，包含 id、name、workspace、model 等字段
   - Channel：位于 channels.feishu 对象中，包含 enabled、connectionMode、accounts 等配置
   - Router：位于 bindings 数组中，通过 type: "route"、agentId、match 字段定义路由规则

3. 哪些字段属于敏感信息？
   - API Key：models.providers.*.apiKey（如 DEEPSEEK_API_KEY）
   - App Secret：channels.feishu.accounts.*.appSecret
   - App ID：channels.feishu.accounts.*.appId（可部分脱敏，保留后4位）
   - open_id：allowFrom 数组中的 ou_ 开头的用户标识
   - chat_id：groupAllowFrom 和 groups 中的 oc_ 开头的群标识
   - Token：gateway.auth.token（如当前配置中的 15c0ae0e...）

4. 如果要把这套网关迁移到另一台机器，哪些配置可以复制，哪些必须重新申请？
   可以复制（需脱敏后）：
   - Provider 和 Agent 的结构定义（不含 apiKey）
   - Channel 的 accounts 结构（不含 appSecret）
   - bindings 路由规则
   - groups 和 groupPolicy 配置
   - Skill 和角色提示词文件

   必须重新申请：
   - DeepSeek API Key（从 DeepSeek 控制台重新获取）
   - 飞书 App ID 和 App Secret（从飞书开放平台重新创建应用）
   - 新机器的 open_id 和 chat_id（在新环境下重新获取）
   - Gateway 端口（如 18789 被占用需更换）

5. 如果 /code 路由误配到本地 Agent，会出现什么现象？
   - 用户发送 "/code 写一个 Python 单元测试" 时，消息会被发给本地 Qwen Agent
   - 本地 Qwen 模型可能无法正确理解代码生成任务，输出质量较差
   - 响应速度较慢（本地模型 60-90 秒），用户体验下降
   - 日志中会显示 provider=ollama，model=qwen2.5:7b-64k，而非 deepseek
   - 如果本地模型未开启 no-thinking，输出中可能出现 <think> 推理过程

6. 如果云端 Base URL 填成错误接口，可能带来什么费用或可用性风险？
   - 可用性风险：Gateway 无法调用模型，所有请求失败，返回 404 或连接错误
   - 费用风险：
     - 填成按量计费接口可能产生意外费用
     - 填成高成本模型接口（如 deepseek-v4-pro）可能消耗更多余额
     - 填成 OpenRouter 免费接口可能因限流导致可用性下降
     - 填成错误接口可能产生无效请求，但仍会计费（取决于服务商）
   - 排查困难：错误信息可能不明确，需要逐一检查 Base URL、模型名、API Key

7. LLM Router 的结构化输出应保存在哪里？哪些字段需要脱敏？
   保存位置：
   - notes/llm_router_check.md（用于实验记录）
   - 或临时目录中的 router.json（用于自动化处理）
   - 不应保存到生产配置文件或版本控制中

   需要脱敏的字段：
   - open_id、chat_id 等用户/群标识
   - 任何可能包含凭证的字段（api_key、token 等）
   - 内部 IP 地址或域名（如涉及内网）
   - 文件名或路径中的敏感信息（如用户目录）

   不需要脱敏的字段：
   - intent、execution_mode、agents 角色、confidence
   - 任务描述、输出格式定义

8. Hermes 的模型、Gateway、Skill 或记忆配置分别在哪里观察？
   - 模型配置：
     - exp4deepseek：~/.hermes/profiles/exp4deepseek/config.yaml 中的 model 和 custom_providers 部分
     - exp4qwen：~/.hermes/profiles/exp4qwen/config.yaml 中的 model 和 custom_providers 部分
     - 命令行验证：exp4deepseek config show、exp4qwen config show
   - Gateway 配置：
     - 飞书相关：.env 文件中的 FEISHU_APP_ID、FEISHU_APP_SECRET、FEISHU_GROUP_POLICY 等
     - 群规则：config.yaml 中的 platforms.feishu.extra.group_rules
     - 状态查看：exp4deepseek status、exp4qwen status、hermes gateway list
   - Skill 配置：
     - exp4deepseek：~/.hermes/profiles/exp4deepseek/skills/domain/exp4-task-planning/SKILL.md
     - exp4qwen：~/.hermes/profiles/exp4qwen/skills/domain/exp4-safety-review/SKILL.md
     - 命令行验证：exp4deepseek chat --skills 或 exp4qwen chat --skills
   - 记忆配置：
     - 记忆文件：~/.hermes/profiles/exp4deepseek/memories/、~/.hermes/profiles/exp4qwen/memories/
     - 记忆开关：config.yaml 中的 memory.memory_enabled、memory.user_profile_enabled
     - 会话文件：~/.hermes/profiles/exp4deepseek/sessions/、~/.hermes/profiles/exp4qwen/sessions/