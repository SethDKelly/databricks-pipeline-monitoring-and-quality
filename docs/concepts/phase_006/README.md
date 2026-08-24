# Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** ACTIVE — Group 01 accepted; HLTH-001–HLTH-008 accepted; Group 02 next

## Goal

Refine how the framework determines whether a pipeline/table state is operationally, structurally, and semantically healthy now that Phase 005 has completed the authority/governance/capability/disclosure model.

Phase 006 uses `HLTH-###` refinement contracts. These contracts define health/metric/schema/statistical semantics over the accepted concepts; they are not new truth-owning concepts, do not extend the Phase 003 SYN range, and do not reopen Phase 004 evidence standards or Phase 005 authority decisions.

## Accepted handoff from Phase 005

Phase 005 is complete with AUTH-001–AUTH-053. Phase 006 consumes rather than redefines these boundaries:

- Assertion Authority determines standing for exact governance assertions but does not make operational evidence true;
- semantic/schema meaning, normative schema compatibility, and realized schema Observation/Change are separate;
- metric meaning, metric-profile selection, threshold/margin, severity, waiver, and high-consequence-use eligibility may have different authoritative holders;
- metric-profile inclusion must be purposeful and lifecycle-governed rather than driven by technical availability;
- Baseline remains descriptive until an authoritative Expectation adopts a criterion;
- authority may require review/suspension after structural Change but cannot manufacture statistical comparability;
- waivers/exceptions do not rewrite Observations or create false clean passes;
- normative conflict remains explicit when no accepted resolver applies;
- high-consequence-use eligibility does not grant gate/safeguard/job capability and does not make stale/unavailable evidence usable;
- Capability Authorization governs which metric/schema/threshold/health details a requester may see;
- technical/business/executive/audit views remain projections over one health truth;
- disclosure may reduce detail but cannot strengthen health/causal/control status.

## Delivery-group design

The phase is reviewed in **seven logical groups**. The grouping is a functional-design dependency and review sequence, not an implementation/service decomposition.

### Group 01 — Measurement Vocabulary, Metric Families, Profiles & Applicability
**Status:** **Accepted — HLTH-001–HLTH-008.**

Defines metric/check/result vocabulary, exact measurement target binding, canonical metric families, metric-definition identity/versioning, metric-profile roles, semantic applicability versus selection/availability, anti-bloat behavior, and measurement provenance.

See [`01_measurement_vocabulary_metric_profiles/README.md`](01_measurement_vocabulary_metric_profiles/README.md).

### Group 02 — Structural / Schema / DDL Compatibility
**Status:** **Next — not started.**

Define structural-change and compatibility semantics for required/optional fields, add/drop/rename, types/precision/scale, nullability/default/generated fields, nested schemas, key/grain changes, contract versions, consumer-specific compatibility, and the structural triggers that affect metric/Baseline applicability.

### Group 03 — Baselines, Comparability, Distribution & Statistical Context
**Status:** Planned — not started.

Define reference-population/window/cohort semantics, Baseline classes, comparability, seasonality, low-volume/sample-size behavior, approximate/statistical observations, distribution/quantile drift, and how structural/semantic change affects historical comparison.

### Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics
**Status:** Planned — not started.

Define functional evaluation against normative Expectations versus descriptive Baselines, absolute/relative/asymmetric tolerance bands, warning/failure semantics, bounded exception/waiver representation, normative conflict, and dimension-specific Assessment vocabulary.

### Group 05 — Transformation Reconciliation & Metric Propagation
**Status:** Planned — not started.

Define transformation-aware metric relationships for joins, filters, aggregations, deduplication, unions and other patterns; distinguish local upstream evidence, propagated/relevant context, and derived reconciliation expectations; prohibit recursive metric copying merely because Lineage exists.

### Group 06 — Composite Health, Readiness Suitability & Progressive Result Timing
**Status:** Planned — not started.

Define whether/how dimension-level Assessments compose into overall health without hiding conflict/unknown state; define technical/business health projection requirements, evidence maturity and freshness for AUTH-023 control-eligible conditions, and progressive result availability from operational facts through enriched/diagnostic/post-ops health.

### Group 07 — Consolidation / Exit Review
**Status:** Planned — not started.

Replay Groups 01–06 across representative ecosystem scenarios and verify that the health model composes without a universal score, hidden authority, false passes, blind propagation, or selected architecture.

## Accepted Group 01 — HLTH-001–HLTH-008

Group 01 establishes the common measurement language before schema, Baseline, threshold, propagation, or composite-health behavior is designed.

Accepted contracts:

- **HLTH-001 — Measurement Target, Scope, Grain, Window & Version Binding**;
- **HLTH-002 — Metric, Check, Observation, Assessment & Result Vocabulary**;
- **HLTH-003 — Canonical Metric-Family Taxonomy**;
- **HLTH-004 — Metric Definition Identity, Version & Semantic Binding**;
- **HLTH-005 — Metric Profile Structure & Profile Roles**;
- **HLTH-006 — Applicability, Selection, Computability & Availability Separation**;
- **HLTH-007 — Metric Anti-Bloat, Routine/Diagnostic Use & Lifecycle Principle**;
- **HLTH-008 — Metric/Check Observation Provenance & Evidence Binding**.

Key results:

