---
name: update-traceability
description: Update DMTZ implementation traceability/status for material behavior already implemented or changed within a human-authorized A2 task. Use only when evidence exists; never mark contracts satisfied from prose, model confidence, or design-only PASS.
---
# Update traceability

## Human-directed boundary

This is an **A2 supporting workflow**. Use it when the human explicitly requests traceability work or when traceability/status updates are directly necessary to complete an already-authorized A2 implementation task.

It does not authorize new product behavior or a new implementation group.

## Workflow

1. Identify the material behavior/change being traced and the active implementation/ADF scope.
2. Resolve the exact stable contract/scenario IDs and acceptance gates that the behavior claims to realize.
3. Inspect the executable/static/manual evidence actually available: tests, validators, deployment/runtime evidence, or accepted review artifacts as appropriate.
4. Update the existing traceability/status/index artifact owned by the active program/group. Do not invent a parallel authority surface merely for convenience.
5. Record only the evidence level actually proven. Distinguish design acceptance, static conformance, executable tests, integration evidence, and runtime/production evidence.
6. Preserve unresolved, degraded, skipped, unavailable, or unverified states explicitly.
7. Ensure the update does not imply that a broader package/group is complete unless its documented mandatory exit gates are satisfied.

## Output

Report:

- traceability/status artifact changed;
- contract/scenario IDs affected;
- supporting evidence references;
- evidence level/status recorded;
- unresolved gaps or claims intentionally not advanced.

## Stop conditions

Do not mark a contract, group, or package satisfied without the required supporting evidence. Do not treat an agent statement or passing unrelated check as proof.