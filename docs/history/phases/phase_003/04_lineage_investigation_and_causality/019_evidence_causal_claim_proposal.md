# SYN-019 — Historical Evidence → Explicit Causal Claim Proposal

**Status:** Accepted — Phase 003 Group 04

## Outcome

Turn a plausible causal explanation into an explicit Causal Claim with a defined cause condition, outcome, temporal context, and rationale rather than letting causality remain implicit in Lineage paths, dashboards, or narrative text.

## Participating concepts and actions

- **Investigation** — `linkClaim`.
- **Causal Claim** — `propose`.
- **Observation**, **Change**, **Execution History**, **Deployment**, **Change Intent**, **Lineage**, **Assessment**, **Propagation Safeguard**, and **Annotation** — possible evidence/context sources.

## Trigger / initiating condition

An analyst or authorized reasoning process identifies a proposition worth evaluating after candidate discovery/evidence assembly.

## Preconditions

The proposed outcome is defined and the proposed cause condition is more specific than mere upstream reachability or temporal proximity.

## Coordination semantics

1. State the **outcome being explained** explicitly.
2. State the proposed causal condition/event/change and any proposed role such as primary, contributing, enabling, or preventing.
3. Record relevant event-time bounds and the Lineage/dependency/mechanism rationale that makes the proposition plausible.
4. Link the claim to the Investigation without treating linkage as endorsement.
5. Attach initial supporting/contradicting evidence references separately when already known.
6. Automated systems may propose claims, but the proposal remains epistemically `proposed` until evidence evaluation justifies a different status.
7. Do not create a Causal Claim merely because an entity is upstream, changed recently, was deployed recently, or appeared in a prospective blast-radius profile.

## State and evidence effects

Causal Claim owns the causal proposition/status. Investigation owns association to the inquiry. Evidence remains in source concepts.

## Ambiguity / failure propagation

If the proposed causal condition, outcome, or temporal relation is too ambiguous to evaluate, keep the proposition unresolved/proposed or refine it rather than creating a falsely precise claim.

## Temporal semantics

Claim proposal time is knowledge time; the proposed causal condition/effect use their own event/effective times.

## Provenance / traceability

Record whether the claim was proposed by an analyst, automated reasoning process, or another authorized source plus its initial rationale/evidence basis.

## Security / authorization

A claim may reference opaque restricted causes/evidence while limiting disclosure to the current audience.

## Invariants

- upstream candidate ≠ Causal Claim;
- temporal proximity ≠ Causal Claim support by itself;
- prospective Impact candidate ≠ retrospective cause;
- proposal ≠ support ≠ confirmation;
- Investigation linkage ≠ endorsement.

## Scenarios

Propose `B population reduction contributed to C row loss`; propose `join-key null increase contributed to C row loss`; propose `active safeguard caused client-delivery delay`; do not automatically propose `recent deployment caused C loss` merely because the timestamps are close.

## Non-goals

Hypothesis-generation algorithm selection, automatic confirmation, numeric probability assignment, or single-root enforcement.

## Later refinement — Phase 007 Group 05

OPS-060 sharpens this synchronization into an explicit semantic handoff. Investigation may retain leads/localization without creating a Causal Claim. A claim is required when the asserted proposition says a condition **caused, contributed to, enabled, triggered, prevented or materially influenced** a defined outcome.

The handoff must bind cause, effect, role where asserted, context/time, material mechanism/transmission assumptions and motivating evidence. Investigation priority, first-deviation position, graph proximity, first post-change run, shared version or remediation outcome never transfers as epistemic status.

After creation, REF-013–REF-020 alone govern causal epistemic evaluation; `confirmed` additionally requires REF-017 plus AUTH-034/Capability Authorization. OPS-061/062 explicitly prohibit Investigation closure, analyst consensus or operational resolution from upgrading a claim.
