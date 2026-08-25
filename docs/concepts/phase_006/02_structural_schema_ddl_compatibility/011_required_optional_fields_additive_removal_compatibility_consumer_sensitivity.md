# HLTH-011 — Required/Optional Fields, Additive/Removal Compatibility & Consumer Sensitivity

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define how field presence and absence interact with structural Expectations without treating `additive` as universally safe or `removed` as universally breaking.

## Contract

Structural Expectations may distinguish, by consumer/context:

- required fields;
- optional fields;
- conditionally required fields;
- prohibited/unrecognized fields where a closed contract applies;
- additive changes allowed, disallowed, or allowed only within explicit extension points;
- removal/deprecation rules and effective transition windows;
- order-sensitive versus name/path-sensitive interfaces.

## Invariants

- Adding an optional field can be compatible for a name-based Spark consumer while incompatible for a positional export, fixed external schema, signature/hash contract, or consumer that rejects unknown fields.
- Removing a field is incompatible only for consumers/contracts that require or materially depend on that field; an unused optional field may be safely removed for one consumer while breaking another.
- Presence of a required field does not prove semantic validity, type compatibility, non-nullness, uniqueness, or business correctness.
- Absence of a prohibited field does not prove the rest of the schema is compatible.
- Required/optional status is normative Expectation state governed under AUTH-019, not inferred merely from whether producers historically populated a field.
- Deprecation or a planned removal window does not prove all consumers migrated before realization.

## Example

Producer P adds `marketing_opt_in`. Consumer C reads named fields and ignores unknown columns: the addition may be compatible. Consumer E emits a positional CSV contract whose exact column order/count is fixed: the same producer change may be incompatible for E.