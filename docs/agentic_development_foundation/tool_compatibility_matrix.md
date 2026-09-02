# Agent Tool Compatibility Matrix

**Status:** DESIGN BASELINE — verify during ADF-G execution

This matrix defines the compatibility contract the foundation expects, not a permanent claim about vendor behavior. `external_standards_baseline.md` records the review date and sources.

| Capability | Cursor | Claude Code | Codex | DMTZ portability rule |
|---|---|---|---|---|
| Shared repository constitution | root `AGENTS.md` | thin `CLAUDE.md` imports/references `AGENTS.md` | root `AGENTS.md` | one shared authority, no semantic copies |
| Scoped/path-specific guidance | `.cursor/rules/*.mdc` | `.claude/rules/*.md` with paths | use shared/nested `AGENTS.md` or native mechanism where justified | scoping is convenience; canonical docs remain authority |
| Knowledge discovery | `knowledge/index.md` + repo search | same | same | OKF bundle is tool-neutral |
| Stable contract lookup | repository search/read | same | same | exact IDs route to canonical `docs/` |
| Portable workflow source | `agent-skills/<name>/SKILL.md` | same canonical source with native adapter | same canonical source/native support as available | workflow semantics defined once |
| Native skill/command adapter | Cursor command/rule mechanism if useful | `.claude/skills/<name>/SKILL.md` | native skills/config if supported | adapter may not change required steps |
| Persistent model/tool memory | noncanonical | auto-memory noncanonical | noncanonical | durable team facts must be checked in |
| Local edits/tests | expected | expected | expected | normal repository acceptance applies |
| Agentic conformance checks | repository scripts/CI | same | same | deterministic validation is shared |
| Human-directed scope boundary | shared `AGENTS.md` + routing rule | shared authority via `CLAUDE.md` | shared `AGENTS.md` | no autonomy implied by native capabilities |
| Autonomous/multi-agent operation | deferred | deferred | deferred | not part of foundation acceptance |

## Compatibility states

For each tool/native feature, execution should record one of:

- **verified** — exercised against the current supported version/profile;
- **degraded** — core development works but one convenience/native integration is unavailable;
- **unverified** — assumed from documentation but not recently exercised;
- **unsupported** — not part of the supported profile; use portable/manual fallback if possible.

Do not turn these into a universal ranking of tools.

## Acceptance principle

A tool is compatible when a developer can complete the bounded repository workflow while preserving shared authority, retrieving canonical context, making/reviewing changes, and passing shared validation. Native UX parity is not required.
