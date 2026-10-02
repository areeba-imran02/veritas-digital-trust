# VERITAS
**Digital Trust & Safety Platform — Understand. Verify. Trust.**

VERITAS helps people understand, verify and safely respond to suspicious digital content
(text, messages, emails, URLs, images, screenshots, QR codes, audio) by combining
**Content + Identity + Context + Evidence + Risk** into an explainable Trust Assessment and a safer next action.

> Status: **Prompt 1 complete — foundation only.** No analysis is implemented yet. See `PROJECT_STATE.md`.

## Run in the cloud (no local installs)
Use any cloud workspace (GitHub Codespaces, Gitpod, etc.) — `.devcontainer/` installs everything.

```bash
# 1. Secret: add GROQ_API_KEY in your workspace secrets (or copy .env.example -> backend/.env)
# 2. Backend
cd backend && uvicorn app.main:app --reload --port 8000
# 3. Frontend (second terminal)
cd frontend && npm run dev          # http://localhost:5173 (proxies /api -> :8000)
# Tests
cd backend && pytest
```

## Deploy
`Dockerfile` builds the frontend and serves it from the FastAPI backend in ONE container
(listens on `$PORT`). Provide `GROQ_API_KEY` as a deployment secret. Variables are listed in `.env.example`.

## Docs
- `PROJECT_STATE.md` — read first when continuing in a new chat
- `docs/ARCHITECTURE.md` — pipeline, contracts, module ownership
- `docs/DESIGN_SYSTEM.md` — the one visual language
- `docs/ROADMAP.md` — Prompts 2–10
