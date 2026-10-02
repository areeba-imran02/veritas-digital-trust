# VERITAS Architecture

## Stack
- **Backend:** Python 3.12, FastAPI, Pydantic v2, Groq SDK (LLM: text, vision, speech-to-text)
- **Frontend:** React 18 + TypeScript + Vite, plain CSS driven by design tokens
- **Deploy:** one Docker image (backend serves built frontend). Cloud-workspace dev via `.devcontainer/`.

## Pipeline
```
User Input
 → Analyzer(s)            multimodal analysis        (app/analyzers)
 → IdentityEngine         identity consistency       (app/identity)
 → RiskEngine             risk analysis              (app/risk)
 → EvidenceEngine         evidence correlation       (app/evidence)
 → TrustEngine            trust assessment           (app/trust)
 → ExplanationEngine      explanation                (app/actions)
 → ActionRecommender      safer action               (app/actions)
        coordinated by Orchestrator                  (app/agents)
```
Contracts: `app/core/schemas.py` (data) and `app/core/interfaces.py` (stage interfaces).

## Folder tree
```
veritas/
├── README.md  PROJECT_STATE.md  Dockerfile  .dockerignore  .gitignore  .env.example
├── .devcontainer/devcontainer.json
├── docs/  ARCHITECTURE.md  DESIGN_SYSTEM.md  ROADMAP.md
├── backend/
│   ├── requirements.txt  requirements-dev.txt  pytest.ini
│   ├── app/
│   │   ├── main.py  config.py
│   │   ├── api/        router.py  routes/health.py   (routes/analyze.py in P2)
│   │   ├── core/       schemas.py  interfaces.py
│   │   ├── llm/        Groq wrapper
│   │   ├── analyzers/  text/message/email, url, qr, image/screenshot, audio
│   │   ├── identity/   risk/   evidence/   trust/   actions/
│   │   ├── agents/     orchestrator
│   │   └── localization/
│   └── tests/
└── frontend/
    ├── package.json  tsconfig.json  vite.config.ts  index.html
    └── src/  main.tsx  App.tsx  lib/api.ts  theme/theme.ts  styles/tokens.css
```
New files in later prompts go inside these packages. New top-level folders are not expected.

## Key rules
- **Signals are the unit of evidence.** Each has dimension (content/identity/context/technical), direction, strength, confidence, and provenance (heuristic/llm/external/user). Conclusions reference signal ids.
- **LLM output is a signal, not a verdict.** Deterministic facts (e.g. URL structure) outweigh model opinion; the trust engine weights by provenance.
- **Insufficient evidence is explicit.** `EvidenceBundle.sufficient=False` ⇒ TrustEngine must not return LOW_RISK; it returns NEEDS_VERIFICATION with `gaps` explained. Identity uses `INSUFFICIENT_EVIDENCE` when nothing can be compared.
- **No fabricated results.** An analyzer that cannot run returns `status=FAILED|SKIPPED` with a reason; the response surfaces it in limitations.
- **Privacy:** uploaded bytes are processed in memory (`AnalysisInput.data`, excluded from serialization) and not persisted by default.

## API (target)
| Method | Path | Added | Purpose |
|---|---|---|---|
| GET | /api/health | P1 | status, version, `llm_configured` (bool only) |
| POST | /api/analyze | P2 | JSON for text/message/email/url; multipart for files (P4). Returns `AnalysisResponse` |

## Configuration
All via environment (`.env.example`). Only secret: `GROQ_API_KEY`.
