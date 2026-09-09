# Group 08 — Cost Attribution Architecture

## Principle

Cost must be observable enough to optimize the product without making cost an invisible evidence-quality policy.

## Attribution dimensions

Where measurable, attribute cost/usage by tenant/deployment, source/integration, service class, component/workload, storage tier and material Investigation/replay/control context.

## Categories

- source/API/query acquisition;
- normalization/reconciliation processing;
- canonical/derived serving compute;
- graph/reasoning/replay work;
- hot/warm/cold/pinned storage and restore;
- search/vector indexing/query;
- model/token/invocation;
- active-control adapters/services;
- network transfer/egress where material.

## Policy boundary

Budgets/alerts can trigger explicit policy such as slower optional enrichment, archival tiering, model disablement or manual review. They may not silently reduce required Monitoring Scope, skip required reconciliation, weaken evidence sufficiency or reuse stale control decisions.

Cost telemetry is operational accounting, not automatically business/customer Impact.