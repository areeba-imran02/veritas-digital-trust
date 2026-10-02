"""Action Agent: practical safer next steps."""

LIBRARY = {
    "click": "Do not click the provided link or open any attachment.",
    "credentials": "Do not share passwords, OTPs, PINs or card details with anyone who contacts you first.",
    "payment": "Confirm the recipient through a separate trusted channel before making any payment.",
    "prize": "Treat unexpected prizes and refunds as unverified; real ones do not require fees or secret codes.",
    "new_number": "Call the person on their known number to confirm it is really them.",
    "secrecy": "Talk to someone you trust before acting; legitimate senders do not ask for secrecy.",
}


def run(ctx: dict) -> dict:
    r = ctx["results"]
    level, ids = r["trust"]["level"], {s["id"] for s in r["risk"]["signals"]}
    actions = [txt for k, txt in LIBRARY.items() if k in ids]
    if r["content"]["urls"] and LIBRARY["click"] not in actions and level != "LOW RISK":
        actions.insert(0, LIBRARY["click"])
    if level in ("HIGH RISK", "NEEDS VERIFICATION"):
        actions.append("Verify through an independent official channel, such as a phone number or app you already trust, not details in the message.")
    if level == "HIGH RISK":
        actions.append("Do not reply. Report the message to the platform or provider and block the sender if appropriate.")
    if level == "LOW RISK":
        actions.append("Stay cautious: only act on requests you expected, and avoid sharing sensitive details by message.")
    if level == "INSUFFICIENT EVIDENCE":
        actions.append("Add the full message, sender name and any links, then analyse again. Until then, do not act on it.")
    return {"actions": list(dict.fromkeys(actions))}
