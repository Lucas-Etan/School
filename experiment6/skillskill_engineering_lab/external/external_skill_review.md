# 外部 Skill 观察记录

## Skill 名称

（示例）GitHub PR 自动化 Skill

## 主要用途

- 自动拉取指定仓库的 PR 列表
- 读取 PR diff、评论和检查状态
- 生成 PR 摘要或风险提示
- 可选：尝试修复简单 CI 错误

## 触发条件

- 用户明确要求：“帮我检查 PR #xxx”
- 或关键词：“PR 状态”、“review”、“CI 失败”

## 组成部分

- **元信息**：
  - 名称：github-pr-helper
  - 版本：1.0.0
  - 权限要求：GitHub token（至少需要 repo 或 public_repo 范围）
  
- **工作流程**：
  1. 调用 GitHub API 获取 PR 信息
  2. 提取 diff 和 check runs
  3. 使用 LLM 分析潜在问题
  4. 输出结构化建议或生成评论草稿

- **资源文件**：
  - `github_api_wrapper.py`
  - `pr_analyzer_prompt.md`
  - `config.example.json`

- **校验方式**：
  - 必须有有效的 GitHub token
  - 必须明确指定仓库与 PR 编号
  - 不支持批量无监督操作

## 我可以直接复用的部分

- PR diff 分析提示词结构
- GitHub API 调用模板（无需改写）
- 输出格式（摘要 / 风险项 / 建议）

## 我需要改造的部分

- 当前仅支持公开仓库，需改造支持内部仓库（若适用）
- 需要增加本地 diff 缓存能力，避免重复请求
- 增加“仅分析不自动评论”的安全模式
- 将输出从英文改为中文提示

## 风险与注意事项

- ⚠️ GitHub token 不可硬编码，必须使用环境变量或密钥管理
- ⚠️ 避免自动执行命令（如 `git push --force`）
- ⚠️ 涉及私有仓库时，必须确认用户已授权
- ⚠️ LLM 对 diff 的分析可能产生误判，不应自动合并建议
- ✅ 建议每次输出前添加人工确认步骤