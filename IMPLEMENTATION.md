# DMTZ Implementation — Start Here

**Current status: Implementation 001-A — NEXT / READY / NOT STARTED.**

Implementation work begins only when a human explicitly selects the implementation package or task. Readiness does not authorize automatic continuation.

## Before implementing

1. Read [`docs/implementation/README.md`](docs/implementation/README.md) for the current implementation program and package boundary.
2. Read [`AGENTS.md`](AGENTS.md) for repository-wide authority, workflow, semantic, and evidence rules.
3. Use [`docs/index.md`](docs/index.md) to locate current concepts, contracts, architecture, policies, invariants, authority, and reference material.
4. Resolve accepted stable IDs with `python3 scripts/agentic/resolve_stable_id.py <ID>`; use `--history` only for explicit provenance work.
5. Treat generated `knowledge/` as OKF compatibility routing, not semantic authority.

Current semantic ownership is declared by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. Historical design and completed program evidence are preserved under `docs/history/` and do not compete with current owners.

## Implementation discipline

Implement only the human-selected package/task and its directly necessary supporting changes. Preserve accepted semantic and architecture contracts, add the lowest-cost executable evidence appropriate to the change, update directly impacted traceability/documentation, and stop at the selected boundary.

Do not claim Databricks runtime support, deployment capability, integration behavior, performance, or production readiness without corresponding executable or target-environment evidence.
