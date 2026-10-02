"""Rendering helpers for the VERITAS interface. All dynamic text is HTML-escaped."""
from html import escape as e

import streamlit as st

LEVEL_CLASS = {"HIGH RISK": "vt-high", "NEEDS VERIFICATION": "vt-need", "LOW RISK": "vt-low", "INSUFFICIENT EVIDENCE": "vt-ins"}
IDENTITY_NOTE = {
    "Mismatch Detected": "The claimed sender and the linked domain do not match.",
    "Needs Verification": "The sender or link cannot be confirmed from the content alone.",
    "Consistent With Claim": "The link appears consistent with the claimed sender, but this is not proof.",
    "No Identity Claim": "The content does not clearly claim an identity.",
}


def header() -> None:
    st.markdown(
        '<h1 class="vt-wordmark">VERITAS</h1><p class="vt-tag">Understand. Verify. Trust.</p>'
        '<p class="vt-intro">Check a suspicious message or link before you click, pay, reply or trust it. '
        'VERITAS shows what it found and why, based on the evidence available.</p>', unsafe_allow_html=True)


def _card(title: str, body: str) -> None:
    st.markdown(f'<div class="vt-card"><h3>{e(title)}</h3>{body}</div>', unsafe_allow_html=True)


def _list(items: list) -> str:
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def result(res: dict) -> None:
    trust, ident, risk, ev, content = res["trust"], res["identity"], res["risk"], res["evidence"], res["content"]
    cls = LEVEL_CLASS[trust["level"]]
    st.markdown(
        f'<div class="vt-hero {cls}" role="status"><h2>Trust Assessment</h2><span class="vt-badge">{e(trust["level"])}</span>'
        f'<p><strong>Why?</strong> {e(trust["explanation"])}</p>'
        f'<p class="vt-muted" style="color:inherit!important">Evidence strength: {e(trust["evidence_strength"])}. '
        f'This is an assessment from available evidence, not a certainty.</p></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        body = f'<p><span class="vt-chip">{e(ident["status"])}</span></p><p>{e(IDENTITY_NOTE[ident["status"]])}</p>'
        if ident["claimed_sender"]:
            body += f'<p class="vt-muted">Claimed sender: {e(ident["claimed_sender"])}</p>'
        if ident["reasoning"]:
            body += f'<p class="vt-muted">{e(ident["reasoning"])}</p>'
        _card("Identity Assessment", body)
    with c2:
        if risk["signals"]:
            body = _list([s["label"] for s in risk["signals"]])
        else:
            body = "<p>No risk signals were detected.</p>"
        _card("Risk Signals", body)

    if content["summary"]:
        _card("What this content says", f'<p>{e(content["summary"])}</p><p class="vt-muted">Language: {e(content["language"])}</p>')

    rows = "".join(f'<div class="vt-row"><span>{e(i["finding"])}</span><span class="vt-src">{e(i["source"])}</span></div>'
                   for i in sorted(ev["items"], key=lambda i: -i["weight"]))
    _card("Evidence", rows or '<p>No suspicious evidence was found in the submitted content.</p>')
    _card("Recommended Action", _list(res["action"]["actions"]))
    _card("Limitations", _list(res["limitations"]) + "".join(f'<p class="vt-muted">{e(n)}</p>' for n in res["notes"]))

    with st.expander("How VERITAS reached this result"):
        st.markdown("The Orchestrator ran each specialist agent in order and passed along their structured results.")
        for t in res["trace"]:
            st.markdown(f"- {t['agent']}: {t['status']}")
