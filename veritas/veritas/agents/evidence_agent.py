"""Evidence Agent: correlates signals from the Content, Identity and Risk agents."""


def run(ctx: dict) -> dict:
    r = ctx["results"]
    content, identity, risk = r["content"], r["identity"], r["risk"]
    items = []
    for s in risk["signals"]:
        ex = f' (excerpt: "{s["excerpt"]}")' if s["excerpt"] else ""
        items.append({"source": "Risk Agent", "finding": s["label"] + ex, "weight": s["severity"]})
    for f in identity["flags"]:
        items.append({"source": "Identity Agent", "finding": f, "weight": 4 if identity["mismatch"] and "Message claims" in f else 2})
    if content["urls"]:
        items.append({"source": "Content Agent", "finding": f"{len(content['urls'])} link(s) found: {', '.join(content['urls'][:3])}", "weight": 1})

    ids = {s["id"] for s in risk["signals"]}
    combos = []
    if "urgency" in ids and ("click" in ids or content["urls"]):
        combos.append("Urgency combined with a link is a common phishing pattern.")
    if "credentials" in ids and (identity["mismatch"] or content["urls"]):
        combos.append("A request for secret codes alongside an unverified link or sender is a strong warning pattern.")
    if "payment" in ids and ({"prize", "secrecy", "new_number", "urgency"} & ids):
        combos.append("A payment request combined with pressure or a reward is typical of advance-fee and impersonation scams.")
    if identity["mismatch"]:
        combos.append("The claimed sender and the linked domain do not match.")
    items += [{"source": "Evidence Agent", "finding": c, "weight": 3} for c in combos]

    total = sum(i["weight"] for i in items)
    strength = "Strong" if total >= 8 or len(items) >= 4 else "Moderate" if total >= 3 else "Weak"
    return {"items": items, "correlations": combos, "total_weight": total, "strength": strength}
