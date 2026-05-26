# 配置文件路径记录

## OpenClaw

| 配置项 | 路径 | 发现方式 |
|--------|------|----------|
| 主配置文件 | ~/.openclaw/openclaw.json | openclaw config validate 提示 |
| 工作区目录 | ~/.openclaw/workspace/ | 从 openclaw.json 中 agents.defaults.workspace 读取 |
| exp4-deepseek 工作区 | ~/.openclaw/workspace-exp4-deepseek/ | 从 openclaw.json 中 agents.list 读取 |
| exp4-qwen 工作区 | ~/.openclaw/workspace-exp4-qwen/ | 从 openclaw.json 中 agents.list 读取 |
| 日志文件 | /tmp/openclaw/openclaw-YYYY-MM-DD.log | openclaw gateway status 输出 |
| systemd 服务文件 | ~/.config/systemd/user/openclaw-gateway.service | systemctl --user status openclaw-gateway 输出 |
| 环境变量文件 | ~/.openclaw/.env | 手动创建，用于存放飞书凭证和 API Key |

## Hermes

| 配置项 | 路径 | 发现方式 |
|--------|------|----------|
| exp4deepseek profile 配置 | ~/.hermes/profiles/exp4deepseek/config.yaml | exp4deepseek config show 输出 |
| exp4deepseek 环境变量 | ~/.hermes/profiles/exp4deepseek/.env | exp4deepseek config show 输出 |
| exp4deepseek 记忆目录 | ~/.hermes/profiles/exp4deepseek/memories/ | config.yaml 中 memory 配置 |
| exp4deepseek 会话目录 | ~/.hermes/profiles/exp4deepseek/sessions/ | exp4deepseek status 输出 |
| exp4deepseek Skill 目录 | ~/.hermes/profiles/exp4deepseek/skills/domain/ | 手动创建 |
| exp4qwen profile 配置 | ~/.hermes/profiles/exp4qwen/config.yaml | exp4qwen config show 输出 |
| exp4qwen 环境变量 | ~/.hermes/profiles/exp4qwen/.env | exp4qwen config show 输出 |
| exp4qwen 记忆目录 | ~/.hermes/profiles/exp4qwen/memories/ | config.yaml 中 memory 配置 |
| exp4qwen 会话目录 | ~/.hermes/profiles/exp4qwen/sessions/ | exp4qwen status 输出 |
| exp4qwen Skill 目录 | ~/.hermes/profiles/exp4qwen/skills/domain/ | 手动创建 |

## 其他

| 配置项 | 路径 | 发现方式 |
|--------|------|----------|
| Ollama 配置 | ~/.ollama/ | ollama list 输出 |
| Ollama 模型存储 | ~/.ollama/models/ | ollama list 输出 |
| 实验目录 | ~/agentops_gateway_lab/ | 手动创建 |
| 笔记目录 | ~/agentops_gateway_lab/notes/ | 手动创建 |
| 配置快照目录 | ~/agentops_gateway_lab/config_snapshots/ | 手动创建 |
| 日志目录 | ~/agentops_gateway_lab/logs/ | 手动创建 |