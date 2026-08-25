# HLTH-024 — Reference Sufficiency, Coverage, Representativeness & Low-Volume Limits

**Status:** Accepted — Phase 006 Group 03

## Purpose

Prevent sparse, incomplete, or unrepresentative history from producing false precision in Baseline-based comparisons.

## Contract

Reference sufficiency considers, as applicable:

- number of eligible observations;
- temporal coverage and missing periods;
- coverage across required calendar/cadence/cohort states;
- population/sample size represented by each Observation;
- whether evidence spans the operating variability the Baseline claims to describe;
- source availability/collection gaps;
- known restrictions that materially narrow the reference universe.

No universal minimum sample count is defined in Phase 006.

## Invariants

- Large raw history is not sufficient if most observations are non-comparable.
- Small reference sets can support narrow descriptive statements but not automatically broad distribution claims.
- A 0% or 100% rate over tiny denominators must retain denominator/coverage context.
- Missing periods are not ordinary zero-valued observations.
- Sparse new metrics/post-change regimes may remain `insufficient reference` while normative Expectations can still be evaluated separately.
- Reference sufficiency is conclusion-relative; mean-level comparison and tail/distribution comparison can require different evidence.
- Restricted evidence can contribute only when the framework is authorized and the resulting projection follows Phase 005 disclosure rules.

## Example

Two month-end runs are enough to say what those two Observations were, but may be insufficient to characterize a stable month-end p95 envelope. The product should return `insufficient reference` rather than fabricate a precise distribution.