# 飞书 Channel 与 Router 配置快照（脱敏版）

> 本文件是实践复盘材料，不是运行时配置。敏感字段已使用占位符替换，学号保留完整。

## 一、OpenClaw 飞书 Channel 配置

### 1.1 Channel 基本信息

| 字段 | 值 | 说明 |
|------|-----|------|
| Channel 名称 | feishu | 飞书通道标识 |
| 连接模式 | websocket | 使用飞书长连接接收事件 |
| 是否启用 | true | |
| 群聊要求 | requireMention: true | 群聊中必须直接 @ 机器人 |

### 1.2 群组权限控制

| 字段 | 值 | 说明 |
|------|-----|------|
| groupPolicy | allowlist | 只允许白名单群组 |
| groupAllowFrom | ["<TEST_GROUP_CHAT_ID>"] | 白名单群组列表 |
| groups | { "<TEST_GROUP_CHAT_ID>": { enabled: true, requireMention: true } } | 测试群规则 |

### 1.3 账号配置（account）

| account ID | 机器人名称 | dmPolicy | allowFrom | groupPolicy | groupAllowFrom |
|------------|-----------|----------|-----------|-------------|----------------|
| oc-deepseek | OC-DeepSeek-2410311401 | allowlist | ["<OC_DEEPSEEK_USER_OPEN_ID>"] | allowlist | ["<TEST_GROUP_CHAT_ID>"] |
| oc-qwen | OC-Qwen-2410311401 | allowlist | ["<OC_QWEN_USER_OPEN_ID>"] | allowlist | ["<TEST_GROUP_CHAT_ID>"] |

### 1.4 groups 群内权限

```json
{
  "<TEST_GROUP_CHAT_ID>": {
    "enabled": true,
    "requireMention": true,
    "allowFrom": ["<OC_DEEPSEEK_USER_OPEN_ID>"]
  }
}