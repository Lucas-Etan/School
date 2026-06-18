from harness import build_feedback, run_tool

REQUESTS = [
    {"tool": "read_text", "path": "note.md"},
    {"tool": "list_files", "path": "."},
    {"tool": "write_text", "path": "summary.md", "content": "Harness 可以限制 Agent 的行为。"},
    {"tool": "read_text", "path": "../blocked/secret.txt"},
    {"tool": "delete_file", "path": "note.md"},
    {"tool": "write_text", "path": "run.sh", "content": "rm -rf /"},
    {"tool": "append_text", "path": "note.md", "content": "x" * 3000},
    {"tool": "read_text", "path": "note.md", "content": "试图给读取工具夹带写入内容"},
]

for request in REQUESTS:
    response = run_tool(request)
    print("=" * 80)
    print("request:", request)
    print("response:", response)
    print("feedback:", build_feedback(response))