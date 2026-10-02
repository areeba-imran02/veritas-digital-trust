import streamlit as st

def render_threat_results(result: dict, localization_mode: str):
    verdict = result.get("trust_verdict", "LOW RISK")
    risk = result.get("risk_evaluation", {})
    action = result.get("action_plan", {})
    cards = result.get("evidence_cards", [])

    st.markdown("---")
    st.markdown("### THREAT INTELLIGENCE ASSESSMENT")

    # Verdict Badge Styling
    color_map = {
        "HIGH RISK": "#da3633",
        "NEEDS VERIFICATION": "#d29922",
        "LOW RISK": "#238636",
        "INSUFFICIENT EVIDENCE": "#8b949e"
    }
    v_color = color_map.get(verdict, "#8b949e")

    st.markdown(f"""
        <div style="background-color: #161b22; border: 1px solid #30363d; border-left: 6px solid {v_color}; padding: 20px; border-radius: 6px; margin-bottom: 20px;">
            <h3 style="margin: 0 0 10px 0; color: {v_color}; font-size: 22px;">VERDICT: {verdict}</h3>
            <p style="margin: 0; color: #8b949e; font-size: 14px;">Calculated Threat Vector Score: <b>{risk.get('threat_score', 0.0)} / 1.0 ({risk.get('severity', 'LOW')} SEVERITY)</b></p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Evidence & Reasoning Trail (\"Why?\")")
        st.info(action.get("reasoning_why", "No detailed reasoning available."))
        
        st.markdown("#### Correlated Evidence Artifacts")
        for card in cards:
            st.markdown(f"""
                <div style="background: #161b22; border: 1px solid #30363d; padding: 12px; border-radius: 6px; margin-bottom: 10px;">
                    <b style="color: #f0f6fc;">{card.get('title')}</b> <span style="float: right; color: #8b949e; font-size: 12px;">Severity: {card.get('severity')}</span>
                    <p style="margin: 5px 0 0 0; font-size: 13px; color: #8b949e;">{card.get('details')}</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Actionable Next Steps")
        steps = action.get("action_checklist", [])
        
        # Localization text translation wrappers if Urdu / Roman Urdu requested
        if localization_mode == "Urdu (اردو)":
            st.markdown("<div dir='rtl'>", unsafe_allow_html=True)
            st.markdown("**حفاظتی اقدامات (Actionable Steps):**")
            for step in steps:
                st.markdown(f"- {step}")
            st.markdown("</div>", unsafe_allow_html=True)
        elif localization_mode == "Roman Urdu":
            st.markdown("**Aap ko ab kya karna chahiye:**")
            for step in steps:
                st.markdown(f"- {step}")
        else:
            for i, step in enumerate(steps, 1):
                st.markdown(f"**{i}.** {step}")