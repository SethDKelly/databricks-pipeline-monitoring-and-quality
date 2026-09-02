---
name: review-change
description: Review a DMTZ change/diff against canonical contracts, human-directed scope, security, temporal/evidence semantics, and executable-test obligations. Use for substantive review; remain read-only unless the human separately requests fixes.
---
# Review change

## Human-directed boundary

This workflow is **A1 — read/review/plan**. Finding a defect does not authorize editing it.

## Workflow

1. Resolve what was intended to change, the human-selected scope, and the applicable active group/package.
2. Inspect the actual diff/files rather than relying on a prose summary of the change.
3. Resolve affected stable contracts and acceptance gates using exact canonical sources.
4. Check for semantic regressions, especially DMTZ non-negotiable distinctions involving evidence, time, identity, authority/authorization, health, Lineage/Impact/causality, historical replay, disclosure, and active-control states where applicable.
5. Check security/privacy boundaries, secrets/sensitive data handling, external-action assumptions, and permission/authority conflation.
6. Check whether tests/fixtures/validation prove the changed behavior at the lowest appropriate executable level.
7. Check status/traceability/documentation only where the change materially affects them.
8. Prioritize substantive correctness/risk findings over style preferences.
9. Distinguish confirmed defects from questions, capability gaps, and unverified assumptions.

## Output

For each material finding provide:

- severity/impact;
- exact file/location;
- violated contract/acceptance expectation when known;
- why it matters;
- bounded remediation direction.

Also state validation gaps and whether no material findings were found.

## Stop conditions

Do not edit files unless the human explicitly changes the task to A2 fix/change work. Do not invent architecture requirements to justify stylistic preferences.