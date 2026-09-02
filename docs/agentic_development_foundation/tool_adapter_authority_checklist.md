# Tool Adapter Authority Checklist

**Status:** ACCEPTED — ADF-C repository-adapter audit complete; runtime compatibility continues in ADF-G

Use this checklist whenever a repository-level adapter is added or materially changed for Cursor, Claude Code, Codex or another supported coding agent.

The checklist verifies that a tool adapter preserves the shared authority/scope model. It does **not** certify a vendor binary/version at runtime; ADF-G owns tool-in-the-loop smoke verification and ADF-F owns CI enforcement.

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
- [x] Portable discovery begins at `knowledge/index.md` when the canonical location is not already known.

## Acceptance/test checks

- [x] Tool output is evaluated using repository files/tests/traceability/review, not agent/model identity.
- [x] Loss of a native convenience feature degrades ergonomics, not semantic correctness.
- [x] Contradictory adapter instructions are detectable through `scripts/agentic/validate_agent_adapters.py` and later ADF-F automation.
- [x] Persistent adapter surfaces remain intentionally small.

## ADF-C surface audit

| Surface | Role | ADF-C result | Follow-up owner |
|---|---|---|---|
| root `AGENTS.md` | shared repository constitution | PASS | ADF-H lifecycle review |
| `knowledge/index.md` | portable discovery entry | PASS | ADF-E/F maintenance/conformance |
| `.cursor/rules/00-implementation-routing.mdc` | scoped current-work router | PASS | ADF-E/F |
| remaining `.cursor/rules/*.mdc` | scoped domain mechanics/guardrails | PASS; no intentional `alwaysApply: true` rules | ADF-F/G runtime confirmation |
| `.cursor/BUGBOT.md` | separate PR-review policy | PASS; does not redefine implementation authority | ADF-F |
| `.claude/CLAUDE.md` | Claude Code compatibility bridge | PASS; imports `../AGENTS.md`, adds only Claude mechanics | ADF-G runtime smoke |
| `.claude/rules/` | optional Claude path-scoped mechanics | NOT REQUIRED by ADF-C; avoid until demonstrated need | future scoped need |
| Codex repository adapter | native root `AGENTS.md` | PASS; no additional semantic adapter introduced | ADF-G runtime smoke |
| `tool_compatibility.json` | operational compatibility manifest | PASS | ADF-H review horizon |

## Deliberate Claude placement decision

ADF-C uses `.claude/CLAUDE.md`, not root `CLAUDE.md`.

Current Claude Code documentation supports either location and resolves relative `@` imports from the containing file. Current Cursor documentation states that a root `CLAUDE.md` is also loaded as persistent project instructions. Using `.claude/CLAUDE.md` therefore avoids adding a second universal instruction surface to Cursor while allowing Claude Code to import `../AGENTS.md` directly.

This is a tool-mechanics decision, not a change to DMTZ authority.

## Failure classification

A failure involving only convenience/loading mechanics may be treated as an ADF-G compatibility gap when canonical authority remains available.

The following are **blocking authority failures** and must not be accepted silently:

- a tool adapter claims semantic authority above canonical DMTZ docs/contracts;
- a tool adapter changes the current status source;
- a review request is configured to edit by default;
- a tool adapter grants unattended merge/deploy or autonomous scope expansion;
- tool memory is treated as canonical project state;
- architecture/change-control obligations are bypassed;
- a new tool-specific persistent file reproduces shared DMTZ semantics instead of importing/routing to them.
