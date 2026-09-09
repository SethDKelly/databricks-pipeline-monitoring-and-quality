# HLTH-018 — Structural Compatibility Proposition, Evidence & Result Semantics

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define what it means to conclude that a realized or proposed structure is compatible with a bounded structural contract without turning missing evidence into compatibility or treating one changed field as the whole schema result.

## Compatibility proposition

A material proposition should bind:

- producer/output/interface and structural version/state;
- consumer or consumer class;
- applicable structural contract/Expectation version;
- transition direction where relevant;
- evaluation time/knowledge cut;
- required structural predicates and material conditions.

## Functional result semantics

For a bounded structural compatibility proposition:

- **compatible** — sufficient applicable evidence shows every required structural predicate/condition in scope is satisfied;
- **incompatible** — sufficient applicable evidence shows at least one required structural predicate is violated;
- **unknown / unresolved** — material required structure, identity, consumer contract, or condition cannot be resolved sufficiently;
- **conflicting** — applicable evidence or governing structural assertions conflict and no accepted resolution applies;
- **unavailable** — required evidence cannot currently be obtained/evaluated;
- **not applicable** — the structural contract/check does not apply to the bound subject/consumer/context.

## Invariants

- `No detected schema diff` is compatible only if the observation mechanism and comparison coverage are sufficient for the exact contract proposition.
- Missing catalog/DDL/contract evidence is not `compatible`.
- One compatible field transition does not prove the entire interface compatible when other required predicates are unevaluated.
- One incompatible required predicate can justify the bounded compatibility result `incompatible`; it does not establish downstream execution failure, Impact, exposure, or causality.
- A waiver/exception can affect later normative response/presentation but does not rewrite an observed structural incompatibility into compatible; Group 04 owns waiver/Assessment composition.
- Compatibility conclusions retain the evidence/contract versions used so later correction or newly discovered consumers can revise current understanding without rewriting the historical result.
- `Compatible` does not mean business data values are healthy; structural compatibility is one health dimension.

## Example

A consumer requires fields A/B/C with B as `DECIMAL(18,2)`. Realized B is `STRING`. If the contract does not allow that representation, the structural proposition is incompatible even if the job succeeded and B values happen to parse successfully in sampled data.