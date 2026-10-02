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
        /* ---- Light content: pure white + black ink ---- */
        --ink: #0a0a0a;
        --text: #262626;
        --text-dim: #525252;
        --text-mute: #737373;
        --surface: #ffffff;
        --line: #e5e5e5;
        --line-strong: #d4d4d4;

        /* ---- Dark surfaces: pure black ---- */
        --black-0: #000000;
        --black-1: #0a0a0a;
        --black-2: #171717;
        --black-line: #2a2a2a;
        --on-dark: #fafafa;
        --on-dark-dim: #b8b8b8;

        /* ---- Single accent (change this one line to re-brand) ---- */
        --accent: #0a0a0a;
        --accent-on-dark: #ffffff;
    }

    /* =========================================================
       BASE
       ========================================================= */
    html, body, .stApp {
        font-family: 'Inter', -apple-system, 'Segoe UI', sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }
    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
        color: var(--text);
    }
    :where(.stApp p, .stApp li, .stApp label) { color: var(--text); }
    [data-testid="stCaptionContainer"] { color: var(--text-mute) !important; }

    #MainMenu, footer { visibility: hidden; }
    header[data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"], [data-testid="stToolbar"] * { color: #262626 !important; }

    .block-container {
        max-width: 1240px;
        padding-top: 2.4rem;
        padding-bottom: 4rem;
    }

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
       SIDEBAR (pure black)
       ========================================================= */
    [data-testid="stSidebar"] {
        background:
            radial-gradient(420px 240px at 0% 0%, rgba(255,255,255,0.07), transparent 65%),
            linear-gradient(180deg, #0f0f0f 0%, #000000 100%);
        border-right: 1px solid var(--black-line);
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] small,
    [data-testid="stSidebar"] label { color: var(--on-dark-dim); }
    [data-testid="stSidebar"] strong { color: #ffffff; font-weight: 600; }

    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4 {
        color: #ffffff !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.18em !important;
        text-transform: uppercase;
        padding: 0 0 12px 14px !important;
        margin: 8px 0 14px 0 !important;
        border-bottom: 1px solid var(--black-line);
        position: relative;
    }
    [data-testid="stSidebar"] h1::before, [data-testid="stSidebar"] h2::before,
    [data-testid="stSidebar"] h3::before, [data-testid="stSidebar"] h4::before {
        content: "";
        position: absolute; left: 0; top: 2px;
        width: 4px; height: 16px; border-radius: 4px;
        background: var(--accent-on-dark);
    }
    [data-testid="stSidebar"] hr { border-color: var(--black-line) !important; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: #d4d4d4 !important;
        font-size: 0.85rem; font-weight: 500;
    }

    /* Sidebar select -> black glass */
    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="select"] > div > div {
        background-color: #171717 !important;
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        border: 1px solid #333333 !important;
        border-radius: 12px !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] * { color: #ffffff !important; }
    [data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #d4d4d4 !important; }
    [data-testid="stSidebar"] [data-baseweb="select"]:hover > div { border-color: #ffffff !important; }

    /* =========================================================
       BUTTONS (black)
       ========================================================= */
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(180deg, #262626 0%, #000000 100%);
        color: #ffffff !important;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.72rem 1.2rem;
        border: 1px solid #000000;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.18);
        transition: transform .15s ease, box-shadow .15s ease;
        width: 100%;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(180deg, #3a3a3a 0%, #0a0a0a 100%);
        box-shadow: 0 12px 28px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.25);
        color: #ffffff !important;
        border-color: #000000;
    }
    .stButton > button:active { transform: translateY(0); }
    .stButton > button p, .stDownloadButton > button p { color: #ffffff !important; font-weight: 600; }

    /* =========================================================
       TABS (no parent prefix -> works on every Streamlit version)
       ========================================================= */
    [data-baseweb="tab-list"] {
        gap: 4px;
        background: transparent !important;
        padding: 0;
        border: none;
        border-bottom: 1px solid var(--line);
    }
    [data-baseweb="tab"], button[role="tab"] {
        height: 46px;
        padding: 0 16px;
        background: transparent !important;
        color: var(--text-mute);
        font-weight: 500;
        border-radius: 8px 8px 0 0;
        transition: color .2s, background .2s;
    }
    [data-baseweb="tab"] p, button[role="tab"] p { color: inherit !important; font-weight: inherit; }
    [data-baseweb="tab"]:hover, button[role="tab"]:hover { color: var(--ink); background: rgba(0,0,0,0.04) !important; }
    [data-baseweb="tab"][aria-selected="true"], button[role="tab"][aria-selected="true"] {
        color: var(--ink) !important;
        font-weight: 700 !important;
    }
    [data-baseweb="tab-highlight"] {
        background: var(--accent) !important;
        background-color: var(--accent) !important;
        height: 3px !important;
        border-radius: 3px;
    }
    [data-baseweb="tab-border"] { background: transparent !important; background-color: transparent !important; }

    /* =========================================================
       INPUTS (white box, black border on focus - no red, no grey)
       ========================================================= */
    [data-testid="stWidgetLabel"] p { color: var(--ink) !important; font-weight: 600; font-size: 0.92rem; }

    [data-baseweb="textarea"], [data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid var(--line-strong) !important;
        border-radius: 12px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
        transition: border-color .15s, box-shadow .15s;
    }
    [data-baseweb="textarea"]:focus-within, [data-baseweb="input"]:focus-within {
        border-color: #0a0a0a !important;
        box-shadow: 0 0 0 3px rgba(0,0,0,0.10) !important;
    }
    [data-baseweb="textarea"] > div, [data-baseweb="input"] > div, [data-baseweb="base-input"] {
        background-color: #ffffff !important;
        border: none !important;
        box-shadow: none !important;
    }
    textarea, input[type="text"], input[type="number"], input[type="password"] {
        background-color: #ffffff !important;
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        line-height: 1.65 !important;
        caret-color: var(--ink);
    }
    textarea::placeholder, input::placeholder {
        color: #a3a3a3 !important;
        -webkit-text-fill-color: #a3a3a3 !important;
    }

    /* Select boxes (main area: white) */
    .stApp [data-baseweb="select"] > div,
    .stApp [data-baseweb="select"] > div > div {
        background-color: #ffffff;
        color: var(--ink);
    }
    .stApp [data-baseweb="select"] > div { border: 1px solid var(--line-strong); border-radius: 12px; }
    .stApp [data-baseweb="select"] * { color: var(--ink); }

    /* Dropdown popup */
    [data-baseweb="popover"] [data-baseweb="menu"], [data-baseweb="popover"] ul {
        background-color: #ffffff !important;
        border: 1px solid var(--line);
        border-radius: 12px;
        box-shadow: 0 16px 40px rgba(0,0,0,0.18);
    }
    [data-baseweb="popover"] li, [data-baseweb="popover"] li * { color: var(--ink) !important; }
    [data-baseweb="popover"] li:hover, [data-baseweb="popover"] li[aria-selected="true"] {
        background-color: #f0f0f0 !important;
    }

    .stRadio label, .stCheckbox label { color: var(--text) !important; }

    /* =========================================================
       FILE UPLOADER
       ========================================================= */
    [data-testid="stFileUploaderDropzone"] {
        background: #ffffff;
        border: 1.5px dashed #a3a3a3;
        border-radius: 14px;
        padding: 1.5rem;
        transition: all .2s;
    }
    [data-testid="stFileUploaderDropzone"]:hover { border-color: #000000; background: #fafafa; }
    [data-testid="stFileUploaderDropzone"] * { color: var(--text-dim) !important; }
    [data-testid="stFileUploaderDropzone"] button {
        background: #0a0a0a !important;
        border: 1px solid #0a0a0a !important;
        border-radius: 8px !important;
        width: auto; box-shadow: none; transform: none;
    }
    [data-testid="stFileUploaderDropzone"] button, [data-testid="stFileUploaderDropzone"] button * { color: #ffffff !important; }
    [data-testid="stFileUploaderFile"] * { color: var(--text) !important; }

    [data-testid="stExpander"] { background: #ffffff; border: 1px solid var(--line); border-radius: 12px; }
    [data-testid="stExpander"] summary p { color: var(--ink) !important; font-weight: 600; }
    [data-testid="stAlert"] { border-radius: 12px; }
    [data-testid="stMetric"] { background: #ffffff; border: 1px solid var(--line); padding: 14px 18px; border-radius: 14px; }
    [data-testid="stMetricLabel"] p { color: var(--text-mute) !important; font-size: 0.78rem; letter-spacing: .08em; text-transform: uppercase; }
    [data-testid="stMetricValue"] { color: var(--ink) !important; font-weight: 800; }

    /* =========================================================
       CUSTOM COMPONENTS
       ========================================================= */

    /* ----- Header (black hero) ----- */
    .vt-header {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(560px 240px at 0% 0%, rgba(255,255,255,0.10), transparent 62%),
            linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
        border: 1px solid #2a2a2a;
        border-radius: 22px;
        padding: 36px 40px 40px 40px;
        margin-bottom: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        flex-wrap: wrap;
        box-shadow: 0 22px 50px rgba(0,0,0,0.30), inset 0 1px 0 rgba(255,255,255,0.10);
    }
    .vt-header::after {
        content: "";
        position: absolute; inset: 0;
        background-image: linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px);
        background-size: 36px 36px;
        mask-image: linear-gradient(90deg, transparent, #000 80%);
        -webkit-mask-image: linear-gradient(90deg, transparent, #000 80%);
        pointer-events: none;
    }
    .vt-header > * { position: relative; z-index: 1; }
    .vt-brand { display: flex; align-items: center; gap: 24px; flex: 1 1 520px; min-width: 0; }

    .vt-logo {
        flex-shrink: 0;
        width: 68px; height: 68px;
        border-radius: 18px;
        display: flex; align-items: center; justify-content: center;
        background: linear-gradient(145deg, #ffffff 0%, #d9d9d9 100%);
        box-shadow:
            0 12px 26px rgba(0,0,0,0.55),
            inset 0 -4px 0 #9a9a9a,
            inset 0 1px 0 #ffffff;
    }

    /* ===== REAL 3D TITLE: white lit face + deep stacked extrusion ===== */
    .stApp .vt-header h1.vt-title {
        margin: 0 !important;
        padding: 0 0 14px 0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 54px !important;
        font-weight: 900 !important;
        letter-spacing: 0.16em !important;
        line-height: 1.05 !important;
        text-transform: uppercase;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff;
        text-shadow:
            0 1px 0 #e6e6e6,
            0 2px 0 #cfcfcf,
            0 3px 0 #b8b8b8,
            0 4px 0 #a1a1a1,
            0 5px 0 #8a8a8a,
            0 6px 0 #737373,
            0 7px 0 #5c5c5c,
            0 8px 0 #454545,
            0 9px 0 #2e2e2e,
            0 10px 0 #1c1c1c,
            0 12px 6px rgba(0,0,0,0.55),
            0 18px 24px rgba(0,0,0,0.55),
            0 0 38px rgba(255,255,255,0.14);
    }
    .vt-subtitle {
        margin: 12px 0 0 0 !important;
        color: var(--on-dark-dim) !important;
        font-size: 14.5px;
        font-weight: 400;
        line-height: 1.55;
    }
    .vt-badge {
        display: inline-flex; align-items: center; gap: 9px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11.5px; font-weight: 700;
        color: #ffffff;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.28);
        padding: 9px 16px;
        border-radius: 999px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .vt-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #22c55e;
        animation: vt-pulse 2s infinite;
    }
    @keyframes vt-pulse {
        0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.6); }
        70% { box-shadow: 0 0 0 9px rgba(34,197,94,0); }
        100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
    }

    /* ----- Section titles ----- */
    .vt-section {
        display: flex; align-items: center; gap: 10px;
        margin: 4px 0 14px 0;
        font-size: 15px; font-weight: 700;
        color: var(--ink);
    }
    .vt-section .vt-section-bar { width: 4px; height: 18px; border-radius: 4px; background: var(--accent); }
    .vt-report-title {
        display: flex; align-items: center; gap: 12px;
        font-size: 12.5px; font-weight: 700;
        letter-spacing: 0.18em; text-transform: uppercase;
        color: var(--text-dim);
        margin: 6px 0 18px 0;
    }
    .vt-report-title::after { content: ""; flex: 1; height: 1px; background: linear-gradient(90deg, var(--line-strong), transparent); }

    /* ----- Cards ----- */
    .vt-card {
        background: #ffffff;
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }
    .vt-card-text { color: var(--text) !important; font-size: 14.5px; line-height: 1.75; margin: 0; }

    /* ----- Verdict banner (black) ----- */
    .vt-verdict {
        position: relative;
        display: flex; justify-content: space-between; align-items: center;
        gap: 28px; flex-wrap: wrap;
        padding: 26px 30px;
        margin-bottom: 26px;
        border-radius: 18px;
        border: 1px solid #2a2a2a;
        box-shadow: 0 18px 40px rgba(0,0,0,0.28);
        overflow: hidden;
    }
    .vt-verdict-label { font-size: 11px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--on-dark-dim); }
    .vt-verdict-value { margin: 8px 0 0 0 !important; font-size: 32px !important; font-weight: 800 !important; letter-spacing: 0.01em !important; line-height: 1.15 !important; }
    .vt-score-box {
        min-width: 280px; flex: 0 1 340px;
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 14px;
        padding: 16px 20px;
    }
    .vt-score-top { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px; }
    .vt-score-label { font-size: 12px; color: var(--on-dark-dim); font-weight: 600; letter-spacing: .04em; }
    .vt-score-num { font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 700; color: #fff; }
    .vt-score-sev { font-size: 12px; font-weight: 700; letter-spacing: .08em; margin-left: 6px; }
    .vt-bar { width: 100%; height: 8px; border-radius: 999px; background: rgba(255,255,255,0.14); overflow: hidden; }
    .vt-bar > div { height: 100%; border-radius: 999px; }

    /* ----- Evidence cards ----- */
    .vt-evidence { padding: 16px 18px; margin-bottom: 12px; }
    .vt-evidence-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 8px; }
    .vt-evidence-title { color: var(--ink); font-size: 14.5px; font-weight: 700; line-height: 1.4; }
    .vt-evidence-body { margin: 0; font-size: 13.5px; color: var(--text-dim) !important; line-height: 1.65; }
    .vt-sev-pill { flex-shrink: 0; font-size: 10.5px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; padding: 4px 11px; border-radius: 999px; }

    /* ----- Checklist ----- */
    .vt-check-head {
        color: var(--ink); font-size: 13.5px; font-weight: 800;
        letter-spacing: 0.08em; text-transform: uppercase;
        padding-bottom: 14px; margin-bottom: 6px;
        border-bottom: 1px solid var(--line);
    }
    .vt-step { display: flex; gap: 14px; align-items: flex-start; padding: 13px 0; border-bottom: 1px dashed var(--line-strong); }
    .vt-step:last-child { border-bottom: none; }
    .vt-step-num {
        flex-shrink: 0;
        width: 28px; height: 28px; border-radius: 9px;
        display: flex; align-items: center; justify-content: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px; font-weight: 700; color: #fff;
        background: linear-gradient(180deg, #333333, #000000);
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    }
    .vt-step-text { color: var(--text); font-size: 14.5px; line-height: 1.65; padding-top: 2px; }
    .vt-empty { color: var(--text-mute); font-size: 14px; padding: 8px 0; }

    /* ----- Urdu / RTL ----- */
    .vt-rtl { direction: rtl; text-align: right; }
    .vt-rtl .vt-step-text, .vt-rtl .vt-check-head {
        font-family: 'Noto Nastaliq Urdu', 'Inter', serif;
        line-height: 2.3; letter-spacing: 0; text-transform: none;
    }
    .vt-rtl .vt-step-text { font-size: 16px; }

    /* ----- Metric card ----- */
    .vt-metric { background: #ffffff; border: 1px solid var(--line); border-radius: 14px; padding: 16px 20px; box-shadow: 0 6px 18px rgba(0,0,0,0.06); }
    .vt-metric-label { font-size: 11px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--text-mute); }
    .vt-metric-value { margin-top: 6px; font-size: 26px; font-weight: 800; color: var(--ink); font-family: 'JetBrains Mono', monospace; }

    @media (max-width: 768px) {
        .stApp .vt-header h1.vt-title { font-size: 32px !important; letter-spacing: .1em !important; }
        .vt-header { padding: 24px; }
        .vt-verdict-value { font-size: 24px !important; }
        .vt-score-box { min-width: 100%; }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
