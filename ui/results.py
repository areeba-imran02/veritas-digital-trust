import html
import streamlit as st


def _safe(value):
    """Safely display dynamic text inside HTML."""
    if value is None:
        return ""

    return html.escape(str(value))


def _verdict_config(verdict: str):
    configs = {
        "HIGH RISK": {
            "color": "#dc2626",
            "soft": "#fef2f2",
            "border": "#fecaca",
            "label": "High Risk",
        },

        "NEEDS VERIFICATION": {
            "color": "#d97706",
            "soft": "#fffbeb",
            "border": "#fde68a",
            "label": "Needs Verification",
        },

        "LOW RISK": {
            "color": "#059669",
            "soft": "#ecfdf5",
            "border": "#a7f3d0",
            "label": "Low Risk",
        },

        "INSUFFICIENT EVIDENCE": {
            "color": "#64748b",
            "soft": "#f8fafc",
            "border": "#cbd5e1",
            "label": "Insufficient Evidence",
        },
    }

    return configs.get(
        verdict,
        configs["INSUFFICIENT EVIDENCE"],
    )


def render_threat_results(result: dict, localization_mode: str):

    # =========================================================
    # DATA
    # =========================================================

    verdict = str(
        result.get(
            "trust_verdict",
            "INSUFFICIENT EVIDENCE",
        )
    ).upper()

    risk = result.get("risk_evaluation", {}) or {}
    action = result.get("action_plan", {}) or {}
    cards = result.get("evidence_cards", []) or []

    config = _verdict_config(verdict)

    threat_score = risk.get("threat_score", 0)

    try:
        score_pct = max(
            0,
            min(
                100,
                int(float(threat_score) * 100),
            ),
        )
    except Exception:
        score_pct = 0

    severity = str(
        risk.get("severity", "LOW")
    ).upper()

    # =========================================================
    # ANSWER / PRIMARY ASSESSMENT
    # =========================================================

    answer = (
        result.get("answer")
        or result.get("final_answer")
        or result.get("assessment")
        or result.get("summary")
        or action.get("reasoning_why")
        or "No detailed assessment was returned."
    )

    answer = _safe(answer)

    # =========================================================
    # SECTION HEADER
    # =========================================================

    st.markdown(
        """
        <div class="results-heading">
            <div>
                <div class="results-eyebrow">
                    VERITAS INTELLIGENCE REPORT
                </div>

                <div class="results-title">
                    Trust & Safety Assessment
                </div>

                <div class="results-subtitle">
                    Multi-agent analysis of the submitted digital content.
                </div>
            </div>

            <div class="report-chip">
                ANALYSIS COMPLETE
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # FINAL VERDICT
    # =========================================================

    st.markdown(
        f"""
        <div class="verdict-card"
             style="
                border-left: 5px solid {config['color']};
             ">

            <div class="verdict-main">

                <div class="verdict-label">
                    FINAL ASSESSMENT
                </div>

                <div class="verdict-value"
                     style="color:{config['color']};">
                    {_safe(config['label'])}
                </div>

                <div class="verdict-answer">
                    {answer}
                </div>

            </div>


            <div class="score-panel">

                <div class="score-label">
                    THREAT SCORE
                </div>

                <div class="score-number">
                    {score_pct}%
                </div>

                <div class="score-severity"
                     style="color:{config['color']};">
                    { _safe(severity) }
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # SCORE BAR
    # =========================================================

    st.markdown(
        f"""
        <div class="score-track">
            <div
                class="score-fill"
                style="
                    width:{score_pct}%;
                    background:{config['color']};
                ">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # MAIN CONTENT
    # =========================================================

    col1, col2 = st.columns(
        [1.15, 0.85],
        gap="large",
    )

    # =========================================================
    # LEFT
    # =========================================================

    with col1:

        # -----------------------------------------------------
        # WHY THIS RESULT
        # -----------------------------------------------------

        st.markdown(
            """
            <div class="section-heading">
                <div class="section-icon">
                    WHY
                </div>

                <div>
                    <div class="section-title">
                        Analysis & Reasoning
                    </div>

                    <div class="section-caption">
                        Key factors behind the assessment
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        reasoning = (
            action.get("reasoning_why")
            or result.get("reasoning")
            or result.get("explanation")
            or "No detailed reasoning was provided."
        )

        st.markdown(
            f"""
            <div class="reasoning-card">

                <div class="reasoning-text">
                    {_safe(reasoning)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------
        # EVIDENCE
        # -----------------------------------------------------

        st.markdown(
            """
            <div class="section-heading evidence-heading">

                <div class="section-icon">
                    EVD
                </div>

                <div>
                    <div class="section-title">
                        Evidence Signals
                    </div>

                    <div class="section-caption">
                        Correlated indicators identified by the agents
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        if cards:

            for card in cards:

                title = _safe(
                    card.get(
                        "title",
                        "Evidence Signal",
                    )
                )

                details = _safe(
                    card.get(
                        "details",
                        "No additional details available.",
                    )
                )

                severity_card = str(
                    card.get(
                        "severity",
                        "Low",
                    )
                ).capitalize()

                if severity_card.lower() == "high":

                    sev_color = "#dc2626"
                    sev_bg = "#fef2f2"
                    sev_border = "#fecaca"

                elif severity_card.lower() == "medium":

                    sev_color = "#d97706"
                    sev_bg = "#fffbeb"
                    sev_border = "#fde68a"

                else:

                    sev_color = "#059669"
                    sev_bg = "#ecfdf5"
                    sev_border = "#a7f3d0"

                st.markdown(
                    f"""
                    <div class="evidence-card">

                        <div class="evidence-top">

                            <div class="evidence-title">
                                {title}
                            </div>

                            <div
                                class="severity-badge"
                                style="
                                    color:{sev_color};
                                    background:{sev_bg};
                                    border-color:{sev_border};
                                "
                            >
                                {severity_card}
                            </div>

                        </div>

                        <div class="evidence-details">
                            {details}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.markdown(
                """
                <div class="empty-card">
                    No correlated evidence signals were returned.
                </div>
                """,
                unsafe_allow_html=True,
            )

    # =========================================================
    # RIGHT
    # =========================================================

    with col2:

        # -----------------------------------------------------
        # ACTION PANEL
        # -----------------------------------------------------

        st.markdown(
            """
            <div class="section-heading">

                <div class="section-icon action-icon">
                    ACT
                </div>

                <div>
                    <div class="section-title">
                        Recommended Actions
                    </div>

                    <div class="section-caption">
                        What you should consider doing next
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        steps = action.get(
            "action_checklist",
            [],
        ) or []

        action_html = ""

        for i, step in enumerate(steps, 1):

            action_html += f"""
                <div class="action-step">

                    <div class="step-number">
                        {i}
                    </div>

                    <div class="step-text">
                        {_safe(step)}
                    </div>

                </div>
            """

        if not action_html:

            action_html = """
                <div class="empty-card">
                    No specific action recommendations were returned.
                </div>
            """

        st.markdown(
            f"""
            <div class="action-card">
                {action_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------------------------------
        # QUICK SECURITY NOTE
        # -----------------------------------------------------

        st.markdown(
            """
            <div class="security-note">

                <div class="security-note-title">
                    VERITAS SAFETY PRINCIPLE
                </div>

                <div class="security-note-text">
                    Treat suspicious requests cautiously.
                    Verify the sender, source and requested action
                    before sharing information, making payments
                    or opening unknown links.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # CSS
    # =========================================================

    st.markdown(
        """
        <style>

        /* =====================================================
           RESULTS
        ===================================================== */

        .results-heading {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;

            margin: 10px 0 22px 0;
        }

        .results-eyebrow {
            color: #2563eb;

            font-size: 10px;
            font-weight: 800;

            letter-spacing: 1.5px;
            text-transform: uppercase;

            margin-bottom: 5px;
        }

        .results-title {
            color: #111827;

            font-size: 26px;
            font-weight: 750;

            letter-spacing: -0.03em;
        }

        .results-subtitle {
            color: #6b7280;

            font-size: 13px;

            margin-top: 5px;
        }

        .report-chip {
            background: #f0fdf4;
            color: #047857;

            border: 1px solid #bbf7d0;

            border-radius: 999px;

            padding: 7px 12px;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.7px;
        }


        /* =====================================================
           VERDICT
        ===================================================== */

        .verdict-card {
            background: #ffffff;

            border-top: 1px solid #e5e7eb;
            border-right: 1px solid #e5e7eb;
            border-bottom: 1px solid #e5e7eb;

            border-radius: 13px;

            padding: 24px 26px;

            display: flex;
            justify-content: space-between;
            gap: 30px;

            box-shadow:
                0 4px 18px rgba(15, 23, 42, 0.045);
        }

        .verdict-main {
            flex: 1;
            min-width: 0;
        }

        .verdict-label {
            color: #6b7280;

            font-size: 10px;
            font-weight: 800;

            letter-spacing: 1.3px;
        }

        .verdict-value {
            font-size: 29px;
            font-weight: 800;

            letter-spacing: -0.025em;

            margin-top: 5px;
        }

        .verdict-answer {
            color: #374151;

            font-size: 14px;
            line-height: 1.7;

            margin-top: 13px;

            max-width: 760px;
        }


        /* =====================================================
           SCORE
        ===================================================== */

        .score-panel {
            min-width: 150px;

            text-align: right;

            padding-left: 20px;

            border-left: 1px solid #e5e7eb;
        }

        .score-label {
            color: #9ca3af;

            font-size: 9px;
            font-weight: 800;

            letter-spacing: 1px;
        }

        .score-number {
            color: #111827;

            font-size: 30px;
            font-weight: 800;

            line-height: 1.2;

            margin-top: 5px;
        }

        .score-severity {
            font-size: 10px;
            font-weight: 800;

            letter-spacing: 0.8px;

            margin-top: 3px;
        }

        .score-track {
            height: 5px;

            background: #e5e7eb;

            border-radius: 99px;

            margin: 0 0 30px 0;

            overflow: hidden;
        }

        .score-fill {
            height: 100%;

            border-radius: 99px;

            transition: width 0.4s ease;
        }


        /* =====================================================
           SECTION HEADINGS
        ===================================================== */

        .section-heading {
            display: flex;
            align-items: center;

            gap: 11px;

            margin: 4px 0 13px 0;
        }

        .section-icon {
            width: 34px;
            height: 34px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: #eff6ff;
            color: #2563eb;

            border: 1px solid #dbeafe;

            border-radius: 8px;

            font-size: 9px;
            font-weight: 800;

            letter-spacing: 0.5px;
        }

        .action-icon {
            background: #f0fdf4;
            color: #059669;
            border-color: #d1fae5;
        }

        .section-title {
            color: #111827;

            font-size: 15px;
            font-weight: 750;
        }

        .section-caption {
            color: #9ca3af;

            font-size: 11px;

            margin-top: 2px;
        }


        /* =====================================================
           REASONING
        ===================================================== */

        .reasoning-card {
            background: #ffffff;

            border: 1px solid #e5e7eb;

            border-radius: 11px;

            padding: 20px;

            margin-bottom: 28px;

            box-shadow:
                0 2px 10px rgba(15, 23, 42, 0.035);
        }

        .reasoning-text {
            color: #374151;

            font-size: 14px;

            line-height: 1.75;

            white-space: normal;
        }


        /* =====================================================
           EVIDENCE
        ===================================================== */

        .evidence-heading {
            margin-top: 4px;
        }

        .evidence-card {
            background: #ffffff;

            border: 1px solid #e5e7eb;

            border-radius: 10px;

            padding: 16px 18px;

            margin-bottom: 10px;

            transition:
                border-color 0.15s ease,
                box-shadow 0.15s ease;
        }

        .evidence-card:hover {
            border-color: #cbd5e1;

            box-shadow:
                0 4px 14px rgba(15, 23, 42, 0.045);
        }

        .evidence-top {
            display: flex;

            align-items: center;
            justify-content: space-between;

            gap: 15px;
        }

        .evidence-title {
            color: #111827;

            font-size: 13px;
            font-weight: 700;
        }

        .severity-badge {
            border: 1px solid;

            border-radius: 999px;

            padding: 3px 8px;

            font-size: 9px;
            font-weight: 800;

            flex-shrink: 0;
        }

        .evidence-details {
            color: #6b7280;

            font-size: 12px;

            line-height: 1.6;

            margin-top: 8px;
        }


        /* =====================================================
           ACTION CARD
        ===================================================== */

        .action-card {
            background: #ffffff;

            border: 1px solid #e5e7eb;

            border-radius: 11px;

            padding: 8px 18px;

            box-shadow:
                0 2px 10px rgba(15, 23, 42, 0.035);
        }

        .action-step {
            display: flex;

            gap: 13px;

            padding: 16px 0;

            border-bottom: 1px solid #f1f5f9;
        }

        .action-step:last-child {
            border-bottom: none;
        }

        .step-number {
            width: 25px;
            height: 25px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 7px;

            background: #eff6ff;
            color: #2563eb;

            font-size: 11px;
            font-weight: 800;
        }

        .step-text {
            color: #374151;

            font-size: 12px;
            line-height: 1.65;

            padding-top: 2px;
        }


        /* =====================================================
           SECURITY NOTE
        ===================================================== */

        .security-note {
            background: #f8fafc;

            border: 1px solid #e2e8f0;

            border-radius: 10px;

            padding: 17px;

            margin-top: 18px;
        }

        .security-note-title {
            color: #475569;

            font-size: 9px;
            font-weight: 800;

            letter-spacing: 1px;
        }

        .security-note-text {
            color: #64748b;

            font-size: 11px;

            line-height: 1.65;

            margin-top: 6px;
        }


        /* =====================================================
           EMPTY
        ===================================================== */

        .empty-card {
            background: #ffffff;

            border: 1px dashed #cbd5e1;

            border-radius: 10px;

            padding: 22px;

            text-align: center;

            color: #94a3b8;

            font-size: 12px;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media (max-width: 800px) {

            .results-heading {
                align-items: flex-start;
                flex-direction: column;
                gap: 12px;
            }

            .verdict-card {
                flex-direction: column;
            }

            .score-panel {
                border-left: none;
                border-top: 1px solid #e5e7eb;

                padding-left: 0;
                padding-top: 16px;

                text-align: left;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )
