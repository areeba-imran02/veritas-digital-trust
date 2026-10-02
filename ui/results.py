from html import escape

import streamlit as st

from ui.theme import render_html


def _esc(value, default: str = "") -> str:
    """Escape text for safe HTML and keep line breaks."""
    text = default if value is None else str(value)
    return escape(text).replace("\n", "<br>")


def render_threat_results(result: dict, localization_mode: str):
    verdict = result.get("trust_verdict", "LOW RISK")
    risk = result.get("risk_evaluation", {}) or {}
    action = result.get("action_plan", {}) or {}
    cards = result.get("evidence_cards", []) or []

    # ---- Color / icon mapping ----
    color_map = {
        "HIGH RISK": "#ef4444",
        "NEEDS VERIFICATION": "#f59e0b",
        "LOW RISK": "#10b981",
        "INSUFFICIENT EVIDENCE": "#94a3b8",
    }
    icon_map = {
        "HIGH RISK": "🚨",
        "NEEDS VERIFICATION": "⚠️",
        "LOW RISK": "✅",
        "INSUFFICIENT EVIDENCE": "❔",
    }
    v_color = color_map.get(verdict, "#94a3b8")
    v_icon = icon_map.get(verdict, "❔")

    try:
        score_pct = max(0, min(100, int(float(risk.get("threat_score", 0.0)) * 100)))
    except (TypeError, ValueError):
        score_pct = 0
    severity = _esc(risk.get("severity", "LOW"))

    render_html('<div class="vt-report-title">Multi-Agent Intelligence Assessment Report</div>')

    # ---- Verdict banner (single HTML block) ----
    render_html(f"""
        <div class="vt-verdict" style="background:
            radial-gradient(520px 200px at 0% 0%, {v_color}26, transparent 65%),
            linear-gradient(135deg, #0f1524 0%, #070a14 100%);
            border-left: 6px solid {v_color};">
            <div>
                <div class="vt-verdict-label">Final Trust Verdict</div>
                <h2 class="vt-verdict-value" style="color:{v_color} !important;">{v_icon}&nbsp; {_esc(verdict)}</h2>
            </div>
            <div class="vt-score-box">
                <div class="vt-score-top">
                    <span class="vt-score-label">Threat Vector Score</span>
                    <span>
                        <span class="vt-score-num">{score_pct}%</span>
                        <span class="vt-score-sev" style="color:{v_color};">{severity}</span>
                    </span>
                </div>
                <div class="vt-bar">
                    <div style="width:{score_pct}%; background: linear-gradient(90deg, {v_color}99, {v_color}); box-shadow: 0 0 12px {v_color}88;"></div>
                </div>
            </div>
        </div>
    """)

    col1, col2 = st.columns(2, gap="large")

    # ================= LEFT COLUMN =================
    with col1:
        render_html('<div class="vt-section"><span class="vt-section-bar"></span>🧠 Forensic Reasoning ("Why?")</div>')
        render_html(f"""
            <div class="vt-card">
                <p class="vt-card-text">{_esc(action.get('reasoning_why'), 'No detailed reasoning available.')}</p>
            </div>
        """)

        render_html('<div class="vt-section" style="margin-top:8px;"><span class="vt-section-bar"></span>📂 Correlated Evidence Cards</div>')

        if not cards:
            render_html('<div class="vt-card"><div class="vt-empty">No correlated evidence found.</div></div>')

        sev_styles = {
            "High": ("#ef4444", "rgba(239,68,68,0.14)"),
            "Medium": ("#f59e0b", "rgba(245,158,11,0.14)"),
            "Low": ("#10b981", "rgba(16,185,129,0.14)"),
        }
        for card in cards:
            c_sev = card.get("severity", "Low")
            fg, bg = sev_styles.get(c_sev, sev_styles["Low"])
            render_html(f"""
                <div class="vt-card vt-evidence" style="border-left: 3px solid {fg};">
                    <div class="vt-evidence-head">
                        <span class="vt-evidence-title">{_esc(card.get('title'), 'Untitled')}</span>
                        <span class="vt-sev-pill" style="background:{bg}; color:{fg}; border:1px solid {fg}55;">{_esc(c_sev)}</span>
                    </div>
                    <p class="vt-evidence-body">{_esc(card.get('details'))}</p>
                </div>
            """)

    # ================= RIGHT COLUMN =================
    with col2:
        render_html('<div class="vt-section"><span class="vt-section-bar"></span>🛡️ Recommended Action Checklist</div>')

        steps = action.get("action_checklist", []) or []

        if localization_mode == "Urdu (اردو)":
            wrapper_cls = "vt-card vt-rtl"
            heading = "حفاظتی اقدامات"
        elif localization_mode == "Roman Urdu":
            wrapper_cls = "vt-card"
            heading = "Aap ko ab kya karna chahiye"
        else:
            wrapper_cls = "vt-card"
            heading = "Immediate Security Protocol"

        if steps:
            steps_html = "".join(
                f'<div class="vt-step"><div class="vt-step-num">{i}</div>'
                f'<div class="vt-step-text">{_esc(step)}</div></div>'
                for i, step in enumerate(steps, 1)
            )
        else:
            steps_html = '<div class="vt-empty">No action steps available.</div>'

        # One single HTML block so the card never breaks
        render_html(f"""
            <div class="{wrapper_cls}">
                <div class="vt-check-head">{heading}</div>
                {steps_html}
            </div>
        """)
