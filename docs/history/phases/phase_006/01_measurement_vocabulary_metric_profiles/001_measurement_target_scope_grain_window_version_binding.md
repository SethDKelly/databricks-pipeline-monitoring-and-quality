# HLTH-001 — Measurement Target, Scope, Grain, Window & Version Binding

**Status:** Accepted — Phase 006 Group 01

## Purpose

Prevent a metric/check value from being interpreted outside the exact subject, grain, time/window, version and context that make the measurement meaningful.

## Contract

Every material metric/check evaluation should be bound, where applicable, to:

- measured subject/entity;
- metric/check definition identity and version;
- environment/context;
- event/effective or evaluation window;
- grain/population/partition/cohort represented;
- relevant output/data/schema version or current-cycle identifier;
- consumer/path when the metric is consumer-specific;
- unit/measure domain;
- evaluation time and framework knowledge cut where historically relevant.

A value without sufficient binding remains ambiguous evidence rather than being silently attached to the nearest table/job/current state.

## Invariants

- `row_count = 1,000,000` is not meaningful health evidence without knowing which table/output/window/grain/version it measures.
- Column metrics must identify the field/semantic role and relevant schema/definition version.
- Transformation metrics must identify the transformation/relationship context rather than being treated as generic table statistics.
- Current retrieval of an older measurement does not make it a current-state measurement.
- Same subject name does not prove same Entity Identity or same measurement grain across time.
- Profile membership does not repair missing metric binding.
- Capability Authorization/disclosure may hide some bound detail from a requester, but the internal measurement must retain enough binding to support the conclusion.

## Handoff

Group 03 later decides whether two bound measurements are empirically comparable. Group 05 later decides when a bound upstream/transformation metric has a meaningful downstream reconciliation relationship.
