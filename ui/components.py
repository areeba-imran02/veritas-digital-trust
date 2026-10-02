import streamlit as st

def render_header():
    st.markdown("""
        <style>
        .veritas-3d-container {
            padding: 10px 0 20px 0;
            border-bottom: 1px solid #30363d;
            margin-bottom: 25px;
        }
        .veritas-wordmark {
            font-size: 38px;
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-shadow: 
                0 1px 0 #cccccc,
                0 2px 0 #c9c9c9,
                0 3px 0 #bbbbbb,
                0 4px 0 #b9b9b9,
                0 5px 0 #aaaaaa,
                0 6px 1px rgba(0,0,0,0.1),
                0 0 5px rgba(0,0,0,0.1),
                0 1px 3px rgba(0,0,0,0.3),
                0 3px 5px rgba(0,0,0,0.4),
                0 5px 10px rgba(0,0,0,0.5),
                0 10px 20px rgba(0,0,0,0.5);
            display: inline-block;
        }
        .veritas-badge {
            font-size: 11px;
            font-weight: 600;
            color: #58a6ff;
            background: rgba(56, 139, 253, 0.1);
            padding: 5px 10px;
            border-radius: 6px;
            border: 1px solid rgba(56, 139, 253, 0.3);
            vertical-align: middle;
            margin-left: 15px;
            letter-spacing: 1px;
        }
        .veritas-subtitle {
            margin: 8px 0 0 0;
            color: #8b949e;
            font-size: 14px;
            font-weight: 400;
        }
        </style>
        
        <div class="veritas-3d-container">
            <div>
                <span class="veritas-wordmark">VERITAS</span>
                <span class="veritas-badge">ENTERPRISE CORE 4.2</span>
            </div>
            <p class="veritas-subtitle">
                Global-First Multimodal Scam Detection & Forensic Threat Intelligence Platform
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_file_dropzone(label: str):
    return st.file_uploader(label, type=["png", "jpg", "jpeg", "pdf", "txt"])

def render_metric_gauge(label: str, value: str):
    st.metric(label=label, value=value)
