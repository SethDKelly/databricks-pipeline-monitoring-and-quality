# Pre-Phase 005 Consideration — Metric Health, Propagation, and Audience Use

**Status:** Accepted handoff consideration — does not start Phase 005 or Phase 006

## Why this matters

A production load is not healthy merely because a Databricks job completed. Table and pipeline health must also consider whether the produced state is plausible, complete, timely, semantically usable, and consistent with the transformation and downstream business expectations.

The project therefore needs an explicit metric model, but the work belongs across several later phases rather than inside Phase 005 alone.

## Phase ownership

### Phase 005 — governance/authority around metrics

Phase 005 should refine **who may define, approve, revise, waive, retire, disclose, or override** metric-related normative state, including:

- which metrics are considered important for an asset or business process;
- who may establish/revise thresholds, margins/tolerance bands, severity, exceptions, and waivers;
- who is authoritative for the business meaning of a metric;
- which technical/business audiences may view metric details or only safe abstractions;
- how conflicting threshold/metric definitions are resolved without changing observed values;
- who may approve a metric profile used by an Execution Gate or other high-consequence control.

Phase 005 should **not** decide the actual metric taxonomy, statistical methods, Metric View/DQX implementation, or propagation algorithm.

### Phase 006 — health metric semantics and metric-profile design

Phase 006 should explicitly own:

- metric families and vocabulary;
- table/pipeline **metric profiles** describing which metrics are useful for each asset/context;
- mandatory core metrics versus targeted critical-column/business metrics versus diagnostic/on-demand metrics;
- threshold, warning/failure margin, tolerance-band, Baseline-deviation, and statistical semantics;
- metric comparability after structural Change;
- metric-to-Assessment composition and whether/how overall health is summarized;
- technical versus business health views without creating separate truth;
- selective metric propagation/reconciliation across transformations;
- metric-bloat controls;
- metric/result freshness and analytical availability expectations;
- Databricks Metric Views and DQX fit at the semantic level.

### Phase 007 — lineage-aware propagation and operational policy

Phase 007 should refine how health evidence is related through Lineage and transformations, including when an upstream metric is:

- merely context for investigation;
- directly comparable downstream;
- transformed into a downstream reconciliation expectation;
- relevant only to a particular path/consumer;
- irrelevant and therefore intentionally not propagated.

Propagation must be **transformation- and semantics-aware**, not a recursive copy of every upstream statistic to every descendant.

### Phase 008 — audience communication

Phase 008 should define how technical and business audiences consume the same underlying metric/Assessment truth at different levels of detail.

### Phase 009/010 — evidence support and technical realization

Phase 009 should determine which metrics can be obtained from Databricks, Metric Views, DQX, table metadata, or other sources; their cost, retention, and latency. Phase 010 should decide collection/precomputation/on-demand architecture and performance budgets.

## Candidate metric families for Phase 006 review

The following are candidate families, not mandatory metrics for every table:

1. **Load/operational state** — execution outcome, output produced, row count, bytes/partitions where useful, load duration, completion time.
2. **Freshness/currency** — max relevant event/business timestamp, ingestion delay, current-cycle state.
3. **Completeness** — null/missing/blank rates for semantically important fields.
4. **Uniqueness/key integrity** — duplicate rate, key uniqueness, unexpected cardinality.
5. **Validity/conformance** — domain/range/type/format/schema checks.
6. **Distribution/shape** — quantiles, min/max, mean/variance where useful, categorical share/top-k, distinct-count/cardinality, distribution drift.
7. **Relational/transformation integrity** — unmatched join rate, referential coverage, join fan-out, source-to-target reconciliation, filtered/dropped-row proportions.
8. **Business-semantic metrics** — totals, rates, cohorts, balances, counts, or other measures whose meaning matters directly to business use.

A table should not automatically receive every metric in every family.

## Metric-profile principle — avoid metric bloat

Metric selection should be purposeful and explainable. A useful future metric profile should distinguish:

- **core metrics** useful for nearly every relevant asset, such as output existence, row count, and freshness where meaningful;
- **critical-field metrics** for columns/keys whose failure would materially affect downstream use;
- **transformation-specific metrics** that validate joins, filters, aggregations, deduplication, or other known failure modes;
- **business-critical metrics** tied to semantic outcomes or client/report use;
- **diagnostic/on-demand metrics** calculated only when an anomaly or Investigation warrants them.

Metric bloat controls should eventually include a reason/purpose for each retained metric, asset applicability, audience/use, cost/latency, owner/authority, and retirement/review behavior. Computing quantiles for identifiers, null rates for meaningless fields, or every possible distribution statistic merely because they are available should be discouraged.

## Technical versus business views

Technical users may need detailed evidence such as:

- exact row-count deltas;
- null/duplicate rates by critical field;
- quantile/distribution changes;
- join match/fan-out rates;
- freshness timestamps;
- threshold/Baseline details;
- upstream/downstream comparison and evidence provenance.

Business users generally need a smaller semantic projection such as:

- whether a critical business population is complete/current;
- whether a business metric is inside its accepted range;
- whether delivery/readiness expectations are satisfied;
- which downstream reports/processes may be affected;
- whether a problem is technical-only or materially affects business use.

These are audience projections over the same underlying evidence/Assessment model, not two different health truths.

## Threshold and margin considerations

Phase 006 should distinguish at least:

- hard normative thresholds;
- warning versus failure boundaries where justified;
- absolute versus relative margins;
- asymmetric tolerance bands;
- Baseline-derived expected ranges versus explicit Expectations;
- seasonal/cohort-aware comparison;
- minimum sample/population conditions;
- temporary exceptions/waivers governed through Phase 005 authority.

A threshold crossing is an Assessment against an accepted criterion. A Baseline anomaly remains comparative evidence and must not silently become a normative failure.

## Metric propagation principle

Metrics should not simply cascade through Lineage.

For A + B → C, useful relationships might include:

- whether A/B were current before C ran;
- A/B/C row-count or key-population reconciliation appropriate to the join/filter semantics;
- join match/unmatched rates;
- null introduction on joined fields;
- preservation or expected transformation of selected business distributions;
- propagation of known upstream quality limitations as Investigation/Impact context.

But `C row count = A row count + B row count` would usually be semantically invalid for a join. Propagation therefore requires knowledge of transformation meaning and should distinguish **local metric**, **related upstream/downstream metric**, and **derived reconciliation expectation**.

## Timing consideration

Metric availability should follow the accepted progressive analytical model:

- fast operational facts as soon as directly available;
- inexpensive/core table metrics soon after output when practical;
- richer Metric View/DQ/distribution metrics when their evidence becomes available;
- expensive diagnostics/RCA metrics on demand or after a trigger;
- retrospective/post-ops metrics when they require late evidence.

No metric should be forced onto the synchronous production path merely for monitoring convenience. A metric used by an explicit Execution Gate is a different high-consequence case and must have an accepted readiness criterion, authority, evidence burden, and later availability architecture.

## Handoff conclusion

The metric concern is **not missing from the roadmap**, but Phase 006 needs an explicit metric-health/propagation scope. Phase 005 should first settle metric/threshold governance and disclosure authority. Phase 007 should later refine lineage-aware propagation mechanics. This preserves the accepted separation between evidence truth, normative health, authority, and architecture.