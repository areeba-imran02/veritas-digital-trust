"""VERITAS - Digital Trust & Safety Platform. Streamlit entry point."""
import streamlit as st

from veritas import llm
from veritas.orchestrator import InputError, analyze
from veritas.ui import components, styles

st.set_page_config(page_title="VERITAS | Understand. Verify. Trust.", page_icon="V", layout="centered")

EXAMPLES = {
    "Bank alert": "URGENT: Your HBL account has been suspended. Verify your account within 2 hours at http://hbl-secure-login.xyz and send your OTP or your account will be closed.",
    "Roman Urdu": "Assalam o alaikum, aap ka Easypaisa inam nikla hai! Fauran 500 rupay processing fee bhejein aur kisi ko mat batana. Link: bit.ly/inam-claim",
    "Everyday message": "Hi, just confirming our meeting tomorrow at 3 pm in the office. Let me know if the time still works for you.",
}

if "text" not in st.session_state:
    st.session_state.text = ""


def load_example(name: str) -> None:
    st.session_state.text = EXAMPLES[name]


theme = st.radio("Theme", ["System", "Dark", "Light"], horizontal=True, key="theme")
st.markdown(styles.css(theme), unsafe_allow_html=True)
components.header()

kind_label = st.radio("What do you want to check?", ["Message text", "Link (URL)"], horizontal=True)
st.caption("Image, screenshot and QR code checks are planned and not available yet.")
placeholder = "Paste the message here" if kind_label == "Message text" else "Paste the link here"
st.text_area("Content to analyse", key="text", height=170, placeholder=placeholder, max_chars=6000)

st.caption("Try an example")
cols = st.columns(len(EXAMPLES))
for col, name in zip(cols, EXAMPLES):
    col.button(name, on_click=load_example, args=(name,), use_container_width=True)

if not llm.available():
    st.info("AI analysis is not configured on this deployment. VERITAS will use rule-based checks only.")

if st.button("Analyse content", type="primary", use_container_width=True):
    try:
        with st.spinner("Running the VERITAS agents"):
            res = analyze(st.session_state.text, "text" if kind_label == "Message text" else "url")
        components.result(res)
    except InputError as err:
        st.warning(str(err))
    except RuntimeError as err:
        st.error(str(err))

st.markdown('<p class="vt-muted" style="margin-top:2rem">Submitted content is processed for this analysis only and is not stored by VERITAS. '
            'When AI analysis is enabled, the text is sent to Groq for processing. Do not submit information you are not comfortable sharing.</p>',
            unsafe_allow_html=True)
