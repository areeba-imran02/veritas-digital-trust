import streamlit as st

def inject_enterprise_theme():
    st.markdown("""
        <style>
        .stApp {
            background-color: #090d16;
            color: #e6edf3;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #0d1117;
            border-right: 1px solid #21262d;
        }
        
        /* Headers */
        h1, h2, h3, h4 {
            color: #f0f6fc;
            font-weight: 700;
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
            color: white;
            border-radius: 8px;
            font-weight: 600;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 4px 12px rgba(35, 134, 54, 0.3);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2ea043 0%, #3fb950 100%);
            box-shadow: 0 6px 16px rgba(46, 160, 67, 0.5);
        }
        
        /* Metric & Card Containers */
        div.stMetric, .css-1r6slb0 {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #0d1117;
            padding: 6px;
            border-radius: 10px;
            border: 1px solid #30363d;
        }
        .stTabs [data-baseweb="tab"] {
            height: 40px;
            color: #8b949e;
            border-radius: 6px;
            font-weight: 500;
        }
        .stTabs [aria-selected="true"] {
            background-color: #21262d !important;
            color: #f0f6fc !important;
            border: 1px solid #30363d;
        }
        </style>
    """, unsafe_allow_html=True)
