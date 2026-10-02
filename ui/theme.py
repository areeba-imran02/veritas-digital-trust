import streamlit as st


def render_html(html: str):
    """
    Streamlit markdown treats lines indented by 4+ spaces as code blocks.
    This strips indentation/blank lines so HTML always renders as HTML.
    """
    cleaned = "\n".join(line.strip() for line in html.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def inject_enterprise_theme():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&family=Noto+Nastaliq+Urdu:wght@400;600&display=swap');

    :root {
        --bg-0: #05070d;
        --bg-1: #0a0e1a;
        --bg-2: #0f1524;
        --bg-3: #151c2e;
        --border: #1e2840;
        --border-soft: #17203a;
        --text: #e8ecf5;
        --text-dim: #a3adc4;
        --text-mute: #6b7794;
        --blue: #3b82f6;
        --blue-2: #2563eb;
        --cyan: #22d3ee;
        --violet: #8b5cf6;
        --red: #ef4444;
        --amber: #f59e0b;
        --green: #10b981;
    }

    /* ---------- Base ---------- */
    html, body, .stApp {
        font-family: 'Inter', -apple-system, 'Segoe UI', sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }
    .stApp {
        background:
            radial-gradient(900px 500px at 8% -5%, rgba(59,130,246,0.14), transparent 60%),
            radial-gradient(800px 480px at 100% 0%, rgba(139,92,246,0.12), transparent 55%),
            linear-gradient(180deg, var(--bg-0) 0%, #070a12 100%);
        color: var(--text);
    }
    .stApp p, .stApp li, .stApp label, .stApp .stMarkdown,
    [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"] p {
        color: var(--text);
    }
    [data-testid="stCaptionContainer"], .stApp small {
        color: var(--text-dim) !important;
    }

    /* Hide default Streamlit chrome */
    #MainMenu, footer { visibility: hidden; }
    header[data-testid="stHeader"] { background: transparent; }

    .block-container {
        max-width: 1240px;
        padding-top: 2.2rem;
        padding-bottom: 4rem;
    }

    /* ---------- Headings ---------- */
    h1, h2, h3, h4, h5 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: -0.02em;
        font-weight: 700 !important;
    }
    h3 { font-size: 1.35rem !important; }
    h4 { font-size: 1.05rem !important; }
    hr { border-color: var(--border) !important; margin: 1.6rem 0 !important; }

    /* ---------- Sidebar ---------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1020 0%, #070a14 100%);
        border-right: 1px solid var(--border);
    }
    [data-testid="stSidebar"] * { color: var(--text); }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 { color: #fff !important; }

    /* ---------- Buttons ---------- */
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.01em;
        padding: 0.7rem 1.2rem;
        border: 1px solid rgba(255,255,255,0.14);
        box-shadow: 0 6px 20px rgba(59,130,246,0.35);
        transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
        width: 100%;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.08);
        box-shadow: 0 10px 28px rgba(99,102,241,0.5);
        border-color: rgba(255,255,255,0.28);
        color: #ffffff !important;
    }
    .stButton > button:active { transform: translateY(0); }
    .stButton > button p { color: #ffffff !important; font-weight: 600; }

    /* ---------- Tabs ---------- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: var(--bg-1);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid var(--border);
    }
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        color: var(--text-dim);
        border-radius: 8px;
        font-weight: 500;
        background: transparent;
        padding: 0 18px;
        transition: all .2s;
    }
    .stTabs [data-baseweb="tab"]:hover { color: #fff; background: rgba(255,255,255,0.04); }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(59,130,246,0.25), rgba(139,92,246,0.22)) !important;
        color: #ffffff !important;
        box-shadow: inset 0 0 0 1px rgba(99,130,246,0.45);
    }
    .stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

    /* ---------- Inputs ---------- */
    .stTextArea textarea, .stTextInput input, .stNumberInput input {
        background-color: var(--bg-1) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
    .stTextArea textarea::placeholder, .stTextInput input::placeholder { color: var(--text-mute) !important; }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.22) !important;
    }

    /* Selectbox / radio / dropdown */
    [data-baseweb="select"] > div {
        background-color: var(--bg-1) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        color: var(--text) !important;
    }
    [data-baseweb="select"] * { color: var(--text) !important; }
    [data-baseweb="popover"] ul, [data-baseweb="menu"] {
        background-color: var(--bg-2) !important;
        border: 1px solid var(--border);
    }
    [data-baseweb="popover"] li:hover { background-color: var(--bg-3) !important; }
    .stRadio label, .stCheckbox label { color: var(--text) !important; }

    /* ---------- File uploader ---------- */
    [data-testid="stFileUploaderDropzone"] {
        background: linear-gradient(135deg, rgba(59,130,246,0.06), rgba(139,92,246,0.05));
        border: 1.5px dashed #2e3b5e;
        border-radius: 14px;
        padding: 1.4rem;
        transition: all .2s;
    }
    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: var(--blue);
        background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(139,92,246,0.09));
    }
    [data-testid="stFileUploaderDropzone"] * { color: var(--text-dim) !important; }
    [data-testid="stFileUploaderDropzone"] button {
        background: var(--bg-3) !important;
        color: #fff !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        width: auto;
        box-shadow: none;
    }
    [data-testid="stFileUploaderFile"] * { color: var(--text) !important; }

    /* ---------- Expander / alerts ---------- */
    [data-testid="stExpander"] {
        background: var(--bg-1);
        border: 1px solid var(--border);
        border-radius: 12px;
    }
    [data-testid="stExpander"] summary p { color: var(--text) !important; font-weight: 600; }
    [data-testid="stAlert"] { border-radius: 12px; }

    /* ---------- Metrics ---------- */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, var(--bg-2), var(--bg-1));
        border: 1px solid var(--border);
        padding: 14px 18px;
        border-radius: 14px;
    }
    [data-testid="stMetricLabel"] p { color: var(--text-dim) !important; font-size: 0.8rem; letter-spacing: .08em; text-transform: uppercase; }
    [data-testid="stMetricValue"] { color: #fff !important; font-weight: 800; }

    /* =========================================================
       Custom components
       ========================================================= */

    /* ----- Header ----- */
    .vt-header {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(600px 220px at 0% 0%, rgba(59,130,246,0.22), transparent 60%),
            radial-gradient(500px 220px at 100% 100%, rgba(139,92,246,0.20), transparent 60%),
            linear-gradient(135deg, #0c1224 0%, #0a0f1e 100%);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 30px 36px;
        margin-bottom: 28px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        flex-wrap: wrap;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .vt-header::after {
        content: "";
        position: absolute; inset: 0;
        background-image: linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
        background-size: 36px 36px;
        mask-image: linear-gradient(90deg, transparent, #000 70%);
        -webkit-mask-image: linear-gradient(90deg, transparent, #000 70%);
        pointer-events: none;
    }
    .vt-header > * { position: relative; z-index: 1; }
    .vt-brand { display: flex; align-items: center; gap: 18px; }
    .vt-logo {
        width: 56px; height: 56px;
        border-radius: 16px;
        display: flex; align-items: center; justify-content: center;
        font-size: 28px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        box-shadow: 0 8px 24px rgba(99,102,241,0.5), inset 0 1px 0 rgba(255,255,255,0.35);
    }
    .vt-title {
        margin: 0 !important;
        font-size: 40px !important;
        font-weight: 900 !important;
        letter-spacing: 0.22em !important;
        line-height: 1.1 !important;
        text-transform: uppercase;
        background: linear-gradient(180deg, #ffffff 20%, #9fb4e6 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent !important;
    }
    .vt-subtitle {
        margin: 8px 0 0 0 !important;
        color: var(--text-dim) !important;
        font-size: 14.5px;
        font-weight: 400;
        letter-spacing: 0.01em;
    }
    .vt-badge {
        display: inline-flex; align-items: center; gap: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11.5px; font-weight: 700;
        color: #7dd3fc;
        background: rgba(34,211,238,0.08);
        border: 1px solid rgba(34,211,238,0.35);
        padding: 8px 14px;
        border-radius: 999px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .vt-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #22d3ee;
        box-shadow: 0 0 0 0 rgba(34,211,238,0.7);
        animation: vt-pulse 2s infinite;
    }
    @keyframes vt-pulse {
        0% { box-shadow: 0 0 0 0 rgba(34,211,238,0.6); }
        70% { box-shadow: 0 0 0 9px rgba(34,211,238,0); }
        100% { box-shadow: 0 0 0 0 rgba(34,211,238,0); }
    }

    /* ----- Section titles ----- */
    .vt-section {
        display: flex; align-items: center; gap: 10px;
        margin: 4px 0 14px 0;
        font-size: 15px; font-weight: 700;
        color: #ffffff;
        letter-spacing: 0.01em;
    }
    .vt-section .vt-section-bar {
        width: 4px; height: 18px; border-radius: 4px;
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
    }
    .vt-report-title {
        display: flex; align-items: center; gap: 12px;
        font-size: 13px; font-weight: 700;
        letter-spacing: 0.18em; text-transform: uppercase;
        color: var(--text-dim);
        margin: 6px 0 18px 0;
    }
    .vt-report-title::after {
        content: ""; flex: 1; height: 1px;
        background: linear-gradient(90deg, var(--border), transparent);
    }

    /* ----- Cards ----- */
    .vt-card {
        background: linear-gradient(145deg, var(--bg-2) 0%, var(--bg-1) 100%);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.28), inset 0 1px 0 rgba(255,255,255,0.03);
    }
    .vt-card-text {
        color: #d5dbea;
        font-size: 14.5px;
        line-height: 1.75;
        margin: 0;
    }

    /* ----- Verdict banner ----- */
    .vt-verdict {
        position: relative;
        display: flex; justify-content: space-between; align-items: center;
        gap: 28px; flex-wrap: wrap;
        padding: 26px 30px;
        margin-bottom: 26px;
        border-radius: 18px;
        border: 1px solid var(--border);
        box-shadow: 0 16px 40px rgba(0,0,0,0.45);
        overflow: hidden;
    }
    .vt-verdict-label {
        font-size: 11px; font-weight: 700;
        letter-spacing: 0.2em; text-transform: uppercase;
        color: var(--text-dim);
    }
    .vt-verdict-value {
        margin: 8px 0 0 0 !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        letter-spacing: 0.01em !important;
        line-height: 1.15 !important;
    }
    .vt-score-box {
        min-width: 280px; flex: 0 1 340px;
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px 20px;
    }
    .vt-score-top {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 10px;
    }
    .vt-score-label { font-size: 12px; color: var(--text-dim); font-weight: 600; letter-spacing: .04em; }
    .vt-score-num { font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 700; color: #fff; }
    .vt-score-sev { font-size: 12px; font-weight: 700; letter-spacing: .08em; margin-left: 6px; }
    .vt-bar { width: 100%; height: 8px; border-radius: 999px; background: #121a2e; overflow: hidden; }
    .vt-bar > div { height: 100%; border-radius: 999px; }

    /* ----- Evidence cards ----- */
    .vt-evidence { padding: 16px 18px; margin-bottom: 12px; }
    .vt-evidence-head {
        display: flex; justify-content: space-between; align-items: flex-start;
        gap: 12px; margin-bottom: 8px;
    }
    .vt-evidence-title { color: #fff; font-size: 14.5px; font-weight: 600; line-height: 1.4; }
    .vt-evidence-body { margin: 0; font-size: 13.5px; color: var(--text-dim); line-height: 1.65; }
    .vt-sev-pill {
        flex-shrink: 0;
        font-size: 10.5px; font-weight: 800;
        letter-spacing: 0.1em; text-transform: uppercase;
        padding: 4px 11px; border-radius: 999px;
    }

    /* ----- Checklist ----- */
    .vt-check-head {
        color: #93c5fd; font-size: 14px; font-weight: 700;
        letter-spacing: 0.06em; text-transform: uppercase;
        padding-bottom: 14px; margin-bottom: 6px;
        border-bottom: 1px solid var(--border);
    }
    .vt-step {
        display: flex; gap: 14px; align-items: flex-start;
        padding: 13px 0;
        border-bottom: 1px dashed var(--border-soft);
    }
    .vt-step:last-child { border-bottom: none; }
    .vt-step-num {
        flex-shrink: 0;
        width: 28px; height: 28px; border-radius: 9px;
        display: flex; align-items: center; justify-content: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px; font-weight: 700; color: #fff;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        box-shadow: 0 4px 12px rgba(99,102,241,0.4);
    }
    .vt-step-text { color: var(--text); font-size: 14.5px; line-height: 1.65; padding-top: 2px; }
    .vt-empty { color: var(--text-mute); font-size: 14px; padding: 8px 0; }

    /* ----- Urdu / RTL ----- */
    .vt-rtl { direction: rtl; text-align: right; }
    .vt-rtl .vt-step-text, .vt-rtl .vt-check-head {
        font-family: 'Noto Nastaliq Urdu', 'Inter', serif;
        line-height: 2.3;
        letter-spacing: 0;
        text-transform: none;
    }
    .vt-rtl .vt-step-text { font-size: 16px; }

    /* ----- Metric card ----- */
    .vt-metric {
        background: linear-gradient(145deg, var(--bg-2), var(--bg-1));
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px 20px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }
    .vt-metric-label {
        font-size: 11px; font-weight: 700; letter-spacing: .14em;
        text-transform: uppercase; color: var(--text-dim);
    }
    .vt-metric-value {
        margin-top: 6px;
        font-size: 26px; font-weight: 800; color: #fff;
        font-family: 'JetBrains Mono', monospace;
    }

    @media (max-width: 768px) {
        .vt-title { font-size: 28px !important; letter-spacing: .14em !important; }
        .vt-header { padding: 22px; }
        .vt-verdict-value { font-size: 24px !important; }
        .vt-score-box { min-width: 100%; }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
