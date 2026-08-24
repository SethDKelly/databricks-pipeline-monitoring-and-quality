# Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** Future phase — not yet started

## Goal

Refine how the framework determines whether a pipeline/table state is operationally, structurally, and semantically healthy after Phase 005 establishes the relevant normative/governance authority.

Phase 006 should turn the accepted Expectation, Baseline, Observation, Assessment, evidence-sufficiency, temporal, schema-governance, **AUTH-016–AUTH-023 normative metric/profile/threshold/waiver governance**, and metric-health handoff boundaries into a coherent health model without selecting technical architecture.

## Explicit metric-health scope

Phase 006 must address:

- metric-family taxonomy and canonical terminology;
- per-asset/table/pipeline **metric profiles**, consistent with the purpose/applicability/lifecycle governance accepted in AUTH-017;
- core versus critical-field versus transformation-specific versus business-critical versus diagnostic/on-demand metrics;
- metric applicability by data type, semantic role, table grain, transformation, business use, and criticality;
- metric-bloat controls and metric lifecycle/retirement principles;
- thresholds, warning/failure margins, tolerance bands, absolute/relative rules, asymmetric bounds, and temporary-exception interaction without redefining Phase 005 authority;
- Baseline-derived ranges versus explicit normative Expectations;
- statistical significance/uncertainty, low-volume/sample-size behavior, seasonality/cohort comparison, and structural-change comparability;
- table/load health composition across execution, output existence, freshness, **schema/structural compatibility**, completeness, uniqueness, validity, distribution, relational integrity, and business-semantic dimensions;
- selective metric propagation/reconciliation across upstream/downstream transformations;
- technical versus business health projections over the same underlying truth;
- whether/how composite or overall health should be represented without hiding dimension-specific disagreement;
- Metric Views/DQX semantic fit;
- functional result-availability expectations for fast operational metrics, schema checks, enriched health metrics, diagnostic/RCA metrics, and post-ops metrics;
- evidence/result freshness and availability semantics for any condition explicitly approved for high-consequence use under AUTH-023.

## Structural / schema / DDL health scope

Phase 006 must treat schema compatibility as a first-class health dimension rather than assuming that a successful run/load proves a usable table.

Candidate structural checks include, where semantically applicable:

- required/optional column existence;
- unexpected column removal/addition;
- declared rename versus uncorrelated drop/add;
- accepted data-type compatibility, including precision/scale and nested types;
- nullability/default/generated-value requirements;
- grain changes;
- declared primary/business-key or identifier-role requirements;
- uniqueness/key integrity as observed health distinct from declared key meaning;
- nested-field evolution;
- schema-contract version compatibility;
- consumer-specific compatibility for transformations, exports, reports, or downstream pipelines.

Phase 006 must preserve:

**declared/governed schema meaning ≠ normative schema contract/Expectation ≠ realized schema Observation/Change ≠ Assessment of compatibility**.

A change can be additive and safe for one consumer but breaking for another. Compatibility must therefore be semantic/consumer-aware rather than a single universal `schema changed = failed` rule.

## Schema interaction with metrics and Baselines

Structural Change can affect health evidence beyond schema itself. Phase 006 must define how schema/grain/key/type changes trigger scoped review of:

- metric definition applicability;
- null/completeness/uniqueness metrics;
- quantile/distribution comparability;
- source-to-target and join/reconciliation relationships;
- Baseline comparability by affected dimension;
- downstream readiness criteria where structural compatibility is required.

Do not globally reset every metric/Baseline after any schema change, and do not blindly preserve comparisons whose meaning changed. AUTH-020 can govern whether a metric/Baseline is intended to remain in use, but Phase 006 evidence/comparability semantics decide whether the comparison is actually valid.

## Candidate metric families for review

Candidate families include:

- execution/load state and output production;
- row count/volume and source-to-target reconciliation;
- freshness/current-cycle state;
- schema/structural conformance and compatibility;
- completeness/null/missing rates for meaningful fields;
- uniqueness/key integrity;
- validity/domain conformance;
- numeric/categorical distribution and drift measures such as selected quantiles or category share where semantically useful;
- relational/join/reference integrity such as unmatched rate and fan-out;
- business-semantic totals, rates, balances, populations, and other context-specific measures.

