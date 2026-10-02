import streamlit as st

def render_threat_results(result: dict, localization_mode: str):
    verdict = result.get("trust_verdict", "LOW RISK")
    risk = result.get("risk_evaluation", {})
    action = result.get("action_plan", {})
    cards = result.get("evidence_cards", [])

    st.markdown("---")
    st.markdown("### 📊 MULTI-AGENT INTELLIGENCE ASSESSMENT REPORT")

    # रंग योजना (Color Mapping)
    color_map = {
        "HIGH RISK": "#ef4444",
        "NEEDS VERIFICATION": "#f59e0b",
        "LOW RISK": "#10b981",
        "INSUFFICIENT EVIDENCE": "#6b7280"
    }
    v_color = color_map.get(verdict, "#6b7280")
    score_pct = int(risk.get('threat_score', 0.0) * 100)

    # मुख्य वर्डिक्ट बैनर
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #111827 0%, #030712 100%); border: 1px solid #1f2937; border-left: 6px solid {v_color}; padding: 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.4);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 11px; color: #9ca3af; letter-spacing: 1.5px; font-weight: 700; text-transform: uppercase;">FINAL TRUST VERDICT</span>
                    <h2 style="margin: 6px 0 0 0; color: {v_color}; font-size: 28px; font-weight: 800; letter-spacing: 0.5px;">{verdict}</h2>
                </div>
                <div style="text-align: right; background: rgba(255,255,255,0.03); padding: 12px 20px; border-radius: 10px; border: 1px solid #1f2937;">
                    <span style="font-size: 12px; color: #9ca3af; font-weight: 500;">Threat Vector Score</span>
                    <div style="font-size: 22px; font-weight: 700; color: #ffffff;">{score_pct}% <span style="font-size: 13px; color: {v_color};">({risk.get('severity', 'LOW')})</span></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### 🧠 Forensic Reasoning (\"Why?\")")
        st.markdown(f"""
            <div style="background: #111827; border: 1px solid #1f2937; padding: 18px; border-radius: 12px; margin-bottom: 20px; color: #d1d5db; font-size: 14px; line-height: 1.6; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                {action.get('reasoning_why', 'No detailed reasoning available.')}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📂 Correlated Evidence Cards")
        for card in cards:
            c_sev = card.get('severity', 'Low')
            badge_bg = "#ef444420" if c_sev == "High" else ("#f59e0b20" if c_sev == "Medium" else "#10b98120")
            badge_color = "#ef4444" if c_sev == "High" else ("#f59e0b" if c_sev == "Medium" else "#10b981")
            
            st.markdown(f"""
                <div style="background: #111827; border: 1px solid #1f2937; padding: 16px; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <b style="color: #ffffff; font-size: 14px; font-weight: 600;">{card.get('title')}</b>
                        <span style="background: {badge_bg}; color: {badge_color}; border: 1px solid {badge_color}40; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: 700;">{c_sev}</span>
                    </div>
                    <p style="margin: 0; font-size: 13px; color: #9ca3af; line-height: 1.5;">{card.get('details')}</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🛡️ Recommended Action Checklist")
        steps = action.get("action_checklist", [])
        
        st.markdown("""
            <div style="background: #111827; border: 1px solid #1f2937; padding: 22px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
        """, unsafe_allow_html=True)
        
        if localization_mode == "Urdu (اردو)":
            st.markdown("<div dir='rtl'>", unsafe_allow_html=True)
            st.markdown("<b style='color: #60a5fa; font-size: 15px;'>حفاظتی اقدامات (Actionable Steps):</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 12px 0; color: #f3f4f6; font-size: 14px; line-height: 1.5;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        elif localization_mode == "Roman Urdu":
            st.markdown("<b style='color: #60a5fa; font-size: 15px;'>Aap ko ab kya karna chahiye:</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 12px 0; color: #f3f4f6; font-size: 14px; line-height: 1.5;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<b style='color: #60a5fa; font-size: 15px;'>Immediate Security Protocol:</b>", unsafe_allow_html=True)
            for i, step in enumerate(steps, 1):
                st.markdown(f"<p style='margin: 12px 0; color: #f3f4f6; font-size: 14px; line-height: 1.5;'><b>{i}.</b> {step}</p>", unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)
