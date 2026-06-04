import re


PHONE_RE = re.compile(r"1[3-9]\d{9}")
API_KEY_RE = re.compile(r"sk-[A-Za-z0-9_-]+")


def redact_sensitive(text: str) -> str:
    text = PHONE_RE.sub("[PHONE]", text)
    text = API_KEY_RE.sub("[API_KEY]", text)
    return text