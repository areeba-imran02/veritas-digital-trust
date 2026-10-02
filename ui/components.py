import streamlit as st

def render_header():
    st.markdown("""
        <style>
        .veritas-header-box {
            background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
            border: 1px solid #1f2937;
            padding: 24px 32px;
            border-radius: 16px;
            margin-bottom: 24px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .veritas-title-3d {
            font-size: 42px;
            font-weight: 900;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            text-shadow: 
                0 1px 0 #cbd5e1,
                0 2px 0 #94a3b8,
                0 3px 0 #64748b,
                0 4px 0 #475569,
                0 5px 0 #334155,
                0 6px 1px rgba(0,0,0,0.2),
                0 0 10px rgba(59, 130, 246, 0.5),
                0 10px 20px rgba(0, 0, 0, 0.6);
            margin: 0;
        }
        .veritas-badge-modern {
            font-size: 12px;
            font-weight: 700;
            color: #60a5fa;
            background: rgba(59, 130, 246, 0.15);
            padding: 6px 12px;
            border-radius: 20px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }
        .veritas-subtext {
            color: #9ca3af;
            font-size: 15px;
            margin-top: 8px;
            margin-bottom: 0;
            font-weight: 400;
        }
        </style>
        
        <div class="veritas-header-box">
            <div>
                <h1 class="veritas-title-3d">VERITAS</h1>
                <p class="veritas-subtext">
                    Enterprise Multimodal Threat Intelligence & Advanced Scam Detection Platform
                </p>
            </div>
            <div>
                <span class="veritas-badge-modern">CORE v4.2 SECURE</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_file_dropzone(label: str):
    return st.file_uploader(label, type=["png", "jpg", "jpeg", "pdf", "txt"])

def render_metric_gauge(label: str, value: str):
    st.metric(label=label, value=value)
