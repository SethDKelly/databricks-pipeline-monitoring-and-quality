# Phase 009 Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence

**Status:** Review complete — accepted

## Result

Group 04 accepts **INTG-084–INTG-119** and **HME04-01–HME04-56**. No new product concept is required.

The group maps concrete structural, measurement, rule, profiling and quality-monitoring surfaces to the accepted Phase 006 health model without creating a vendor-owned universal health truth.

The central source chain is:

**exact subject/run/output/context → realized structural or metric/check source evidence → Observation → explicit Baseline/reference and/or governed Expectation binding → Assessment → transformation reconciliation / composite-profile composition → freshness/result-suitability context**.

No layer automatically creates the next.

## Accepted contracts

1. **INTG-084** — Current Realized Schema Metadata Surface
2. **INTG-085** — Table-History Structural Change & Replay
3. **INTG-086** — Schema Identity, Rename & Recreate Continuity
4. **INTG-087** — Constraint Declaration & Enforcement Separation
5. **INTG-088** — Consumer-Specific Compatibility Source Gap
6. **INTG-089** — DQX Surface, Version & Pinning
7. **INTG-090** — DQX Rule Identity, Definition & Storage
8. **INTG-091** — DQX Detailed Result Observation
9. **INTG-092** — DQX Summary Metrics & Run Binding
10. **INTG-093** — DQX Profiling / Rule-Generation Candidate Boundary
11. **INTG-094** — DQX Criticality / Action Governance Boundary
12. **INTG-095** — Lakeflow Expectation Definition & Action
13. **INTG-096** — Lakeflow Expectation Event-Log Metrics
14. **INTG-097** — Lakeflow Fail-Expectation Metric Gap
15. **INTG-098** — Metric-View Definition & Measure Semantics
16. **INTG-099** — Metric-View Specification Version vs Definition Revision
17. **INTG-100** — Metric-View Query Observation & Grain
18. **INTG-101** — Metric-View Materialization & Freshness Boundary
19. **INTG-102** — Data-Profiling Profile Metrics as Observations
20. **INTG-103** — Data-Profiling Drift & Baseline Semantics
21. **INTG-104** — Data-Profiling Custom Metric Definition
22. **INTG-105** — Anomaly-Detection Freshness / Completeness Model
23. **INTG-106** — Anomaly-Detection Health-Status Projection
24. **INTG-107** — Anomaly-Detection Root-Cause / Impact Label Boundary
25. **INTG-108** — Baseline Membership, Version & Authority Contract
26. **INTG-109** — Measurement Window, Slice & Cohort Binding
27. **INTG-110** — Measurement ↔ Run / Output-Version Binding
28. **INTG-111** — Reconciliation Source Evidence Contract
29. **INTG-112** — Join / Fan-Out Metric-Semantics Boundary
30. **INTG-113** — Commit Freshness vs Event Freshness
31. **INTG-114** — Current-Cycle Alignment & Input-Version Gap
32. **INTG-115** — Result Timing, Scan / Refresh & Availability
33. **INTG-116** — Health-Source Historical Replay & Retention
34. **INTG-117** — Missing Metric / Check / Schema Negative Claims
35. **INTG-118** — Health-Source Conflict & Composition
36. **INTG-119** — Group 04 Health Source Matrix & Group 05 Handoff

## Structural evidence

Unity Catalog Information Schema is a strong current realized-structure source for objects/columns visible to the querying principal. It remains observer-relative and current-state focused.

Delta/Iceberg table history adds version/operation/time/provenance evidence, but its retention is configurable and distinct from retained data files required for time travel. Historical structural claims therefore remain source-window bound.

Structural metadata also does not close consumer compatibility. Group 04 preserves:

**declared/governed schema meaning ≠ realized structure ≠ engine-supported evolution/cast ≠ consumer/interface contract ≠ compatibility Assessment**.

Declared PK/FK relationship constraints are not empirical integrity evidence merely because they exist. Where health requires uniqueness/referential integrity, a measurement/check must observe it or another sufficient source must establish the proposition.

## DQX

DQX is useful as an optional check execution, result and profiling source. It can provide row/dataset rules, detailed issue results, summary metrics, stored history and generated rule candidates.

Group 04 deliberately separates:

**DQX rule definition → governed Expectation adoption → DQX execution Observation → framework Assessment**.

Rule availability, profiler generation, AI assistance, `warn`/`error` criticality and action configuration do not create Assertion Authority, business severity, waiver status or Gate/control truth.

