from harness import build_feedback, run_tool


def test_allowed_read():
    result = run_tool({"tool": "read_text", "path": "note.md"})
    assert result["ok"] is True


def test_block_path_traversal():
    result = run_tool({"tool": "read_text", "path": "../blocked/secret.txt"})
    assert result["ok"] is False
    assert "路径越界" in result["error"]


def test_block_unknown_tool():
    result = run_tool({"tool": "delete_file", "path": "note.md"})
    assert result["ok"] is False
    assert "工具未授权" in result["error"]


def test_block_extension():
    result = run_tool({"tool": "write_text", "path": "run.sh", "content": "echo hi"})
    assert result["ok"] is False
    assert "不允许的文件类型" in result["error"]


def test_block_missing_path():
    result = run_tool({"tool": "read_text"})
    assert result["ok"] is False
    assert "path 参数必须是非空字符串" in result["error"]


def test_block_wrong_content_type():
    result = run_tool({"tool": "write_text", "path": "note.md", "content": ["bad"]})
    assert result["ok"] is False
    assert "content 参数必须是字符串" in result["error"]


def test_block_missing_content_for_write():
    result = run_tool({"tool": "write_text", "path": "note.md"})
    assert result["ok"] is False
    assert "缺少 content 参数" in result["error"]


def test_block_read_with_content():
    result = run_tool({"tool": "read_text", "path": "note.md", "content": "overwrite"})
    assert result["ok"] is False
    assert "不应包含 content 参数" in result["error"]


def test_block_long_write():
    result = run_tool({"tool": "append_text", "path": "note.md", "content": "x" * 3000})
    assert result["ok"] is False
    assert "写入内容过长" in result["error"]


def test_feedback_for_failure():
    result = run_tool({"tool": "delete_file", "path": "note.md"})
    feedback = build_feedback(result)
    assert "工具执行失败" in feedback
    assert "工具未授权" in feedback