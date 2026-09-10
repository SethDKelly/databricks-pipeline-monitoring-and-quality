# Implementation Agent / Developer Instructions

**Current status: Implementation 001-A — NEXT / READY / NOT STARTED.**

Implementation begins only after the human explicitly selects a package or task. This directory governs implementation planning and execution boundaries; it does not own DMTZ semantics.

## Resolve authority before changing code

- Use `docs/index.md` when the current semantic location is unknown.
- Use `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` for exact current semantic ownership.
- Resolve known stable IDs with `python3 scripts/agentic/resolve_stable_id.py <ID>`; use `--history` only for explicit provenance/rationale work.
- Read the selected implementation package and the smallest current concept/contract/architecture/policy context needed for the task.
- Treat generated `knowledge/` as OKF compatibility routing only.

## Execution boundary

Implement the selected package/task and directly necessary supporting changes only. Do not automatically continue to the next package, perform broad speculative refactoring, weaken accepted semantics to simplify implementation, or infer deployment/runtime support from documentation.

Add the lowest-cost tests or executable evidence that prove the changed behavior where required. Update directly impacted traceability, ADRs, status, or documentation so the repository remains accurate.

Follow root `AGENTS.md` and `docs/agentic_development_foundation/authority_scope_policy.md` for shared human-directed, security, external-action, and change-control rules.
