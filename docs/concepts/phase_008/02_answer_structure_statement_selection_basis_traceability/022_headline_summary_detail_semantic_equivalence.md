# EXPL-022 — Headline, Summary & Detail Semantic Equivalence

**Status:** Accepted — Phase 008 Group 02

## Requirement

Allow one material statement or answer set to be rendered at different levels of detail while preserving compatible proposition meaning and epistemic strength.

A headline/summary may omit implementation detail, raw values or secondary context when that omission does not change:

- subject/scope materially;
- polarity;
- source/epistemic category;
- causal/Impact/control status;
- material temporal perspective;
- a limitation necessary to prevent overclaiming.

## Invariants

- concise ≠ stronger;
- detailed ≠ more certain merely because more basis is shown;
- headline and drill-down must not intentionally contradict the same underlying proposition;
- `cause unresolved` cannot become `root cause identified` in a headline;
- `exposure unknown` cannot become `no downstream impact` through summary compression.
