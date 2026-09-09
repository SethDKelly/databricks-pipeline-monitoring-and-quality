# OPS-003 — Relationship Scope, Granularity & Semantic Role

**Status:** Accepted — Phase 007 Group 01

## Purpose

Prevent an established Lineage relationship from being treated as relevant to every field, key, population, consumer or version of its endpoint entities.

## Contract

A relationship may be bound at the narrowest meaningful supported scope, including where applicable:

- whole entity/interface;
- semantic field/column or field set;
- key/identifier role;
- measure/business metric input;
- partition/cohort/population/subpopulation;
- producer/transformation definition and version;
- target interface/schema version;
- consumer/use/path;
- environment/context;
- other explicit semantic role needed to interpret the relationship.

Source scope and target scope are independently bound. A relationship can therefore state, for example, that `B.customer_id` participates in the join determining a subset of `C`, while another field in B has no demonstrated relationship to the questioned C field.

## Granularity rules

- Whole-asset relationship evidence does not automatically establish field-level derivation.
- Field-level evidence does not automatically establish that the entire source asset is relevant to every target property.
- A table-level consumption path does not prove that every column was selected or exposed.
- A relationship established for one transformation/interface version does not automatically apply to another.
- Population/filter semantics can make a source relevant only to a bounded target population.
- Consumer-specific interfaces/contracts can make the same producer relevant differently to different consumers.

## Operational relevance preparation

Relationship scope is stored/interpreted as relationship truth. **Operational relevance** is evaluated later under OPS-007 for a specific question/traversal.

If material scope needed to judge relevance is missing, the framework must preserve that limitation. It may return the relationship as potentially reachable while marking relevance indeterminate rather than broadening the edge to the entire entity.

## Column-level Lineage boundary

Phase 007 accepts **column/field-capable semantics** but does not require that every integration provide complete column-level Lineage.

Concrete source support, extraction cost and MVP coverage belong to Phase 009/Phase 011. Missing column-level evidence cannot be repaired by pretending an asset-level edge proves field-level derivation.

## Invariants

- Asset reachability ≠ field relevance.
- Field derivation ≠ whole-asset derivation.
- Population influence ≠ universal row/value influence.
- Same endpoint pair ≠ same relationship scope across versions.
- Semantic role is not a causal role.
- Scope restrictions do not imply the unmentioned portion is independent unless sufficient evidence establishes that negative claim.

## Handoff

OPS-007 uses these bindings to decide whether individual edges and multi-hop paths are operationally relevant to a defined question.