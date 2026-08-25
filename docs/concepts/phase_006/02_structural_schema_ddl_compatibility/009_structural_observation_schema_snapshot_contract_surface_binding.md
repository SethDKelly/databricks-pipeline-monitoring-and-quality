# HLTH-009 — Structural Observation, Schema Snapshot & Contract-Surface Binding

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define the structural object being observed or evaluated so that schema health is never inferred from an unbound DDL diff or from whichever metadata source happens to be available.

## Contract

A material structural Observation or compatibility proposition should bind, where applicable:

- producer/output subject and stable identity;
- realized output/data version or current-cycle context;
- schema or interface version when known;
- structural surface being evaluated, such as physical table schema, logical view/interface, export contract, stream/message shape, or other consumer-visible interface;
- field/path identities and nesting context;
- grain/key semantic references where relevant;
- event/effective time and framework knowledge/evaluation time;
- consumer or consumer class when compatibility is consumer-specific;
- applicable structural Expectation/contract version for normative evaluation.

## Invariants

- A schema snapshot is Observation evidence, not a new Schema concept.
- A producer's physical table schema and the schema actually presented to a consumer can differ; compatibility must bind the relevant interface.
- A DDL statement or repository contract describes intended/declared structure unless evidence establishes that it became realized state.
- Unity Catalog/Databricks metadata, Git-managed specifications, generated DDL, DQ rules, or monitoring metadata are evidence/assertion sources, not universal truth owners by technical availability alone.
- Structural observation of one output/version/window does not prove another version or consumer saw the same structure.
- `Schema known` does not mean `schema compatible`.

## Example

A producer table adds `customer_segment`, but a downstream view continues to expose the prior stable projection. The physical table changed; the view-facing consumer contract may remain structurally unchanged. The framework should evaluate the interface actually consumed rather than declaring every downstream consumer broken from the producer-table DDL alone.