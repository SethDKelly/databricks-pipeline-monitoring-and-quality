# Concept: Baseline

**Status:** Candidate — introduced in Phase 002

## Purpose

Let the ecosystem represent reference behavior derived from historical or comparative evidence without asserting that the behavior is normatively correct.

## Operational principle

Table C has historically produced 19–21 million rows on comparable business days. A new 14-million-row observation is materially different from the applicable baseline even though no explicit row-count expectation exists. The system can describe the deviation without claiming the historical range is an approved quality requirement.

## Actors

- Data Engineer
- Business Analyst
- Data Steward
- Monitoring framework

## State

- subject and measured dimension;
- reference population/window/context;
- derived reference characteristics or range;
- effective/comparison context;
- derivation provenance and evidence coverage;
- validity/quality limitations.

## Actions

### `derive`
Establishes a reference behavior from defined evidence/context.

### `refresh`
Updates the baseline prospectively while preserving which baseline supported prior assessments.

### `resolveApplicable`
Returns a baseline appropriate for the subject/context/time or `insufficient evidence`.

## Invariants / behavioral expectations

- Baseline is descriptive, not normative.
- Historical abnormality does not become acceptable merely by appearing in a baseline.
- Baseline derivation retains evidence window/context.
- Insufficient history must produce insufficient baseline rather than artificial precision.
- Baseline does not own the underlying observations.

## Ambiguity and missing evidence

Seasonality, sparse history, structural breaks, or known business events may make a baseline non-comparable. The concept must be able to return `not applicable` or `insufficient evidence`.

## Synchronizations

- Observation supplies historical evidence.
- Assessment may compare a new observation to a baseline.
- Change may describe structural shifts that make a prior baseline stale.
- Annotation may add known business context without mutating the baseline evidence.

## Security / privacy / governance considerations

A baseline can reveal sensitive volumes, seasonality, or business activity even if it contains no row-level data. Its visibility and derivation inputs must respect source authorization.

## Evidence / provenance considerations

The reference population, time window, comparison context, derivation basis, and data sufficiency must remain attached to the baseline. A refreshed baseline must not erase what supported earlier assessments.

## Representative scenarios

### Happy path
A comparable historical window provides a stable row-count reference for Table C.

### Degraded path
A new structural shift makes the prior baseline stale and non-comparable.

### Conflicting evidence
Two plausible baseline windows produce materially different references; the system exposes the ambiguity.

### Unauthorized evidence
A user can receive a deviation status without being shown restricted historical volumes.

## Non-goals

- setting approved thresholds;
- declaring health;
- anomaly detection implementation;
- causal inference.

## Open questions

- Which baseline classes are necessary for MVP?
- How is baseline validity challenged after structural change?
