# SYN-028 — Propagation Safeguard + Impact → Prevented Exposure / Operational Consequence

**Status:** Accepted — Phase 003 Group 05

## Outcome

Represent when an enforced safeguard prevented a reachable downstream consumer from encountering suspect state, while separately preserving any operational delay/non-delivery effect created by the safeguard.

## Participating concepts and actions

- **Propagation Safeguard** — `resolveAt` and active/enforcement evidence.
- **Impact** — `evaluateExposure`, `linkDownstreamEffect`, `recordConsequence`.
- **Execution History** and **Observation** — publication, refresh, delivery, and timing facts.
- **Assessment** — downstream delivery/readiness health where relevant.
- **Causal Claim** — owns any proposition that the safeguard caused/contributed to an operational consequence.
- **Capability Authorization** — controls safeguard/impact disclosure.

## Trigger / initiating condition

A safeguard was proposed/active near a downstream consumption boundary and Impact analysis needs to determine whether exposure was prevented and what operational effects followed.

## Preconditions

The relevant safeguard boundary/scope, candidate consumer, affected state/time window, and enforcement evidence are sufficiently identified.

## Coordination semantics

1. Resolve safeguard state for the relevant boundary/time.
2. A merely proposed safeguard cannot establish prevented exposure.
3. If sufficient enforcement plus consumer/consumption coverage establishes that the affected state could not cross the protected boundary, Impact may record `not exposed` with safeguard enforcement as the basis and Explanation may describe `prevented exposure` where authorized.
4. If enforcement is unknown or partial, exposure remains unknown/partial rather than assumed prevented.
5. If the consumer received a prior stale version while the current version was blocked, reason separately about that consumed state; `current suspect version blocked` does not imply healthy/fresh delivery.
6. Observe/assess any delay, missed refresh, publication hold, or delivery non-occurrence independently.
7. If asserting that safeguard enforcement caused or contributed to the delay/non-delivery, create/evaluate a Causal Claim; Impact alone does not make that attribution.
8. Safeguard effectiveness does not prove the protected data was defective, and release does not prove health.

## State and evidence effects

Safeguard owns control state. Impact owns exposure/effect/consequence state. Execution/Observation/Assessment own runtime facts. Causal Claim owns attribution.

## Ambiguity / failure propagation

Proposed-but-unconfirmed enforcement, partial consumer coverage, alternate delivery routes, restricted controls, or missing refresh evidence leave prevented exposure unresolved. Do not claim `protected` merely from the existence of a safeguard record.

## Temporal semantics

Safeguard effective interval, consumption window, and delivery effect are resolved independently with event/knowledge time. Later enforcement evidence can revise retrospective exposure while preserving earlier uncertainty.

## Provenance / traceability

Prevented-exposure statements link to active safeguard scope/enforcement evidence and negative consumption coverage. Operational-effect statements link to their own runtime evidence.

## Security / authorization

Safeguard scope/control details can be sensitive. An audience may see `delivery intentionally held by an authorized protection` without learning the control mechanism or restricted consumer identity.

## Invariants

- proposed safeguard ≠ enforced safeguard;
- enforced safeguard ≠ data defect proof;
- blocked suspect version ≠ fresh/healthy delivery;
- prevented exposure requires enforcement + negative-consumption coverage;
- safeguard-induced effect ≠ causal attribution unless Causal Claim supports it;
- release ≠ health proof.

## Scenarios

**Prevented client exposure:** active enforced hold blocks C's suspect version before Report R refreshes; R is reachable but not exposed to that version.

**Stale fallback:** current C output is held, but R continues showing an older state; suspect-version exposure is prevented while freshness can still fail.

**Safeguard delay:** protection prevents suspect consumption but separately causes a delivery-latency violation; both truths remain visible.

## Non-goals

Safeguard authority definition, enforcement implementation, causal confirmation, rollback, or treating protection as a health verdict.

## Deferred questions

Minimum enforcement evidence needed to claim prevented exposure across representative consumer/publication patterns.