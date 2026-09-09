# HLTH-010 — Structural Change Taxonomy, Field Identity, Add/Drop/Rename & Reordering

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define structural-change categories without equating name-level differences with semantic identity changes or compatibility outcomes.

## Structural change categories

A realized or planned schema transition may include, independently:

- field/column addition;
- field/column removal;
- field/path rename;
- field reorder;
- movement within a nested path;
- type change;
- precision/scale change;
- nullability change;
- default/generated-value rule change;
- key/identifier-role or grain change;
- nested-structure shape change;
- interface/contract version change.

## Identity rules

- **rename ≠ drop + add by coincidence.** A rename assertion requires sufficient identity evidence from Entity Identity, Semantic Definition, Change Intent, explicit migration mapping, or equivalent provenance.
- Same field name does not guarantee same semantic identity if meaning/population/grain changes.
- Different field names can represent one continued semantic identity when an explicit supported rename/mapping exists.
- Field order is a structural property only where the relevant consumer contract is order-sensitive; name-based consumers may legitimately treat reorder as non-material.
- Case changes, aliases, nested-path movement, or generated projections require consumer/interface semantics rather than universal compatibility rules.
- A schema diff can contain several simultaneous structural changes; do not collapse them into one generic `schema changed` fact.

## Compatibility separation

Structural classification says **what changed**. It does not itself say whether the change is compatible, healthy, planned, or causally responsible for downstream behavior.

## Example

`customer_id` disappears and `customer_identifier` appears. Without a governed mapping or other identity evidence, the safe structural description is one removal plus one addition, not an inferred rename.