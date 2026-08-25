# EXPL-038 — Transformation & Reconciliation Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

Questions such as `did the numbers reconcile?`, `where did rows go?`, or `does the output match the transformation rule?` must use the exact transformation/version/reconciliation definition and resulting Observation/Assessment.

## Rules

- local upstream/downstream metric values do not create a generic propagation equation;
- joins, filters, aggregations, dedupe, merge/upsert and derived-value behavior use their accepted reconciliation semantics;
- multi-input version/current-cycle alignment remains explicit;
- a reconciliation mismatch can support localization/diagnostic context without becoming root cause;
- `reconciles` does not automatically imply overall health;
- `does not reconcile` does not automatically imply downstream exposure or business consequence.