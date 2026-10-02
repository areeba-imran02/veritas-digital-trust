from html import escape

import streamlit as st

from ui.theme import render_html


def render_header():
    render_html("""
        <div class="vt-header">
            <div class="vt-brand">
                <div class="vt-logo">🛡️</div>
                <div>
                    <h1 class="vt-title">VERITAS</h1>
                    <p class="vt-subtitle">
                        Enterprise Multimodal Threat Intelligence &amp; Advanced Scam Detection Platform
                    </p>
                </div>
            </div>
            <div>
                <span class="vt-badge"><span class="vt-dot"></span>CORE v4.2 SECURE</span>
            </div>
        </div>
    """)


def render_file_dropzone(label: str):
    return st.file_uploader(label, type=["png", "jpg", "jpeg", "pdf", "txt"])


def render_metric_gauge(label: str, value: str):
    render_html(f"""
        <div class="vt-metric">
            <div class="vt-metric-label">{escape(str(label))}</div>
            <div class="vt-metric-value">{escape(str(value))}</div>
        </div>
    """)
