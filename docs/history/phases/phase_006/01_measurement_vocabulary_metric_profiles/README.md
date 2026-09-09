# Phase 006 Group 01 — Measurement Vocabulary, Metric Families, Profiles & Applicability

**Status:** Accepted — HLTH-001–HLTH-008

## Goal

Establish a precise functional language for measurement before Phase 006 defines structural compatibility, statistical Baselines, threshold evaluation, transformation propagation, or composite health.

The group answers:

- what a metric/check/result means in the accepted concept model;
- how a measurement is bound to subject, grain, window and definition version;
- which broad metric families exist without making every family mandatory for every asset;
- how metric-profile roles relate to semantic applicability;
- how `not applicable`, `not selected`, `unsupported`, `unavailable`, `pending`, and unknown/conflicting applicability differ;
- how anti-bloat and diagnostic-on-demand behavior should work;
- what provenance every material metric/check Observation must retain.

It does not yet decide schema compatibility rules, Baseline math, anomaly algorithms, thresholds/margins, waiver Assessment behavior, metric propagation formulas, composite health, or concrete source/compute architecture.

## Concept-boundary conclusion

**No new concept is required.**

- metric/check definition meaning belongs with Semantic Definition and Entity Identity as applicable;
- measured numeric/categorical/boolean facts are Observation;
- normative or comparative interpretation is Assessment;
- Expectation and Baseline remain the respective normative/descriptive comparison bases;
- metric profile remains the governed selection/applicability structure accepted in AUTH-017, not a new truth owner;
- Lineage, Impact, Causal Claim, Execution Gate, Propagation Safeguard and Capability Authorization keep their existing truth.

A `Metric`, `Metric Profile`, `Check`, `Health Result`, or `DQ Result` concept is therefore not introduced merely because those terms may exist as domain entities or presentation objects.

## Accepted contracts

1. [`001_measurement_target_scope_grain_window_version_binding.md`](001_measurement_target_scope_grain_window_version_binding.md) — **HLTH-001**
2. [`002_metric_check_observation_assessment_result_vocabulary.md`](002_metric_check_observation_assessment_result_vocabulary.md) — **HLTH-002**
3. [`003_canonical_metric_family_taxonomy.md`](003_canonical_metric_family_taxonomy.md) — **HLTH-003**
4. [`004_metric_definition_identity_version_semantic_binding.md`](004_metric_definition_identity_version_semantic_binding.md) — **HLTH-004**
5. [`005_metric_profile_structure_and_roles.md`](005_metric_profile_structure_and_roles.md) — **HLTH-005**
6. [`006_applicability_selection_computability_availability.md`](006_applicability_selection_computability_availability.md) — **HLTH-006**
7. [`007_metric_anti_bloat_routine_diagnostic_lifecycle.md`](007_metric_anti_bloat_routine_diagnostic_lifecycle.md) — **HLTH-007**
8. [`008_metric_check_observation_provenance_evidence_binding.md`](008_metric_check_observation_provenance_evidence_binding.md) — **HLTH-008**

See [`scenario_review.md`](scenario_review.md) for the Group 01 replay.

## Canonical metric families

Group 01 accepts the following functional families as broad classification, not mandatory implementation modules:

1. **Operational / output** — execution occurrence/state, duration/latency, output existence and related operational facts.
2. **Temporal / freshness** — current-cycle state, data age, expected availability timing and related temporal measures.
3. **Structural / schema** — observed structure and later compatibility/conformance evaluation.
4. **Volume / population** — row/object/population counts and related size measures.
5. **Completeness / missingness** — null/missing/empty coverage for semantically meaningful fields/populations.
6. **Uniqueness / key integrity** — duplicate rates, uniqueness and key-integrity measures where key semantics justify them.
7. **Validity / domain conformance** — allowed-domain, format, range or semantic-validity measures.
8. **Distribution / shape** — selected quantiles, proportions, category shares, moments or drift measures where meaningful.
9. **Relational / transformation integrity** — join match/unmatched rate, fan-out, referential relationships and transformation reconciliation.
10. **Business-semantic measurement** — governed totals, rates, balances, populations or other business-defined measures.

Readiness, Impact, causality, authorization, control enforcement and compliance are not metric families. Metrics may provide evidence to those concepts/refinements, but the metric does not inherit their conclusion.

## Profile roles

A governed profile may identify a metric/check as one or more of:

- **core operational/table health** — small broadly useful routine set;
- **critical-field/business health** — selected for explicitly important fields, populations or business semantics;
- **transformation-specific reconciliation** — selected because a transformation has a meaningful invariant or reconciliation relationship;
- **diagnostic/on-demand** — useful for Investigation/deeper analysis but not required routinely.

`Business critical`, `control eligible`, `technical`, `business audience`, or `expensive` are not substitutes for these functional roles. AUTH-023 separately governs high-consequence use and AUTH-044–AUTH-053 separately govern disclosure.

## Core distinctions

Preserve:

**metric definition ≠ metric Observation ≠ Assessment**

**semantic applicability ≠ profile selection ≠ technical computability ≠ evidence availability ≠ Assessment outcome**

**not applicable ≠ not selected ≠ unsupported ≠ unavailable ≠ pending ≠ pass**

**metric available ≠ metric useful**

**metric useful locally ≠ metric should propagate downstream**

**diagnostic metric evaluated once ≠ permanent routine profile membership**

**same display name ≠ same metric definition/version**

## Scenario result

The Group 01 scenario suite passes without a new concept or architecture choice. In particular:

- quantiles for opaque identifiers can be `not applicable` rather than computed because available;
- distinct-count or null-rate metrics can be semantically applicable without being profile-selected;
- profile-selected metrics with missing telemetry become `unavailable`, not pass/zero;
- a metric can be observed descriptively without an Expectation and therefore without normative pass/fail;
- a material calculation/denominator/grain change creates a definition/version boundary and later comparability review;
- diagnostic metrics can be invoked for an Investigation without becoming permanent routine metrics;
- restricted evidence can support an internally authorized Observation while requester disclosure remains separately governed;
- an upstream metric does not become a downstream metric merely because Lineage exists.

## Group exit

Group 01 exits with **HLTH-001–HLTH-008 accepted** and no 25th concept.

**Next:** Group 02 — Structural / Schema / DDL Compatibility.
