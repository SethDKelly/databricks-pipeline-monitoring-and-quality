# Phase 006 Group 05 — Transformation Reconciliation & Metric Propagation

**Status:** Accepted — HLTH-041–HLTH-054; H05-01–H05-44 pass

## Goal

Define when upstream/downstream evidence has a valid transformation-aware measurement relationship, while prohibiting recursive copying of statistics or local health statuses through Lineage.

## Accepted contracts

- **HLTH-041 — Reconciliation Vocabulary, Transformation Binding & Derived Measurement Identity**;
- **HLTH-042 — Join Eligibility, Match/Unmatched Population & Directionality**;
- **HLTH-043 — Join Cardinality, Fan-Out, Key Integrity & Duplicate Effects**;
- **HLTH-044 — Filter Selection, Inclusion/Exclusion & Population Reconciliation**;
- **HLTH-045 — Aggregation, Conservation & Non-Composable Measure Semantics**;
- **HLTH-046 — Deduplication, Survivor Selection & Uniqueness Reconciliation**;
- **HLTH-047 — Union, Merge/Upsert, Source Contribution & Overlap Semantics**;
- **HLTH-048 — Null, Default, Cast & Derived-Value Transformation Semantics**;
- **HLTH-049 — Freshness, Current-Cycle & Multi-Input Version Alignment**;
- **HLTH-050 — Distribution, Quantile, Unit & Normalization Preservation Boundaries**;
- **HLTH-051 — Reconciliation Evidence, Provenance, Uncertainty & Restriction Propagation**;
- **HLTH-052 — Multi-Hop Composition, Path-Specific Relevance & No Blind Status Propagation**;
- **HLTH-053 — Historical Transformation Version, Rule Binding & Reassessment**;
- **HLTH-054 — Reconciliation Relevance, Localization, Downstream Assessment & Causal Separation**.

## Core reconciliation model

Preserve:

**local Observation ≠ downstream-relevant upstream context ≠ reconciliation definition/check ≠ derived reconciliation Observation ≠ reconciliation Assessment ≠ Causal Claim**.

No new Reconciliation or Metric Propagation concept is required. Lineage owns typed time-valid relationships; Semantic Definition/check definitions own transformation/reconciliation meaning; Observation owns local and derived evidence; Expectation owns normative reconciliation criteria; Assessment owns evaluation.

## Transformation binding

Every reconciliation binds the exact transformation/version, material inputs and roles, output, fields/keys/measures, grain/population/window/current-cycle context and derivation rule. Asset-level Lineage alone never creates equality, conservation or status inheritance.

A material change to join keys, filter predicate, aggregation grain, dedupe survivor rule, merge behavior, null/default handling or equivalent transformation semantics creates a reconciliation-definition/version boundary where applicable.

## Joins

Join health is described through eligible populations and exact join semantics, not generic input/output row arithmetic. Useful measures can include directional match rates, unmatched populations, matched-pair counts, zero/one/many-match populations and fan-out/cardinality shape.

`left matched %` and `right matched %` are different. Many-to-many joins can legitimately amplify output. Duplicate keys can create fan-out without missing input records. A declared key role does not prove observed uniqueness.

## Filters

For a pure row filter with stable grain, a bounded reconciliation can use eligible input, included/output and excluded populations. `input = output + excluded` is valid only when the exact transformation semantics justify it.

Filtering can intentionally reduce row count while also changing completeness, distribution and category-share metrics through selection. Those downstream metrics are newly observed; they are not inherited from the input.

## Aggregation

Conservation is measure-specific. Additive totals can reconcile when semantic additivity, filtering, duplication, unit and grouping conditions support it. Row counts, averages, ratios, percentages, distinct counts and quantiles are not generically composable.

A business balance equation requires explicit semantic meaning; arithmetic convenience is not enough to create a health rule.

## Deduplication

Dedup reconciliation binds duplicate equivalence and survivor-selection semantics. Input/output population, duplicate-group counts, records removed and post-dedup uniqueness can be related when the rule is evidenced.

Successful dedupe can produce a unique output while the upstream source remains non-unique. Survivor selection can materially change completeness/distributions even when removed-record count is expected.

## Union / merge / upsert

Bag/append union can support additive contribution reconciliation only when no hidden filtering/dedupe/overlap behavior intervenes. Distinct union is not additive when sources overlap.

Merge/upsert reconciliation uses action semantics such as inserts, updates, unchanged matches and deletes/tombstones where applicable. Input row count alone does not determine resulting target population.

## Nulls, defaults and derived values

A transformation can preserve, introduce, remove, replace or reinterpret null/value state. Outer joins, filters, coalesce/defaulting, casts/parses, conditional derivation and source fallbacks all have distinct consequences.

Lower downstream null rate does not prove upstream completeness improved. Sentinel/default replacement can produce physical non-nullness while violating validity or business semantics.

## Freshness and current-cycle alignment

Multi-input health binds the exact input versions/windows actually consumed. C completing now does not prove that A and B were both current. Different inputs can have intentionally different allowed cadences, so alignment is criterion-relative rather than universal timestamp equality.

Missing version/consumption evidence remains unresolved. Current-cycle reconciliation can support later readiness semantics but is not a gate decision or enforcement state.

## Distribution and normalization

Quantiles/distributions are not generically propagated through joins, filters, unions or aggregations. A known deterministic unit/value transform or an explicitly defined normalization can support a derived comparison when the relevant population/grain semantics remain valid.

Selection effects, overlap, aggregation and approximation limitations remain visible; generic `drift` status is never copied downstream.

## Evidence and restrictions

Derived reconciliation evidence retains every material source Observation, transformation/reconciliation version, input/output versions, coverage, uncertainty, sampling/approximation, non-comparability, restriction state and temporal provenance.

Derivation cannot upgrade evidence quality. Required unavailable inputs do not become zero. Restricted source evidence can support an authorized derived projection, but aggregation/derivation is not declassification.

## Multi-hop behavior

Reconciliation relationships are transformation-local. A valid A↔B rule plus B↔C rule does not automatically create a direct A↔C equality or conservation rule. Multi-hop reasoning requires a valid explicit composition.

Likewise, Lineage never recursively propagates local metric values, Baseline status, warning, violation, severity or waiver. An upstream condition is downstream-relevant only where the material path consumes the corresponding field/population/version under semantics that make it relevant.

## Relevance versus causality

Reconciliation can establish a mismatch, identify a material upstream condition, and localize a discrepancy to a transformation boundary. It does not establish root cause by itself.

Upstream violations can coexist with healthy downstream criteria when the transformation isolates/repairs them; upstream success can coexist with downstream failure when transformation logic introduces a problem. Multiple upstream conditions can remain relevant simultaneously.

Any proposition that A/B caused or contributed to C belongs in Causal Claim and uses REF-013–REF-020. Downstream exposure/Impact remains separately evidenced.

## Historical behavior

Historical reconciliation binds the time-valid Lineage, transformation/version, input/output versions, reconciliation definition, current-cycle context, Expectations/Baselines and knowledge cutoff. Current code/rules are never projected backward.

Later-discovered Lineage or corrected metrics can justify retrospective reassessment without rewriting the earlier historical Assessment.

## Scenario review

See [`scenario_review.md`](scenario_review.md). H05-01–H05-44 pass.

## Exit result

- no new concept;
- HLTH-041–HLTH-054 accepted;
- HLTH-001–HLTH-040 remain accepted;
- concept count remains 24;
- SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged;
- no Spark/SQL/DQX/Metric View/graph/storage/compute architecture selected;
- **Group 06 — Composite Health, Readiness Suitability & Progressive Result Timing is next and has not started.**
