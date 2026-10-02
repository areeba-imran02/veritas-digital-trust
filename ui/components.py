import streamlit as st

def render_header():
    st.markdown("""
        <div style="border-bottom: 1px solid #30363d; padding-bottom: 15px; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 28px; letter-spacing: -0.5px; color: #f0f6fc;">
                VERITAS <span style="font-size: 14px; font-weight: 400; color: #8b949e; background: #21262d; padding: 4px 8px; border-radius: 4px; border: 1px solid #30363d;">ENTERPRISE THREAT INTELLIGENCE</span>
            </h1>
            <p style="margin: 5px 0 0 0; color: #8b949e; font-size: 14px;">
                Global-First Multimodal Scam Detection & Forensic Artifact Correlation Platform
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_file_dropzone(label: str):
    return st.file_uploader(label, type=["png", "jpg", "jpeg", "pdf", "txt"])

def render_metric_gauge(label: str, value: str):
    st.metric(label=label, value=value)
