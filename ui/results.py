import streamlit as st

def render_threat_results(result: dict, localization_mode: str):
    verdict = result.get("trust_verdict", "LOW RISK")
    risk = result.get("risk_evaluation", {})
    action = result.get("action_plan", {})
    cards = result.get("evidence_cards", [])

    st.markdown("---")
    st.markdown("### 🔍 MULTI-AGENT INTELLIGENCE ASSESSMENT REPORT")

    # Dynamic Verdict Color Styling
    color_map = {
        "HIGH RISK": "#f85149",
        "NEEDS VERIFICATION": "#d29922",
        "LOW RISK": "#3fb950",
        "INSUFFICIENT EVIDENCE": "#8b949e"
    }
    v_color = color_map.get(verdict, "#8b949e")
    score_pct = int(risk.get('threat_score', 0.0) * 100)

    # Top Verdict Banner
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #161b22 0%, #0d1117 100%); border: 1px solid #30363d; border-left: 8px solid {v_color}; padding: 22px; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 12px; color: #8b949e; letter-spacing: 1px; font-weight: 600;">FINAL TRUST VERDICT</span>
                    <h2 style="margin: 5px 0 0 0; color: {v_color}; font-size: 26px; font-weight: 800; letter-spacing: 0.5px;">{verdict}</h2>
                </div>
                <div style="text-align: right; background: rgba(255,255,255,0.03); padding: 10px 18px; border-radius: 8px; border: 1px solid #30363d;">
                    <span style="font-size: 12px; color: #8b949e;">Threat Vector Score</span>
                    <div style="font-size: 20px; font-weight: 700; color: #f0f6fc;">{score_pct}% <span style="font-size: 12px; color: {v_color};">({risk.get('severity', 'LOW')})</span></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("#### 🧠 Forensic Reasoning (\"Why?\")")
        st.markdown(f"""
            <div style="background: #161b22; border: 1px solid #30363d; padding: 16px; border-radius: 8px; margin-bottom: 20px; color: #c9d1d9; font-size: 14px; line-height: 1.5;">
                {action.get('reasoning_why', 'No detailed reasoning available.')}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📂 Correlated Evidence Cards")
        for card in cards:
            c_sev = card.get('severity', 'Low')
            badge_color = "#f85149" if c_sev == "High" else ("#d29922" if c_sev == "Medium" else "#3fb950")
            st.markdown(f"""
                <div style="background: #161b22; border: 1px solid #30363d; padding: 14px; border-radius: 8px; margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <b style="color: #f0f6fc; font-size: 14px;">{card.get('title')}</b>
                        <span style="background: rgba(255,255,255,0.05); color: {badge_color}; border: 1px solid {badge_color}; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">{c_sev}</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #8b949e; line-height: 1.4;">{card.get('details')}</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🛡️ Recommended Action Checklist")
        steps = action.get("action_checklist", [])
        
        st.markdown("""
            <div style="background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 8px;">
        """, unsafe_allow_html=True)
        
        if localization_mode == "Urdu (اردو)":
            st.markdown("<div dir='rtl'>", unsafe_allow_html=True)
            st.markdown("<b style='color: #58a6ff;'>حفاظتی اقدامات (Actionable Steps):</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 10px 0; color: #e6edf3; font-size: 14px;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        elif localization_mode == "Roman Urdu":
            st.markdown("<b style='color: #58a6ff;'>Aap ko ab kya karna chahiye:</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 10px 0; color: #e6edf3; font-size: 14px;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<b style='color: #58a6ff;'>Immediate Security Protocol:</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 10px 0; color: #e6edf3; font-size: 14px;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)
