# Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** ACTIVE — Groups 01–03 accepted; HLTH-001–HLTH-029 accepted; Group 04 next

## Goal

Refine how the framework determines whether a pipeline/table state is operationally, structurally, statistically, and semantically healthy now that Phase 005 has completed the authority/governance/capability/disclosure model.

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
- Capability Authorization governs which metric/schema/threshold/Baseline/health details a requester may see;
- technical/business/executive/audit views remain projections over one health truth;
- disclosure may reduce detail but cannot strengthen health/causal/control status.

## Delivery-group design

The phase is reviewed in **seven logical groups**. The grouping is a functional-design dependency and review sequence, not an implementation/service decomposition.

### Group 01 — Measurement Vocabulary, Metric Families, Profiles & Applicability
**Status:** **Accepted — HLTH-001–HLTH-008.**

Defines metric/check/result vocabulary, exact measurement target binding, canonical metric families, metric-definition identity/versioning, metric-profile roles, semantic applicability versus selection/availability, anti-bloat behavior, and measurement provenance.

See [`01_measurement_vocabulary_metric_profiles/README.md`](01_measurement_vocabulary_metric_profiles/README.md).

### Group 02 — Structural / Schema / DDL Compatibility
**Status:** **Accepted — HLTH-009–HLTH-018.**

Defines structural observation and contract-surface binding, add/drop/rename/reorder identity, required/optional/additive/removal behavior, type/precision/nested compatibility, nullability/default/generated-value semantics, key/grain transitions, consumer/interface/version-specific compatibility, proposed-versus-realized validation horizons, structural effects on metrics/Baselines, and evidence-backed compatibility outcomes.

See [`02_structural_schema_ddl_compatibility/README.md`](02_structural_schema_ddl_compatibility/README.md).

### Group 03 — Baselines, Comparability, Distribution & Statistical Context
**Status:** **Accepted — HLTH-019–HLTH-029.**

Defines bounded Baseline reference membership, multidimensional comparability, fixed/rolling/seasonal/cohort/post-change references, structural/semantic regime segmentation, reference sufficiency, approximation/sampling uncertainty, distribution/shape comparison, explicit normalization, rolling/adaptive contamination controls, and multi-Baseline ambiguity.

See [`03_baselines_comparability_distribution_statistical_context/README.md`](03_baselines_comparability_distribution_statistical_context/README.md).

### Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics
**Status:** **Next — not started.**

Define functional evaluation against normative Expectations versus descriptive Baselines, absolute/relative/asymmetric tolerance bands, warning/failure semantics, bounded exception/waiver representation, normative conflict, evidence-limited boundary evaluation, and dimension-specific Assessment vocabulary.

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

- no new concept is required; metric definitions/meaning synchronize with Semantic Definition/Entity Identity, measured results are Observation, comparative/normative interpretation is Assessment, and profile selection remains the governed non-concept structure accepted in AUTH-017;
- a measurement binds subject, definition/version, grain/population, evaluation window, relevant output/data/schema/current-cycle context, and material temporal provenance;
- metric values and observed structural facts are not themselves health pass/fail;
- canonical families are operational/output, temporal/freshness, structural/schema, volume/population, completeness, uniqueness/key integrity, validity/domain, distribution/shape, relational/transformation integrity, and business-semantic measurement;
- semantic applicability, governed profile selection, technical support/computability, current evidence availability, and Assessment outcome remain independent;
- profile roles are core operational/table, critical-field/business, transformation-specific reconciliation, and diagnostic/on-demand; control eligibility and audience are not profile roles;
- technical availability never creates automatic profile membership; routine profiles remain purposeful and bounded;
- material metric-definition changes require explicit version/revision handling and later comparability review;
- Observations retain definition/source/scope/time/coverage/approximation/restriction provenance;
- local metric existence never implies downstream propagation.

## Accepted Group 02 — HLTH-009–HLTH-018

Group 02 preserves:

**declared/governed schema meaning ≠ normative structural Expectation/contract ≠ proposed/planned structural state ≠ realized structural Observation/Change ≠ compatibility Assessment**.

Accepted contracts:

