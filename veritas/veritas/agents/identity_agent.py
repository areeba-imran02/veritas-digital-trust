"""Identity Agent: who claims to be whom, and does the evidence support it?"""
import re
from urllib.parse import urlparse

from veritas import llm

SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "cutt.ly", "is.gd", "rb.gy", "ow.ly", "shorturl.at", "tiny.cc"}
RISKY_TLDS = (".xyz", ".top", ".click", ".link", ".info", ".gq", ".tk", ".icu")
GENERIC = {"the", "bank", "team", "support", "service", "services", "official", "customer", "care", "dept", "department"}

SYSTEM = (
    "You are the Identity Agent of a digital trust platform. Given a claimed sender and the domains in a message, "
    'return JSON {"reasoning": "..."} with one or two cautious sentences on whether the domains plausibly belong to the '
    "claimed sender. Never state certainty; you cannot verify ownership. Do not invent facts."
)


def _domain(url: str) -> str:
    host = urlparse(url if "//" in url else "//" + url).hostname or ""
    return host.lower().removeprefix("www.")


def _tokens(name: str) -> list:
    return [t for t in re.split(r"[^a-z0-9]+", name.lower()) if len(t) >= 3 and t not in GENERIC]


def run(ctx: dict) -> dict:
    content = ctx["results"]["content"]
    claimed = content["claimed_sender"].strip()
    domains = [d for d in (_domain(u) for u in content["urls"]) if d]
    flags = []
    for d in domains:
        if d in SHORTENERS:
            flags.append(f"Link uses a URL shortener ({d}), which hides the real destination.")
        if d.endswith(RISKY_TLDS):
            flags.append(f"Domain {d} uses a top-level domain frequently abused in scams.")
        if d.count("-") >= 2 or d.count(".") >= 3:
            flags.append(f"Domain {d} has an unusual structure.")
        if "xn--" in d:
            flags.append(f"Domain {d} uses encoding that can imitate other names.")

    status, mismatch = "No Identity Claim", False
    if claimed:
        toks = _tokens(claimed)
        if not domains:
            status = "Needs Verification"
        elif toks and any(t in d for t in toks for d in domains):
            status = "Needs Verification" if flags else "Consistent With Claim"
            if flags:
                flags.append("The domain mentions the claimed name but other warning signs are present; lookalike domains are common.")
        elif toks:
            status, mismatch = "Mismatch Detected", True
            flags.append(f"Message claims to be {claimed}, but the linked domain(s) {', '.join(domains)} do not reference that name.")
        else:
            status = "Needs Verification"
    elif domains:
        status = "Needs Verification"
        flags.append("Message contains a link but does not clearly state who it is from.")

    reasoning = ""
    if claimed and domains:
        try:
            reasoning = str(llm.ask_json(SYSTEM, f"Claimed sender: {claimed}\nDomains: {domains}").get("reasoning", ""))[:400]
        except llm.LLMUnavailable:
            pass
    return {"status": status, "claimed_sender": claimed, "domains": domains, "mismatch": mismatch,
            "flags": flags, "reasoning": reasoning}
