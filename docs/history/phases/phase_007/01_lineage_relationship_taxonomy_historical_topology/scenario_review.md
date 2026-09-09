# Phase 007 Group 01 — Lineage / Historical Topology Scenario Review

**Status:** Accepted — L01-01–L01-18 pass

The scenarios test OPS-001–OPS-009 against normal, ambiguous, conflicting, negative-evidence, restricted and historical cases. Passing means the scenario can be represented without a new concept, hidden source precedence, blind propagation, exposure shortcut, causal shortcut or selected implementation architecture.

## L01-01 — A + B → C with different transformation roles

A contributes projected values to C while B participates only in join/match/filter behavior that determines C's eligible population.

**Pass.** Both are `data_derivation` relationships, but OPS-003 preserves distinct semantic roles/scopes. B need not be falsely described as the source of every C value. No generic row-count/metric propagation is implied.

## L01-02 — Same endpoints, multiple relationships

P both produces table C and has an operational dependency on upstream output B through its logical execution responsibility.

**Pass.** OPS-001 makes relationship family/role part of proposition identity. Production and operational dependency remain separate even if a graph implementation could connect similar nodes.

## L01-03 — Planned new source D

A Change Intent says future C will incorporate D, but the active version still uses only A/B.

**Pass.** D remains planned topology in Change Intent under OPS-004. It does not appear as effective Lineage until sufficient realization evidence exists.

## L01-04 — B1 → B2 migration over time

January C uses B1; after a migration boundary February C uses B2. Current metadata shows only B2.

**Pass.** OPS-004 preserves effective intervals and historical traversal. Current topology cannot overwrite January's B1 relationship.

## L01-05 — Late discovery of an old relationship

In March the framework discovers runtime evidence showing a relationship was effective in January but had not been known then.

**Pass.** Event/effective time and framework knowledge time remain distinct. Retrospective January topology may improve while an as-known-in-January view excludes the March discovery.

## L01-06 — Catalog says no edge; runtime shows dynamic dependency

Catalog metadata omits D→C, while a bounded runtime plan directly shows D participated for one execution.

**Pass.** No catalog-wins or runtime-wins rule exists. Runtime evidence can establish a bounded relation for that execution/version; catalog omission does not establish global absence. Broader effective relationship remains scoped to the evidence.

## L01-07 — Code declares dependency but runtime does not exercise branch

Source/configuration declares an optional B dependency; one run follows a branch that does not use B.

**Pass.** Declared logical/effective topology and specific runtime use are different propositions under OPS-006. The run does not erase the logical relationship; the declaration does not invent actual encounter.

## L01-08 — Conflicting authoritative topology assertions

Two simultaneously authoritative governed sources assert incompatible dependencies for the same relationship target/context/time and no resolver applies.

**Pass.** Assertion Authority conflict remains explicit and Lineage resolution is `conflicting`; majority, recency or ingestion order cannot choose a winner.

## L01-09 — Missing source edge under incomplete coverage

No dependency is found in one metadata source, but that source is known not to observe dynamic queries.

**Pass.** OPS-005/OPS-008 return unknown/incomplete rather than `absent`.

## L01-10 — Proven bounded absence

For a particular interface version, an authoritative and empirically validated exhaustive dependency manifest plus adequate runtime coverage establishes that no direct `data_derivation` relationship from D existed during the interval.

**Pass.** `absent` is supportable for the exact bounded proposition. The conclusion does not generalize to other relationship families, versions or intervals.

## L01-11 — Field-level relevance differs from table reachability

A is upstream of B and B upstream of C, but the questioned `C.customer_status` is evidenced to derive from B fields unrelated to A.

**Pass.** A remains graph-reachable. OPS-003/OPS-007 can mark the exact A→…→C field path not relevant when scope evidence is sufficient, without claiming A is unrelated to all of C.

## L01-12 — Insufficient field detail

Only table-level A→B→C topology is available while a user asks whether A influenced a particular C field.

**Pass.** The path is reachable but field relevance is `indeterminate`. Asset-level Lineage is not silently upgraded to field-level derivation.

## L01-13 — Cross-repository operational dependency

A producer in repository X feeds a dependent pipeline in repository Y.

**Pass.** Repository boundaries remain provenance/context and do not terminate Lineage traversal. Repository membership itself is not promoted to a Lineage relationship family.

## L01-14 — Restricted intermediate node

A requester is allowed to know C has a restricted upstream dependency but not the identity/details of R between A and C.

**Pass.** Authorized projection may show an opaque path if existence disclosure is allowed. The path remains internally bound; hidden detail does not become absent. If existence itself is restricted, the response preserves only an authorized limitation.

## L01-15 — Monitoring Scope stops before upstream dependency

C is monitored; its upstream B is known but out of Monitoring Scope.

**Pass.** The Lineage relationship remains. Scope affects monitoring responsibility, not topology existence. Investigation may later report incomplete evidence beyond the scope boundary without deleting the edge.

## L01-16 — Cyclic/recursive topology

A legitimate bounded recursive/iterative relationship creates a cycle in the graph-shaped topology.

**Pass.** OPS-007 does not assume a DAG. Traversal must be bounded/cycle-safe, while the existence of a cycle is not automatically a defect or causal conclusion.

## L01-17 — Gate configured over a dependency

C has an operational dependency on B and an Execution Gate is later configured to enforce a B-readiness criterion.

**Pass.** The operational dependency can be Lineage. Gate configuration/decision/enforcement remains Execution Gate truth. Disabling the gate does not erase the logical dependency.

## L01-18 — Topology change without registered intent

Runtime/catalog evidence establishes that C now derives from D even though no Change Intent exists.

**Pass.** Effective Lineage can be established from sufficient realized evidence. Missing intent does not block truth. The difference from prior topology is eligible Change evidence for Group 02; it is not automatically improper, unhealthy or causal.

## Cross-scenario result

OPS-001–OPS-009 represent all reviewed cases with:

- five minimum relationship families;
- exact proposition/scope/version/time binding;
- evidence/authority separation;
- no universal Lineage confidence or completeness score;
- positive/negative evidence asymmetry;
- question-bound relevance;
- bounded/cycle-safe traversal;
- non-rewriting historical topology;
- restricted/incomplete traversal without fabricated absence;
- existing concept ownership preserved.

**No 25th concept is required.**