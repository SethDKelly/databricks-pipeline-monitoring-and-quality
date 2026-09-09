# OPS-005 — Relationship Evidence, Existence/Absence & Coverage

**Status:** Accepted — Phase 007 Group 01

## Purpose

Apply Phase 004 evidence discipline to Lineage so topology does not depend on a generic edge-confidence score or convert missing metadata into non-existence.

## Supersession of earlier shorthand

The Phase 002 Lineage concept used `evidence quality/confidence` as preliminary language for inferred relationships. Under REF-001–REF-005, that shorthand is refined and superseded by explicit:

- evidence applicability;
- provenance/basis;
- opportunity to observe;
- bounded coverage;
- corroboration/common derivation/conflict;
- conclusion-specific sufficiency.

Phase 007 accepts **no universal Lineage confidence, trust or completeness score**.

## Evidence bases

Material relationship evidence retains its provenance and basis, such as:

- source/actor assertion;
- direct runtime/catalog/query observation;
- reproducible derived/inferred relationship;
- correction/supersession evidence;
- other evidence whose applicability can be evaluated.

These basis classes are not a universal ranking. A source assertion can be authoritative for a declared logical dependency while a bounded runtime observation may be stronger evidence for what a particular execution actually did; they may answer different propositions.

## Relationship resolution states

For a **bounded relationship-existence proposition**, the framework may resolve:

- `established` — applicable evidence is sufficient to support that the relationship existed/applied;
- `absent` — applicable evidence with adequate opportunity and coverage is sufficient to support that the relationship did not exist/apply for the exact bounded proposition;
- `unknown` — evidence is materially insufficient to establish either existence or absence;
- `conflicting` — applicable evidence/assertions materially disagree and remain unresolved;
- `unavailable` — required evidence needed for resolution cannot currently be obtained/processed.

`Restricted` is a disclosure/authorization qualifier on what a requester may see, not a replacement internal relationship truth state.

## Positive and negative asymmetry

One qualifying observation can sometimes establish a positive relationship for a bounded execution/version/context. The reverse conclusion—`no such relationship existed`—usually requires a mechanism capable of observing the relevant relationship universe plus sufficient coverage for that interval/scope.

Examples:

- absence of a catalog edge does not prove no dynamic runtime dependency existed;
- no code-search match does not prove a dependency was absent if generated/dynamic SQL is possible;
- one runtime query plan can establish a relationship for that query without proving it applies to all versions/runs;
- an explicitly complete bounded dependency manifest may support absence for the exact manifest-defined proposition, but not unrelated runtime relationship families.

## Invariants

- Missing edge evidence ≠ absent edge.
- Source outage/query failure ≠ empty topology.
- Source count ≠ independent corroboration.
- Mirrored copies of one lineage assertion do not become multiple evidence sources.
- Evidence sufficient for one relationship family/scope/version ≠ sufficient for every related proposition.
- `established` relationship ≠ causal support, exposure or health propagation.

## Handoff

OPS-006 applies Assertion Authority where relationship assertions have governed standing. OPS-008 uses coverage to qualify traversal completeness and missing-edge claims.