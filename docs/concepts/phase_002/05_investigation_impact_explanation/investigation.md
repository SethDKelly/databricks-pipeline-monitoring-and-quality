# Concept: Investigation

**Status:** Candidate

## Purpose

Let a user organize a bounded inquiry into a symptom, question, or degraded assessment and gather the relevant evidence needed to understand it.

## Operational principle

A degraded assessment for Table C starts an investigation over the affected time window. The investigation gathers upstream lineage, A/B/C observations, execution history, deployment changes, semantic context, and competing causal claims while allowing the outcome to remain unresolved.

## Actors

- Data Engineer
- Business Analyst
- Data Steward / Owner
- Monitoring framework

## State

- investigation identity and initiating question/symptom;
- subjects and time window;
- linked evidence/assessments/changes;
- investigation status;
- linked causal claims and impact analyses;
- participating/owning actors where relevant;
- provenance/history of material investigation updates.

## Actions

### `open`
Creates a bounded inquiry from a question, symptom, or assessment.

### `addEvidence`
Links relevant evidence without mutating the source evidence.

### `refineScope`
Adjusts subject/time/question boundaries with history where material.

### `close`
Marks the inquiry resolved, unresolved, or otherwise complete according to later lifecycle semantics.

## Invariants / behavioral expectations

- Investigation does not require one root cause.
- Evidence remains owned by its source concepts.
- Closing unresolved is valid.
- Investigation scope/time is explicit enough to support historical replay.
- Restricted evidence can remain unavailable without forcing disclosure.

## Ambiguity and missing evidence

An investigation may have incomplete, conflicting, stale, or inaccessible evidence. It must be able to remain open or close unresolved and must disclose material evidence gaps rather than manufacturing completeness.

## Synchronizations

Assessment can initiate Investigation; Lineage/Change/Execution History/Deployment/Observation enrich it; Causal Claim organizes explanations; Impact evaluates downstream exposure; Ownership identifies responsible parties; Explanation communicates results.

## Security / privacy / governance considerations

Investigation can aggregate metadata from many systems and therefore create new inference risk. Evidence visibility must remain authorization-aware, and the investigation container must not become a bypass around source restrictions.

## Evidence / provenance considerations

Material evidence links preserve source concept provenance. Investigation history should preserve when scope, evidence, and conclusions changed so a later reader can reconstruct what was known at the time.

## Representative scenarios

### Happy path
A degraded C assessment opens a bounded investigation and collects relevant A/B/C evidence.

### Degraded path
Critical upstream evidence is unavailable; the investigation remains unresolved with an explicit gap.

### Conflicting evidence
Two data sources support competing explanations; both remain linked.

### Unauthorized evidence
The investigation can show that restricted evidence exists without exposing it to the current user.

## Non-goals

- incident/ticketing workflow implementation;
- automatically proving causality;
- altering source data/pipelines;
- broadening authorization.

## Open questions

- Can investigations be nested/related?
- What lifecycle/status vocabulary is needed for MVP?
