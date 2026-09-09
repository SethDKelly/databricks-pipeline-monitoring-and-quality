# HLTH-019 — Baseline Reference Set, Regime, Population & Window Binding

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define what evidence belongs to one descriptive Baseline regime without turning a reference set into a normative target.

## Contract

A Baseline/reference set binds, where material:

- subject and measured dimension;
- metric/check definition and version;
- grain and population semantics;
- structural/interface/schema regime;
- environment and operating context;
- reference period/window and inclusion/exclusion rule;
- cadence/calendar/cohort context;
- evidence coverage and provenance;
- derivation/refresh version and knowledge time.

A current Observation remains distinct from the reference set used to compare it. If the current Observation may participate in a rolling reference, that inclusion timing must be explicit rather than silently allowing self-comparison.

## Invariants

- Baseline is descriptive evidence, not an Expectation.
- Reference membership must be explainable from explicit context/rules; it is not whatever history happens to be available.
- More history is not automatically better if it mixes non-comparable regimes.
- The newest history is not automatically the correct reference.
- Historical Observations remain unchanged when Baseline membership or derivation changes.
- A new Baseline version may reuse eligible historical Observations without rewriting earlier Baseline versions or Assessments.

## Example

A daily row-count Baseline for C may bind ordinary business weekdays under metric definition v3 and grain `one row per account`. Month-end runs and post-grain-change observations do not join that reference set merely because they are temporally adjacent.