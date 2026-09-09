# AUTH-014 — Derived, Inherited, and Propagated Governance Assertions

**Status:** Accepted — Phase 005 Group 02

## Purpose

Prevent governance state from silently propagating across containers, Lineage, schemas, consumers, or derived artifacts merely because a relationship exists.

## Contract

A semantic, responsibility, classification, policy, or criticality assertion produced by inheritance/derivation remains a provenance-bearing assertion whose standing must be explicitly governed.

Examples include:

- domain-to-table or table-to-column inherited classifications;
- repository/domain ownership propagated to pipelines/tables;
- source-to-downstream semantic assumptions inferred through Lineage;
- classification crosswalks;
- derived policy applicability;
- schema- or tag-based inferred governance assertions.

## Invariants

- Lineage does not automatically propagate Semantic Definition, Classification, Responsibility Assignment, Policy Context, criticality, or Assertion Authority.
- Container membership does not automatically transfer governance state.
- A derived assertion identifies its derivation/source basis and does not masquerade as a direct authoritative assertion.
- An automated derivation process may be granted authoritative standing for a bounded target only through an explicit Assertion Authority rule.
- A downstream table does not inherit an upstream business definition, key role, classification, or criticality merely because it consumes that upstream table.
- Schema/DDL inspection may produce technical evidence or advisory assertions, but semantic/policy authority must still be resolved explicitly.
- Crosswalked labels preserve the original source classification and the crosswalk provenance.

## Example

Table B is classified `Restricted`. Table C consumes B. C does not automatically inherit `Restricted` solely through Lineage. An accepted governance/policy rule may require or derive such a classification, but that is an explicit governed assertion with provenance rather than implicit propagation.