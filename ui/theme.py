import streamlit as st

def inject_enterprise_theme():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .css-18e3th9 {
            background-color: #161b22;
        }
        h1, h2, h3 {
            color: #ffffff;
            font-weight: 600;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 6px;
            font-weight: 600;
            border: none;
        }
        .stButton>button:hover {
            background-color: #2ea043;
        }
        div.stMetric {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 15px;
            border-radius: 6px;
        }
        </style>
    """, unsafe_allow_html=True)
