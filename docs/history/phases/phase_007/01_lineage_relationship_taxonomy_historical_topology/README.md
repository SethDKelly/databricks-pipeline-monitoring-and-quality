# Phase 007 Group 01 — Lineage Relationship Taxonomy, Historical Topology & Operational Relevance

**Status:** Review complete — accepted

## Goal

Define the operational Lineage vocabulary and evidence needed to reason about historical topology without turning topology into metric/status propagation, exposure, causality or a graph-shaped copy of every other concept.

## Group result

Group 01 retains **Lineage** as the existing truth owner and accepts **OPS-001–OPS-009**. No new concept is required.

The major refinement is that a Lineage relationship is a **bounded proposition**, not merely an edge between two entities. Its family, role, semantic scope, context/version, effective interval and evidence basis are all material to interpretation.

The preliminary Phase 002 `evidence quality/confidence` wording is refined by Phase 004 evidence semantics: Lineage now uses proposition-specific applicability, provenance, opportunity/coverage, corroboration/conflict and conclusion-specific sufficiency. **No universal Lineage confidence or completeness score is accepted.**

## Accepted OPS contracts

1. [`OPS-001 — Lineage Relationship Proposition Identity & Direction`](001_lineage_relationship_proposition_identity_direction.md)
2. [`OPS-002 — Minimum Operational Lineage Relationship Taxonomy`](002_minimum_operational_relationship_taxonomy.md)
3. [`OPS-003 — Relationship Scope, Granularity & Semantic Role`](003_relationship_scope_granularity_semantic_role.md)
4. [`OPS-004 — Effective Topology, Historical Time & Relationship Lifecycle`](004_effective_historical_topology_time_state.md)
5. [`OPS-005 — Relationship Evidence, Existence/Absence & Coverage`](005_relationship_evidence_existence_absence_coverage.md)
6. [`OPS-006 — Assertion Authority, Source Disagreement & Empirical Separation`](006_assertion_authority_source_disagreement_empirical_separation.md)
7. [`OPS-007 — Traversal Profile, Operational Relevance & Path Composition`](007_traversal_profile_operational_relevance_path_composition.md)
8. [`OPS-008 — Topology Completeness, Missing Edges & Restricted Projection`](008_topology_completeness_missing_edges_restricted_projection.md)
9. [`OPS-009 — Topology Transition, Cross-Concept Ownership & Group 02 Handoff`](009_topology_transition_cross_concept_ownership_handoff.md)

## Minimum operational relationship taxonomy

Group 01 accepts five minimum semantic families:

| Family | Meaning | Explicitly does not prove |
| --- | --- | --- |
| `data_derivation` | source data participates in determining target data state | health/status propagation, cause |
| `production` | logical process/transformation produces/materializes an output/interface | run success, output existence/currentness, health |
| `operational_dependency` | downstream logical operation has an upstream prerequisite/dependency | actual wait/order/consumption, readiness, enabled gate |
| `publication` | output/data is made available through a serving/publication surface | successful current-cycle delivery or encounter |
| `consumption_path` | consumer/use has a configured/established route from an output/interface | actual encounter, exposure, effect or consequence |

Transformation-specific roles such as join/match, filter/selection, aggregation, dedupe, union/merge/upsert and value/reference participation qualify `data_derivation`; they do not become universal propagation formulas.

Repository membership, deployment provenance, Change state, execution state, gate/safeguard state, authority/authorization and causality remain owned elsewhere rather than becoming generic Lineage families.

## Relationship resolution vocabulary

For one exact relationship-existence proposition, Group 01 accepts:

- `established`;
- `absent` only with adequate opportunity and coverage;
- `unknown`;
- `conflicting`;
- `unavailable`.

A restricted requester projection is an authorization/disclosure limitation over internal truth, not another relationship truth state.

## Operational relevance

Graph reachability is not enough for operational reasoning.

A traversal is bound to direction, permitted relationship families, event/effective time, historical knowledge cut where needed, semantic field/key/population/consumer/version context and authorization. An effective relationship/path is `relevant`, `not relevant` or `indeterminate` **for that bounded question**.

There is no global edge relevance score. Directness, shortest path and repository proximity do not imply causal importance.

Multi-hop relevance requires semantic scope to compose across intermediate edges. Missing field/population detail yields indeterminate relevance rather than whole-asset over-generalization.

## Historical topology

Preserve:

**planned topology (Change Intent) ≠ effective Lineage topology ≠ specific execution/consumer encounter ≠ historical as-known topology ≠ current retrospective topology**.

Relationship effective/event time and framework knowledge time remain distinct. Later evidence can improve retrospective topology without rewriting what was known earlier.

## Source disagreement and authority

Code, catalog, runtime, human and platform sources do not have a universal precedence hierarchy. Assertion Authority applies when a governed relationship assertion needs standing; empirical evidence sufficiency remains separate.

An authoritative declaration can still be wrong or stale, and a strong runtime observation can establish a bounded fact without gaining authority to redefine all future logical topology.

Concrete source mappings remain Phase 009 work.

## Completeness and negative evidence

Topology completeness is bounded to an explicit relationship universe, scope, time/cut, depth and evidence/authorization coverage. No global `complete graph` or numeric completeness score is accepted.

`No edge found` is not `edge absent`. Negative relationship/path conclusions require opportunity-to-observe and sufficient bounded coverage under REF-001–REF-005.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **L01-01–L01-18**, including:

- multi-role A+B→C derivation;
- planned versus effective source changes;
- historical B1/B2 migration;
- late topology discovery;
- code/catalog/runtime disagreement;
- bounded absence versus incomplete evidence;
- field-level versus asset-level relevance;
- cross-repository dependency;
- restricted/opaque paths;
- Monitoring Scope boundaries;
- cyclic topology;
- gate/dependency separation;
- unregistered realized topology change.

## Durable boundaries

- Lineage ≠ causality.
- Lineage relation ≠ metric/status/governance propagation.
- Reachable ≠ operationally relevant ≠ exposed/affected.
- Planned topology ≠ effective topology.
- Current topology ≠ historical topology.
- Declared relationship ≠ specific runtime encounter.
- Missing edge evidence ≠ absent edge.
- Assertion Authority ≠ evidence sufficiency.
- Operational dependency ≠ Execution Gate state/enforcement.
- Consumption path ≠ exposure.
- Relationship transition ≠ realized Change truth or causal attribution.

## Architecture boundary

Group 01 does not select graph storage/query language, Unity Catalog Lineage APIs, Spark/query-plan extraction, GitHub dependency parsing, event storage, path algorithms, cache/streaming topology or source authority assignments.

The functional model is graph-compatible and column/field-capable without selecting how either is implemented.

## Group exit gate

**Satisfied.** OPS-001–OPS-009 and L01-01–L01-18 establish a minimum operational taxonomy, exact relationship proposition identity, semantic scope, bitemporal topology, evidence/authority discipline, question-bound traversal relevance, bounded completeness and cross-concept ownership without a 25th concept.

**Next: Phase 007 Group 02 — Change Intent, Deployment Realization & Realized Change.**