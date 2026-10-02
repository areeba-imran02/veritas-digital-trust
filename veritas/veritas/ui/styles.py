"""VERITAS design system: colour tokens, typography and component styles. Contrast targets WCAG AA."""

LIGHT = """--bg:#F4F6F9;--surface:#FFFFFF;--surface2:#EBEFF5;--text:#0F172A;--muted:#41506A;--border:#C3CDDB;--accent:#0B6B6B;--accent-text:#FFFFFF;--focus:#0B4FD6;
--wm-hi:#FFFFFF;--wm-lo:rgba(15,23,42,.28);
--high-bg:#FDE8E6;--high-fg:#8A1C12;--high-bd:#D9534A;--need-bg:#FFF1D6;--need-fg:#6B4100;--need-bd:#D4912A;
--low-bg:#E1F4E8;--low-fg:#0E5A2B;--low-bd:#3A9B62;--ins-bg:#E9EDF3;--ins-fg:#2F3B52;--ins-bd:#8795AD;"""
DARK = """--bg:#0A101C;--surface:#121B2B;--surface2:#1A2539;--text:#EEF2F8;--muted:#B3BFD2;--border:#2F3F5A;--accent:#5CD6C8;--accent-text:#04201D;--focus:#8DB4FF;
--wm-hi:rgba(255,255,255,.22);--wm-lo:rgba(0,0,0,.65);
--high-bg:#3A1513;--high-fg:#FFB4AC;--high-bd:#E5675C;--need-bg:#3A2A0C;--need-fg:#FFD58A;--need-bd:#D9A441;
--low-bg:#0F2F1E;--low-fg:#9BE3B8;--low-bd:#45B574;--ins-bg:#1E2A3F;--ins-fg:#D3DCEA;--ins-bd:#8795AD;"""

BASE = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,800&family=Inter:wght@400;500;600;700&display=swap');
html,body,.stApp{background:var(--bg)!important;color:var(--text)!important;font-family:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;}
header[data-testid="stHeader"]{background:transparent!important;}
.block-container{max-width:1040px;padding:2rem 1.25rem 4rem!important;}
.stApp p,.stApp li,.stApp label,.stApp span,.stApp div[data-testid="stMarkdownContainer"]{color:var(--text);}
.vt-wordmark{font-family:'Fraunces',Georgia,serif;font-weight:800;font-size:clamp(2.4rem,7vw,3.8rem);letter-spacing:.14em;line-height:1.05;margin:0;color:var(--text);
 text-shadow:0 1px 0 var(--wm-hi),0 2px 0 var(--wm-lo),0 3px 1px var(--wm-lo),0 6px 10px var(--wm-lo);}
.vt-tag{font-size:1.125rem;font-weight:500;color:var(--muted);margin:.35rem 0 0;}
.vt-intro{font-size:1rem;line-height:1.6;color:var(--muted);max-width:60ch;margin:.9rem 0 1.6rem;}
.vt-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:1.25rem 1.4rem;margin:0 0 1rem;}
.vt-card h3{font-size:1.05rem;font-weight:700;margin:0 0 .7rem;color:var(--text);}
.vt-card p,.vt-card li{font-size:1rem;line-height:1.6;color:var(--text);}
.vt-card ul{margin:0;padding-left:1.2rem;}.vt-card li{margin:.35rem 0;}
.vt-muted{color:var(--muted)!important;font-size:.92rem!important;}
.vt-badge{display:inline-block;padding:.45rem 1rem;border-radius:999px;font-weight:700;font-size:1.1rem;letter-spacing:.04em;border:2px solid;}
.vt-hero{border-radius:16px;padding:1.5rem 1.6rem;border:2px solid;margin:0 0 1rem;}
.vt-hero h2{font-size:1rem;font-weight:600;margin:0 0 .6rem;color:inherit;}
.vt-hero p{margin:.9rem 0 0;font-size:1.05rem;line-height:1.6;color:inherit;}
.vt-high{background:var(--high-bg);color:var(--high-fg);border-color:var(--high-bd);}
.vt-need{background:var(--need-bg);color:var(--need-fg);border-color:var(--need-bd);}
.vt-low{background:var(--low-bg);color:var(--low-fg);border-color:var(--low-bd);}
.vt-ins{background:var(--ins-bg);color:var(--ins-fg);border-color:var(--ins-bd);}
.vt-hero .vt-badge{background:transparent;color:inherit;border-color:currentColor;}
.vt-row{display:flex;gap:.6rem;align-items:baseline;justify-content:space-between;border-top:1px solid var(--border);padding:.65rem 0;}
.vt-row:first-of-type{border-top:0;}.vt-src{font-size:.85rem;font-weight:600;color:var(--muted);white-space:nowrap;}
.vt-chip{display:inline-block;padding:.2rem .65rem;border-radius:8px;background:var(--surface2);border:1px solid var(--border);font-weight:600;font-size:.95rem;color:var(--text);}
textarea,input{background:var(--surface)!important;color:var(--text)!important;border:1px solid var(--border)!important;border-radius:10px!important;font-size:1rem!important;}
textarea::placeholder{color:var(--muted)!important;opacity:1;}
div[data-baseweb="textarea"],div[data-baseweb="base-input"]{background:var(--surface)!important;border-radius:10px!important;}
div[data-testid="stRadio"] label p{color:var(--text)!important;font-size:1rem;}
.stButton>button,.stFormSubmitButton>button{border-radius:10px;font-weight:600;font-size:1rem;min-height:2.8rem;border:1px solid var(--border);background:var(--surface);color:var(--text);transition:transform .12s ease,box-shadow .12s ease;}
.stButton>button:hover{transform:translateY(-1px);border-color:var(--accent);box-shadow:0 3px 10px rgba(0,0,0,.12);}
.stButton>button[kind="primary"]{background:var(--accent);color:var(--accent-text);border-color:var(--accent);}
.stButton>button[kind="primary"] p{color:var(--accent-text)!important;}
.stButton>button:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid var(--focus)!important;outline-offset:2px;}
details{background:var(--surface);border:1px solid var(--border)!important;border-radius:12px;}
details summary p{color:var(--text)!important;font-weight:600;}
div[data-testid="stAlert"]{border-radius:12px;}
@media (max-width:640px){.block-container{padding:1.2rem .9rem 3rem!important;}.vt-row{flex-direction:column;gap:.15rem;}.vt-hero{padding:1.2rem;}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;}}
"""


def css(theme: str) -> str:
    if theme == "Dark":
        tokens = f":root{{{LIGHT}}}:root{{{DARK}}}"
    elif theme == "Light":
        tokens = f":root{{{LIGHT}}}"
    else:
        tokens = f":root{{{LIGHT}}}@media (prefers-color-scheme:dark){{:root{{{DARK}}}}}"
    return f"<style>{tokens}{BASE}</style>"
