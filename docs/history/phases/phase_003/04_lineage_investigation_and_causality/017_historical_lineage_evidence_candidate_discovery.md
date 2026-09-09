# SYN-017 — Investigation Scope + Historical Lineage → Evidence Candidate Discovery

**Status:** Accepted — Phase 003 Group 04

## Outcome

Use the Investigation's subject/question/time window to discover structurally relevant upstream/dependency evidence candidates from the topology that actually applied at the incident time, without treating graph reachability as causal support.

## Participating concepts and actions

- **Investigation** — current scope and `linkEvidence`.
- **Lineage** — `traverseAt`.
- **Entity Identity**, **Monitoring Scope**, **Semantic Definition**, **Classification**, and **Policy Context** — context where relevant/authorized.

## Trigger / initiating condition

An open Investigation needs upstream/dependency candidates for evidence gathering.

## Preconditions

The investigated subject and a sufficiently bounded historical time window are available.

## Coordination semantics

1. Select Lineage relationship families relevant to the question rather than traversing every edge indiscriminately.
2. Traverse the historical topology effective for the Investigation window.
3. Preserve direct edges, transitive paths, relationship type, provenance, inferred/asserted status, and completeness limitations.
4. Treat every traversed entity/path as an **evidence candidate**, not a cause or Causal Claim.
5. Preserve out-of-scope/restricted candidates as opaque boundaries when authorized rather than dropping them.
6. Planned-only topology from Change Intent remains planned context and is not substituted for historical active Lineage.
7. If an upstream node is the earliest monitored location where a related deviation is later found, describe it as first-observed localization, not root cause.

## State and evidence effects

Lineage continues to own topology truth; Investigation may link the relevant path/subgraph as inquiry evidence/context. No causal state is created.

## Ambiguity / failure propagation

Incomplete, conflicting, stale, inferred, restricted, or missing Lineage produces an incomplete candidate set with explicit limitations. Missing topology is never interpreted as no upstream dependency.

## Temporal semantics

Traversal resolves the topology effective during the investigated interval. Current topology cannot overwrite historical candidate discovery.

## Provenance / traceability

Every candidate remains traceable to typed path evidence and the historical Lineage version used.

## Security / authorization

An Investigation may know that an opaque upstream boundary exists without exposing its identity or path details. Traversal never broadens authorization.

## Invariants

- Lineage reachability ≠ cause;
- first observed deviation ≠ root cause;
- current topology ≠ historical topology;
- planned topology ≠ active Lineage;
- out-of-scope ≠ nonexistent;
- incomplete traversal ≠ exhaustive candidate set.

## Scenarios

A+B→C discovers A and B as direct data-derivation candidates. A long-running upstream pipeline is discovered through operational dependency Lineage. A January incident traverses B1 rather than the current B2 path. A restricted upstream dependency remains an opaque evidence boundary.

## Non-goals

Causal ranking, hypothesis confirmation, graph-search implementation, or downstream Impact evaluation.
