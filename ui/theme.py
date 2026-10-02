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
        /* Light content palette */
        --ink: #0f172a;
        --text: #1e293b;
        --text-dim: #475569;
        --text-mute: #64748b;
        --surface: #ffffff;
        --surface-2: #f8fafc;
        --line: #dbe3f0;
        --line-soft: #e8eef8;

        /* Dark surfaces (sidebar / hero) */
        --navy-0: #070b17;
        --navy-1: #0b1226;
        --navy-2: #121a33;
        --navy-line: #1d2848;
        --on-dark: #e8ecf5;
        --on-dark-dim: #aeb9d3;

        --blue: #3b82f6;
        --indigo: #6366f1;
        --violet: #8b5cf6;
        --cyan: #22d3ee;
    }

    /* =========================================================
       BASE
       ========================================================= */
    html, body, .stApp {
        font-family: 'Inter', -apple-system, 'Segoe UI', sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }
    .stApp {
        background:
            radial-gradient(900px 480px at 85% -8%, rgba(99,102,241,0.12), transparent 60%),
            radial-gradient(800px 460px at 5% 0%, rgba(59,130,246,0.10), transparent 60%),
            linear-gradient(180deg, #eef2fa 0%, #f6f8fc 100%);
        color: var(--text);
    }
    /* zero-specificity so component classes can override freely */
    :where(.stApp p, .stApp li, .stApp label) { color: var(--text); }
    [data-testid="stCaptionContainer"] { color: var(--text-mute) !important; }

    #MainMenu, footer { visibility: hidden; }
    header[data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"], [data-testid="stToolbar"] * { color: #334155 !important; }

    .block-container {
        max-width: 1240px;
        padding-top: 2.4rem;
        padding-bottom: 4rem;
    }

    /* Headings (main area) */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5 {
        color: var(--ink) !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: -0.02em;
        font-weight: 800 !important;
    }
    .stApp h2 { font-size: 1.7rem !important; }
    .stApp h3 { font-size: 1.35rem !important; }
    .stApp h4 { font-size: 1.05rem !important; }
    hr { border-color: var(--line) !important; margin: 1.6rem 0 !important; }

    /* =========================================================
       SIDEBAR (dark)
       ========================================================= */
    [data-testid="stSidebar"] {
        background:
            radial-gradient(500px 260px at 0% 0%, rgba(59,130,246,0.16), transparent 65%),
            linear-gradient(180deg, var(--navy-1) 0%, var(--navy-0) 100%);
        border-right: 1px solid var(--navy-line);
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] small,
    [data-testid="stSidebar"] label { color: var(--on-dark-dim); }
    [data-testid="stSidebar"] strong { color: #93c5fd; font-weight: 600; }

    /* Sidebar section headings -> small clean caps with accent bar */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4 {
        color: #ffffff !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.18em !important;
        text-transform: uppercase;
        padding: 0 0 12px 12px !important;
        margin: 8px 0 14px 0 !important;
        border-bottom: 1px solid var(--navy-line);
        position: relative;
    }
    [data-testid="stSidebar"] h1::before, [data-testid="stSidebar"] h2::before,
    [data-testid="stSidebar"] h3::before, [data-testid="stSidebar"] h4::before {
        content: "";
        position: absolute; left: 0; top: 2px;
        width: 4px; height: 16px; border-radius: 4px;
        background: linear-gradient(180deg, var(--blue), var(--violet));
    }
    [data-testid="stSidebar"] hr { border-color: var(--navy-line) !important; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: #cbd5e1 !important;
        font-size: 0.85rem; font-weight: 500;
    }

    /* Sidebar select boxes -> dark glass */
    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="select"] > div > div {
        background-color: #141d38 !important;
        border-color: #26335a !important;
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] > div { border: 1px solid #26335a !important; }
    [data-testid="stSidebar"] [data-baseweb="select"] * { color: #ffffff !important; }
    [data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #93c5fd !important; }
    [data-testid="stSidebar"] [data-baseweb="select"]:hover > div { border-color: var(--blue) !important; }

    /* =========================================================
       BUTTONS
       ========================================================= */
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.72rem 1.2rem;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 20px rgba(79,102,241,0.30);
        transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
        width: 100%;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.07);
        box-shadow: 0 12px 28px rgba(79,102,241,0.42);
        color: #ffffff !important;
    }
    .stButton > button:active { transform: translateY(0); }
    .stButton > button p, .stDownloadButton > button p { color: #ffffff !important; font-weight: 600; }

    /* =========================================================
       TABS (light, clean underline)
       ========================================================= */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: transparent;
        padding: 0;
        border: none;
        border-bottom: 1px solid var(--line);
    }
    .stTabs [data-baseweb="tab"] {
        height: 46px;
        padding: 0 16px;
        background: transparent;
        color: var(--text-mute);
        font-weight: 500;
        border-radius: 8px 8px 0 0;
        transition: color .2s, background .2s;
    }
    .stTabs [data-baseweb="tab"] p { color: inherit !important; font-weight: inherit; }
    .stTabs [data-baseweb="tab"]:hover { color: var(--ink); background: rgba(59,130,246,0.06); }
    .stTabs [aria-selected="true"] {
        color: #1d4ed8 !important;
        font-weight: 700 !important;
        background: transparent !important;
        box-shadow: none !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
        height: 3px !important;
        border-radius: 3px;
    }
    .stTabs [data-baseweb="tab-border"] { background: transparent !important; }

    /* =========================================================
       INPUTS (light)
       ========================================================= */
    [data-testid="stWidgetLabel"] p { color: var(--text) !important; font-weight: 600; font-size: 0.92rem; }

    [data-baseweb="textarea"], [data-baseweb="input"], [data-baseweb="base-input"] {
        background-color: var(--surface) !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        box-shadow: 0 1px 2px rgba(15,23,42,0.04);
        transition: border-color .15s, box-shadow .15s;
    }
    [data-baseweb="textarea"]:focus-within, [data-baseweb="input"]:focus-within, [data-baseweb="base-input"]:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.20) !important;
    }
    .stTextArea textarea, .stTextInput input, .stNumberInput input {
        background-color: transparent !important;
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        line-height: 1.65 !important;
        border: none !important;
        box-shadow: none !important;
    }
    .stTextArea textarea::placeholder, .stTextInput input::placeholder {
        color: #94a3b8 !important;
        -webkit-text-fill-color: #94a3b8 !important;
    }

    /* Select boxes in main area (light) */
    [data-testid="stMain"] [data-baseweb="select"] > div,
    [data-testid="stMain"] [data-baseweb="select"] > div > div {
        background-color: var(--surface) !important;
        color: var(--ink) !important;
    }
    [data-testid="stMain"] [data-baseweb="select"] > div { border: 1px solid #cbd5e1 !important; border-radius: 12px !important; }
    [data-testid="stMain"] [data-baseweb="select"] * { color: var(--ink) !important; }

    /* Dropdown popup (rendered outside sidebar, so style globally) */
    [data-baseweb="popover"] [data-baseweb="menu"], [data-baseweb="popover"] ul {
        background-color: #ffffff !important;
        border: 1px solid var(--line);
        border-radius: 12px;
        box-shadow: 0 16px 40px rgba(15,23,42,0.18);
    }
    [data-baseweb="popover"] li, [data-baseweb="popover"] li * { color: var(--ink) !important; }
    [data-baseweb="popover"] li:hover, [data-baseweb="popover"] li[aria-selected="true"] {
        background-color: #eaf1ff !important;
    }

    .stRadio label, .stCheckbox label { color: var(--text) !important; }

    /* =========================================================
       FILE UPLOADER (light)
       ========================================================= */
    [data-testid="stFileUploaderDropzone"] {
        background: linear-gradient(135deg, #ffffff, #f3f7ff);
        border: 1.5px dashed #aebbd6;
        border-radius: 14px;
        padding: 1.5rem;
        transition: all .2s;
    }
    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: var(--blue);
        background: linear-gradient(135deg, #ffffff, #e9f1ff);
    }
    [data-testid="stFileUploaderDropzone"] * { color: var(--text-dim) !important; }
    [data-testid="stFileUploaderDropzone"] button {
        background: linear-gradient(135deg, #0f172a, #1e293b) !important;
        border: 1px solid #0f172a !important;
        border-radius: 8px !important;
        width: auto; box-shadow: none; transform: none;
    }
    [data-testid="stFileUploaderDropzone"] button, [data-testid="stFileUploaderDropzone"] button * { color: #ffffff !important; }
    [data-testid="stFileUploaderFile"] * { color: var(--text) !important; }

    /* Expander / alert / metric */
    [data-testid="stExpander"] {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
    }
    [data-testid="stExpander"] summary p { color: var(--ink) !important; font-weight: 600; }
    [data-testid="stAlert"] { border-radius: 12px; }
    [data-testid="stMetric"] {
        background: var(--surface);
        border: 1px solid var(--line);
        padding: 14px 18px;
        border-radius: 14px;
    }
    [data-testid="stMetricLabel"] p { color: var(--text-mute) !important; font-size: 0.78rem; letter-spacing: .08em; text-transform: uppercase; }
    [data-testid="stMetricValue"] { color: var(--ink) !important; font-weight: 800; }

    /* =========================================================
       CUSTOM COMPONENTS
       ========================================================= */

    /* ----- Header (dark hero) ----- */
    .vt-header {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(620px 240px at 0% 0%, rgba(59,130,246,0.30), transparent 60%),
            radial-gradient(520px 240px at 100% 100%, rgba(139,92,246,0.30), transparent 60%),
            linear-gradient(135deg, #0d1530 0%, #0a1024 100%);
        border: 1px solid #1f2b52;
        border-radius: 22px;
        padding: 32px 38px;
        margin-bottom: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        flex-wrap: wrap;
        box-shadow: 0 22px 50px rgba(15,23,42,0.28), inset 0 1px 0 rgba(255,255,255,0.06);
    }
    .vt-header::after {
        content: "";
        position: absolute; inset: 0;
        background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
        background-size: 36px 36px;
        mask-image: linear-gradient(90deg, transparent, #000 75%);
        -webkit-mask-image: linear-gradient(90deg, transparent, #000 75%);
        pointer-events: none;
    }
    .vt-header > * { position: relative; z-index: 1; }
    .vt-brand { display: flex; align-items: center; gap: 22px; flex: 1 1 520px; min-width: 0; }
    .vt-logo {
        flex-shrink: 0;
        width: 64px; height: 64px;
        border-radius: 18px;
        display: flex; align-items: center; justify-content: center;
        font-size: 30px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        box-shadow: 0 10px 26px rgba(99,102,241,0.55), inset 0 1px 0 rgba(255,255,255,0.4);
    }

    /* Clean 3D title: gradient face + stacked extrusion via drop-shadow */
    .vt-title {
        margin: 0 !important;
        padding: 0 0 6px 0 !important;
        font-size: 46px !important;
        font-weight: 900 !important;
        letter-spacing: 0.2em !important;
        line-height: 1.1 !important;
        text-transform: uppercase;
        background: linear-gradient(180deg, #ffffff 0%, #dbe7ff 55%, #a9c2ff 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent !important;
        filter:
            drop-shadow(0 1px 0 #3b6fe0)
            drop-shadow(0 1px 0 #3262cc)
            drop-shadow(0 1px 0 #2a55b8)
            drop-shadow(0 1px 0 #2349a3)
            drop-shadow(0 1px 0 #1c3d8e)
            drop-shadow(0 10px 14px rgba(2,6,23,0.55));
    }
    .vt-subtitle {
        margin: 10px 0 0 0 !important;
        color: var(--on-dark-dim) !important;
        font-size: 14.5px;
        font-weight: 400;
        line-height: 1.5;
    }
    .vt-badge {
        display: inline-flex; align-items: center; gap: 9px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11.5px; font-weight: 700;
        color: #7dd3fc;
        background: rgba(34,211,238,0.10);
        border: 1px solid rgba(34,211,238,0.40);
        padding: 9px 16px;
        border-radius: 999px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .vt-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #22d3ee;
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
        color: var(--ink);
    }
    .vt-section .vt-section-bar {
        width: 4px; height: 18px; border-radius: 4px;
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
    }
    .vt-report-title {
        display: flex; align-items: center; gap: 12px;
        font-size: 12.5px; font-weight: 700;
        letter-spacing: 0.18em; text-transform: uppercase;
        color: var(--text-dim);
        margin: 6px 0 18px 0;
    }
    .vt-report-title::after {
        content: ""; flex: 1; height: 1px;
        background: linear-gradient(90deg, var(--line), transparent);
    }

    /* ----- Cards (white) ----- */
    .vt-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 16px;
        box-shadow: 0 6px 18px rgba(15,23,42,0.06);
    }
    .vt-card-text {
        color: var(--text) !important;
        font-size: 14.5px;
        line-height: 1.75;
        margin: 0;
    }

    /* ----- Verdict banner (dark) ----- */
    .vt-verdict {
        position: relative;
        display: flex; justify-content: space-between; align-items: center;
        gap: 28px; flex-wrap: wrap;
        padding: 26px 30px;
        margin-bottom: 26px;
        border-radius: 18px;
        border: 1px solid #1f2b52;
        box-shadow: 0 18px 40px rgba(15,23,42,0.28);
        overflow: hidden;
    }
    .vt-verdict-label {
        font-size: 11px; font-weight: 700;
        letter-spacing: 0.2em; text-transform: uppercase;
        color: var(--on-dark-dim);
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
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 14px;
        padding: 16px 20px;
    }
    .vt-score-top { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px; }
    .vt-score-label { font-size: 12px; color: var(--on-dark-dim); font-weight: 600; letter-spacing: .04em; }
    .vt-score-num { font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 700; color: #fff; }
    .vt-score-sev { font-size: 12px; font-weight: 700; letter-spacing: .08em; margin-left: 6px; }
    .vt-bar { width: 100%; height: 8px; border-radius: 999px; background: rgba(255,255,255,0.10); overflow: hidden; }
    .vt-bar > div { height: 100%; border-radius: 999px; }

    /* ----- Evidence cards ----- */
    .vt-evidence { padding: 16px 18px; margin-bottom: 12px; }
    .vt-evidence-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 8px; }
    .vt-evidence-title { color: var(--ink); font-size: 14.5px; font-weight: 700; line-height: 1.4; }
    .vt-evidence-body { margin: 0; font-size: 13.5px; color: var(--text-dim) !important; line-height: 1.65; }
    .vt-sev-pill {
        flex-shrink: 0;
        font-size: 10.5px; font-weight: 800;
        letter-spacing: 0.1em; text-transform: uppercase;
        padding: 4px 11px; border-radius: 999px;
    }

    /* ----- Checklist ----- */
    .vt-check-head {
        color: #1d4ed8; font-size: 13.5px; font-weight: 800;
        letter-spacing: 0.08em; text-transform: uppercase;
        padding-bottom: 14px; margin-bottom: 6px;
        border-bottom: 1px solid var(--line);
    }
    .vt-step {
        display: flex; gap: 14px; align-items: flex-start;
        padding: 13px 0;
        border-bottom: 1px dashed var(--line);
    }
    .vt-step:last-child { border-bottom: none; }
    .vt-step-num {
        flex-shrink: 0;
        width: 28px; height: 28px; border-radius: 9px;
        display: flex; align-items: center; justify-content: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px; font-weight: 700; color: #fff;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        box-shadow: 0 4px 12px rgba(99,102,241,0.35);
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
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 16px 20px;
        box-shadow: 0 6px 18px rgba(15,23,42,0.06);
    }
    .vt-metric-label { font-size: 11px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--text-mute); }
    .vt-metric-value { margin-top: 6px; font-size: 26px; font-weight: 800; color: var(--ink); font-family: 'JetBrains Mono', monospace; }

    @media (max-width: 768px) {
        .vt-title { font-size: 30px !important; letter-spacing: .14em !important; }
        .vt-header { padding: 22px; }
        .vt-verdict-value { font-size: 24px !important; }
        .vt-score-box { min-width: 100%; }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
