# OPS-008 — Topology Completeness, Missing Edges & Restricted Projection

**Status:** Accepted — Phase 007 Group 01

## Purpose

Prevent a partial or authorization-filtered Lineage view from being presented as a complete topology or used to support unjustified negative dependency claims.

## Completeness is bounded

Topology/traversal completeness is evaluated only relative to a defined traversal universe, including where relevant:

- requested relationship families/roles;
- source/target/entity scope;
- field/key/population/consumer granularity;
- event/effective interval and knowledge cut;
- traversal depth/path boundary;
- evidence-source opportunity and coverage;
- identity resolution coverage;
- integration/source availability;
- requester projection/authorization limitations.

There is no global `lineage completeness %` or universal confidence score.

## Traversal coverage results

A traversal may be described as sufficiently covered for the exact bounded question, incomplete, unknown, conflicting or unavailable, with material reasons preserved.

A sufficiently covered result for one family/source/time does not imply complete ecosystem topology.

## Missing-edge claims

`No relationship/path exists` is a negative conclusion and inherits REF-003/REF-004 evidence burdens.

It is valid only when the relevant relationship opportunity/universe was observable and coverage is sufficient for that exact conclusion. Otherwise the framework reports unknown/incomplete rather than treating omitted edges as absent.

## Restricted projections

Capability Authorization/disclosure may hide identities, scopes, paths or evidence. The internal Lineage truth remains separate from what a requester can see.

Where authorized, a projection may expose an opaque node/path or state that additional restricted topology exists. Where even existence is restricted, the visible response must preserve a limitation without indirectly revealing the hidden relationship.

A requester-visible graph with hidden content must not be labeled globally complete merely because all **visible** edges were returned.

## Invariants

- Missing source data ≠ no dependency.
- Authorization-filtered view ≠ complete internal topology.
- Opaque path existence is disclosed only when independently authorized.
- `No upstream relationship found` ≠ `no upstream relationship exists` unless coverage supports the latter.
- Complete direct-edge coverage ≠ complete multi-hop coverage if relevant intermediate universes are not covered.
- Restricted evidence remains restricted rather than absent.

## Handoff

OPS-009 defines the ownership boundary when relationship state changes and hands Group 01's topology semantics into Group 02.