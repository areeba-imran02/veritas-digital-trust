# PROJECT_STATE — read this first in any new chat

**Project:** VERITAS · Digital Trust & Safety Platform · *Understand. Verify. Trust.*
**Positioning:** global-first. Pakistan is only an optional localization/validation layer (Prompt 9).
**Last completed prompt:** 1 (foundation)
**Next prompt:** 2 (see docs/ROADMAP.md)

## Rules for every future prompt
1. Continue from these files. Do NOT redesign, restructure or rename files/packages/contracts.
2. Contracts live in `backend/app/core/schemas.py` and `backend/app/core/interfaces.py`. Extend additively; any change must be reflected in `docs/ARCHITECTURE.md`.
3. Evidence-based only. No fake AI results, no placeholder behaviour presented as real. Failures return `ModuleStatus.FAILED`, never invented output.
4. Never claim certainty without sufficient evidence. Trust levels: LOW_RISK / NEEDS_VERIFICATION / HIGH_RISK. Identity states: CONSISTENT / NEEDS_VERIFICATION / MISMATCH_DETECTED / INSUFFICIENT_EVIDENCE.
5. `GROQ_API_KEY` comes from the environment only. Never hardcode, log or return it.
6. One visual language: `frontend/src/styles/tokens.css` + `docs/DESIGN_SYSTEM.md`. No new styles outside tokens.
7. Add dependencies only when a prompt needs them; record them in `backend/requirements.txt` / `frontend/package.json`.
8. No unrelated features, pages, dashboards, social features or fake integrations.

## Implemented so far
- Config (`app/config.py`), health endpoint (`GET /api/health`), static serving of built frontend
- Shared contracts + pipeline interfaces
- Frontend shell (theme tokens, theme controller, API client, connectivity check)
- Docker, devcontainer, env template, 3 baseline tests

## Not implemented yet
Everything functional: `/api/analyze`, Groq client, all analyzers, identity/risk/evidence/trust/action engines, orchestrator, real UI, localization.

## Known notes
- No lockfiles committed (generated in an offline sandbox). Run `npm install` once in the cloud workspace and commit `package-lock.json`.
- Tests were compile-checked but not executed in the creation sandbox (no network). Run `pytest` first in the cloud workspace.
- Groq model names in `.env.example` must be verified against Groq's current model list in Prompt 2.
