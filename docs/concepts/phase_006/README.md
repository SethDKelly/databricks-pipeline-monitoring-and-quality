# Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** Future phase — not yet started

## Goal

Refine how the framework determines whether a pipeline/table state is operationally and semantically healthy after Phase 005 establishes the relevant normative/governance authority.

Phase 006 should turn the accepted Expectation, Baseline, Observation, Assessment, evidence-sufficiency, temporal, and metric-governance boundaries into a coherent health model without selecting technical architecture.

## Explicit metric-health scope

Phase 006 must address:

- metric-family taxonomy and canonical terminology;
- per-asset/table/pipeline **metric profiles**;
- core versus critical-field versus transformation-specific versus business-critical versus diagnostic/on-demand metrics;
- metric applicability by data type, semantic role, table grain, transformation, business use, and criticality;
- metric-bloat controls and metric lifecycle/retirement principles;
- thresholds, warning/failure margins, tolerance bands, absolute/relative rules, asymmetric bounds, and temporary-exception interaction;
- Baseline-derived ranges versus explicit normative Expectations;
- statistical significance/uncertainty, low-volume/sample-size behavior, seasonality/cohort comparison, and structural-change comparability;
- table/load health composition across execution, output existence, freshness, completeness, uniqueness, validity, distribution, relational integrity, and business-semantic dimensions;
- selective metric propagation/reconciliation across upstream/downstream transformations;
- technical versus business health projections over the same underlying truth;
- whether/how composite or overall health should be represented without hiding dimension-specific disagreement;
- Metric Views/DQX semantic fit;
- functional result-availability expectations for fast operational metrics, enriched health metrics, diagnostic/RCA metrics, and post-ops metrics.

## Candidate metric families for review

Candidate families include:

- execution/load state and output production;
- row count/volume and source-to-target reconciliation;
- freshness/current-cycle state;
- completeness/null/missing rates for meaningful fields;
- uniqueness/key integrity;
- validity/domain/schema conformance;
- numeric/categorical distribution and drift measures such as selected quantiles or category share where semantically useful;
- relational/join/reference integrity such as unmatched rate and fan-out;
- business-semantic totals, rates, balances, populations, and other context-specific measures.

These are candidates, not a requirement to compute every metric for every table.

## Metric-bloat principle

A metric should have an identifiable purpose, applicable asset/context, expected consumer, cost/latency profile, and governance/retirement path. Availability of a statistic is not enough reason to persist or display it.

The model should favor a small purposeful core plus targeted metrics for known failure modes and critical semantics, with deeper diagnostics calculated or exposed when Investigation warrants them.

## Metric propagation principle

Metric propagation is **selective and transformation-aware**.

An upstream metric may be:

- directly relevant downstream;
- transformed into a reconciliation relationship;
- useful only as Investigation context;
- applicable to only one consumer/path;
- semantically invalid downstream and therefore intentionally not propagated.

For example, A + B → C does not imply a generic arithmetic row-count relationship. Join type, filters, deduplication, aggregation, grain, key semantics, and business rules determine which count/null/distribution relationships are meaningful.

Phase 006 defines the health/metric semantics of those relationships. Phase 007 later refines Lineage-aware propagation/operational behavior; Phase 009 evaluates source support; Phase 010 selects realization.

## Technical versus business health

Technical and business audiences may receive different authorized projections without receiving different health truth.

Technical views may require detailed diagnostic metrics, distributions, field-level thresholds, join behavior, and provenance. Business views may emphasize freshness, completeness of critical populations, business metric validity, delivery readiness, and downstream business consequence.

Phase 005 governs who may define/approve/disclose these metric/threshold states. Phase 008 later defines audience-specific Explanation/UX.

## Timing handoff

Phase 006 should define **functional** availability objectives such as:

- immediate operational facts;
- near-real-time core load/table health;
- enriched DQ/distribution health;
- on-demand/deeper diagnostic metrics;
- retrospective/post-ops health.

It must not choose service topology, caching, compute engine, or fixed technical performance implementation. Phase 009 characterizes evidence-source latency/cost; Phase 010 sets architecture/performance budgets; Phase 011 turns them into MVP acceptance criteria.

## Phase boundaries

Phase 006 must not:

- redefine Phase 004 evidence sufficiency;
- override Phase 005 metric/Expectation authority;
- turn Baseline regularity into normative failure automatically;
- introduce a universal health/confidence score without explicit aggregation semantics;
- propagate every upstream metric blindly through Lineage;
- require production-path computation merely because a metric is useful for monitoring;
- select Metric Views/DQX or another metric engine as mandatory architecture;
- select storage, streaming, caching, graph, orchestration, or service architecture.

**Phase 006 has not started.**