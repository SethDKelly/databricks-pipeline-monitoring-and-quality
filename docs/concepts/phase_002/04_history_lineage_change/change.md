# Concept: Change

**Status:** Accepted — Phase 002 Group 04; refined by Phase 007 Group 02 (OPS-014–OPS-019)

## Purpose

Let users identify and describe a realized difference or state transition that evidence establishes actually occurred, while preserving its basis, timing, magnitude, and uncertainty without judging health or cause.

## Operational principle

A filter Change Intent predicts lower output from Table C. After the related Deployment activates, Observations establish that C's row volume fell and its key distribution changed. Change describes those realized differences with before/after evidence and timing. It does not claim that the filter caused them, that they match intent, or that they are healthy; those interpretations require separate context and later reasoning.

## Actors

- Monitoring framework
- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Data Steward / Governance Steward
- Integration/source systems

## State

- identified changed subject or relationship;
- changed facet/dimension/type;
- before/after state or evidence references when comparison-derived;
- explicit source change-event reference when source-declared;
- realized change description/direction/magnitude when supportable;
- effective/change interval or transition time when known;
- comparison context/comparability limitations;
- provenance/derivation basis and knowledge time;
- uncertainty/conflict/correction history;
- optional association to relevant Change Intent/Deployment as context without asserting conformance/cause.

## Actions

### `derive`
- **Intent:** compare sufficiently comparable before/after evidence and record the realized difference.
- **Failure / unknown behavior:** non-comparable or insufficient evidence does not yield a fabricated delta.

### `recordOccurred`
- **Intent:** record an explicit source-reported change event that is known to have occurred.
- **State effect:** preserves source semantics/provenance rather than assuming the event's effects.

### `correct`
- **Intent:** record correction/supersession of earlier Change evidence while preserving historical knowledge.

### `resolveWindow`
- **Intent:** return realized Changes relevant to a subject/facet/time window with provenance and uncertainty.

## Invariants / behavioral expectations

- Change is realized/descriptive; Change Intent is planned/anticipatory.
- A Change Intent alone is not a Change.
- A Deployment alone is not necessarily a meaningful data/schema/topology Change; the activated code/configuration transition itself may be a Change while its downstream effects still require evidence.
- Change is not automatically good, bad, healthy, degraded, valid, invalid, expected, or unexpected.
- Change is not cause.
- Before/after comparison retains evidence, semantic units, context, and comparability basis.
- Missing prior evidence is not a zero/default state.
- Different change kinds remain typed rather than flattened into one undifferentiated signal.
- A realized Change can be consistent with intent while another health dimension still violates an Expectation.
- A realized Change can differ from intent without proving why.
- Event/effective time and knowledge/record time remain distinguishable when late discovery/correction matters.

## Change kinds

Candidate change families include, without prescribing implementation taxonomy:

- code/configuration activation;
- execution behavior;
- data volume/distribution/schema/content-property;
- Lineage/topology;
- Semantic Definition;
- Responsibility Assignment;
- Classification/Policy Context;
- Expectation/Baseline lifecycle/comparability;
- Monitoring Scope/identity-reference context.

A later design may refine which are first-class for MVP.

## Phase 007 Group 02 refinement

OPS-014 makes a realized Change a bounded proposition over subject/relationship, facet, before/after state, semantic grain/population/interface/version, transition time/interval, comparison semantics, provenance and limitations.

An activated code/configuration transition can itself be a Change of implementation state. It still does not create downstream Change automatically. `F2 became active`, `C volume decreased`, `C null rate rose`, and `D→C Lineage became effective` are distinct realized propositions with different evidence owners.

OPS-015 keeps intent conformance outside Change truth. `Matched`, `partially matched`, `diverged`, `not realized`, `not evidenced`, `indeterminate`, `conflicting`, and `unavailable` are derived comparisons against an exact Change Intent component; they are not Change states.

OPS-016 keeps realized Change target/slice specific during phased rollout and preserves overlapping intents without using compatibility as causal attribution.

OPS-017 distinguishes realized Change with no matching registered intent from the stronger claim that a change was actually unplanned under a governing process. Change remains valid even when intent/deployment context is missing.

OPS-018 makes rollback/reversion non-rewriting. Reversion of one implementation facet does not imply every data/schema/topology/downstream facet reverted. A restored/equivalent state requires bounded evidence.

OPS-019 preserves event/effective and knowledge time independently. Later evidence can revise retrospective Change timing/comparison while preserving prior recorded knowledge/results.

For topology, **Lineage remains relationship truth owner**. Change may describe a realized topology transition from OPS-001–OPS-009 Lineage history; it does not own or manufacture the edge.

## Ambiguity and missing evidence

If states are non-comparable, incomplete, time-misaligned, conflicting, or unauthorized, Change may be partial/unknown/non-comparable. A change can also be established at a coarse level while sensitive details remain restricted.

## Synchronizations

- **Observation** provides before/after evidence for measurable state changes.
- **Baseline** can be marked non-comparable when a realized structural Change establishes a new context; the Baseline itself remains descriptive.
- **Expectation** changes are realized normative-state Changes but preserve their own concept semantics/history.
- **Change Intent** provides planned context and anticipated effects; comparing realized Change to intent does not by itself establish health/cause.
- **Deployment** supplies active code/configuration transitions and temporal context.
- **Execution History** supplies run ordering/context.
- **Lineage** supplies before/after topology for realized relationship changes.
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, and **Policy Context** can expose their own historical state transitions as Change evidence without giving Change ownership of those concepts.
- **Assessment** interprets health/typicality separately.
- **Investigation/Causal Claim** later use Change timing/sequence as evidence for hypotheses.

## Security / privacy / governance considerations

Change descriptions can expose sensitive volume, schema, policy, semantics, topology, deployment, or organizational information. The concept must support authorized abstraction/redaction.

## Evidence / provenance considerations

Derived Change retains before/after evidence references, comparison context, derivation meaning, effective/change time, knowledge time, and limitations. Source-declared Changes retain the original source reference/semantics. Corrections do not invisibly rewrite earlier knowledge.

## Representative scenarios

### Planned valid structural change
A filter intentionally lowers C's population. Deployment/Observation evidence establishes the realized lower volume. Change records the shift; a revised Expectation can establish acceptability, while a new Baseline is derived later.

### Planned change with unintended quality issue
C's volume falls as intended, but null rate also rises. Change records both realized differences. Assessment may say the new volume meets its revised Expectation while completeness violates another Expectation.

### Unplanned source shift
B's distribution changes without any registered Change Intent or Deployment. Change still records the realized shift from Observation evidence.

### Deployment without data change
A refactor deployment occurs but material data Observations remain comparable. The deployment/configuration transition exists; no downstream data Change is fabricated.

### Historical topology change
C switches from B1 to B2. Change uses historical Lineage evidence to describe the realized topology transition while preserving both periods.

## Non-goals

- planned-change registration;
- health/quality assessment;
- intent-conformance truth ownership;
- root-cause attribution;
- anomaly-detection implementation;
- requiring full raw snapshots.

## Deferred questions

- first-class Change kinds for MVP;
- threshold for promoting raw Observation differences into meaningful Change records;
- concrete source support for gradual/partial transition intervals;
- implementation/source mechanisms for change capture remain Phase 009/010 work.
