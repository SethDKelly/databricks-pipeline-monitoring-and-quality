# HLTH-045 — Aggregation, Conservation & Non-Composable Measure Semantics

## Rule

Aggregation reconciliation is measure- and transformation-specific. Conservation applies only when the measure is semantically additive under the exact grouping/filtering/duplication/unit rules.

Potential relationships include:

- additive total before versus after grouping;
- source subtotal to output total reconciliation;
- record-to-group cardinality relationship;
- explicitly weighted numerator/denominator reconciliation;
- balance equations where business semantics establish conservation.

## Invariants

- Input row count does not generally equal aggregated output row count.
- Sums are not universally conserved when filtering, duplicate amplification, unit conversion, null handling, late-arriving data or other transformations intervene.
- Averages, ratios, percentages and quantiles are not generally composable by averaging upstream summaries.
- Distinct counts are not additive across overlapping partitions unless overlap semantics are explicitly handled.
- Business balance/conservation rules require an explicit semantic basis; arithmetic convenience is insufficient.
- Aggregation grain changes can invalidate historical reconciliation definitions and Baselines.
- A reconciliation difference is descriptive evidence until an Expectation defines acceptable tolerance/relationship.
