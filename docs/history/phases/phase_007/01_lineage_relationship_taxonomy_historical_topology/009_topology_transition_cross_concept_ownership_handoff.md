# OPS-009 — Topology Transition, Cross-Concept Ownership & Group 02 Handoff

**Status:** Accepted — Phase 007 Group 01

## Purpose

Keep Lineage authoritative for relationship/topology history without absorbing Change Intent, Deployment, Change, execution, Impact or active-control truth.

## Lineage ownership

Lineage owns:

- typed relationship propositions under OPS-001/OPS-002;
- relationship semantic scope under OPS-003;
- effective/historical relationship intervals under OPS-004;
- provenance/evidence-backed existence resolution under OPS-005/OPS-006;
- traversal/relevance/completeness under OPS-007/OPS-008;
- correction/supersession history for relationship truth.

## Synchronization boundaries

### Change Intent

May describe proposed future topology. It does not create effective Lineage.

### Deployment

May provide evidence that a relevant artifact/configuration became active. Deployment activation does not universally prove every intended topology relation became effective.

### Change

Owns the realized difference/state transition. Establishing/ending/materially changing a Lineage relationship can provide evidence for a realized topology Change, while the Lineage relationship history remains Lineage truth.

### Execution History

Owns actual execution-instance lifecycle/order. An `operational_dependency` edge does not prove the dependent run waited for or consumed a particular upstream run/output.

### Impact

Owns actual encounter/exposure/effect/consequence. `consumption_path` is only candidate topology.

### Execution Gate

Owns enabled/configured gate prerequisites, decisions and enforcement. `operational_dependency` does not silently enable a gate, and a gate configuration is not converted into generic Lineage truth merely to make a graph edge.

### Propagation Safeguard

Owns protection state/enforcement. Publication/consumption-path Lineage can identify possible protected paths but does not prove a safeguard controlled them.

### Observation / Assessment / Health

May attach evidence/results to endpoints/transformation context. No local metric, Assessment, warning, waiver or composite status recursively propagates through Lineage.

### Investigation / Causal Claim

May traverse relevant historical Lineage. Lineage never becomes causal status.

## Entity replacement/succession

Replacement, migration, split, merge and succession remain Entity Identity/Change history unless a later scenario proves a separately useful Lineage proposition. They are not added to the minimum operational taxonomy merely to connect historical names/assets.

## Group 02 handoff

Group 02 must refine how evidence moves through:

**Change Intent → Deployment attempt/activation → realized state evidence → Change → effective Lineage transition where applicable**

without assuming those stages are one lifecycle or that one universally proves the next.

It must also handle one intent realized by several Deployments, one Deployment realizing several intents, partial/mismatched realization, unplanned topology Change, rollback/reversion and historical active-version reconstruction.

## Invariants

- Lineage relation state ≠ Change Intent ≠ Deployment ≠ realized Change.
- Relationship transition ≠ causal attribution.
- Logical dependency ≠ gate configuration/enforcement.
- Consumption path ≠ exposure.
- Publication path ≠ successful/current delivery.
- Lineage relevance ≠ metric/status propagation.
- No new truth-owning concept is required for Group 01.