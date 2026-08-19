# Concept: Observation

**Status:** Candidate

## Purpose

Record a time-bounded fact or measurement about execution, data state, schema, distribution, or another monitored property with enough provenance to be used as evidence.

## Operational principle

After a run, the system records that Table C contained 14 million rows, with the subject, measurement meaning, event/effective time, collection time, source, and evidence provenance. The observation remains a fact even if later analysis decides the value is expected or explains why it occurred.

## Actors

- Monitoring framework
- Data Engineer
- Databricks / integration sources
- Data Steward

## State

- observed subject and property/dimension;
- observed value/summary/state;
- event/effective time and collection time where distinct;
- provenance/source;
- evidence quality/completeness/visibility indicators;
- correction/supersession relationship when a source observation is later corrected.

## Actions

### `record`
Adds a provenance-bearing observation.

### `correct`
Supersedes an incorrect observation without silently deleting the original evidentiary history.

### `retrieve`
Returns observations for a subject/property/time window subject to authorization.

## Invariants / behavioral expectations

- Observation does not declare healthy/degraded.
- Observation does not assert causality.
- Source and relevant time context are preserved.
- Collection time is not silently substituted for event/effective time.
- Missing/unauthorized evidence is not represented as a zero/false measurement.

## Ambiguity and missing evidence

Observations may be late, partial, stale, conflicting, unavailable, or inaccessible. The concept represents those evidence-quality conditions rather than hiding them.

## Synchronizations

- Asset Identity identifies the subject.
- Expectation/Baseline provide comparison context.
- Assessment interprets observations.
- Change compares observations/states across time.
- Investigation cites observations as evidence.

## Security / privacy / governance considerations

Prefer aggregate/metadata observations. Raw/row-level evidence requires explicit later security semantics and must not be assumed necessary.

## Evidence / provenance considerations

Observations are evidence-bearing by definition. Source, observed/effective time, collection time, measurement meaning, evidence completeness, and any correction history must be retained.

## Representative scenarios

### Happy path
A row-count observation for Table C is recorded with run/time provenance.

### Degraded path
The observation arrives late; the system preserves event time and collection time separately.

### Conflicting evidence
Two sources report different counts for the same logical interval; both observations remain available with provenance.

### Unauthorized evidence
An aggregate quality observation can be exposed while row-level examples remain inaccessible.

## Non-goals

- deciding health;
- defining expected behavior;
- storing arbitrary raw production datasets;
- causal explanation.

## Open questions

- What minimum observation metadata is required for trustworthy RCA?
- How should conflicting observations from separate sources be represented?
