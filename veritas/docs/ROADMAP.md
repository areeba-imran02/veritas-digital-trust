# Roadmap (Prompts 2–10)

| # | Scope | Main files |
|---|---|---|
| 2 | Core pipeline end-to-end for **text / message / email**: Groq client, text analyzer (heuristics + LLM signals), first-version identity/risk/evidence/trust/explanation/action engines, orchestrator, `POST /api/analyze`, tests | `llm/`, `analyzers/text.py`, `agents/orchestrator.py`, `api/routes/analyze.py` |
| 3 | **URL intelligence** (structure, lookalike/punycode, redirects, TLD/age signals where available) + **QR analysis** (decode → URL pipeline) | `analyzers/url.py`, `analyzers/qr.py` |
| 4 | **Image / screenshot** (vision + OCR via Groq vision) and **audio / voice notes** (Groq speech-to-text → text pipeline); multipart upload | `analyzers/image.py`, `analyzers/audio.py` |
| 5 | **Identity Consistency** engine (claimed vs observed: brand/domain/sender/handle) with the four identity states | `identity/` |
| 6 | **Evidence correlation + Trust hardening + Actions**: corroboration/contradiction, sufficiency rules, calibration, localized-ready action sets | `evidence/`, `trust/`, `actions/` |
| 7 | **Agent orchestration**: multi-input cases, cross-modal routing (e.g. screenshot → text → URL), follow-up verification steps | `agents/` |
| 8 | **Frontend design system + app shell**: components, wordmark, theme switcher (dark/light/system) | `frontend/src/components`, `styles/` |
| 9 | **Frontend results experience** wired to API (trust, identity, evidence, actions) + **localization** (en default; Pakistan layer, e.g. Urdu) | `frontend/src`, `localization/` |
| 10 | **Testing, hardening, deployment guide**: end-to-end tests, error handling, limits, final docs | `backend/tests`, `docs/` |

Each prompt must keep filenames/interfaces stable and update `PROJECT_STATE.md`.