These are candidates, not a requirement to compute every metric/check for every table.

## Metric-bloat principle

A metric/check should have an identifiable purpose, applicable asset/context, expected consumer, cost/latency profile, and governance/retirement path. Availability of a statistic or schema attribute is not enough reason to persist, alert on, or display it.

The model should favor a small purposeful core plus targeted metrics/checks for known failure modes and critical semantics, with deeper diagnostics calculated or exposed when Investigation warrants them.

## Threshold, Baseline, and waiver semantics

Phase 006 must define the functional meaning of:

- hard normative criteria versus warning/failure bands;
- Baseline-derived expected ranges versus explicit Expectations;
- absolute/relative/asymmetric tolerances;
- low-volume/sample-size/seasonality behavior;
- normative conflict versus simultaneously valid rules in different contexts;
- bounded exception/waiver/suspension state in Assessment and composite-health output.

A waiver must not become a false data-quality `pass`. The product should be able to represent both the underlying observed/Assessment condition and the bounded normative exception/response state.

## Metric propagation principle

Metric propagation is **selective and transformation-aware**.

An upstream metric may be:

- directly relevant downstream;
- transformed into a reconciliation relationship;
- useful only as Investigation context;
- applicable to only one consumer/path;
- semantically invalid downstream and therefore intentionally not propagated.

For example, A + B → C does not imply a generic arithmetic row-count relationship. Join type, filters, deduplication, aggregation, grain, key semantics, schema compatibility, and business rules determine which count/null/distribution relationships are meaningful.

Phase 006 defines the health/metric/schema semantics of those relationships. Phase 007 later refines Lineage-aware propagation/change behavior; Phase 009 evaluates source support; Phase 010 selects realization.

## Technical versus business health

Technical and business audiences may receive different authorized projections without receiving different health truth.

Technical views may require schema diffs, field-level diagnostics, distributions, thresholds, join behavior, waiver state, and provenance. Business views may emphasize freshness, completeness of critical populations, business metric validity, delivery readiness, approved exceptions, and downstream business consequence.

Phase 005 governs who may define/approve/disclose these metric/schema/threshold states. Phase 008 later defines audience-specific Explanation/UX.

## Timing and control-eligible-condition handoff

Phase 006 should define **functional** availability objectives such as:

- immediate operational facts;
- fast/proactive schema-contract validation where evidence is available;
- near-real-time core load/table/schema health;
- enriched DQ/distribution health;
- on-demand/deeper diagnostic metrics;
- retrospective/post-ops health.

For AUTH-023 high-consequence-use eligible conditions, Phase 006 must define the functional evidence/result freshness and maturity required before the condition can safely participate in readiness/control evaluation. Eligibility alone never makes unavailable or stale evidence usable.

Phase 006 must not choose service topology, validation location, caching, compute engine, or fixed technical performance implementation. Phase 009 characterizes GitHub/GitHub Actions, Databricks/Unity Catalog, Metric Views/DQX, and other evidence-source latency/cost/support; Phase 010 sets architecture/performance budgets and decides where checks run; Phase 011 turns them into MVP acceptance criteria.

## Phase boundaries

Phase 006 must not:

- redefine Phase 004 evidence sufficiency;
- override Phase 005 metric/Expectation/schema authority or high-consequence-use eligibility;
- turn Baseline regularity into normative failure automatically;
- allow authority to manufacture Baseline comparability;
- present a waived/suspended violation as a fictional clean underlying measurement/pass;
- introduce a universal health/confidence score without explicit aggregation semantics;
- treat every schema change as breaking without semantic/consumer context;
- globally reset metrics/Baselines merely because any DDL changed;
- propagate every upstream metric blindly through Lineage;
- require production-path computation merely because a metric/schema check is useful for monitoring;
- select GitHub Actions, Unity Catalog, the monitoring application, Metric Views/DQX, or another engine as the mandatory validation architecture;
- select storage, streaming, caching, graph, orchestration, or service architecture.

**Phase 006 has not started.**