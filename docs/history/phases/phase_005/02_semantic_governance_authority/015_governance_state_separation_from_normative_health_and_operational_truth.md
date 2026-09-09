# AUTH-015 — Governance State Separation from Normative Health and Operational Truth

**Status:** Accepted — Phase 005 Group 02

## Purpose

Keep descriptive/governance authority from becoming schema-health, data-quality, access, impact, or control truth.

## Required separations

- authoritative Semantic Definition ≠ observed physical state;
- authoritative schema declaration ≠ normative schema Expectation;
- authoritative schema Expectation ≠ evidence the realized schema conforms;
- authoritative key/grain meaning ≠ observed uniqueness/cardinality integrity;
- criticality Classification ≠ actual Impact/consequence;
- Policy Context ≠ Capability Authorization/enforcement/compliance;
- Responsibility Assignment ≠ Assertion Authority/Capability Authorization;
- descriptive governance conflict ≠ data-health failure unless a relevant Expectation/Assessment establishes one.

## Schema/DDL validation rule

A structural validation should be expressible as:

1. resolve the governed semantic/schema meaning required to interpret the subject;
2. resolve the applicable normative structural Expectation/compatibility rule;
3. observe the realized schema/change with sufficient evidence;
4. assess conformance/compatibility;
5. use Lineage/Impact/Investigation to reason about downstream consequences where needed.

This sequence does not prescribe where the validation runs.

## Invariants

- Git/CI validation of proposed DDL does not prove production schema state.
- Unity Catalog/Databricks schema metadata does not automatically prove a Git/source contract was intended or business semantics are correct.
- A monitoring application can independently evaluate realized schema without becoming authoritative for the underlying business definition unless explicitly granted that standing.
- Schema change can legitimately trigger Baseline/metric-profile/comparability review without automatically declaring all prior Baselines or metrics invalid.
- A schema-compatible change can still cause data-quality or business-semantic degradation, and a schema-breaking change can be caught before any data load occurs.

## Example

A source renames `customer_id` to `customer_identifier`. CI may flag the proposed contract change before deployment; runtime metadata later establishes the actual rename; Semantic Definition/Change Intent may establish whether it is a semantic rename versus drop/add; Expectations determine downstream compatibility; Lineage/Impact identify consumers at risk.