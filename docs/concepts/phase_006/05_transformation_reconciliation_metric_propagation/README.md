# Phase 006 Group 05 — Transformation Reconciliation & Metric Propagation

**Status:** Planned — not yet started

## Goal

Define when upstream/downstream metrics have meaningful transformation-aware relationships rather than recursively copying statistics through Lineage.

## Review scope

- local metric versus related upstream evidence versus derived reconciliation measure;
- joins: match/unmatched rate, fan-out, key completeness and population effects;
- filters and expected exclusion/reconciliation;
- aggregations and balance/total conservation where semantically valid;
- deduplication and uniqueness effects;
- unions/merges and source contribution measures;
- null introduction/removal through transformation;
- freshness/current-cycle dependency alignment;
- distribution/quantile relationships only when transformation semantics preserve meaning;
- multiple upstream contributors without forced causal attribution;
- downstream consumer/path-specific relevance;
- propagation of metric limitations/provenance without blind metric inheritance.

## Accepted handoff

HLTH-001–HLTH-008 bind local measurements and explicitly prohibit Lineage-only propagation. Groups 02–04 provide structural compatibility, Baseline/comparability and Assessment semantics before reconciliation is composed across transformations.

## Boundaries

A+B→C never implies generic row-count arithmetic. Upstream anomaly does not automatically become downstream failure or cause. Group 05 defines functional reconciliation; Phase 007 later refines Lineage-aware operational propagation/change behavior.

**Group 05 has not started.**
