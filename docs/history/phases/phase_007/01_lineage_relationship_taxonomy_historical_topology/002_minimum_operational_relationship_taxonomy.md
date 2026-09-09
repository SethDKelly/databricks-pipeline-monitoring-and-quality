# OPS-002 — Minimum Operational Lineage Relationship Taxonomy

**Status:** Accepted — Phase 007 Group 01

## Purpose

Define the smallest useful operational Lineage vocabulary without turning Lineage into a graph-shaped copy of every concept in the framework.

## Accepted minimum families

### `data_derivation`

Source data materially participates in producing or determining target data state under a transformation/definition context.

The relationship may carry semantic roles such as value derivation, join/match participation, filter/selection influence, aggregation, deduplication, union/merge/upsert participation, lookup/reference use, ordering/window behavior or another transformation-specific role.

Those roles describe how the source participates; they do not create generic metric-conservation or causality rules.

### `production`

A logical process/transformation/producer produces or materializes a data asset or output interface.

Production topology does not prove that a particular execution succeeded, that an output existed for a particular cycle, or that the produced state was healthy.

### `operational_dependency`

A downstream logical operation has an operational prerequisite/dependency on an upstream subject/output/service context.

This describes dependency topology. It does **not** establish current readiness, actual run ordering, consumed version, an enabled Execution Gate, or control enforcement.

### `publication`

A data/output state is made available through a named serving/publication surface or interface.

Publication topology describes an available route/surface, not proof that current data was actually published successfully for a particular cycle or encountered by a consumer.

### `consumption_path`

A consumer/use has a configured, declared or empirically established path from a data/publication surface.

This creates a downstream candidate path. It does **not** establish actual encounter, exposure, downstream effect or consequence.

## Deliberate exclusions from the minimum Lineage taxonomy

The following remain context owned by their existing concepts unless a later scenario proves a genuine Lineage relationship is independently required:

- repository membership/ownership;
- Change Intent;
- Deployment provenance and activation;
- realized Change itself;
- execution/run lifecycle state;
- specific run-to-run or version encounter truth;
- Execution Gate configuration/decision/enforcement;
- Propagation Safeguard configuration/enforcement;
- Responsibility Assignment;
- Assertion Authority or Capability Authorization;
- governance/classification/policy inheritance;
- causal contribution;
- entity replacement/succession as a generic Lineage shortcut.

Repository, Deployment, Change, Gate, Safeguard, authority and authorization facts may be synchronized with or used to interpret Lineage, but they are not converted into Lineage edges merely because a graph could represent them.

## Taxonomy extensibility

This is a minimum functional taxonomy, not a permanently closed enum. A later relationship family may be added only when a concrete scenario has materially different purpose, invariants and truth ownership that cannot be represented through one of these families plus OPS-003 scope/role.

Do not add a family merely because a source system exposes a different edge label.

## Invariants

- Relationship family is semantic, not vendor/source-specific.
- `data_derivation` does not imply health/status propagation.
- `operational_dependency` does not imply active control.
- `publication` does not imply current successful delivery.
- `consumption_path` does not imply encounter/exposure.
- Repository/deployment proximity does not become Lineage by convenience.
- The taxonomy does not select a graph model, schema or ingestion source.

## Handoff

OPS-003 supplies field/key/population/consumer/version scope so these families do not over-generalize whole-asset relationships.