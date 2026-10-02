"""Groq client. Reads GROQ_API_KEY from the environment only. Nothing is logged or stored."""
import json
import os

import requests

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


class LLMUnavailable(Exception):
    """Raised when Groq cannot be used (no key, network error, bad response)."""


def available() -> bool:
    return bool(os.environ.get("GROQ_API_KEY"))


def ask_json(system: str, user: str) -> dict:
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        raise LLMUnavailable("GROQ_API_KEY is not configured")
    body = {
        "model": os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile"),
        "temperature": 0.1,
        "max_tokens": 700,
        "response_format": {"type": "json_object"},
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
    }
    try:
        r = requests.post(GROQ_URL, headers={"Authorization": f"Bearer {key}"}, json=body, timeout=30)
        r.raise_for_status()
        data = json.loads(r.json()["choices"][0]["message"]["content"])
        if not isinstance(data, dict):
            raise ValueError("not an object")
        return data
    except Exception as exc:  # never include request details (headers carry the key)
        raise LLMUnavailable(type(exc).__name__) from None
