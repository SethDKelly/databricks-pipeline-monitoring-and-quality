# SYN-001 — Entity Identity + Monitoring Scope Resolution

**Status:** Accepted — Phase 003 Group 01

## Outcome

Allow any later reasoning chain to know **which logical entity a reference denotes** and **whether monitoring responsibility covered that entity at the relevant time** without treating scope as identity, existence, evidence availability, or authorization.

## Participating concepts and actions

- **Entity Identity** — `recognize` (and, upstream of this synchronization, provenance-bearing establish/associate/separate behavior).
- **Monitoring Scope** — `resolveAt`.

## Trigger / initiating condition

A later concept or scenario needs subject-specific reasoning from a source reference and relevant time/context.

## Preconditions

- a source-specific reference/context is available to Entity Identity;
- the caller supplies the relevant time when historical resolution matters.

## Coordination semantics

1. Resolve the reference using `Entity Identity.recognize` for the relevant context/time.
2. If the result is one identified Entity Identity, pass that identity—not the raw source name—to `Monitoring Scope.resolveAt`.
3. Preserve the two results separately: identity resolution and scope disposition.
4. If identity is ambiguous/unknown/conflicting, do not guess an entity in order to obtain scope.
5. If identity is known but scope is excluded/unknown/conflicting, retain the known identity and the scope boundary rather than treating the entity as nonexistent.

This ordering is semantic, not a requirement for synchronous API calls or a transaction.

## State and evidence effects

Entity Identity owns identity/equivalence history. Monitoring Scope owns scope assertions/history. The synchronization owns no new canonical entity/scope state; it provides a traceable paired resolution to downstream reasoning.

## Ambiguity / failure propagation

- ambiguous identity → subject-specific scope remains unresolved;
- unknown identity → no guessed scope assertion;
- known identity + unknown scope → known entity with unknown monitoring responsibility;
- known identity + excluded scope → known contextual entity outside monitoring responsibility;
- conflicting scope → preserve conflict;
- unauthorized identity detail → an opaque identity may participate only where source/security policy allows;
- unavailable source evidence does not become `excluded`.

## Temporal semantics

Identity-reference validity and Monitoring Scope effective time resolve at the requested event/effective time. Recorded/knowledge time remains available for later historical replay when a mapping/scope assertion was learned or corrected later.

## Provenance / traceability

A downstream user must be able to trace why a source reference mapped to an Entity Identity and which scope assertion(s) produced the relevant disposition, subject to authorized disclosure.

## Security / authorization

Monitoring Scope never grants access. An opaque/restricted identity may be sufficient to say that monitoring coverage stops at a boundary without exposing the restricted name/reference.

## Invariants

- raw name equality does not bypass Entity Identity;
- scope never creates identity;
- identity never implies inclusion;
- inclusion never implies evidence availability;
- exclusion never erases known Lineage/context;
- authorization is not inferred from scope;
- repository membership does not propagate scope.

## Scenarios

**Known boundary:** C is included; A is identified but excluded. Later RCA may state that upstream monitoring coverage is incomplete at A.

**Historical onboarding:** A is excluded in January and included February 1. A January replay resolves excluded.

**Ambiguous alias:** a reference could mean prod or dev. No scope result is guessed from either candidate.

## Non-goals

Discovery/onboarding implementation, authorization decisions, Observation collection policy, Lineage traversal, service/API sequencing.

## Deferred questions

Exact MVP entity kinds independently scopeable and authority/source-precedence rules for scope assertions.
