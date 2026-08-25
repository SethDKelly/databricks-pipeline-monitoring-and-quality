# HLTH-013 — Nullability, Defaults, Generated Values & Population-Presence Compatibility

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define structural compatibility for value-presence rules that can change independently from field existence or data type.

## Contract

Compatibility evaluation may distinguish:

- nullable versus non-nullable structural declaration;
- applicable normative non-null requirements;
- default-value behavior for newly absent producer input;
- generated/computed-field behavior;
- whether a consumer expects explicit producer values versus accepts generated/default values;
- transition behavior for historical versus newly written records where material.

## Invariants

- `NOT NULL` → nullable can be structurally breaking for a consumer that requires guaranteed presence even if current data happens to contain no nulls.
- nullable → `NOT NULL` can be incompatible with producer/write behavior or historical records even if it improves a consumer-facing guarantee.
- A default does not prove semantically meaningful completeness; `0`, empty string, sentinel or generated values may satisfy physical presence while violating business validity/completeness Expectations.
- Default/generated-value changes can materially alter downstream business semantics even when field type and nullability remain unchanged.
- Observed zero nulls do not convert a nullable declaration into a non-null structural guarantee.
- Declared non-nullness does not prove runtime data is non-null unless the platform/control actually enforces it and relevant evidence confirms realized state.
- Structural compatibility and completeness Assessment remain related but distinct: this group defines the contract transition; Group 04 later defines normative Assessment interaction.

## Example

A field changes from required producer-supplied `country_code` to nullable with default `UNKNOWN`. The schema may remain technically consumable, but a downstream business contract that requires an actual country code can be structurally/semantically incompatible even while physical null rate stays at zero.