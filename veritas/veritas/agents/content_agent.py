"""Content Agent: understands and structures the submitted content."""
import re

from veritas import llm

URL_RE = re.compile(r"(?:https?://|www\.)[^\s<>\"')]+|\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|net|org|co|io|xyz|top|info|link|click|pk|app|me|ly|gl)\b(?:/[^\s]*)?", re.I)

SYSTEM = (
    "You are the Content Agent of a digital trust platform. Read the message (English, Urdu, Roman Urdu or other) "
    "and return JSON with keys: language (string), summary (one sentence), claimed_sender (organisation or person the "
    "message claims to be from, or empty string), requested_actions (list of short strings: what the sender wants the "
    "reader to do), topic (one of: payment, account, delivery, job, prize, relationship, support, other). "
    "Use only what is in the text. Do not invent details."
)


def run(ctx: dict) -> dict:
    text = ctx["text"]
    urls = [u.rstrip(".,;") for u in URL_RE.findall(text)]
    out = {"urls": list(dict.fromkeys(urls)), "language": "unknown", "summary": "", "claimed_sender": "",
           "requested_actions": [], "topic": "other", "ai_used": False, "length": len(text)}
    try:
        data = llm.ask_json(SYSTEM, text[:4000])
        out.update({
            "language": str(data.get("language", "unknown"))[:40],
            "summary": str(data.get("summary", ""))[:300],
            "claimed_sender": str(data.get("claimed_sender", ""))[:80],
            "requested_actions": [str(a)[:120] for a in (data.get("requested_actions") or [])][:5],
            "topic": str(data.get("topic", "other"))[:30],
            "ai_used": True,
        })
    except llm.LLMUnavailable as exc:
        ctx["notes"].append(f"Content Agent used basic extraction only ({exc}).")
    return out
