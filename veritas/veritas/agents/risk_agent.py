"""Risk Agent: social-engineering signals (English, Urdu, Roman Urdu patterns plus AI reading)."""
import re

from veritas import llm

# (id, label, severity, regex)
PATTERNS = [
    ("urgency", "Urgency or deadline pressure", 2,
     r"\b(urgent|immediately|right now|within \d+ ?(hours?|minutes?)|last chance|expires?|final notice|act now|today only|abhi|fauran|foran|jaldi|aaj hi)\b|فوری|جلدی"),
    ("credentials", "Requests passwords, OTP, PIN or card details", 4,
     r"\b(otp|one[- ]time (code|password)|password|pin( code)?|cvv|card number|verification code|login details|security code)\b|پاس ورڈ"),
    ("payment", "Requests money, fees or a transfer", 3,
     r"\b(send money|wire|transfer|processing fee|advance fee|gift cards?|crypto|bitcoin|western union|easypaisa|jazzcash|pay (a )?fee|paisay (bhej|send)|raqam (bhej|transfer))\b|پیسے بھیج"),
    ("prize", "Unexpected prize, reward or refund", 3,
     r"\b(you('ve| have)? won|winner|lottery|prize|reward|claim your|refund (is )?pending|cashback|free gift|inam)\b|انعام"),
    ("threat", "Threat of account closure, penalty or legal action", 3,
     r"\b(suspend(ed)?|blocked|locked|deactivated|legal action|arrest|penalty|unauthori[sz]ed (login|access|transaction)|band ho (jaye|jayega)|block ho (jaye|jayega))\b|بند ہو"),
    ("click", "Pushes the reader to click a link or open a file", 2,
     r"\b(click (here|the link|below)|tap (here|the link)|open (the )?attachment|log ?in (here|now)|verify (your )?(account|identity)|link par click)\b"),
    ("secrecy", "Asks for secrecy or to avoid contacting others", 3,
     r"\b(don'?t tell|keep (this )?(secret|confidential)|do not share this|kisi ko mat batana)\b"),
    ("impersonation", "Claims authority (bank, courier, government, support)", 2,
     r"\b(bank|customer (care|support)|security team|tax (office|authority)|police|courier|customs|it (support|helpdesk))\b"),
    ("new_number", "Claims to be a known person on a new number", 3,
     r"\b(new (number|phone)|lost my phone|changed my number|naya number)\b"),
]

SYSTEM = (
    "You are the Risk Agent of a digital trust platform. Identify social-engineering or scam indicators in the message "
    "(English, Urdu, Roman Urdu or other). Return JSON with key signals: a list (max 5) of objects {label (short), severity "
    "(1 low to 4 high), quote (a short exact excerpt from the message)}. Only report indicators actually present. If the "
    "message looks ordinary, return an empty list."
)


def run(ctx: dict) -> dict:
    text = ctx["text"]
    signals, seen = [], set()
    for sid, label, weight, rx in PATTERNS:
        m = re.search(rx, text, re.I)
        if m:
            seen.add(label.lower())
            signals.append({"id": sid, "label": label, "severity": weight, "excerpt": m.group(0)[:80], "source": "pattern"})
    ai_used = False
    try:
        for s in (llm.ask_json(SYSTEM, text[:4000]).get("signals") or [])[:5]:
            if not isinstance(s, dict):
                continue
            label = str(s.get("label", "")).strip()[:90]
            quote = str(s.get("quote", "")).strip()
            if not label or label.lower() in seen:
                continue
            sev = s.get("severity", 2)
            sev = min(4, max(1, int(sev))) if isinstance(sev, (int, float)) else 2
            if quote and quote.lower() not in text.lower():
                quote = ""  # drop excerpts the model did not take from the message
            signals.append({"id": "ai", "label": label, "severity": sev, "excerpt": quote[:80], "source": "ai"})
        ai_used = True
    except llm.LLMUnavailable as exc:
        ctx["notes"].append(f"Risk Agent used pattern rules only ({exc}).")
    return {"signals": signals, "ai_used": ai_used}
