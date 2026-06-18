from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

WORKSPACE_DIR = (BASE_DIR / "workspace").resolve()

LOG_DIR = (BASE_DIR / "logs").resolve()
AUDIT_LOG = LOG_DIR / "audit.jsonl"

ALLOWED_TOOLS = {
    "read_text",
    "write_text",
    "append_text",
    "list_files",
}

ALLOWED_EXTENSIONS = {".txt", ".md", ".json", ".csv"}

MAX_WRITE_CHARS = 2000