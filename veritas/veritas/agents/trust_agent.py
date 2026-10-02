"""Trust Agent: overall trust assessment from the available evidence."""
from veritas import llm

SYSTEM = (
    "You are the Trust Agent of a digital trust platform. Write a concise explanation (2 to 4 plain sentences) of why the "
    "content received the given trust level, in Urdu or Roman Urdu if the user's message used it, otherwise English. Base it "
    "ONLY on the evidence provided. Never claim certainty; say 'based on the available evidence'. "
    'Return JSON: {"explanation": "..."}'
)

FALLBACK = {
    "HIGH RISK": "Based on the available evidence, several strong warning signs appear together in this content.",
    "NEEDS VERIFICATION": "Based on the available evidence, some warning signs or unverified claims are present. Verify before acting.",
    "LOW RISK": "Based on the available evidence, no significant warning signs were found. This is not a guarantee of safety.",
    "INSUFFICIENT EVIDENCE": "There is not enough content or context to make a meaningful assessment.",
}


def _level(total: int, mismatch: bool, text_len: int, has_hook: bool) -> str:
    if text_len < 12:
        return "INSUFFICIENT EVIDENCE"
    if total >= 9 or (mismatch and total >= 5):
        return "HIGH RISK"
    if total >= 3 or mismatch:
        return "NEEDS VERIFICATION"
    if total == 0 and not has_hook and text_len < 40:
        return "INSUFFICIENT EVIDENCE"
    return "NEEDS VERIFICATION" if total >= 1 and has_hook else "LOW RISK"


def run(ctx: dict) -> dict:
    r = ctx["results"]
    ev, ident, content = r["evidence"], r["identity"], r["content"]
    level = _level(ev["total_weight"], ident["mismatch"], len(ctx["text"]), bool(content["urls"] or ident["claimed_sender"]))
    top = [i["finding"] for i in sorted(ev["items"], key=lambda i: -i["weight"])[:5]]
    explanation, ai_used = FALLBACK[level], False
    try:
        data = llm.ask_json(SYSTEM, f"Trust level: {level}\nSummary: {content['summary']}\nIdentity: {ident['status']}\nEvidence: {top}")
        text = str(data.get("explanation", "")).strip()
        if text:
            explanation, ai_used = text[:700], True
    except llm.LLMUnavailable:
        pass
    return {"level": level, "explanation": explanation, "ai_used": ai_used, "evidence_strength": ev["strength"]}
