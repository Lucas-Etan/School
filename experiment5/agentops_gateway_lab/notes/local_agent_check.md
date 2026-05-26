## 本地 Agent 验证

- Ollama 版本：0.6.2

- 本地模型名称：`qwen2.5:7b-64k`

- Provider 名称：

  - OpenClaw: `ollama-nothink` / `ollama/qwen2.5:7b-64k`
  - Hermes: `custom` (base_url: http://127.0.0.1:11434/v1)

- Agent 名称：

  - OpenClaw: `exp4-qwen`
  - Hermes: `exp4qwen`

- 验证命令：

```bash
# OpenClaw 模型级烟测
openclaw infer model run \
  --local \
  --model ollama/qwen2.5:7b-64k \
  --prompt $'/no_think\n最终答案只输出这一句：OpenClaw Ollama qwen2.5 已经跑通。' \
  --json

# OpenClaw Agent 级烟测
openclaw agent \
  --agent exp4-qwen \
  --local \
  --message $'/no_think\n只回复一句：exp4-qwen agent 已经跑通。' \
  --json

# Hermes CLI 验证
exp4qwen chat -q "只回复：HERMES_QWEN_OK" -Q --max-turns 1
```

- 是否断网测试：是

- 响应耗时主观观察：约 1 分钟左右

- CPU/内存/显存占用观察： CPU 占用率大于 96%，内存占用率约 45%，显存无法查看
