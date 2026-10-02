"""VERITAS Orchestrator: delegates to specialist agents in order and combines their structured results."""
from veritas.agents import action_agent, content_agent, evidence_agent, identity_agent, risk_agent, trust_agent

PIPELINE = [
    ("content", "Content Agent", content_agent),
    ("identity", "Identity Agent", identity_agent),
    ("risk", "Risk Agent", risk_agent),
    ("evidence", "Evidence Agent", evidence_agent),
    ("trust", "Trust Agent", trust_agent),
    ("action", "Action Agent", action_agent),
]
MAX_CHARS = 6000
SUPPORTED_KINDS = {"text", "url"}  # image, screenshot and QR inputs are on the roadmap


class InputError(ValueError):
    pass


def analyze(text: str, kind: str = "text") -> dict:
    if kind not in SUPPORTED_KINDS:
        raise InputError(f"Input type '{kind}' is not available yet.")
    text = (text or "").strip()
    if not text:
        raise InputError("Paste a message or link to analyse.")
    if len(text) > MAX_CHARS:
        raise InputError(f"Content is too long. The limit is {MAX_CHARS} characters.")
    ctx = {"text": text, "kind": kind, "results": {}, "notes": []}
    trace = []
    for key, name, agent in PIPELINE:
        try:
            ctx["results"][key] = agent.run(ctx)
            trace.append({"agent": name, "status": "completed"})
        except Exception:
            raise RuntimeError(f"{name} could not complete the analysis. Please try again.") from None
    r = ctx["results"]
    limits = ["This assessment is based only on the content you submitted. VERITAS cannot confirm who really sent it.",
              "Links are analysed as text. They are not opened or checked against live reputation databases.",
              "Images, screenshots and QR codes are not analysed in this version."]
    if not (r["content"]["ai_used"] or r["trust"]["ai_used"]):
        limits.insert(0, "AI analysis was unavailable, so rule-based checks were used. Results may be less detailed.")
    return {"trace": trace, "notes": ctx["notes"], "limitations": limits, **r}
