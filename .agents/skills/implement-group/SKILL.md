---
name: implement-group
description: Implement one human-selected DMTZ implementation package/group/task to its documented acceptance boundary. Use only when the human explicitly requests change/build/fix work; perform necessary in-scope edits and safe validation, then stop instead of beginning the next package.
---
# Implement group

## Human-directed boundary

This workflow is **A2 — change/build/fix** and only applies after a human selects the implementation package, group, or task to execute.

It may perform directly necessary supporting edits and safe validation inside that scope. It may not choose another backlog item, continue into the next package/group, delegate implementation to another agent, merge/deploy unattended, weaken DMTZ semantics, or convert bounded execution into autonomous continuation.

## Workflow

1. Resolve the task context using the `resolve-context` procedure: current implementation state, selected package/group, current semantic owners, affected stable IDs, and acceptance gates.
2. Inspect the existing files, tests, schemas, configuration, and prior execution evidence relevant to the selected task.
3. State the smallest compliant realization and any target-environment assumptions that materially affect it.
4. Implement the requested behavior without broad speculative refactoring.
5. Add or update the lowest-cost tests/fixtures/checks that prove the changed behavior when executable proof is part of the selected acceptance boundary.
6. Run the relevant safe, non-destructive validation available in the repository/environment. Do not rewrite requirements merely to make checks pass.
7. Update directly impacted documentation, status, indexes, ADRs, or traceability when required to keep the repository accurate.
8. Re-read the selected task's acceptance criteria and identify any unresolved mandatory item, degraded capability, or unverified external assumption.
9. Report completion evidence and stop at the boundary of the human-selected task.

## Supporting-change rule

Ordinary supporting changes do not require repetitive approval when directly necessary to finish the selected task, including tests, fixtures, same-task configuration/schema changes, directly impacted status/index updates, and bounded documentation corrections.

Unrelated cleanup, speculative features, another implementation package/group, broad architecture changes, or external/destructive actions are outside this envelope.

## Escalation

- For A3 actions, obtain explicit task-specific human authorization and preserve normal repository/team gates.
- For A4 conflicts, follow DMTZ change control. Implementation difficulty is not permission to change semantics.
- If a mandatory acceptance criterion cannot be proven, report it as unresolved; do not self-approve it.

## Output

Report scope completed, files/artifacts changed, contracts/acceptance gates addressed, validation/tests run or unavailable, traceability/status updates, assumptions/degraded states/failures, residual obligations, and the next eligible work as information only.

## Stop conditions

Stop after the selected package/group/task. Do not automatically start the next one even when all checks pass.