Historical DQX use requires exact release/configuration plus rule-set/run/input/result provenance and retained storage.

## Lakeflow expectations

Lakeflow pipeline expectations can implement exact governed quality criteria when their definition/version/authority/applicability is established. Event logs can provide pass/fail/drop counts for qualifying flows and exact update/flow identity.

The source has important evidence asymmetry: Databricks documents that fail-update expectations do not emit the same tracking metrics after an invalid-record failure. A violation may therefore be known while population counts remain unavailable.

Expectation action also remains separate from normative result: `warn`, `drop` and `fail update` describe processing response, not business severity or framework control policy.

## Metric Views

Unity Catalog Metric Views are strong candidates for reusable governed metric semantics because they encode source, joins, filters, fields/dimensions and measures centrally.

Preserve two version dimensions:

- Databricks YAML specification/runtime feature version;
- organization-governed metric-definition revision.

The YAML `version` field does not supply the second dimension.

A query result becomes a usable Observation only with exact measure-definition, grouping/filter/parameter/window and source-context binding. Optional materialization is an optimization mechanism, not by itself a DMTZ freshness/currentness criterion.

Metric-view join/cardinality declarations likewise cannot substitute for empirical key/reconciliation evidence where an incorrect assumption can alter a measure.

## Data profiling

Databricks data profiling creates queryable profile and drift metric Delta tables across windows/slices and optional baseline-table comparisons.

These are especially valuable for descriptive Observation/Baseline work, but Group 04 retains:

**profile metric ≠ Baseline membership ≠ drift Assessment ≠ normative Expectation ≠ health violation**.

A configured baseline table is a reference source. Framework Baseline membership, regime, comparability and versioning still follow HLTH-019–029.

## Anomaly detection / data-quality monitoring

Databricks anomaly detection currently supplies learned-pattern freshness/completeness Assessments and a source-owned table-level health projection. This can be useful operational evidence, but it is not a universal substitute for explicit SLAs, governed quality criteria or HLTH-055 composite profiles.

The current source also makes a decisive freshness distinction: commit freshness is supported; event freshness based on event time/ingestion latency is not currently supplied by anomaly detection.

Vendor `root_cause_analysis` and downstream-impact fields are retained as source/context assertions only. They cannot bypass the framework's Investigation/Causal Claim/Impact evidence chain.

## Baselines, reconciliation and current-cycle evidence

All source-native historical/reference capabilities remain candidates for framework Baseline construction rather than implicit membership rules.

Reconciliation requires the exact transformation/version, inputs/output, populations, grain, keys/measures, window and current-cycle semantics required by HLTH-041–054. Similar upstream/downstream metrics or Lineage adjacency are insufficient.

Group 03's generic exact multi-input-version gap remains material. Exact multi-input current-cycle alignment is therefore **unsupported out of the box / conditional** for arbitrary workloads unless explicit consumption/version instrumentation exists.

## Result timing and historical replay

Health sources have different clocks and retention surfaces: rule execution, flow/update event, Metric View query/materialization refresh, profiling refresh, anomaly scan, table commit, result availability and retrieval time are not interchangeable.

Historical health replay also requires retained definitions—not just retained values. Old check/metric results without the exact rule/metric/Baseline/profile version may be insufficient for historical Assessment.

## Strong negatives

`No schema change`, `no failed check`, `no anomaly`, `no metric result`, `no quality issue` and similar conclusions require expected opportunity plus adequate population/history/source coverage and source health.

Disabled monitoring, an intelligent-scan skip, a failed DQX job, unsupported expectation metrics, permission filtering or retention expiry remains a limitation rather than a clean pass.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — HME04-01–HME04-56 pass.
- [`../../../decisions/phase_009_group_04_health_measurement_sources.md`](../../../decisions/phase_009_group_04_health_measurement_sources.md) — D-1022–D-1071.

## Architecture boundary

Group 04 does not choose DQX deployment mode, rule-store schema, metric warehouse, monitor scheduling strategy, Metric View authoring workflow, Baseline algorithm, anomaly model, reconciliation engine, data-retention service, alerting architecture or health-serving API. Phase 010 owns technical realization.

## Handoff

**Group 05 — Lineage, Consumer Use, Exposure, Effect & Impact Evidence is next.**

Group 05 may consume exact Group 04 Observations/Assessments only with their subject/version/window/population/provenance/coverage limitations. A failed check, anomaly status, drift, structural incompatibility or composite-health result does not establish publication, consumer encounter, exposure, downstream effect, consequence or causality.
