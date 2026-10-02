import streamlit as st
import os
from core.config import Config
from core.orchestrator import Orchestrator
from ui.theme import inject_enterprise_theme
from ui.components import render_header, render_file_dropzone, render_metric_gauge
from ui.results import render_threat_results

st.set_page_config(
    page_title="VERITAS | Enterprise Threat Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_enterprise_theme()

def main():
    render_header()
    
    # Sidebar Configuration & Localization
    st.sidebar.markdown("### PLATFORM CONTROLS")
    localization_mode = st.sidebar.selectbox("Localization Layer", ["English", "Urdu (اردو)", "Roman Urdu"])
    scan_mode = st.sidebar.selectbox("Analysis Engine", ["Full Multimodal Deep Scan", "Fast Heuristic Scan", "Forensic Artifact Correlation"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### SYSTEM STATUS")
    api_status = "Online (Groq LPU Active)" if os.environ.get("GROQ_API_KEY") else "Offline (Running Heuristic Fallback)"
    st.sidebar.markdown(f"**Groq API:** {api_status}")
    st.sidebar.markdown(f"**Region:** Pakistan (PK) / Global Edge")
    st.sidebar.markdown(f"**Engine Version:** 4.2.0-Enterprise")

    # Main Input Interface
    st.markdown("### Multimodal Artifact Ingestion")
    
    tab_text, tab_url, tab_media, tab_qr, tab_audio = st.tabs([
        "Text / Email", "URL / Domain", "Image / Screenshot", "QR Code", "Audio / Voice Note"
    ])
    
    input_payload = {}
    
    with tab_text:
        text_input = st.text_area("Paste suspicious message, SMS, or email content:", height=150, placeholder="e.g., Dear user, your account has been suspended. Click here to verify your credentials immediately...")
        sender_id = st.text_input("Sender Identifier (Phone number, email address, or handle):", placeholder="e.g., +923001234567 or support@secure-bank-update.com")
        if text_input or sender_id:
            input_payload = {"type": "text", "content": text_input, "sender": sender_id}

    with tab_url:
        url_input = st.text_input("Enter target URL or suspicious link:", placeholder="https://login-verify-bank-pk.com/auth")
        if url_input:
            input_payload = {"type": "url", "url": url_input}

    with tab_media:
        uploaded_image = st.file_uploader("Upload chat screenshot or payment receipt image", type=["png", "jpg", "jpeg"])
        if uploaded_image:
            input_payload = {"type": "screenshot", "file": uploaded_image}

    with tab_qr:
        uploaded_qr = st.file_uploader("Upload QR code image", type=["png", "jpg", "jpeg"])
        if uploaded_qr:
            input_payload = {"type": "qr", "file": uploaded_qr}

    with tab_audio:
        uploaded_audio = st.file_uploader("Upload voice note or intercepted audio call (.wav, .mp3)", type=["wav", "mp3", "m4a"])
        if uploaded_audio:
            input_payload = {"type": "audio", "file": uploaded_audio}

    st.markdown("---")
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        run_scan = st.button("INITIATE THREAT INTELLIGENCE SCAN", type="primary", use_container_width=True)
    with col2:
        clear_cache = st.button("Reset Pipeline", use_container_width=True)
        if clear_cache:
            st.rerun()

    if run_scan:
        if not input_payload:
            st.error("Please provide at least one ingestion artifact before running the scan.")
            return

        with st.status("Executing Multi-Agent Threat Intelligence Pipeline...", expanded=True) as status:
            st.write("Routing payload to specialized analyzers...")
            orchestrator = Orchestrator()
            
            st.write("Executing Content & Identity Agents...")
            st.write("Evaluating Risk Vectors & Evidence Correlation...")
            
            result = orchestrator.analyze(input_payload)
            status.update(label="Threat Intelligence Analysis Complete.", state="complete", expanded=False)

        render_threat_results(result, localization_mode)

if __name__ == "__main__":
    main()
