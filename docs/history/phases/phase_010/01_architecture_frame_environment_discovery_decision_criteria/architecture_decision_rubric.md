# Phase 010 Group 01 — Architecture Decision / ADR Rubric

## Required record for a major decision

Each material ARCH/ADR selection should include:

1. **Decision proposition** — what exact architecture question is being decided.
2. **Scope** — environments, services, capabilities and use classes affected.
3. **Incoming requirements** — relevant ARCH plus SYN/REF/AUTH/HLTH/OPS/EXPL/INTG contracts and GAP-009 items.
4. **Environment facts** — verified target facts used by the decision.
5. **Public/vendor facts** — dated external facts that constrain options but are not tenant facts.
6. **Assumptions/unknowns** — unresolved facts and why the decision can or cannot proceed.
7. **Hard-constraint evaluation** — explicit pass/fail for applicable constraints.
8. **Alternatives** — at least one meaningful alternative for material/hard-to-reverse selections unless only one technically/contractually feasible option remains and that is evidenced.
9. **Tradeoffs** — decision-specific quality attributes, capability gains/losses, operational/cost/quota/security implications.
10. **Failure/degradation behavior** — what happens when dependencies are absent, delayed, restricted or unhealthy.
11. **Historical/disclosure implications** — where relevant.
12. **Reversibility** — readily reversible / costly / hard to reverse and migration/exit notes.
13. **Verification plan** — how the chosen design will be tested/replayed.
14. **Residual risks/gaps** — what remains unresolved or moves to a later group.
15. **Status/history** — proposed / accepted / superseded / rejected, with decision date and supersession linkage.

## Decision acceptance tests

A decision is not accepted if it:

- relies on an undocumented capability assumption that materially determines feasibility;
- promotes a vendor public default into a tenant fact;
- violates a Phase 002–009 semantic boundary;
- hides capability loss or unsupported propositions;
- treats source outage/permission/quota failure as domain absence;
- cannot explain why its alternatives were rejected;
- uses one aggregate score to conceal material tradeoffs;
- makes a hard-to-reverse technology choice while a decisive environment fact is still unknown and no safe rationale exists.

## Small decisions

Low-impact/reversible implementation choices need not receive a heavyweight ADR. They still must not violate accepted ARCH contracts. Later groups may define thresholds for when an implementation choice becomes architecture-significant.
