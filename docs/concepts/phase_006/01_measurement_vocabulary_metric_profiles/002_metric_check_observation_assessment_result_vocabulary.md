# HLTH-002 — Metric, Check, Observation, Assessment & Result Vocabulary

**Status:** Accepted — Phase 006 Group 01

## Purpose

Prevent implementation-oriented terms such as `metric`, `check`, `DQ result`, or `pass/fail` from collapsing the accepted Observation / Expectation / Baseline / Assessment boundaries.

## Vocabulary

### Metric definition
A semantic definition of a measurable quantity, including calculation meaning, unit/domain, inputs, aggregation/denominator/filter behavior, grain/window and material versioning.

### Metric Observation
The measured value/state produced under a specific metric definition and bound scope. It is an **Observation**.

### Observed structural/predicate fact
A directly observed boolean/categorical fact such as `column X exists`, `schema fingerprint = F`, or `output exists`. It is an Observation when no normative interpretation is embedded.

### Check definition
A configured evaluative operation that may obtain one or more Observations and, when bound to an Expectation or explicit comparative basis, produce an Assessment. `Check` is a useful domain term, not an independent truth owner.

### Assessment
The interpreted state against an explicit normative Expectation and/or descriptive Baseline basis. Pass/fail/warn/degraded/atypical semantics belong here, not in the raw measurement.

### Result
A presentation/integration term that must identify whether it is returning an Observation, Assessment, limitation/state of evaluation, or composite view. `Result` does not create a separate truth layer.

## Invariants

- `metric value observed` ≠ `healthy`.
- `column exists = true` ≠ `schema compatible` unless the applicable structural Expectation makes existence sufficient.
- `calculation completed successfully` ≠ `check passed`.
- `metric unavailable` ≠ `metric value = 0`.
- A metric can exist and be observed without any normative Expectation.
- Baseline comparison can establish typical/atypical behavior without creating normative pass/fail unless an Expectation explicitly adopts that meaning.
- A boolean implementation function named `check_*` does not determine whether the resulting truth belongs to Observation or Assessment; the semantic proposition does.

## Canonical wording rule

Use `pass`, `fail`, `warning`, or equivalent normative language only when the result is an Assessment against a defined applicable criterion. For raw extraction/measurement state prefer wording such as `observed`, `available`, `unavailable`, `not applicable`, `pending`, or the exact observed predicate.
