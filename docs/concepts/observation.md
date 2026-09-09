# Observation

**Canonical key:** `concept.observation`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.observation`

**Owns current question:** What provenance-bearing fact was measured/retrieved about a subject/property/time/context?

**Stable IDs:** N/A

## Current semantics

Observation owns measured/retrieved values, states, events, aggregates or summaries together with subject/property meaning, unit/grain/context, event/effective time, collection/knowledge time, source/provenance, coverage/completeness, derivation basis, correction history, conflict, and visibility limitations.

## Actions

- `record` — preserve a provenance-bearing fact without interpreting health/cause.
- `correct` — add a source-supported correction while retaining the original evidence history.
- `retrieve` — return authorized Observations with provenance and evidence limitations.

## Invariants / boundaries

- Observation is evidence; Assessment is interpretation.
- Observation does not declare healthy, degraded, stale-as-subject, anomalous, compliant, or causal.
- Bare values without measurement meaning/unit/grain/subject/time are insufficient.
- Event/effective time ≠ collection/knowledge time.
- Missing evidence ≠ zero, false, empty, or observed absence.
- An absence is observed only when an applicable measurement/query with sufficient opportunity/coverage establishes it for a bounded interval.
- Independent conflicting facts remain separate Observations unless correction provenance establishes supersession.
- Aggregate/minimized evidence can be valid Observation; raw rows are not required by the concept.

## Ambiguity / evidence

Evidence may be partial, late, conflicting, unavailable, unauthorized, or stale-for-use. These describe evidence condition, not subject health.

## Synchronizations / related canonical resources

Expectation/Baseline provide references; Assessment interprets Observation; Baseline derives from Observation populations; Execution History/Change/Investigation may cite facts without taking ownership.

## Non-goals

Normative criteria, health interpretation, causal explanation, raw-data warehousing, or treating missing telemetry as absence.

## Provenance

- `docs/concepts/phase_002/03_health_evaluation/observation.md`
- `docs/concepts/phase_004/`
