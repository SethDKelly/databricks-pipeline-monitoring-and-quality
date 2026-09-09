# HLTH-012 — Type, Precision, Scale, Casting & Nested-Shape Compatibility

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define type/shape compatibility as a semantic consumer contract rather than a universal widening/narrowing lookup table.

## Contract

Type compatibility evaluation may need to bind:

- source and target logical/physical type;
- precision/scale, length, signedness or equivalent bounded representation where meaningful;
- scalar versus collection/struct/map/nested shape;
- element/key/value/nested-field types and required paths;
- consumer conversion/casting semantics where explicitly part of the contract;
- overflow, truncation, precision-loss, parse, timezone/encoding, or representation risks where relevant;
- applicable consumer/interface version and structural Expectation.

## Invariants

- `wider type` is not universally compatible; consumer semantics decide whether the transition preserves accepted values and meaning.
- `narrower type` is not automatically incompatible if the applicable contract and observed population establish safe representability, but absence of observed overflow alone does not rewrite the normative contract.
- Decimal precision/scale changes can be independently material even when the broad type remains decimal.
- String length/format, timestamp timezone semantics, numeric representation and nested-shape changes can be structurally significant even when a platform can technically cast them.
- Implicit/runtime cast capability is evidence about technical computability, not proof of governed compatibility.
- Adding a nested optional field can be safe for tolerant consumers and breaking for strict schema readers.
- Removing or changing a nested field is evaluated at its exact path rather than only the top-level struct name.
- Compatibility of one transition direction does not imply compatibility in reverse.

## Example

`DECIMAL(18,2)` → `DECIMAL(22,4)` may be acceptable for a consumer designed for higher precision, but incompatible with an external fixed-width contract. A Spark engine's ability to cast the value does not settle that consumer-specific compatibility proposition.