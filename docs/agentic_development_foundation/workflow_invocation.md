# DMTZ Workflow Invocation Guide

**Status:** ACCEPTED — ADF-D

The canonical workflows live under `.agents/skills/`. They are human-directed task procedures, not autonomous workers.

| Workflow | Cursor | Claude Code | Codex | Default action class |
|---|---|---|---|---|
| `resolve-context` | `/resolve-context` | `/resolve-context` bridge | `$resolve-context` | A1 |
| `implement-group` | `/implement-group` | `/implement-group` bridge | `$implement-group` | A2 |
| `resolve-contract` | `/resolve-contract` | `/resolve-contract` bridge | `$resolve-contract` | A1 |
| `run-conformance` | `/run-conformance` | `/run-conformance` bridge | `$run-conformance` | A1 |
| `review-change` | `/review-change` | `/review-change` bridge | `$review-change` | A1 |
| `update-traceability` | `/update-traceability` | `/update-traceability` bridge | `$update-traceability` | A2 supporting |
| `exit-review` | `/exit-review` | `/exit-review` bridge | `$exit-review` | A1; A2 when explicitly recording exit artifacts |

Native invocation syntax is a compatibility convenience and remains subject to ADF-G runtime verification. If native discovery is unavailable, explicitly tell the tool to read `.agents/skills/<name>/SKILL.md` and follow it for the current task.

## Example intent

- “Use `resolve-context` for Implementation 003-C.” — read-only context resolution.
- “Use `implement-group` to execute ADF-E.” — implements only the selected group and stops.
- “Use `review-change` on this diff.” — review-only; findings do not authorize fixes.
- “Run `run-conformance` for the current change.” — safe checks/reporting; no deployment/external mutation.
- “Execute and record the group exit review.” — `exit-review` may create/update the bounded review/status artifact.

A skill name never overrides the human request. If the request and workflow conflict, apply `authority_scope_policy.md` and use the narrower authorized action.