# AUTH-019 — Structural / Schema Compatibility Expectation Authority

**Status:** Accepted — Phase 005 Group 03

## Purpose

Govern who may establish or revise normative structural/schema compatibility rules for an asset or consumer without conflating governed schema meaning with required compatibility or realized production structure.

## Contract

Structural Expectation authority can cover, where applicable:

- required versus optional columns/fields;
- allowed or prohibited additions/removals;
- accepted type compatibility, precision/scale, nested-shape, nullability/default/generated-value conditions;
- key/identifier and grain requirements;
- schema-contract/version compatibility;
- consumer-specific compatibility requirements;
- rules for a planned schema transition and its effective activation boundary.

## Invariants

- Technical schema-definition authority (AUTH-009) does not automatically grant structural Expectation authority.
- A repository schema file, CI rule, Unity Catalog state, or DQ rule syntax does not become authoritative merely because it encodes a check.
- Realized schema state requires Observation/Change evidence; an authoritative structural Expectation does not prove production conformance.
- Compatibility can be consumer/context specific. An additive column may be acceptable for one consumer and prohibited for another.
- A declared key role is semantic state; an Expectation can require key uniqueness/non-nullness, but actual satisfaction remains Assessment evidence.
- Column rename compatibility requires an explicitly governed semantic/identity relationship where needed; drop/add name coincidence is insufficient.
- Planned schema intent can prompt prospective Expectation revision but cannot self-authorize it.
- A structural Expectation used for active control still requires separate high-consequence control-use approval and later control authority/evidence.

## Example

A governed technical schema may declare a new optional field. A report/export authority may nevertheless maintain a consumer-specific Expectation forbidding additive columns until its positional contract is revised.