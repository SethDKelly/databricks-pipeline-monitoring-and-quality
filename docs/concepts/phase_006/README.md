# Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** ACTIVE — Groups 01–02 accepted; HLTH-001–HLTH-018 accepted; Group 03 next

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
**Status:** **Accepted — HLTH-009–HLTH-018.**

Defines structural observation and contract-surface binding, add/drop/rename/reorder identity, required/optional/additive/removal behavior, type/precision/nested compatibility, nullability/default/generated-value semantics, key/grain transitions, consumer/interface/version-specific compatibility, proposed-versus-realized validation horizons, structural effects on metrics/Baselines, and evidence-backed compatibility outcomes.

See [`02_structural_schema_ddl_compatibility/README.md`](02_structural_schema_ddl_compatibility/README.md).

### Group 03 — Baselines, Comparability, Distribution & Statistical Context
**Status:** **Next — not started.**

Define reference-population/window/cohort semantics, Baseline classes, empirical comparability, seasonality, low-volume/sample-size behavior, approximate/statistical observations, distribution/quantile drift, and how structural/semantic change affects historical comparison.

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
- a metric/check result binds subject, definition/version, grain, evaluation window, relevant output/version/partition/consumer context, and evaluation/knowledge time where material;
- metric values and observed structural facts are not themselves health pass/fail;
- `check passed` is reserved for an Assessment against an applicable Expectation or explicitly defined comparative criterion rather than a generic extraction success message;
- canonical families are operational/output, temporal/freshness, structural/schema, volume/population, completeness, uniqueness/key integrity, validity/domain, distribution/shape, relational/transformation integrity, and business-semantic measurement;
- readiness, Impact, causality, control enforcement, and compliance are not metric families and remain owned by their accepted concepts/refinements;
- metric semantic applicability, governed profile selection, technical computability/support, current evidence availability, and eventual Assessment result are independent dimensions;
- `not applicable`, `not selected`, `unsupported`, `unavailable`, `pending/not yet evaluated`, and `unknown/conflicting applicability` must not collapse into `pass`, `zero`, or `no issue`;
- profile roles include core operational/table, critical-field/business, transformation-specific reconciliation, and diagnostic/on-demand; `control eligible` is not a profile role and remains AUTH-023 governance;
- technical availability never creates automatic profile membership; routine profiles remain purposeful and small while diagnostics can be evaluated on demand;
- material metric-definition changes trigger explicit definition/version handling and later comparability review rather than silent historical continuity;
- Observations retain provenance to definition/version, source/input evidence, scope/window/grain, relevant times, limitations and restricted-evidence state;
- local metric existence never implies downstream propagation; Group 05 owns transformation-aware propagation/reconciliation.

## Accepted Group 02 — HLTH-009–HLTH-018

Group 02 treats structural/schema compatibility as a first-class health dimension while preserving the accepted ownership split:

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

- no new Schema, Schema Contract, Schema Version or Compatibility concept is required;
- compatibility binds the actual consumer-visible interface/contract, not merely the producer physical table;
- add/drop/rename/reorder/type/precision/nullability/default/generated/key/grain/nested changes remain independently representable;
- rename identity requires evidence; drop/add coincidence is not enough and identical names do not guarantee unchanged semantics;
- additive/removal compatibility is consumer-specific; tolerant name-based and strict positional/closed consumers can legitimately reach different conclusions for the same producer change;
- platform cast/parse capability is not proof of type compatibility;
- zero observed nulls do not preserve a non-null structural guarantee after a nullable transition; defaults can preserve physical presence while violating business semantics;
- key/grain changes are structurally material even when columns/types remain unchanged and can invalidate volume, uniqueness, distribution and join assumptions without automatically constituting a defect;
- compatibility is consumer/interface/version scoped and not automatically transitive through Lineage/interfaces;
- prospective/pre-deployment validation is distinct from realized production validation; a successful check of a proposal does not prove deployment or realized state;
- structural changes trigger scoped metric/Profile/Baseline review rather than global reset;
- `compatible` is a positive evidence-backed conclusion requiring sufficient coverage of all applicable required predicates in scope;
- `unknown/unresolved`, `conflicting`, `unavailable`, and `not applicable` remain distinct from compatible/incompatible;
- structural incompatibility does not prove downstream execution failure, exposure, Impact, consequence, or causality;
- clustering/storage-layout/optimization changes are not logical schema incompatibility unless the relevant consumer/interface contract depends on them;
- validation placement remains deferred: GitHub Actions, Databricks/Unity Catalog, DQX, Metric Views and an independent monitoring application remain candidate later realizations.

