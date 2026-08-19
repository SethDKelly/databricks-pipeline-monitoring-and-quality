# Concept: Causal Claim

**Status:** Candidate — introduced in Phase 002

## Purpose

Represent a proposed or reviewed causal explanation with explicit epistemic status, supporting/contradicting evidence, and uncertainty.

## Operational principle

For C's row-count degradation, one causal claim proposes that B's upstream volume reduction materially contributed; another proposes changed join behavior. Evidence supports the first and weakens the second. An authorized engineer later confirms the source-feed outage as a contributing cause. The system preserves the evidence trail and does not erase the rejected alternative.

## Actors

- Data Engineer
- Data Steward / Owner
- Monitoring framework
- Authorized reviewer

## State

- claim statement and affected symptom/subject/time;
- status such as proposed, supported, weakened, rejected, confirmed, unresolved (final vocabulary deferred);
- supporting and contradicting evidence references;
- contribution role if multiple causes are involved;
- uncertainty/confidence rationale;
- proposer/reviewer/confirmation provenance where applicable;
- supersession/history.

## Actions

### `propose`
Creates a causal explanation as a claim, not a fact.

### `support`
Associates supporting evidence/rationale.

### `contradict`
Associates contradicting evidence/rationale.

### `reviseStatus`
Changes epistemic status based on evidence without rewriting the underlying evidence.

### `confirm` / `reject`
Records an authorized review outcome with provenance according to an agreed evidence/authority standard.

## Invariants / behavioral expectations

- Correlation alone does not imply confirmed causation.
- A claim can have both supporting and contradicting evidence.
- Multiple contributing claims may coexist.
- `confirmed` requires an explicit future evidence/authority standard; Phase 002 does not invent one.
- Rejected claims remain historically visible when material to the investigation.

## Ambiguity and missing evidence

Evidence can be insufficient, contradictory, temporally misaligned, or inaccessible. A claim may remain proposed/supported without progressing, and lack of contradicting evidence is not proof.

## Synchronizations

- Investigation scopes and groups causal claims.
- Change, Observation, Assessment, Lineage, Execution History, and Deployment provide evidence.
- Annotation may add context to a claim.
- Explanation must state the claim's epistemic status accurately.

## Security / privacy / governance considerations

Causal claims can reveal sensitive operational or business conclusions. Proposal, review, confirmation, and visibility must respect actor authority and policy context.

## Evidence / provenance considerations

Support/contradiction links, proposers/reviewers, timestamps, status changes, and confirmation authority must remain traceable. A claim never replaces the evidence it cites.

## Representative scenarios

### Happy path
B volume reduction is supported as a contributing cause of C degradation and later confirmed by an authorized engineer.

### Degraded path
Several plausible causes remain supported with insufficient evidence to choose among them.

### Conflicting evidence
One observation supports a deployment cause while another contradicts the expected timing.

### Unauthorized evidence
A viewer may see that the cause is unresolved without seeing a restricted causal claim.

## Non-goals

- generating hypotheses by a specific AI/algorithm;
- defining a numerical confidence model;
- changing assessments;
- implying legal/audit-grade causality by default.

## Open questions

- What operational evidence standard permits `confirmed`?
- How should contributing versus primary causes be represented?
- Do we need a separate Attribution concept later, or is status within Causal Claim sufficient?
