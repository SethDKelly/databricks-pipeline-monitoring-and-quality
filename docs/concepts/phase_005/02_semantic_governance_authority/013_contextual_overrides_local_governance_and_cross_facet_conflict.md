# AUTH-013 — Contextual Overrides, Local Governance, and Cross-Facet Conflict

**Status:** Accepted — Phase 005 Group 02

## Purpose

Define when local/context-specific governance assertions coexist with broader assertions versus when they create a real conflict, without inventing implicit `more specific wins` precedence.

## Contract

A governance assertion may be scoped to environment, tenant, purpose/use, jurisdiction, business context, consumer, semantic facet, classification scheme, responsibility type, or another explicit context dimension.

Two assertions are not conflicting merely because their text/labels differ if they apply to different legitimate contexts or facets. They conflict when they materially disagree for the same bound target/context/time and both have applicable standing.

## Invariants

- Narrower scope does not automatically override broader scope.
- Local override behavior exists only when an accepted authority rule explicitly defines the override/precedence relationship or the assertions apply to distinct contexts.
- Business and technical semantic facets may disagree in wording without being conflict when they answer different questions.
- Different classification schemes do not conflict merely because labels differ.
- Cross-facet inconsistency may be surfaced as a governance-quality/investigation concern, but the framework does not silently rewrite one facet to match another.
- Current local governance does not backfill historical contexts.
- Context omission is not a license to select the most convenient assertion.

## Example

A metric may have a valid internal operational definition and a different external-reporting definition. If both are explicitly context-scoped, they coexist. If two authoritative sources assert incompatible external-reporting definitions for the same period, the result is authoritative assertion conflict.