# VERITAS File Record Index (29 Modules)

## Root Files
1. `app.py` - Main Streamlit UI entry point.
2. `requirements.txt` - Python package dependencies.
3. `README.md` - Enterprise documentation & architecture guide.
4. `FILE_RECORD.md` - Complete workspace manifest.

## Agents (`agents/`)
5. `agents/content_agent.py` - Psychological manipulation & scam signature evaluation.
6. `agents/identity_agent.py` - Sender consistency & spoofing detection.
7. `agents/risk_agent.py` - Vector threat score & severity computation.
8. `agents/evidence_agent.py` - Multimodal artifact cross-correlation.
9. `agents/trust_agent.py` - Final verdict issuer (Low Risk, Needs Verification, High Risk, Insufficient Evidence).
10. `agents/action_agent.py` - Actionable remediation steps & structured reasoning ("Why?").

## Core (`core/`)
11. `core/orchestrator.py` - Central coordination engine.
12. `core/config.py` - System constants & configuration management.

## Analyzers (`analyzers/`)
13. `analyzers/url_analyzer.py` - URL syntax, TLD reputation, typosquatting & HTTPS inspection.
14. `analyzers/qr_analyzer.py` - QR code decoding & payload extraction.
15. `analyzers/image_analyzer.py` - Visual context & OCR artifact extraction.
16. `analyzers/screenshot_analyzer.py` - Chat UI & payment receipt forensic parser.
17. `analyzers/audio_analyzer.py` - Acoustic pattern & voice threat analysis foundation.

## Services (`services/`)
18. `services/groq_service.py` - Groq SDK wrapper with JSON fallbacks.
19. `services/evidence_service.py` - Evidence aggregation & card formatting.

## UI (`ui/`)
20. `ui/theme.py` - Enterprise CSS injection (Dark/Light/System theme).
21. `ui/components.py` - UI layout components & file dropzones.
22. `ui/results.py` - Verdict rendering & multilingual advice display.

## Tests (`tests/`)
23. `tests/test_content_agent.py` - Unit tests for content agent.
24. `tests/test_identity_agent.py` - Unit tests for identity agent.
25. `tests/test_risk_agent.py` - Unit tests for risk agent.
26. `tests/test_trust_agent.py` - Unit tests for trust agent.
27. `tests/test_qr_analyzer.py` - Unit tests for QR analyzer.
28. `tests/test_url_analyzer.py` - Unit tests for URL analyzer.
29. `tests/test_orchestrator.py` - Integration tests for orchestrator pipeline.
