# HLTH-004 — Metric Definition Identity, Version & Semantic Binding

**Status:** Accepted — Phase 006 Group 01

## Purpose

Ensure metric values can be interpreted and historically compared only against the calculation semantics that actually produced them.

## Contract

A material metric/check definition should identify, where applicable:

- semantic name and purpose;
- subject/field/relationship semantics;
- measure unit/domain and value type;
- input population and inclusion/exclusion filters;
- aggregation/calculation formula;
- denominator/reference population for rates;
- null/missing-value handling;
- grain and evaluation window semantics;
- grouping/cohort semantics;
- exact/approximate/sampled nature where material;
- precision/rounding behavior where material;
- effective definition version/revision and provenance.

A material change to those semantics is a metric-definition revision/version boundary rather than silent continuity merely because the display name remains the same.

## Examples

`customer_null_rate` defined as null customer IDs divided by **all rows** is not automatically the same metric as null customer IDs divided by **eligible active rows**.

`p95_processing_time` over per-record processing latency is not the same metric as p95 over job duration.

A row-count measure after a table grain changes from `account` to `account-day` remains a row count but no longer carries the same interpretation.

An approximate distinct-count implementation may be a legitimate metric definition when approximation semantics are explicit; it is not silently interchangeable with an exact distinct count for every later comparison.

## Invariants

- Same display name ≠ same metric identity/version.
- Same formula text ≠ same metric semantics if input population, grain, unit, denominator or semantic role changed.
- Metric-definition revision does not erase historical metric Observations.
- Phase 005 Assertion Authority governs authoritative standing for metric meaning; this contract defines the semantic binding required for health reasoning once meaning is established.
- A definition change may trigger comparability review but does not by itself decide that historical values are comparable or non-comparable; Group 03 owns that decision.
- A definition being valid does not imply the metric belongs in a profile; HLTH-005–HLTH-007 govern profile/application behavior.
