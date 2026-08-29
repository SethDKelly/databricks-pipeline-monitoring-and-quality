# Input / Output Attestation Model

## Goal

Provide exact run/task/query-specific data-state bindings where the underlying platform can prove them, while preserving unknown when it cannot.

## `input_consumption`

Representative fields:

- execution/task/query ID
- canonical/source input entity ID
- source type
- exact version/generation/digest/offset range where known
- read/access mode
- logical cycle/window
- native versus instrumented evidence class
- evidence/acquisition IDs
- completeness limitation

## `output_production`

Representative fields:

- execution/task/query ID
- canonical/source output entity ID
- exact produced version/generation/digest where known
- write/transaction/operation identity
- output window/cycle
- source/attestation basis
- acquisition/coverage state

## Exactness tiers

- **native_exact** — source explicitly binds execution to exact version/state.
- **attested_exact** — approved workload/runtime attestation binds execution to exact state.
- **bounded_partial** — source establishes read/write relationship but exact version is missing.
- **unknown** — evidence is insufficient or unavailable.

These are support classes, not confidence scores.

## Delta/Iceberg

Table history is strong write/version evidence. Exact consumed input version remains separate and requires qualifying runtime/query instrumentation or source evidence.

## Streaming

Exactness can be expressed as offset/version ranges, checkpoint state and watermarks when the source/runtime exposes them. `Subscribed to topic/table` is not `consumed all events through X`.

## Current-cycle alignment

A current-cycle result is valid only when each required input/output/measurement is bound to the same governed cycle/window rule. Latest state from mixed cycles remains misaligned/unknown.
