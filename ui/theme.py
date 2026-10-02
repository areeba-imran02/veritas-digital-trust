import streamlit as st

def inject_enterprise_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        .stApp {
            background-color: #030712;
            color: #f3f4f6;
            font-family: 'Inter', sans-serif;
        }
        
        /* मॉडर्न साइडबार */
        [data-testid="stSidebar"] {
            background-color: #0b0f19;
            border-right: 1px solid #1f2937;
        }
        
        /* हेडिंग्स */
        h1, h2, h3, h4 {
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.025em;
        }
        
        /* मॉडर्न बटन */
        .stButton>button {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.6rem 1.2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
            transition: all 0.2s ease-in-out;
            width: 100%;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
            border-color: rgba(255, 255, 255, 0.2);
        }
        
        /* कार्ड्स और कंटेनर्स */
        div.stMetric, .element-container {
            font-family: 'Inter', sans-serif;
        }
        
        /* टैब्स की मॉडर्न स्टाइलिंग */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background-color: #0b0f19;
            padding: 8px;
            border-radius: 12px;
            border: 1px solid #1f2937;
        }
        .stTabs [data-baseweb="tab"] {
            height: 44px;
            color: #9ca3af;
            border-radius: 8px;
            font-weight: 500;
            background-color: transparent;
            border: none;
            transition: all 0.2s;
        }
        .stTabs [aria-selected="true"] {
            background-color: #1f2937 !important;
            color: #ffffff !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        
        /* टेक्स्ट एरिया और इनपुट्स */
        .stTextArea textarea, .stTextInput input {
            background-color: #0b0f19 !important;
            color: #f3f4f6 !important;
            border: 1px solid #374151 !important;
            border-radius: 8px !important;
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
        }
        </style>
    """, unsafe_allow_html=True)
