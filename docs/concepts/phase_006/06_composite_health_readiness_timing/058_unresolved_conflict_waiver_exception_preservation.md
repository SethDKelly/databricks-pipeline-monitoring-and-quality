# HLTH-058 — Unresolved State, Conflict, Waiver & Exception Preservation in Composite Health

**Status:** Accepted — Phase 006 Group 06

## Purpose

Ensure composition does not convert incomplete, conflicting, waived, or non-applicable component state into a falsely clean summary.

## Rules

- Required `indeterminate/insufficient`, `conflicting`, and `unavailable` states remain visible in the composite unless explicit composition logic renders that branch irrelevant.
- `violates + waived response` remains a violation for composite health; the waiver is retained as a separate disposition qualifier.
- A bounded exception that makes a criterion genuinely `not applicable` can remove that component from the applicable profile according to the accepted rule.
- Waiver of alerting, escalation, or another response class does not automatically waive composite-health truth or readiness/control consequences.
- Restricted component detail may be hidden in an Authorized Analytical Projection, but a hidden required violation or unresolved component cannot be translated into `healthy`.
- A known violation plus unresolved components can be summarized as degraded with incomplete/unresolved qualifiers when that is the logical result.
- A required conflict is not silently resolved by selecting the more favorable or more severe child.
- `not applicable` is not counted as a passing vote.

## Invariant

Composition may reduce detail for an audience, but never strengthen the underlying health proposition.