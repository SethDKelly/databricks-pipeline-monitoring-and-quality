---
name: run-conformance
description: Run or guide the deterministic DMTZ checks appropriate to the current human-selected change/review scope and report evidence faithfully. Use for tests, validators, static checks, and scenario conformance; do not change requirements or fix failures unless the human also requested fixes.
---
# Run conformance

## Human-directed boundary

This workflow is normally **A1 — read/review/plan** even though it may execute safe, non-destructive tests and validators.

Running checks does not itself authorize repository edits. If the human also requested fixes, any fixes occur under the enclosing A2 task and its scope.

## Workflow

1. Resolve the current task/change scope and affected acceptance criteria/contracts.
2. Select the lowest-cost relevant checks defined by the repository: structural validators, unit/property, contract/schema, persistence, adapter, integration, scenario, or end-to-end only as justified.
3. Prefer repository-defined commands/configuration over remembered commands or tool-specific guesses.
4. Run safe, non-destructive checks available in the current environment. Do not trigger deployment, external mutation, destructive resets, or credential-dependent actions without explicit A3 authorization.
5. Capture pass/fail/skipped/unavailable results and enough evidence to make the result reproducible.
6. Distinguish design-scenario `PASS`, static configuration validation, and actual executable/runtime proof.
7. Report failures against the requirement; never weaken or rewrite the requirement to convert a failure into a pass.
8. Identify environment/tool limitations separately from product defects.

## Output

Report:

- checks selected and why;
- exact commands/checks run when applicable;
- pass/fail/skipped/unavailable evidence;
- requirement/contract coverage represented by the checks;
- environment or capability limitations;
- fixes required, without making them unless separately authorized.

## Stop conditions

Stop for explicit approval before A3 external/destructive actions. Route A4 semantic conflicts through DMTZ change control.