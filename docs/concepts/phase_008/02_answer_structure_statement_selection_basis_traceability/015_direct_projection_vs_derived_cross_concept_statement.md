# EXPL-015 — Direct Projection vs Derived Cross-Concept Statement

**Status:** Accepted — Phase 008 Group 02

## Requirement

Classify a material answer statement as either:

1. **direct projection** — communicates a proposition already resolved by one accepted truth owner; or
2. **derived cross-concept statement** — communicates a proposition whose validity depends on an accepted synchronization/refinement rule over multiple source-owned facts.

A derived statement must retain the join/derivation rule and all material source propositions needed for that result.

## Examples

- `Completeness Assessment failed` is a direct projection of Assessment state.
- `Consumer R was not exposed to suspect V because it encountered safe V-1` may be a derived Impact statement only when the accepted encounter/version/path evidence satisfies the relevant OPS/REF rules.
- `The planned deployment caused the failure` is not licensed merely by combining Change Intent, Deployment timing and a failed Assessment; it requires a Causal Claim at the appropriate status.

## Invariants

Multiple true facts placed in one sentence do not automatically create a valid derived proposition. Cross-concept derivation must use accepted semantic composition rules rather than narrative implication.
