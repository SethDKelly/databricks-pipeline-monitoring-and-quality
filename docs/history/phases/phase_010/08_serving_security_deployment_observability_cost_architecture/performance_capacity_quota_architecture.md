# Group 08 — Performance, Capacity & Quota Architecture

## Capacity model

Capacity is planned across source acquisition volume, canonical writes, retained history, concurrent exact queries, graph/replay work, optional model calls, control opportunities and archive restore bursts.

## Priority and isolation

SC-06 and required near-current operational work receive explicit priority. Heavy replay/model/index work can be queued/deferred. Reconciliation cannot be starved indefinitely because its coverage is required for strong negatives.

## Backpressure

Use bounded concurrency/queues and explicit deferred/unavailable states. Optional enrichment is shed before required evidence/control behavior.

## Source quota ledger

Rate/quota state is first-class operational telemetry. Acquisition records request volume, throttling, Retry-After/reset/secondary-limit information where exposed and allocates source budget by plan/service class.

## Databricks

Prefer deployment-verified bulk/system-table/reconciliation surfaces and selective incremental/on-demand API calls over naive object-by-object polling. Endpoint-specific limits and source publication lag remain environment facts.

## GitHub

Use installation/repository scoping, webhooks/incremental collection plus reconciliation, selective/conditional requests and observed rate-limit guidance. Webhook silence never proves completeness.

## Exhaustion

Quota exhaustion degrades freshness/coverage for affected propositions; it never becomes a negative domain fact.