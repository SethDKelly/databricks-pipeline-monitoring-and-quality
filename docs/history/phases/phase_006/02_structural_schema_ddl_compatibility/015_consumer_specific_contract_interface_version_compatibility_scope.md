# HLTH-015 — Consumer-Specific Contract, Interface Version & Compatibility Scope

**Status:** Accepted — Phase 006 Group 02

## Purpose

Make structural compatibility explicitly consumer- and interface-relative so the framework does not collapse a producer schema transition into one ecosystem-wide `compatible` or `breaking` label.

## Contract

A structural compatibility proposition should identify, where material:

- producer/output/interface being consumed;
- consumer or bounded consumer class;
- consumer interaction mode, such as name-based read, positional export, typed application contract, SQL/view projection, stream/message reader, Metric View, or downstream transformation;
- applicable contract/schema version;
- accepted compatibility direction and transition window;
- required structural facets and tolerated extension behavior;
- relevant deployment/current-cycle/effective time.

## Invariants

- Compatibility is not necessarily transitive across consumers or interfaces.
- Producer P compatible with intermediate interface V does not prove downstream consumer C is compatible with P's physical schema.
- A stable view or projection can preserve compatibility for a consumer even when the backing table changes.
- Conversely, unchanged producer schema can still become incompatible if a consumer contract/version changes.
- `Backward compatible` and `forward compatible` must be bound to a declared transition direction and consumer contract; they are not universal labels.
- An interface version bump does not itself prove compatibility or incompatibility; the actual contract relationship must be evaluated.
- Consumers with materially different structural expectations require separate compatibility conclusions rather than one global status.
- Lineage identifies candidate consumers but does not prove which contract/version was actually used at the relevant time.

## Example

A new nullable field is backward compatible with Consumer C's name-based Spark read, but not forward compatible with an older strict Avro reader that rejects unknown fields. Both conclusions can be simultaneously correct.