- **HLTH-009 — Structural Observation, Schema Snapshot & Contract-Surface Binding**;
- **HLTH-010 — Structural Change Taxonomy, Field Identity, Add/Drop/Rename & Reordering**;
- **HLTH-011 — Required/Optional Fields, Additive/Removal Compatibility & Consumer Sensitivity**;
- **HLTH-012 — Type, Precision, Scale, Casting & Nested-Shape Compatibility**;
- **HLTH-013 — Nullability, Defaults, Generated Values & Population-Presence Compatibility**;
- **HLTH-014 — Key, Identifier, Grain & Cardinality-Shape Compatibility**;
- **HLTH-015 — Consumer-Specific Contract, Interface Version & Compatibility Scope**;
- **HLTH-016 — Planned, Declared, Proposed & Realized Structural State**;
- **HLTH-017 — Structural Change Impact on Metric/Profile/Baseline Applicability**;
- **HLTH-018 — Structural Compatibility Proposition, Evidence & Result Semantics**.

Key results:

- no new Schema/Contract/Version/Compatibility concept is required;
- compatibility binds the consumer-visible interface/contract and can differ by consumer/version;
- add/drop/rename/reorder/type/precision/nullability/default/generated/key/grain/nested changes remain independently representable;
- rename identity requires evidence and same names do not guarantee same meaning;
- engine cast capability is not compatibility;
- key/grain changes can invalidate measurement assumptions even when columns/types remain unchanged;
- prospective validation and realized validation are different truths;
- structural change triggers scoped metric/Baseline review rather than global reset;
- `compatible` is a positive evidence-backed conclusion;
- incompatibility does not prove downstream execution failure, exposure, Impact or causality;
- validation placement remains deferred.

## Accepted Group 03 — HLTH-019–HLTH-029

Group 03 preserves:

**Observation ≠ reference-set membership ≠ Baseline summary/version ≠ comparative Assessment ≠ normative Expectation/health**.

Accepted contracts:

- **HLTH-019 — Baseline Reference Set, Regime, Population & Window Binding**;
- **HLTH-020 — Empirical Comparability Dimensions & Result States**;
- **HLTH-021 — Baseline Classes, Fixed/Rolling Reference & Version Semantics**;
- **HLTH-022 — Seasonality, Cadence, Business Calendar & Cohort Context**;
- **HLTH-023 — Structural/Semantic Breaks, Segmentation & New Reference Regimes**;
- **HLTH-024 — Reference Sufficiency, Coverage, Representativeness & Low-Volume Limits**;
- **HLTH-025 — Approximation, Sampling & Measurement-Uncertainty Comparability**;
- **HLTH-026 — Distribution, Quantile, Category-Share & Shape Reference Semantics**;
- **HLTH-027 — Explicit Normalization & Transformed Comparison Semantics**;
- **HLTH-028 — Baseline Refresh, Adaptation, Exclusion & Contamination Control**;
- **HLTH-029 — Comparable-Baseline Resolution, Ambiguity & Descriptive Assessment**.

Key results:

- no new Reference Set, Statistical Profile, Drift Result or Anomaly concept is required;
- available history is not automatically eligible reference history; membership/window/cohort/regime rules are explicit and provenance-bearing;
- comparability is multidimensional, conclusion-relative and never one universal numeric score;
- bounded states include directly comparable, comparable under explicit normalization, non-comparable, insufficient reference, ambiguous, conflicting, unavailable, unknown/unresolved and not applicable;
- fixed, rolling, seasonal/cadence, cohort and post-change/new-regime references are functional classes, not algorithms;
- recency does not override calendar/cadence/cohort context;
- realized semantic/structural breaks segment affected references only, while unaffected dimensions can retain continuity;
- new post-change Baselines derive from realized evidence rather than planned/target values;
- reference sufficiency considers eligible observation count, temporal/cohort coverage, population/denominator size, operating variability and measurement limitations; no universal minimum count exists;
- approximate/sampled metrics can be valid evidence, but material method uncertainty remains visible and method changes can create comparability breaks;
- distribution references remain purpose-driven; quantiles require semantic ordering and no universal drift/divergence score is introduced;
- explicit normalization can support a derived comparison while raw values remain non-comparable; the normalization itself is versioned/provenance-bearing;
- rolling/adaptive Baselines require explicit membership, lag/holdout, exclusion and version semantics;
- an Observation cannot silently redefine the reference used to assess itself;
- `looks anomalous` alone cannot justify reference exclusion;
- repeated abnormal behavior can become descriptively typical without becoming acceptable;
- multiple Baselines can coexist; newest/largest/narrowest/broadest/closest never silently wins;
- historical Baseline versions and Assessments remain preserved across refresh and regime replacement.

