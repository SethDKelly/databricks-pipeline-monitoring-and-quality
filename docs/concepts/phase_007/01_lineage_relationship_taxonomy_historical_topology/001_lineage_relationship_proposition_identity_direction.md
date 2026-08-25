# OPS-001 — Lineage Relationship Proposition Identity & Direction

**Status:** Accepted — Phase 007 Group 01

## Purpose

Prevent a Lineage edge from becoming an ambiguous connection whose meaning changes depending on the traversal or consumer.

## Contract

Every material Lineage relationship proposition must bind, where applicable:

- source **Entity Identity**;
- target **Entity Identity**;
- one explicit relationship family from OPS-002;
- source and target semantic scope under OPS-003;
- relationship role/meaning within that family;
- environment/context when the relationship is context-specific;
- transformation, interface, logical-process or other definition/version when material to the relationship meaning;
- effective/valid interval under OPS-004;
- provenance/evidence basis under OPS-005;
- recorded/knowledge time where historical reconstruction matters.

The proposition is the bounded claim that **this relationship family and role connected this source scope to this target scope in this context during this effective interval**.

## Direction

Relationship direction follows downstream functional flow:

- source data → derived target data;
- producer/process → produced data/interface;
- prerequisite → dependent logical operation;
- data/output → publication surface;
- publication/data surface → consumer/use.

An upstream traversal walks against that direction. A downstream traversal walks with it. Traversal orientation never reverses the underlying relationship meaning.

## Relationship identity

Source + target alone is not relationship identity. The same endpoints may legitimately have several simultaneous relationships with different families, roles, scopes, consumers or versions.

Material change to relationship meaning, scope or version must be represented through explicit version/supersession/history semantics rather than silently mutating an old edge into a different proposition.

## Invariants

- A generic untyped `A → C` edge is insufficient for serious reasoning.
- Name equality, repository path equality or nearby deployment timing does not establish endpoint identity or relationship identity.
- Directness/path length is not part of relationship truth and is not a causal ranking.
- Relationship direction does not mean causal direction.
- Relationship existence does not establish that a particular execution or consumer actually encountered a particular data version.
- Capability Authorization may redact relationship detail from a requester, but internal relationship identity remains sufficiently bound.

## Handoff

OPS-002 defines the minimum relationship families. OPS-003 defines the semantic granularity needed to decide whether a bound relationship is relevant to a later operational question.