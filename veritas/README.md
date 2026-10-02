# VERITAS: Digital Trust & Safety Platform

**Understand. Verify. Trust.**

VERITAS is a global-first digital trust platform. It helps people assess suspicious messages and links before they click, pay, respond or trust them. It supports English, Urdu and Roman Urdu patterns as an initial localization layer, and is designed for international use.

## Core problem
Scam and impersonation messages are written to create pressure. People rarely have a quick, clear way to see why something looks suspicious or what to do next.

## Solution
Paste a message or link. VERITAS runs it through a team of specialist agents and returns a Trust Level, the reasons, an identity assessment, the evidence, safer next steps and the limits of the analysis. It never claims certainty.

Trust levels: `LOW RISK`, `NEEDS VERIFICATION`, `HIGH RISK`, `INSUFFICIENT EVIDENCE`.

## Multi-agent architecture
```
User Input -> VERITAS Orchestrator -> Content -> Identity -> Risk -> Evidence -> Trust -> Action -> Final Trust Assessment
```
The Orchestrator (`veritas/orchestrator.py`) validates input, runs each agent in order and gives every agent the structured results of the earlier ones. Agents never call each other directly.

| Agent | Responsibility | Uses Groq |
|---|---|---|
| Content Agent | Extracts links, language, summary, claimed sender, requested actions | Yes |
| Identity Agent | Compares the claimed sender with linked domains, flags shorteners and risky domains | Yes (reasoning text) |
| Risk Agent | Detects urgency, credential requests, payment pressure, secrecy and other social-engineering signals | Yes, plus pattern rules |
| Evidence Agent | Correlates signals across agents into weighted evidence and combined patterns | No (deterministic) |
| Trust Agent | Produces the trust level from the evidence and writes the explanation | Yes (explanation) |
| Action Agent | Maps findings to safer next steps | No (deterministic) |

Generative AI interprets unstructured content and writes explanations. The trust level itself comes from transparent, deterministic scoring so results are explainable. If Groq is unavailable, the pipeline falls back to rule-based checks and says so in the Limitations section.

## Technology stack
Python 3.10+, Streamlit, Requests, Groq API (OpenAI-compatible chat completions; default model `llama-3.3-70b-versatile`, override with optional `GROQ_MODEL`).

## Project structure
```
app.py                     Streamlit entry point
requirements.txt
.streamlit/config.toml     Server and privacy settings
veritas/orchestrator.py    Agent coordination
veritas/llm.py             Groq client
veritas/agents/            Six specialist agents
veritas/ui/styles.py       Design system (dark, light, system themes)
veritas/ui/components.py   Result rendering
```
See `FILE_RECORD.md` for the full inventory.

## Configure `GROQ_API_KEY`
The code only reads the environment variable `GROQ_API_KEY`. No key is stored in this repository, and there is no `.env` file.

- **Streamlit Community Cloud:** App settings -> Secrets, add `GROQ_API_KEY = "your-key"`.
- **Other platforms:** add `GROQ_API_KEY` under Environment Variables or Secrets.
- **Local:** `export GROQ_API_KEY=your-key` (macOS/Linux) or `$env:GROQ_API_KEY="your-key"` (PowerShell).

Streamlit exposes top-level secrets as environment variables, so no code change is needed.

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```
Without a key the app still runs using rule-based checks.

## Cloud deployment
1. Push the project to GitHub.
2. On Streamlit Community Cloud choose New app, select the repository, branch and `app.py`.
3. Add `GROQ_API_KEY` in Secrets, then deploy.

## Security and privacy
- No secrets in the repository; the key is read from the environment and never logged.
- Submitted content is not written to disk or a database. Errors never echo request details.
- When AI is enabled, submitted text is sent to Groq for processing. The UI says so.
- All dynamic text is HTML-escaped before display. Input length is capped at 6,000 characters.

## Limitations
- Assessments rely only on the submitted content. Links are not opened or checked against live reputation data.
- Sender identity cannot be verified from text alone.
- Image, screenshot and QR inputs are not implemented yet.
- Rule patterns cover English, Urdu and Roman Urdu and are not exhaustive.

## Future roadmap
Image and screenshot analysis (vision model through Groq), QR decoding, URL reputation and domain-age lookups, more language packs, and a reporting export.