## Group 04 handoff — Expectations, Thresholds, Margins, Waivers & Assessment Semantics

Group 04 now defines normative evaluation over the evidence/reference semantics stabilized by Groups 01–03.

It must address:

- hard criteria versus warning/failure bands;
- absolute, relative and asymmetric thresholds/margins;
- exact boundary semantics and units/denominators;
- normative Expectation versus descriptive Baseline results;
- low-volume/approximate/uncertain evidence near normative boundaries;
- no-Baseline/non-comparable/ambiguous-Baseline cases;
- multiple normative rules versus genuine conflict;
- bounded waiver/exception/suspension without false pass;
- dimension-level normative Assessment vocabulary;
- severity/priority versus health-state separation;
- historical rule/waiver/evidence binding and reassessment.

Preserve:

**authoritative Expectation ≠ sufficient current evidence ≠ descriptive typicality**.

A perfectly authoritative threshold can remain unresolved when current measurement uncertainty/coverage is insufficient. Conversely, a new post-change regime can have no Baseline yet while a current Observation is still sufficient to evaluate an explicit normative requirement.

## Metric-health principles retained for later groups

### Metric profiles and anti-bloat
A metric/check needs an identifiable purpose and governed profile role. Availability is not enough reason to compute/store/display/propagate it.

### Baseline and threshold separation
Baseline remains descriptive. Typicality never creates a normative requirement and adaptive reference behavior never approves repeated defects.

### Transformation-aware propagation
For A+B→C, row counts, null rates, quantiles or other metrics do not automatically propagate or combine. Group 05 owns transformation-aware relationships.

### Technical versus business health
Technical/business/executive/audit views remain authorized projections over one truth. Group 06 defines health-composition requirements; Phase 008 later defines Explanation/UX.

### Progressive result timing
Group 06 will distinguish immediate operational facts, fast schema/core health, enriched DQ/distribution results, deeper diagnostic/RCA metrics and retrospective/post-ops health. Phase 009 characterizes actual source latency/support; Phase 010 selects architecture/performance budgets.

## Phase boundaries

Phase 006 must not:

- redefine Phase 004 evidence sufficiency;
- override Phase 005 authority, authorization, control-use eligibility, or disclosure governance;
- create convenience concepts for Metric, Metric Profile, Check, Schema, Baseline Reference Set, Drift Result, Anomaly Result, Health Result or Composite Health absent a later proven ownership gap;
- turn metric extraction, structural compatibility or Baseline typicality into normative health automatically;
- allow authority to manufacture empirical comparability/evidence sufficiency;
- silently absorb incidents into adaptive Baselines or exclude history merely because it appears anomalous;
- use planned values as empirical post-change Baseline evidence;
- force non-comparable raw observations into one series through ad-hoc normalization;
- hide approximation/sampling/low-volume limitations behind false precision;
- introduce a universal comparability/confidence/drift/anomaly score;
- present waived/suspended violations as fictional clean passes;
- globally reset metrics/Baselines merely because any DDL changed;
- propagate upstream metrics blindly through Lineage;
- require production-path computation merely because a metric is useful for monitoring;
- weaken evidence standards for latency;
- create separate technical/business health truths;
- select GitHub Actions, Unity Catalog, Metric Views/DQX, anomaly/statistical algorithms, storage, streaming, caching, graph, orchestration, IAM, redaction, or service architecture.

## Phase direction

**Phase 006 is ACTIVE. Groups 01–03 are accepted with HLTH-001–HLTH-029. Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics is next and has not started.**