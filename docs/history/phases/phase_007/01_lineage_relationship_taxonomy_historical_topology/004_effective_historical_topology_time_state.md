# OPS-004 — Effective Topology, Historical Time & Relationship Lifecycle

**Status:** Accepted — Phase 007 Group 01

## Purpose

Keep planned, effective, historical and later-discovered topology distinct while preserving non-rewriting Lineage history.

## Contract

Every material Lineage proposition must retain enough temporal state to distinguish:

- the effective/event interval during which the relationship is asserted/established to apply;
- source production/observation and availability time where relevant;
- framework recorded/knowledge time;
- correction/supersession knowledge time;
- current retrospective resolution versus what was known at an earlier cutoff.

## Topology classes

### Planned topology

A proposed relationship that would exist if a Change Intent is realized. Planned topology remains **Change Intent context**, not active/effective Lineage.

### Effective Lineage topology

Relationships whose proposition is established as applying for the relevant effective interval under OPS-005 evidence semantics.

### Historical Lineage topology

Effective Lineage resolved for a past event/effective time, optionally under a selected historical knowledge cutoff.

### Runtime-instance evidence

Evidence from a run/query/execution may support a bounded Lineage proposition. The specific execution sequence, output existence and consumed input/output version remain owned by Execution History/Observation/Impact rather than being collapsed into generic topology.

## Lifecycle behavior

Relationships may be established, ended/superseded or corrected without deleting prior history.

- Supersession/end records that a previously applicable relationship no longer applies after an effective boundary.
- Correction changes the current retrospective understanding of a prior relationship while preserving when the earlier understanding was known/used.
- An unknown end time is not proof that a relationship remained effective forever.
- Reappearance after an inactive interval is a new effective interval/versioned relationship state rather than historical erasure.

## Planned-to-effective boundary

A Change Intent or deployment configuration may provide evidence about expected topology but does not activate the Lineage relationship by itself. Sufficient realization/effective-state evidence is required. Group 02 will refine that realization handoff.

## Invariants

- Planned topology ≠ effective topology.
- Current topology ≠ historical topology.
- Effective relationship at event time ≠ relationship known by the framework at that time.
- Later discovery can revise retrospective topology without backdating framework knowledge.
- Deployment attempt/activation alone does not universally prove every intended relationship became effective.
- Specific run/consumer encounter truth remains separate from effective general topology.

## Handoff

OPS-005 defines the evidence burden for establishing or excluding a relationship. Group 02 will refine Change Intent → Deployment → realized Change evidence that can trigger topology transitions.