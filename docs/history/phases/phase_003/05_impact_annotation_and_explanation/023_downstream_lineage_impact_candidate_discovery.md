# SYN-023 — Historical Downstream Lineage → Impact Candidate Discovery

**Status:** Accepted — Phase 003 Group 05

## Outcome

Identify plausible downstream consumers/entities for an originating runtime, data, change, investigation, or safeguard concern using the topology that was actually applicable at the relevant time, without presenting reachability as exposure, downstream effect, business consequence, or causation.

## Participating concepts and actions

- **Entity Identity** — resolves originating and downstream subjects.
- **Lineage** — `traverseAt` for typed historical downstream relationships.
- **Impact** — `identifyCandidates`.
- **Capability Authorization** — `resolveFor` where candidate/path disclosure is requested by an actor.
- **Investigation**, **Assessment**, **Change**, or another accepted concept may supply the bounded originating condition/question; they do not become Impact state.

## Trigger / initiating condition

An actor or Investigation asks what could be downstream of an identified condition, affected output, realized Change, or incident-time subject.

## Preconditions

The originating subject resolves to Entity Identity and the relevant effective/event-time context is sufficiently bounded for historical Lineage resolution. Relationship type and topology uncertainty remain explicit.

## Coordination semantics

1. Resolve the originating Entity Identity, relevant condition/question, and incident/change time window.
2. Traverse downstream Lineage using relationships valid for that historical context rather than current topology.
3. Include only relationship types semantically relevant to the impact question; data derivation, operational dependency, publication/consumption, and other edge meanings remain distinct.
4. For each reachable authorized subject, Impact records a candidate/reachability result with path basis and completeness/provenance limitations.
5. Planned-only topology from Change Intent is not treated as active downstream Lineage. Pre-realization blast-radius reasoning remains SYN-008 Prospective Impact Profile behavior.
6. Out-of-scope or restricted consumers may remain opaque candidates when that disclosure is authorized; they are not treated as absent.
7. Criticality, business meaning, policy sensitivity, or client-facing status may prioritize review but do not upgrade candidate state into exposure or consequence.

## State and evidence effects

Lineage owns historical relationships. Impact owns candidate/reachability state. Capability Authorization constrains what the requesting actor may see. The synchronization owns no independent blast-radius or impact truth.

## Ambiguity / failure propagation

Incomplete, conflicting, stale, inferred, restricted, or unavailable Lineage produces an explicitly incomplete candidate view. Missing topology never means `no downstream consumer`. An unauthorized identity can remain an opaque restricted node/path where allowed.

## Temporal semantics

Candidate discovery uses Lineage valid at the originating event time and records the knowledge time at which the candidate set was produced. Later topology discovery can enrich retrospective Impact without rewriting what was known during the incident.

## Provenance / traceability

Every candidate remains traceable to one or more typed Lineage paths and their source/evidence/provenance state.

## Security / authorization

Candidate identity, path detail, relationship type, business use, and even the existence of a restricted consumer may require separate authorization. Traversal does not broaden access merely because the origin is visible.

## Invariants

- downstream reachability ≠ exposure;
- downstream reachability ≠ downstream effect;
- downstream reachability ≠ business consequence;
- downstream reachability ≠ cause;
- criticality ≠ observed Impact;
- planned topology ≠ active Lineage;
- incomplete topology ≠ no dependency;
- repository boundary ≠ reasoning boundary.

## Scenarios

**A+B→C:** C's affected output traverses to a Metric View and two reports; all become candidates with distinct path bases.

**Historical topology:** a report consumed C through an older publication path during the incident even though the current topology differs.

**Restricted consumer:** the analyst sees that an additional restricted downstream consumer exists without its identity or full path.

**Critical but unexposed candidate:** a high-criticality client report is reachable and prioritized for review but remains only a candidate until exposure evidence exists.

## Non-goals

Exposure proof, downstream-health evaluation, causal attribution, risk-score calculation, criticality modeling, or graph implementation.

## Deferred questions

Minimum relationship types required for first-MVP impact traversal and how candidate prioritization should consume later-refined criticality semantics.