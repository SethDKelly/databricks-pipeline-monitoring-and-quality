# Concept: Expectation

**Status:** Candidate

## Purpose

Let an authorized owner/steward state what behavior or data condition should be considered acceptable for a defined subject and context.

## Operational principle

A data owner states that an output should be refreshed by 7:00 AM on business days and that a key field should remain below an agreed null threshold. When the expectation changes next quarter, historical assessments continue using the version that applied at their incident time.

## Actors

- Data Owner / Steward
- Data Engineer
- Data Platform Administrator
- Monitoring framework

## State

- subject/scope;
- expectation definition and dimension;
- applicability context;
- lifecycle/effective time;
- severity/criticality context where meaningful;
- provenance and responsible authority;
- waiver/suspension/supersession state if adopted.

## Actions

### `establish`
Creates an expectation with purpose, scope, provenance, and effective time.

### `revise`
Supersedes future applicability without rewriting prior versions.

### `waive`
Records a time/context-bounded exception without deleting the underlying expectation.

### `resolveApplicable`
Returns the expectation(s) applicable to a subject/context/time.

## Invariants / behavioral expectations

- Expectations are normative and must not be fabricated from historical behavior without explicit promotion/authority.
- Historical assessments retain the expectation version used.
- A waiver is not evidence that observed behavior was healthy; it changes applicability/handling according to explicit semantics.
- Expectation does not own observations or assessments.

## Ambiguity and missing evidence

No applicable expectation is a valid result. Conflicting expectations remain explicit until authority/priority rules are defined.

## Synchronizations

- Asset Identity identifies the subject.
- Ownership identifies responsible parties.
- Observation provides measured facts.
- Assessment compares applicable expectations and observations.
- Baseline can supplement evaluation but cannot silently replace an expectation.

## Security / privacy / governance considerations

Expectations may encode sensitive business thresholds or handling requirements. Only authorized actors/sources should establish or revise normative expectations, and visibility may vary by audience.

## Evidence / provenance considerations

The asserting source/actor, effective interval, revision history, and any waiver authority must be retained so historical assessments can explain which expectation applied.

## Representative scenarios

### Happy path
A freshness expectation is active and the latest observation satisfies it.

### Degraded path
An asset misses its freshness expectation even though its Databricks job succeeded.

### Conflicting evidence
Two sources define incompatible freshness expectations; the assessment does not choose one silently.

### Unauthorized evidence
A user may see that an expectation was violated without seeing a sensitive threshold definition.

## Non-goals

- measuring data;
- deriving historical baselines;
- determining cause;
- implementing DQX rule syntax.

## Open questions

- Which expectation lifecycle states are essential?
- How should multiple simultaneously applicable expectations combine?
