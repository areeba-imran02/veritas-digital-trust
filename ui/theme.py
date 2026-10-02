import streamlit as st


def inject_enterprise_theme():
    st.markdown(
        """
        <style>

        /* =========================================================
           VERITAS — GLOBAL ENTERPRISE LIGHT THEME
        ========================================================= */

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #f5f7fb;
            --surface: #ffffff;
            --surface-soft: #f8fafc;
            --border: #e5e7eb;
            --border-strong: #d1d5db;

            --text: #111827;
            --text-secondary: #4b5563;
            --text-muted: #6b7280;

            --navy: #0f172a;
            --blue: #2563eb;
            --blue-dark: #1d4ed8;
            --blue-soft: #eff6ff;

            --green: #059669;
            --green-soft: #ecfdf5;

            --amber: #d97706;
            --amber-soft: #fffbeb;

            --red: #dc2626;
            --red-soft: #fef2f2;

            --gray-soft: #f3f4f6;
        }


        /* APP */

        .stApp {
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
        }

        .main .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }


        /* REMOVE DEFAULT TOP SPACE */

        header[data-testid="stHeader"] {
            background: transparent;
        }


        /* SIDEBAR */

        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] * {
            font-family: 'Inter', sans-serif;
        }


        /* HEADINGS */

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif !important;
            color: var(--text) !important;
            letter-spacing: -0.02em;
        }

        h1 {
            font-weight: 800 !important;
        }

        h2, h3 {
            font-weight: 700 !important;
        }


        /* BODY TEXT */

        p, span, label, div {
            font-family: 'Inter', sans-serif;
        }


        /* BUTTONS */

        .stButton > button {
            width: 100%;
            min-height: 44px;

            background: var(--navy);
            color: #ffffff;

            border: 1px solid var(--navy);
            border-radius: 9px;

            font-size: 14px;
            font-weight: 600;

            transition:
                background 0.18s ease,
                transform 0.18s ease,
                box-shadow 0.18s ease;
        }

        .stButton > button:hover {
            background: #1e293b;
            border-color: #1e293b;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.15);
            transform: translateY(-1px);
        }


        /* INPUTS */

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] > div {
            background: #ffffff !important;
            color: var(--text) !important;

            border: 1px solid var(--border-strong) !important;
            border-radius: 9px !important;

            font-family: 'Inter', sans-serif !important;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {
            border-color: var(--blue) !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.10) !important;
        }


        /* FILE UPLOADER */

        [data-testid="stFileUploader"] {
            background: #ffffff;
            border: 1px dashed #cbd5e1;
            border-radius: 10px;
            padding: 8px;
        }


        /* TABS */

        .stTabs [data-baseweb="tab-list"] {
            background: #ffffff;
            border: 1px solid var(--border);
            padding: 5px;
            gap: 4px;
            border-radius: 10px;
        }

        .stTabs [data-baseweb="tab"] {
            color: var(--text-muted);
            border-radius: 7px;
            font-weight: 600;
            padding: 8px 16px;
        }

        .stTabs [aria-selected="true"] {
            background: var(--navy) !important;
            color: #ffffff !important;
        }


        /* METRICS */

        [data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 16px;
        }

        [data-testid="stMetricLabel"] {
            color: var(--text-muted) !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--text) !important;
        }


        /* DIVIDERS */

        hr {
            border: none !important;
            border-top: 1px solid var(--border) !important;
            margin: 28px 0 !important;
        }


        /* ALERTS */

        [data-testid="stAlert"] {
            border-radius: 9px;
        }


        /* SCROLLBAR */

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }

        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }


        /* MOBILE */

        @media (max-width: 768px) {

            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .stButton > button {
                min-height: 42px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )
