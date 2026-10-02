# VERITAS: Enterprise Multimodal Cybersecurity & Scam Detection Platform

VERITAS is an enterprise-grade, global-first multimodal threat intelligence and scam detection platform built for high-security environments. It integrates multi-agent reasoning, deep artifact analyzers, and high-performance Large Language Model inference via Groq to deliver definitive trust verdicts.

## Architecture Overview
- **Core Orchestrator**: Coordinates asynchronous multi-agent pipelines.
- **Analyzers**: Specialized parsers for URLs, QR codes, images, UI screenshots, and audio streams.
- **Agent Mesh**: Content, Identity, Risk, Evidence, Trust, and Action agents working in concert.
- **Localization Layer**: Supports English, Urdu, and Roman Urdu with regional context tailored for Pakistan (PK) operations.

## Security & Compliance
- **Zero Hardcoded Secrets**: API keys are strictly loaded via `os.environ.get("GROQ_API_KEY")`.
- **No Key Files**: Environment files are strictly excluded from version control.

## Setup & Execution
1. Install dependencies: `pip install -r requirements.txt`
2. Set your Groq API key: `export GROQ_API_KEY="your_api_key_here"`
3. Launch dashboard: `streamlit run app.py`
