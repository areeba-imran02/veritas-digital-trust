# VERITAS Design System

**Tone:** premium, modern, futuristic, professional, global — digital trust / cybersecurity SaaS.
**One language.** All UI uses `frontend/src/styles/tokens.css`. No component may hard-code colours, radii, spacing or fonts.

## Themes
Dark, Light, System. System = no `data-theme` attribute (follows `prefers-color-scheme`). Controlled by `src/theme/theme.ts`.

## Colour roles
- Surfaces: `--bg`, `--surface`, `--surface-2`, `--border`
- Text: `--text`, `--text-muted`
- Accent (single brand accent): `--accent`, `--accent-contrast`
- Trust semantics (used ONLY for assessments): `--risk-low` (green), `--risk-verify` (amber), `--risk-high` (red). Never rely on colour alone — always pair with label/icon.

## Type, space, shape, motion
Sans UI font with mono for technical values (URLs, domains, hashes). 4px spacing scale. Radii 8/12/18. Motion is minimal and purposeful (120–220ms, honours reduced-motion).

## Wordmark
`VERITAS` in wide-tracked uppercase with a subtle dimensional treatment (soft layered depth/gradient, light-aware in both themes). No gaming/cartoon effects. Implemented as one reusable component in Prompt 8.

## Mapping
LOW_RISK → `--risk-low` · NEEDS_VERIFICATION → `--risk-verify` · HIGH_RISK → `--risk-high`.
Identity states use the same semantic colours (CONSISTENT=low, NEEDS_VERIFICATION/INSUFFICIENT_EVIDENCE=verify/neutral, MISMATCH_DETECTED=high).
