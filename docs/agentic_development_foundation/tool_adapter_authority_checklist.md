# Tool Adapter Authority Checklist

**Status:** ACCEPTED — ADF-C repository-adapter audit complete / ROUTING REBOUND DPTN-F

Use this checklist whenever a repository-level adapter is added or materially changed for Cursor, Claude Code, Codex or another supported coding agent.

The checklist verifies that a tool adapter preserves the shared authority/scope model. It does **not** certify a vendor binary/version at runtime; ADF-G owns tool-in-the-loop verification and repository conformance owns deterministic adapter checks.

## Shared-authority checks

- [x] Every supported adapter identifies or inherits root `AGENTS.md` as shared repository behavioral authority.
- [x] Adapters inherit `authority_scope_policy.md` through `AGENTS.md`; no separate action model is maintained.
- [x] No adapter duplicates the full DMTZ semantic contract stack.
- [x] No adapter declares a different live project/implementation status authority.
- [x] No adapter downgrades frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH obligations.
- [x] Tool-specific mechanics are lower precedence than shared repository authority.

## Human-directed boundary checks

- [x] Review/inspect/audit requests remain read/review unless edits are explicitly requested.
- [x] Implement/change/fix requests allow ordinary in-scope repository edits and safe validation without repetitive approval prompts.
- [x] Completing one group does not automatically authorize starting the next group.
- [x] Adapters do not authorize autonomous backlog selection or reprioritization.
- [x] Adapters do not authorize agent-to-agent implementation delegation under the current foundation.
- [x] External/destructive actions remain subject to task-specific human authorization plus repository/team gates.
- [x] Architecture/semantic changes route through DMTZ change control.

## Memory/context checks

- [x] Native memory/auto-memory/chat history remains noncanonical.
- [x] No adapter prefers remembered state over repository status/docs.
- [x] Important persistent discoveries must be promoted to repository artifacts.
- [x] Repository-native discovery begins at `docs/index.md` when the current location is not already known.
- [x] Generated `knowledge/index.md` is identified only as an OKF v0.2 compatibility entry.
- [x] Exact stable IDs bypass discovery through `scripts/agentic/resolve_stable_id.py`; historical lookup is explicit `--history` only.

## Acceptance/test checks

- [x] Tool output is evaluated using repository files/tests/traceability/review, not agent/model identity.
- [x] Loss of a native convenience feature degrades ergonomics, not semantic correctness.
- [x] Contradictory adapter instructions are detectable through `scripts/agentic/validate_agent_adapters.py` and repository conformance.
- [x] Persistent adapter surfaces remain intentionally small.

## Current surface audit

| Surface | Role | Result / owner |
|---|---|---|
| root `AGENTS.md` | shared repository constitution | current |
| `docs/index.md` | repository-native discovery root | current; DPTN-F rebound |
| generated `knowledge/index.md` | OKF compatibility entry | current compatibility only |
| `.cursor/rules/00-implementation-routing.mdc` | scoped current-work router | current |
| remaining `.cursor/rules/*.mdc` | scoped domain mechanics/guardrails | current; first-class paths after DPTN-F |
| `.cursor/BUGBOT.md` | separate PR-review policy | does not redefine implementation authority |
| `.claude/CLAUDE.md` | Claude Code compatibility bridge | imports `../AGENTS.md`; routes discovery to `docs/index.md` |
| `.claude/rules/` | optional Claude path-scoped mechanics | avoid until demonstrated need |
| Codex repository adapter | native root `AGENTS.md` | no additional semantic adapter |
| `tool_compatibility.json` | operational compatibility manifest | current discovery/compatibility split |

## Deliberate Claude placement decision

DMTZ uses `.claude/CLAUDE.md`, not root `CLAUDE.md`. This avoids adding a second universal instruction surface while allowing Claude Code to import shared `AGENTS.md` directly. This is a tool-mechanics decision, not a change to DMTZ authority.

## Failure classification

A failure involving only convenience/loading mechanics may be treated as a provider compatibility gap when canonical authority remains available.

The following are **blocking authority failures** and must not be accepted silently:

- a tool adapter claims semantic authority above current DMTZ owners;
- a tool adapter changes the current status source;
- a review request is configured to edit by default;
- a tool adapter grants unattended merge/deploy or autonomous scope expansion;
- tool memory is treated as canonical project state;
- architecture/change-control obligations are bypassed;
- a new tool-specific persistent file reproduces shared DMTZ semantics instead of importing/routing to them.
