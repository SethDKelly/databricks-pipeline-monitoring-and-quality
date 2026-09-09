# OPS-054 — Localization Vocabulary: First Observed, Earliest Evidenced, Boundary & Consumer Effect

**Status:** Accepted — Phase 007 Group 05

## Purpose

Prevent the common RCA error of treating every form of `first` as root cause.

## Contract

For an exact Investigation question, distinguish at least:

- **first observed deviation** — earliest qualifying deviation visible in the evidence/monitoring set under the chosen event-time ordering;
- **earliest evidenced state change** — earliest evidence-supported material state transition relevant to the outcome;
- **first localized transformation/reconciliation boundary** — earliest boundary where a previously satisfied/compatible relationship becomes mismatched under applicable reconciliation semantics;
- **first downstream consumer effect** — earliest evidenced downstream effect in consumer/Impact reasoning.

These can refer to different entities/times and can remain unknown, conflicting or indeterminate.

A `first` statement binds the searched scope, path/traversal criteria, metric/criterion, version/time ordering basis and evidence coverage.

## Invariants

- first observed deviation ≠ earliest true deviation.
- earliest evidenced change ≠ cause.
- first boundary mismatch ≠ cause.
- first consumer effect ≠ origin.
- restricted/out-of-scope upstream evidence can make localization indeterminate.
- later evidence may revise retrospective localization without rewriting the original as-known result.
