---
name: update-traceability
description: Update DMTZ implementation traceability/status for material behavior already implemented or changed within a human-authorized A2 task. Use only when evidence exists; never mark contracts satisfied from prose, model confidence, or design-only PASS.
---
# Update traceability

## Human-directed boundary

This is an **A2 supporting workflow**. Use it only when traceability is explicitly requested or directly necessary to complete an already-authorized A2 implementation task. It does not authorize new behavior.

## Workflow

1. Identify the behavior/change and active implementation/ADF scope.
2. Resolve each accepted contract ID with `python3 scripts/agentic/resolve_stable_id.py <ID>` and retain the returned canonical **locator** (`owner_path::ID`). Use `--history` only when provenance is itself evidence needed by the traceability question.
3. Keep contract identity/location separate from implementation evidence. Resolver success proves routing, not implementation.
4. Inspect the executable/static/manual/integration/runtime evidence actually available.
5. Update only the existing traceability/status artifact owned by the active program/group; do not create a parallel authority surface.
6. Record only the evidence level actually proven and preserve unresolved/degraded/skipped/unavailable/unverified states.
7. Do not imply a broader package/group is complete unless its mandatory exit gates are satisfied.

## Output

Report the traceability/status artifact changed, contract IDs and canonical locators, supporting evidence references, evidence level/status, and unresolved claims intentionally not advanced.

## Stop conditions

Do not mark a contract/group/package satisfied without required evidence. A canonical locator, agent statement or unrelated passing check is not implementation proof.
