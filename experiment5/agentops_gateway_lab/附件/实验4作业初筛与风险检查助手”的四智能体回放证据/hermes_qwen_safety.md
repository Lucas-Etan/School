  ⚠ tirith security scanner enabled but not available — command scanning will use pattern matching only

session_id: 20260526_173136_f3ef41
1. 检查智能体权限是否最小化：
   - [ ] 核查每个智能体的权限设置
   - [x] 确认无真实 API Key, App Secret, chat_id, open_id

2. 检查飞书群全量消息范围：
   - [ ] 验证消息历史记录是否超过必要期限保存
   - [x] 确认无真实 API Key, App Secret, chat_id, open_id

3. 检查 pairing/allowlist 配置安全性：
   - [ ] 核实允许列表中未包含敏感信息或凭据
   - [x] 确认 no real API Keys, App Secrets, chat_ids or open_ids 存在

4. 日志脱敏处理检查：
   - [ ] 审阅日志记录，确保不泄露敏感详情如密码、信用卡号等数据
   - [x] 所有 log 表明未出现真实 api_keys, app_secrets 等信息

5. 截图内容审查：
   - [ ] 检查所有本地备份的截图是否包含敏感信息如账户名，密码或验证码
   - [x] 确认截图中未发现真实 API Keys, App Secrets, chat_ids, open_ids

6. 配置片段安全检查：
   - [ ] 评估配置文件是否暴露关键凭证和敏感信息
   - [x] 确保 no sensitive tokens/keys like api_keys or auth_secrets 出现在文档中
