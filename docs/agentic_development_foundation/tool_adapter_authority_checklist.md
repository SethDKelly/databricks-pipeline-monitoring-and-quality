# Tool Adapter Authority Checklist

**Status:** ACCEPTED — ADF-A checklist; adapter realization continues in ADF-C/G

Use this checklist whenever a repository-level adapter is added or materially changed for Cursor, Claude Code, Codex or another supported coding agent.

The checklist verifies that a tool adapter preserves the shared authority/scope model. It does **not** certify native feature compatibility; ADF-C/G own that later work.

## Shared-authority checks

- [ ] Adapter identifies or inherits root `AGENTS.md` as shared repository behavioral authority where the tool permits it.
- [ ] Adapter references `docs/agentic_development_foundation/authority_scope_policy.md` or inherits equivalent wording through `AGENTS.md`.
- [ ] Adapter does not duplicate the full DMTZ semantic contract stack.
- [ ] Adapter does not declare a different live project/implementation status authority.
- [ ] Adapter cannot downgrade frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH obligations.
- [ ] Tool-specific convenience instructions are clearly lower precedence than shared repository authority.

## Human-directed boundary checks

- [ ] Review/inspect/audit requests remain read/review unless edits are explicitly requested.
- [ ] Implement/change/fix requests allow ordinary in-scope repository edits and safe validation without repetitive approval prompts.
- [ ] Completing one group does not automatically authorize starting the next group.
- [ ] Adapter does not authorize autonomous backlog selection or reprioritization.
- [ ] Adapter does not authorize agent-to-agent implementation delegation under the current foundation.
- [ ] External/destructive actions require task-specific human authorization plus applicable repository/team gates.
- [ ] Architecture/semantic changes route through DMTZ change control.

## Memory/context checks

- [ ] Native memory/auto-memory/chat history is described as noncanonical where the tool exposes such a feature.
- [ ] Adapter does not tell the agent to prefer remembered state over repository status/docs.
- [ ] Important persistent discoveries are promoted to repository artifacts rather than retained only in tool memory.

## Acceptance/test checks

- [ ] Tool output is evaluated using repository files/tests/traceability/review, not the identity of the agent/model.
- [ ] Loss of a native convenience feature degrades ergonomics, not semantic correctness.
- [ ] Contradictory adapter instructions are detectable through review or later ADF-F validation.
- [ ] Adapter remains small enough that it does not recreate monolithic persistent context.

## Initial ADF-A surface audit

| Surface | Current role | ADF-A result | Follow-up owner |
|---|---|---|---|
| root `AGENTS.md` | shared repository constitution | PASS after ADF-A synchronization | ADF-H lifecycle review |
| `.cursor/rules/00-implementation-routing.mdc` | scoped current-work router | PASS after ADF-A synchronization | ADF-C/E/F |
| remaining `.cursor/rules/*.mdc` | scoped domain mechanics/guardrails | PASS at authority layer; no known conflicting status authority | ADF-C/F full adapter audit |
| `.cursor/BUGBOT.md` | PR review policy | PASS; review-only surface does not grant implementation authority | ADF-C/F |
| `CLAUDE.md` / `.claude/` | not yet introduced | NOT YET APPLICABLE | ADF-C |
| Codex-specific repository adapter | intentionally not required yet beyond shared `AGENTS.md` | NOT YET APPLICABLE | ADF-C/G |

## Failure classification

A checklist failure involving only convenience/loading mechanics may be treated as an ADF-C/G compatibility gap.

The following are **blocking authority failures** and must not be accepted silently:

- a tool adapter claims semantic authority above canonical DMTZ docs/contracts;
- a tool adapter changes the current status source;
- a review request is configured to edit by default;
- a tool adapter grants unattended merge/deploy or autonomous scope expansion;
- tool memory is treated as canonical project state;
- architecture/change-control obligations are bypassed.
