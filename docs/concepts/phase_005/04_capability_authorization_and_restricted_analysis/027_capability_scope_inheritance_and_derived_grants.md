# AUTH-027 — Capability Scope, Inheritance, and Derived Grants

**Status:** Accepted — Phase 005 Group 04

## Purpose

Prevent subject/container/Lineage relationships from silently propagating capability authorization.

## Contract

Any inherited or derived capability should identify the source authorization, relationship used, target subject set, capability, context, conditions, effective interval, and accepted inheritance rule.

## Invariants

- Domain, catalog, schema, table, pipeline, repository, job, consumer, or Lineage containment does not automatically propagate authorization.
- Permission on an upstream asset does not imply permission on downstream assets, and vice versa.
- Permission to view a parent/domain does not automatically grant child raw-data or metric visibility.
- Permission to inspect one node in Lineage does not grant the full path.
- Derived/inherited grants retain provenance and can be independently revoked/superseded according to the governing rule.
- Unknown or ambiguous subject identity blocks silent inheritance.
- Scope expansion requires an explicit accepted rule; convenience is not inheritance semantics.
