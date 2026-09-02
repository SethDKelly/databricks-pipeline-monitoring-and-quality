# DMTZ Agent Context Budget Policy

**Status:** ACCEPTED — ADF-E

## Purpose

Keep persistent and routinely loaded agent context measurably small while leaving detailed DMTZ semantics available on demand.

Budgets use **UTF-8 bytes**, not model tokens. Bytes are deterministic in repository validation; provider-specific token counts remain observational compatibility data for ADF-G.

Machine-readable limits live in `context_budget.json`.

## Persistent-surface budgets

| Surface | Limit |
|---|---:|
| root `AGENTS.md` | 16 KiB |
| `.claude/CLAUDE.md` | 2 KiB |
| one `.cursor/rules/*.mdc` | 6 KiB |
| all Cursor project rules combined | 32 KiB |
| Cursor root baseline (`AGENTS.md` + intentionally always-applied rule content + root `CLAUDE.md` if ever introduced) | 20 KiB |
| Claude root baseline (`AGENTS.md` + `.claude/CLAUDE.md`) | 18 KiB |
| Codex root baseline (`AGENTS.md`) | 16 KiB |

The tool baselines are conservative repository byte envelopes, not claims about exact vendor prompt construction.

## On-demand budgets

| Surface | Limit |
|---|---:|
| one canonical `.agents/skills/*/SKILL.md` | 7 KiB |
| one `.claude/commands/*.md` bridge | 1 KiB |
| `knowledge/index.md` | 4 KiB |
| one nested `knowledge/**/index.md` | 6 KiB |
| one non-index OKF routing concept | 4 KiB |

These limits keep routing/procedure artifacts focused. A canonical DMTZ contract document is not forced into these budgets; it is retrieved only when needed.

## Current measured baseline

At ADF-E execution on 2026-09-02, GitHub reports:

- root `AGENTS.md`: 12,699 bytes;
- `.claude/CLAUDE.md`: 1,054 bytes.

Both remain below their ADF-E limits. Cursor domain rules remain scoped/relevance-driven and no ADF rule is intentionally `alwaysApply: true`.

## Budget semantics

- Budget failure is a context/configuration conformance problem, not permission to delete required repository semantics.
- Move detailed procedure/domain material to on-demand skills/OKF/canonical docs rather than truncating obligations.
- A measured need may justify revising a budget through ADF governance; a tool's larger context window alone is not sufficient justification.
- Aggregate repository documentation size is irrelevant to startup context when progressive disclosure is working.

## Measurement

`scripts/agentic/measure_context_budget.py` measures the repository surfaces above and exits nonzero when a hard byte budget is exceeded.

ADF-F owns CI integration. ADF-G may add observed tool-specific prompt/token measurements without replacing these deterministic byte checks.
