# Agentic Change Governance

**Status:** ACCEPTED — ADF-H

Agentic artifacts follow DMTZ authority; they do not create semantic authority by themselves.

## Change classes

| Class | Typical changes | Required review/evidence |
|---|---|---|
| **G1 — routing/content maintenance** | OKF links, descriptions, lifecycle metadata, navigation | canonical resource still correct; OKF validation; no semantic copy introduced |
| **G2 — workflow behavior** | `.agents/skills/`, Claude command bridges | A1–A4 boundary review; skill/adapter validation; affected fixtures; conformance |
| **G3 — tool adapter / compatibility** | Cursor rules, `.claude/CLAUDE.md`, provider bridges, compatibility evidence | vendor behavior reverified where material; adapter/runtime state updated; degraded fallback preserved; conformance |
| **G4 — shared authority / security** | root `AGENTS.md`, authority policy, secret/sensitive-data rules, permission boundary | cross-tool impact review; security validator/scanner; context budgets; full agentic conformance |
| **G5 — DMTZ semantic / architecture** | accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meaning | existing DMTZ semantic/change-control process first; agentic routing refreshed only as a consequence |

A lower class cannot be used to disguise a higher-impact change.

## Review ownership

- Humans own acceptance of shared authority, security policy and DMTZ semantics.
- Deterministic validators may establish structural/process conformance only.
- An agent may propose or implement a human-selected G1–G4 change under A2, but may not self-authorize A3/A4 consequences.
- Agent-generated content is not independent verification merely because another pass of the same agent rereads it.

## Provider-specific changes

A tool-specific adapter may improve ergonomics, but may not weaken shared security, human-direction, canonical-reference or semantic requirements.

If a provider cannot express a required repository behavior natively, use a documented shared/manual fallback and mark the feature degraded/unverified. Do not fork DMTZ semantics to achieve native UX parity.

## External integrations

A repository-level MCP server, plugin, extension, remote agent or cloud execution integration is at least G3 and becomes G4 when it changes permission, secret, network, retention or security boundaries.

Record the provider/source, privileges, data exposure, retention/telemetry, update path and fallback before adoption.

## Emergency rollback

If an agentic change causes unsafe routing or blocks ordinary development:

1. restore the last reviewed repository instruction/workflow state;
2. keep canonical DMTZ docs/contracts unchanged unless a separate semantic change is authorized;
3. mark affected tool compatibility `degraded` or `unverified`;
4. record the failure and required re-verification;
5. rerun agentic conformance before restoring normal support claims.
