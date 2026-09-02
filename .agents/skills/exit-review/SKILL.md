---
name: exit-review
description: Evaluate one human-selected DMTZ ADF/implementation group or package against its documented exit gates and evidence. Use to produce a rigorous exit decision; unresolved mandatory criteria cannot be self-approved or converted to PASS.
---
# Exit review

## Human-directed boundary

Evaluation is **A1 — read/review/plan**. If the human explicitly asks to execute/record the repository exit review, writing the bounded review/status artifact is an **A2 supporting action** within that selected group.

This workflow cannot start the next group.

## Workflow

1. Identify the exact group/package selected by the human and its canonical exit/acceptance criteria.
2. Resolve the governing authority, relevant stable IDs, and any required execution-evidence standard.
3. Inventory delivered files/artifacts and inspect the actual resulting repository state.
4. Inventory validation evidence and classify it accurately: design review, static structure, executable test, integration/runtime, production/deployment, manual verification, skipped/unavailable.
5. Evaluate each mandatory exit criterion independently as PASS, FAIL, DEGRADED/WAIVED where explicitly permitted, or UNVERIFIED.
6. Confirm non-goals/deferred work have not leaked into accepted scope and that unresolved items have explicit owners/dependencies.
7. Check live status/index surfaces for consistency if the review is being recorded as an A2 task.
8. Make one exit decision based on the mandatory gates, not on overall confidence or effort spent.
9. If accepted and repository recording was requested, update only the directly affected exit/status artifacts and then stop.

## Output

Provide:

- review question and conclusion;
- delivered artifacts;
- criterion-by-criterion findings;
- validation/evidence classification;
- residual obligations/debt;
- explicit exit decision;
- next eligible group as information only.

## Stop conditions

Do not self-waive a mandatory criterion, manufacture evidence, equate design PASS with executable proof, or begin the next group after acceptance.