# SYN-033 — Event-Time + Knowledge Cut → Historical State Reconstruction

**Status:** Accepted — Phase 003 Group 06

## Outcome

Reconstruct a historically honest view of ecosystem state for a defined event/effective-time question using only evidence and concept state that was known by a defined recorded/knowledge-time cutoff, without projecting later corrections, topology, governance, authorization, reference context, or control state backward.

## Participating concepts and actions

All accepted concepts may participate when relevant to the question. The synchronization especially coordinates:

- **Entity Identity**, **Monitoring Scope**, **Semantic Definition**, **Responsibility Assignment**, **Classification**, **Policy Context**, **Capability Authorization**;
- **Expectation**, **Baseline**, **Observation**, **Assessment**;
- **Change Intent**, **Deployment**, **Execution History**, **Lineage**, **Change**;
- **Execution Gate**, **Propagation Safeguard**;
- **Investigation**, **Causal Claim**, **Impact**, **Annotation**, **Explanation**.

No new historical-state concept is created. The result is a query/replay view over independently owned concept histories.

## Trigger / initiating condition

A user/system asks a historical question such as:

- what happened at time/window `T`?
- what did the monitoring ecosystem know by cutoff `K`?
- what topology/reference/governance/control state was applicable then?
- what evidence, Assessment, Investigation, causal, Impact, or Explanation state had actually been recorded by then?

## Preconditions

- the requested subject/question is sufficiently identified;
- event/effective-time target or window is explicit enough for the question;
- knowledge cutoff is explicit for an `as-known-then` view; if omitted for a retrospective view, the current/latest permitted knowledge cut may be used but must be labeled;
- per-concept provenance and temporal information are preserved enough to resolve the requested cut.

## Coordination semantics

1. Establish two independent coordinates:
   - **event/effective time** — when the questioned condition/event/state applied;
   - **knowledge cutoff** — latest recorded/knowledge time evidence is allowed to contribute.
2. Resolve Entity Identity/reference mappings applicable to the event-time question **using only identity evidence known by the knowledge cutoff**. A later identity correction is excluded from a contemporaneous cut even if it later becomes effective for retrospective interpretation.
3. Resolve each participating concept independently using its own effective-time semantics plus the knowledge cutoff. Current state is never substituted merely because it is easier to query.
4. Include a fact/assertion/change only when its evidence was available by the knowledge cutoff. Evidence recorded later but effective earlier is excluded from the contemporaneous cut and may appear in a later retrospective cut.
5. Preserve each concept's unknown/conflicting/unavailable/unauthorized/non-comparable state rather than filling gaps from later knowledge.
6. Distinguish **actual historical state** from **replay-derived interpretation**:
   - an Assessment/Causal Claim/Impact/Annotation/Explanation that was actually recorded by the cutoff may be returned as historical state;
   - a current computation over the historical input cut may be produced where useful, but it is labeled `replay-derived` and cannot be presented as something that was actually assessed, believed, decided, or explained then.
7. Resolve historical gate/safeguard configuration and actual hold/admit/override/activate/release state separately from runtime execution/output facts.
8. Preserve source evidence, effective intervals, corrections, supersessions, and the selected temporal coordinates in the replay result.

## State and evidence effects

The synchronization creates no new canonical state. It returns a historical projection over existing histories. If a replay-derived result is retained later, the owning concept must record it with its **new** knowledge/evaluation time rather than backdating it into the historical cut.

## Ambiguity / failure propagation

Insufficient temporal metadata, unavailable source history, ambiguous identity, incomplete historical Lineage, unknown control enforcement, or restricted evidence can produce partial replay. A partial replay remains valid and explicitly limited.

Missing record by cutoff means `not known/recorded by cutoff` only when coverage is sufficient to establish that statement. It does not automatically mean the underlying real-world condition did not exist.

## Temporal semantics

This synchronization is explicitly bitemporal:

- event/effective time answers **when the subject condition applied**;
- recorded/knowledge time answers **when the ecosystem could use the evidence/assertion**.

A single event-time question can therefore yield different valid results under different knowledge cutoffs.

## Provenance / traceability

Every material replay statement is traceable to:

- event-time target/window;
- knowledge cutoff;
- concept state/evidence included in the cut;
- excluded later evidence where material to understanding the difference;
- replay-derived versus actually-recorded status.

## Security / authorization

Internal historical reconstruction does not widen current disclosure. Historical Capability Authorization is itself historical evidence, while the current requester's applicable disclosure authorization is applied separately through SYN-035.

## Invariants

- event/effective time ≠ recorded/knowledge time;
- current state ≠ historical state;
- current topology ≠ historical Lineage;
- current reference ≠ historical applicable Expectation/Baseline;
- later correction ≠ fact known earlier;
- historical Capability Authorization ≠ current disclosure permission;
- historical gate/safeguard configuration ≠ current control configuration;
- replay-derived interpretation ≠ actually recorded historical Assessment/claim/Impact/Explanation;
- historical replay ≠ counterfactual rewrite.

## Scenarios

### Late Deployment activation evidence
At 10:15, monitoring did not yet know Deployment R2 activated at 09:55. An `event=10:00, knowledge=10:15` cut excludes the late activation evidence. A later retrospective cut can include it while preserving the earlier uncertainty.

### Historical Lineage correction
A dependency edge effective during an incident is discovered the next day. The contemporaneous cut lacks that path; the retrospective cut includes it and may support new Investigation candidates without pretending responders knew the edge during the incident.

### Gate state
A downstream run was held at 07:00 under an enabled gate. Historical replay returns the actual hold and readiness evidence known then. A later rule change cannot alter that past action.

## Non-goals

- selecting a temporal database/event store;
- materializing a snapshot architecture;
- computing counterfactual `what would have happened if` scenarios;
- inventing historical facts from current state;
- defining retention periods.

## Deferred questions

- exact first-MVP query syntax for event-time and knowledge-cut selection;
- which concept histories require persisted snapshots versus reconstructible version history;
- evidence completeness needed to state `not known by cutoff` confidently;
- performance/retention strategy for long-range replay.
