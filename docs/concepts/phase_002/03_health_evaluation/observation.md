# Concept: Observation

**Status:** Accepted — Phase 002 Group 03

## Purpose

Record an evidence-bearing measured or retrieved fact about an identified subject and relevant time/context without interpreting whether that fact is healthy, expected, anomalous, or causal.

## Operational principle

After a pipeline run, the product records that Table C contained 14,032,118 rows for a defined output interval. The Observation preserves the subject, measurement meaning, unit/grain, event/effective time, collection time, source, and provenance. Later analysis may determine that the value is atypical, acceptable, expected, or caused by another event, but none of those interpretations changes the Observation itself.

## Actors

- Monitoring framework
- Databricks / integration source
- Data Engineer / Pipeline Maintainer
- Data Steward / Governance Steward
- Other authorized evidence source

## State

- identified subject;
- observed property/dimension;
- measured/retrieved value, state, event, aggregate, or summary;
- measurement meaning, unit/grain, and relevant context;
- event/effective time or observed interval;
- collection/retrieval time when distinct;
- source and evidence provenance;
- observation coverage/completeness information where needed to interpret evidence absence;
- derivation basis for aggregate/derived factual observations;
- correction/supersession history;
- relationships to conflicting observations when relevant;
- visibility/security metadata necessary for safe evidence use.

## Actions

### `record`
- **Intent:** preserve a provenance-bearing measured/retrieved fact.
- **State effect:** adds an Observation without evaluating its health meaning.

### `correct`
- **Intent:** record a source-supported correction to an earlier Observation.
- **State effect:** preserves the original Observation and correction relationship instead of silently rewriting evidence history.
- **Important:** disagreement from a second independent source is not automatically a correction; it remains a separate Observation unless correction provenance establishes otherwise.

### `retrieve`
- **Intent:** return authorized Observations for a subject/property/time/context with their provenance and evidence-quality limitations.

## Invariants / behavioral expectations

- Observation is evidence, not Assessment.
- Observation does not declare healthy, degraded, stale, anomalous, compliant, or causal.
- A derived aggregate can still be an Observation when its measurement/derivation meaning and source evidence are preserved.
- Measurement meaning, unit/grain, subject, and relevant time context are part of the fact; a bare numeric value is insufficient.
- Event/effective time is not silently replaced with collection time.
- Missing evidence is not represented as zero, false, empty, or `no event`.
- An observed absence is legitimate only when a measurement/query with sufficient coverage positively establishes the absence over a defined interval, such as zero qualifying runs in a completely queried interval.
- Late collection does not change the event/effective time of the observed fact.
- Conflicting source facts remain separate provenance-bearing Observations unless an explicit correction relationship applies.
- Correction preserves evidentiary history and does not erase the prior fact from historical reasoning.
- Observation does not require raw row-level values; metadata, aggregates, fingerprints, statuses, and other minimized evidence are preferred where sufficient.

## Ambiguity and missing evidence

Observations may be unavailable, partial, stale as evidence, conflicting, late-arriving, or unauthorized. Those conditions describe evidence availability/quality, not subject health. When monitoring coverage is insufficient to know whether an event occurred, the result is missing/insufficient evidence rather than an Observation asserting non-occurrence.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Monitoring Scope** indicates where evidence collection is expected but does not itself create an Observation.
- **Semantic Definition** can supply the measurement meaning needed to interpret grain/units.
- **Expectation** provides normative comparison criteria without changing the Observation.
- **Baseline** can be derived from a population of Observations.
- **Assessment** interprets authorized Observation evidence against applicable Expectations and/or comparable Baselines.
- **Execution History**, **Change**, and **Investigation** can later cite or organize Observations without taking ownership of the source fact.

## Security / privacy / governance considerations

Observations can reveal sensitive business activity even when aggregated. Evidence visibility must respect source authorization and policy context. The product should prefer minimized aggregate/metadata evidence; raw or sampled values are not assumed necessary for the concept.

A derived status shown to a user must not be used as a path to reconstruct restricted underlying measurements beyond the viewer's authorized evidence view.

## Evidence / provenance considerations

Observation is evidence-bearing by definition. It must preserve source, subject, measurement meaning, observed/effective interval, collection time where distinct, coverage/completeness when material, derivation basis for aggregates, and correction history.

## Representative scenarios

### Row-count fact
Table C is observed to contain 14,032,118 rows for the latest completed output interval. No health conclusion is attached to the count.

### Successful execution fact
A Databricks run completed successfully at a given time. That is an Observation/Execution fact and does not imply that resulting data was fresh or high quality.

### Observed absence versus missing telemetry
A complete query of the authoritative run source shows zero qualifying runs before a deadline. That can support an observed absence. If the source query failed or monitoring was unavailable, the product records insufficient evidence instead of zero runs.

### Late-arriving evidence
A source observation arrives two hours late. Event time and collection time remain distinct so historical reasoning can reconstruct what occurred and when the product learned about it.

### Conflicting measurements
Two independent sources report different row counts for the same interval. Both remain provenance-bearing facts until later reasoning or authority resolves the discrepancy.

### Correction
A source later corrects a faulty measurement. The correction supersedes the earlier Observation for appropriate current use but preserves both facts and their history.

### Unauthorized evidence
A user may receive an authorized aggregate/null-rate Observation while restricted example values remain inaccessible.

## Non-goals

- defining expected behavior;
- deciding whether evidence is healthy or degraded;
- deriving normative conclusions;
- causal explanation;
- storing arbitrary raw production datasets;
- treating missing telemetry as evidence of absence.

## Deferred questions

- What minimum measurement/provenance metadata is required for first-MVP RCA trustworthiness?
- Which evidence-coverage indicators are necessary to support negative/absence observations safely?
- How should observations sourced from deterministic queries versus probabilistic/estimated measurements expose uncertainty later?
