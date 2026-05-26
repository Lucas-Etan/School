## LLM Router 编排观察

- 原始用户指令：请规划飞书四机器人接入流程，检查权限风险，并给出 OpenClaw 配置复盘清单。

- 使用的 Router：Hermes-DeepSeek-2410311401 对应 profile（exp4deepseek）

- Router 输出是否为结构化 JSON：是

- intent：实验 4 作业初筛与风险检查

- execution_mode：sequential_then_review

- confidence：0.85

- 被选择的 Agent 顺序：

  1. exp4-deepseek（工程配置审查）
  2. exp4-qwen（本地模型推理说明）
  3. exp4qwen（安全与隐私复核）
  4. exp4-deepseek（综合交叉验证）

- 是否包含安全复核：是（safety_gate.review_agent: exp4qwen）

- 低置信度时是否要求反问：是

| 步骤 | 计划中的 Agent       | 实际调用方式                         | 输出摘要              | 是否需要修正 |
| ---- | -------------------- | ------------------------------------ | --------------------- | ------------ |
| 1    | hermes-exp4-deepseek | exp4deepseek chat -q                 | JSON 四智能体编排计划 | 否           |
| 2    | exp4-deepseek        | openclaw agent --agent exp4-deepseek | 配置文件检查清单表格  | 否           |
| 3    | exp4-qwen            | openclaw agent --agent exp4-qwen     | 学生补交反馈模板      | 否           |
| 4    | hermes-exp4-qwen     | exp4qwen chat -q                     | 安全复核检查清单      | 否           |

## 反思

- 规则 Router 能解决的问题：

  - 前缀路由（如 /code、/chat）稳定可靠，适合已知任务类型
  - 飞书 account binding 按机器人身份分流，成本低、可解释性强
  - 权限白名单（allowlist、groupPolicy）等不可变安全边界

- LLM Router 比规则 Router 更适合的问题：

  - 用户不写前缀的自然语言复合指令
  - 需要动态判断任务类型、拆分多个子任务的场景
  - 任务需要安全复核、多 Agent 协作的复杂链路
  - 意图模糊时，LLM Router 可以输出低置信度并要求反问

- LLM Router 可能误判的地方：

  - 将低风险任务错误标记为需要安全复核
  - 遗漏关键子任务或 Agent 顺序不合理
  - 置信度虚高，强行路由导致错误执行
  - 对超出 Agent 能力范围的指令仍尝试编排

- 如果 Router 置信度低，系统应该如何 fail closed：
  - 置信度低于阈值（如 0.65）时，不自动执行编排计划
  - 输出反问或澄清问题，要求用户补充信息
  - 记录低置信度决策到日志，供人工审计
  - 可选：将低置信度请求转给人工审核队列
  - 绝不自动执行高风险操作（如权限变更、文件写入）
