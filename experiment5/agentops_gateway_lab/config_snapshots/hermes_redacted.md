# Hermes 配置快照（脱敏版）

> 本文件是实践复盘材料，不是运行时配置。敏感字段已使用占位符替换，学号保留完整。

## 一、exp4deepseek profile（Hermes-DeepSeek-2410311401）

### 1.1 模型配置

| 字段 | 值 | 说明 |
|------|-----|------|
| provider | custom | 使用自定义 OpenAI 兼容接口 |
| default | deepseek-v4-flash | 默认模型（低价默认） |
| base_url | https://api.deepseek.com | DeepSeek 官方 API 地址 |
| api_key | ${DEEPSEEK_API_KEY} | 从环境变量读取 |
| context_length | 65536 | 上下文长度 |

### 1.2 飞书 Gateway 配置（.env）

| 字段 | 值 | 说明 |
|------|-----|------|
| FEISHU_APP_ID | <HERMES_DEEPSEEK_APP_ID> | 飞书应用 ID，共享时脱敏 |
| FEISHU_APP_SECRET | <HERMES_DEEPSEEK_APP_SECRET> | 飞书应用 Secret，仅本机保存 |
| FEISHU_DOMAIN | feishu | 飞书中国区 |
| FEISHU_CONNECTION_MODE | websocket | 长连接接收事件 |
| FEISHU_HOME_CHANNEL | <TEST_GROUP_CHAT_ID> | 测试群 chat_id |
| FEISHU_HOME_CHANNEL_NAME | AgentOps实验4测试群 | 测试群显示名称 |
| FEISHU_GROUP_POLICY | disabled | 默认禁用未知群 |
| FEISHU_ALLOW_ALL_USERS | false | 不开放所有用户 |
| FEISHU_ALLOWED_USERS | <HERMES_DEEPSEEK_USER_OPEN_ID> | 授权用户的 open_id |

### 1.3 群组规则（config.yaml）

```yaml
platforms:
  feishu:
    home_channel:
      platform: feishu
      chat_id: <TEST_GROUP_CHAT_ID>
      name: AgentOps实验4测试群
    extra:
      default_group_policy: disabled
      group_rules:
        <TEST_GROUP_CHAT_ID>:
          policy: open
          require_mention: true