## Group 03 handoff — Baselines, Comparability, Distribution & Statistical Context

Group 03 must now define **empirical comparison validity** over Group 01 measurement identity and Group 02 structural state.

It should address:

- Baseline classes and reference populations/windows/cohorts;
- exact metric-definition/version continuity requirements;
- same-grain/same-population versus transformed/comparable contexts;
- structural and semantic change as comparability boundaries;
- seasonality and cohort segmentation;
- low-volume/sample-size behavior;
- approximate/sampled metric uncertainty;
- quantile/distribution comparability and drift;
- sparse/new metrics with insufficient history;
- partial continuity after structural change rather than all-or-nothing Baseline reset;
- whether and how known transformations/normalizations can make two observations comparable without rewriting their original meaning.

Preserve:

**governed permission to keep using a Baseline ≠ empirical comparability**.

AUTH-020 can govern review/use decisions, but Group 03 must determine whether the observations actually support a valid comparison.

## Metric-health principles retained for later groups

### Metric profiles and anti-bloat

A metric/check needs identifiable purpose, applicable asset/context, expected consumer/use, cost/latency profile, and governance/retirement path. Availability of a statistic or schema attribute is not enough reason to persist, alert on, display, or propagate it.

### Baseline and threshold separation

Baseline remains descriptive. Group 03 defines reference/comparability semantics without allowing historical regularity to become normative by itself. Group 04 separately defines threshold/margin/waiver Assessment behavior under Phase 005 authority.

### Transformation-aware propagation

For A+B→C, row counts, null rates, quantiles or other metrics do not automatically propagate or combine arithmetically. Join/filter/deduplication/aggregation/grain/key/business semantics determine valid relationships. Group 05 owns those functional relationships.

### Technical versus business health

Technical and business audiences may receive different authorized projections without receiving different health truth. Phase 005 AUTH-044–AUTH-053 continues to govern disclosure; Group 06 will define health-composition/projection requirements, and Phase 008 later defines Explanation/UX.

### Progressive result timing

Phase 006 must eventually distinguish immediate operational facts, fast schema/core health, enriched DQ/distribution results, deeper diagnostic/RCA metrics, and retrospective/post-ops health. Group 06 owns functional timing/maturity semantics. Phase 009 characterizes actual source latency/support; Phase 010 selects architecture/performance budgets.

## Phase boundaries

Phase 006 must not:

- redefine Phase 004 evidence sufficiency;
- override Phase 005 metric/Expectation/schema authority, authorization, control-use eligibility, or disclosure governance;
- create a new Metric, Metric Profile, Check, Schema, Schema Contract, Health Result, or Composite Health concept merely for convenience unless a later scenario proves independently owned behavior;
- turn metric existence or extraction success into health success;
- turn Baseline regularity into normative failure automatically;
- allow authority to manufacture Baseline comparability;
- present waived/suspended violations as fictional clean underlying passes;
- hide conflicting/unknown/unavailable dimensions behind a clean composite state;
- treat every schema change as breaking without semantic/consumer context;
- infer rename identity from drop/add coincidence;
- use engine cast capability as universal type compatibility;
- globally reset metrics/Baselines merely because any DDL changed;
- treat pre-deployment validation success as proof of realized production state;
- propagate every upstream metric blindly through Lineage;
- require production-path computation merely because a metric/schema check is useful for monitoring;
- weaken evidence standards merely to meet a latency objective;
- create separate technical/business health truth models;
- select GitHub Actions, Unity Catalog, the monitoring application, Metric Views/DQX, or another engine as mandatory validation architecture;
- select storage, streaming, caching, graph, orchestration, IAM, redaction, or service architecture.

## Phase direction

**Phase 006 is ACTIVE. Groups 01–02 are accepted with HLTH-001–HLTH-018. Group 03 — Baselines, Comparability, Distribution & Statistical Context is next and has not started.**
