# Concept: Change

**Status:** Candidate

## Purpose

Let users identify and describe meaningful differences in an entity, relationship, observation pattern, definition, deployment, or other monitored state across time.

## Operational principle

The investigation of Table C finds that B's row volume changed first, C's join match rate then changed, and a deployment occurred between the two observations. Change describes each transition with before/after context and timing without declaring which transition caused the degradation.

## Actors

- Monitoring framework
- Data Engineer
- Business Analyst
- Data Steward

## State

- changed subject/facet;
- before/after or prior/current evidence references;
- change kind/magnitude/description;
- effective/change interval when known;
- provenance/derivation basis;
- comparability/uncertainty context.

## Actions

### `compare`
Compares two comparable states/observations and describes differences.

### `record`
Records a known explicit change event from an authoritative source.

### `resolveWindow`
Returns relevant changes for a subject/facet/time window.

## Invariants / behavioral expectations

- Change is descriptive, not automatically good/bad.
- Change is not cause.
- Comparisons retain their basis and time context.
- Non-comparable states must not yield misleading deltas.
- Semantic, topology, deployment, schema, volume, distribution, and ownership changes may be different change kinds rather than one flattened signal.

## Ambiguity and missing evidence

If before/after states are not comparable, time-aligned, complete, or authorized, the change may be unknown or only partially described. Missing prior evidence is not a zero-value baseline.

## Synchronizations

- Observation/Baseline provide comparable data-state evidence.
- Deployment provides deployment transitions.
- Semantic Definition/Ownership/Classification/Policy Context can surface governance changes.
- Lineage can surface topology changes.
- Investigation uses Change to prioritize temporal hypotheses.

## Security / privacy / governance considerations

Change summaries may reveal sensitive business volume, schema, policy, or topology information. The concept must support safe abstraction/redaction.

## Evidence / provenance considerations

Every derived change retains the before/after evidence, comparison basis, time interval, and derivation provenance. Explicit source change events retain their original source reference.

## Representative scenarios

### Happy path
B row volume drops before C output volume drops.

### Degraded path
A schema changed, but no comparable pre-change distribution evidence exists.

### Conflicting evidence
Two source snapshots disagree about when a change became effective.

### Unauthorized evidence
A viewer can learn that a material upstream change occurred without seeing restricted values.

## Non-goals

- health assessment;
- causal attribution;
- anomaly detection implementation;
- storing full raw snapshots by requirement.

## Open questions

- Which change kinds are first-class for MVP RCA?
- When is a detected delta promoted to a meaningful Change versus remaining raw observation difference?
