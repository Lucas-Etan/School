from openai import OpenAI

# 初始化 Ollama 客户端。
# Ollama 本地服务默认监听 11434 端口，并在 /v1 路径上兼容 OpenAI Chat Completions API。
# api_key 对本地 Ollama 不做真实鉴权，但 OpenAI SDK 要求必须提供一个字符串。
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='local',
    timeout=120
)

# 测试连接。
# 这里选择 qwen3.6:35b-a3b，是因为本实验主线以 MoE 模型完成 Agent 编排。
# max_tokens 设置较小，避免环境验证阶段生成太久。
try:
    response = client.chat.completions.create(
        model="qwen3.6:35b-a3b",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=10
    )
    print("✅ Ollama API 连接成功")
    print(f"模型回复: {response.choices[0].message.content}")
except Exception as e:
    # 连接失败时通常是 Ollama 服务未启动、模型未下载、端口被占用或内存不足。
    print(f"❌ Ollama API 连接失败: {e}")