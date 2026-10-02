# FILE RECORD

Inventory of every file in the VERITAS project.

| Path | Filename | Purpose | Component / Agent | Dependencies | Role |
|---|---|---|---|---|---|
| `app.py` | app.py | Streamlit entry point: theme, input, example loader, result display | UI | `veritas.orchestrator`, `veritas.llm`, `veritas.ui.*`, streamlit | Connects the UI to the backend |
| `requirements.txt` | requirements.txt | Python dependencies (streamlit, requests) | Deployment | none | Installed by the host |
| `.gitignore` | .gitignore | Keeps `.env` files, caches and secrets out of Git | Security | none | Prevents accidental secret commits |
| `.streamlit/config.toml` | config.toml | Headless server, XSRF protection, usage stats off | Deployment | none | Streamlit runtime settings |
| `README.md` | README.md | Project documentation | Docs | none | Setup, architecture, deployment |
| `FILE_RECORD.md` | FILE_RECORD.md | This inventory | Docs | none | Keeps files documented |
| `veritas/__init__.py` | __init__.py | Package marker | Core | none | Makes `veritas` importable |
| `veritas/llm.py` | llm.py | Groq client reading `GROQ_API_KEY` from the environment | Generative AI layer | requests | Used by Content, Identity, Risk, Trust agents |
| `veritas/orchestrator.py` | orchestrator.py | Validates input and runs the agent pipeline in order | VERITAS Orchestrator | all agents | Central coordinator, returns the final assessment |
| `veritas/agents/__init__.py` | __init__.py | Package marker | Agents | none | Makes `veritas.agents` importable |
| `veritas/agents/content_agent.py` | content_agent.py | Extracts links and structures the content | Content Agent | `veritas.llm` | First stage |
| `veritas/agents/identity_agent.py` | identity_agent.py | Claimed sender vs. linked domains | Identity Agent | `veritas.llm`, content result | Second stage |
| `veritas/agents/risk_agent.py` | risk_agent.py | Social-engineering signal detection | Risk Agent | `veritas.llm` | Third stage |
| `veritas/agents/evidence_agent.py` | evidence_agent.py | Correlates signals into weighted evidence | Evidence Agent | content, identity, risk results | Fourth stage |
| `veritas/agents/trust_agent.py` | trust_agent.py | Trust level and explanation | Trust Agent | `veritas.llm`, evidence, identity, content results | Fifth stage |
| `veritas/agents/action_agent.py` | action_agent.py | Safer next steps | Action Agent | trust and risk results | Final stage |
| `veritas/ui/__init__.py` | __init__.py | Package marker | UI | none | Makes `veritas.ui` importable |
| `veritas/ui/styles.py` | styles.py | Design tokens, themes, component CSS | UI | none | Premium, accessible visual identity |
| `veritas/ui/components.py` | components.py | Header and result rendering | UI | streamlit | Shows the final trust assessment |