- no new concept is required; metric definitions/meaning synchronize with Semantic Definition and Entity Identity, measured results are Observation, normative/comparative interpretation is Assessment, and governed profile selection remains the non-concept structure accepted in AUTH-017;
- a metric/check result must bind subject, definition/version, grain, evaluation window, relevant output/version/partition/consumer context, and evaluation/knowledge time where material;
- a metric value or observed structural fact is not itself a health pass/fail;
- `check passed` is reserved for an Assessment against an applicable Expectation or explicitly defined comparative criterion rather than a generic data-extraction success message;
- canonical families are operational/output, temporal/freshness, structural/schema, volume/population, completeness, uniqueness/key integrity, validity/domain, distribution/shape, relational/transformation integrity, and business-semantic measurement;
- readiness, Impact, causality, control enforcement, and compliance are not metric families and remain owned by their accepted concepts/refinements;
- metric semantic applicability, governed profile selection, technical computability/support, current evidence availability, and eventual Assessment result are independent dimensions;
- `not applicable`, `not selected`, `unsupported`, `unavailable`, `pending/not yet evaluated`, and `unknown/conflicting applicability` must not collapse into `pass`, `zero`, or `no issue`;
- profile roles include core operational/table, critical-field/business, transformation-specific reconciliation, and diagnostic/on-demand; `control eligible` is not a profile role and remains AUTH-023 governance;
- technical availability never creates automatic profile membership; routine profiles should remain purposeful and small while diagnostics can be evaluated on demand;
- metric-definition changes in formula, denominator, filters, unit, grain, window, missing-value handling, approximation, or other material semantics create a new definition/version or explicit revision and trigger later comparability review rather than silent historical continuity;
- Observations retain provenance to the metric/check definition, source/input evidence, scope/window/grain, event/effective time where relevant, framework knowledge/evaluation time, coverage/sampling/approximation limitations where material, and restricted-evidence status;
- local metric existence never implies downstream propagation; Group 05 owns transformation-aware propagation/reconciliation.

## Structural / schema / DDL health scope — Group 02 handoff

Phase 006 treats schema compatibility as a first-class health dimension rather than assuming that successful execution proves a usable table.

Group 02 will evaluate, where semantically applicable:

- required/optional column existence;
- unexpected column removal/addition;
- declared rename versus uncorrelated drop/add;
- accepted data-type compatibility including precision/scale and nested types;
- nullability/default/generated-value requirements;
- grain changes;
- declared primary/business-key or identifier-role requirements;
- uniqueness/key integrity as observed health distinct from declared key meaning;
- nested-field evolution;
- schema-contract version compatibility;
- consumer-specific compatibility for transformations, exports, reports, Metric Views, applications, or downstream pipelines.

Preserve:

**declared/governed schema meaning ≠ normative schema contract/Expectation ≠ realized schema Observation/Change ≠ Assessment of compatibility**.

A change can be additive and safe for one consumer but breaking for another.

## Metric-health principles retained for later groups

### Metric profiles and anti-bloat

A metric/check should have an identifiable purpose, applicable asset/context, expected consumer/use, cost/latency profile, and governance/retirement path. Availability of a statistic or schema attribute is not enough reason to persist, alert on, display, or propagate it.

### Baseline and threshold separation

Baseline remains descriptive. Phase 006 must later define reference/comparability semantics without allowing historical regularity to become normative by itself. Group 04 will separately define threshold/margin/waiver Assessment behavior under Phase 005 authority.

### Transformation-aware propagation

For A+B→C, row counts, null rates, quantiles or other metrics do not automatically propagate or combine arithmetically. Join/filter/deduplication/aggregation/grain/key/business semantics determine valid relationships. Group 05 owns those functional relationships.

### Technical versus business health

Technical and business audiences may receive different authorized projections without receiving different health truth. Phase 005 AUTH-044–AUTH-053 continues to govern disclosure; Group 06 will define health-composition/projection requirements, and Phase 008 later defines Explanation/UX.

### Progressive result timing

Phase 006 must eventually distinguish immediate operational facts, fast schema/core health, enriched DQ/distribution results, deeper diagnostic/RCA metrics, and retrospective/post-ops health. Group 06 owns the functional timing/maturity semantics. Phase 009 characterizes actual source latency/support; Phase 010 selects architecture/performance budgets.

## Phase boundaries

Phase 006 must not:

- redefine Phase 004 evidence sufficiency;
- override Phase 005 metric/Expectation/schema authority, authorization, control-use eligibility, or disclosure governance;
- create a new Metric, Metric Profile, Check, Health Result, or Composite Health concept merely for convenience unless a later scenario proves independently owned behavior;
- turn metric existence or extraction success into health success;
- turn Baseline regularity into normative failure automatically;
- allow authority to manufacture Baseline comparability;
- present waived/suspended violations as fictional clean underlying passes;
- hide conflicting/unknown/unavailable dimensions behind a clean composite state;
- treat every schema change as breaking without semantic/consumer context;
- globally reset metrics/Baselines merely because any DDL changed;
- propagate every upstream metric blindly through Lineage;
- require production-path computation merely because a metric/schema check is useful for monitoring;
- weaken evidence standards merely to meet a latency objective;
- create separate technical/business health truth models;
- select GitHub Actions, Unity Catalog, the monitoring application, Metric Views/DQX, or another engine as mandatory validation architecture;
- select storage, streaming, caching, graph, orchestration, IAM, redaction, or service architecture.

## Phase direction

**Phase 006 is ACTIVE. Group 01 is accepted with HLTH-001–HLTH-008. Group 02 — Structural / Schema / DDL Compatibility is next and has not started.**
