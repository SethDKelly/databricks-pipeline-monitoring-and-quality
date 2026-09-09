# Group 04 — Source-Specific Acquisition Strategy

## Databricks

### Preferred source hierarchy by use

- account/system tables for bulk/reconciliation and account-wide history where the exact table supports the proposition;
- direct Delta/system-table reads for efficient bounded incremental processing where verified;
- REST APIs for targeted current/source-specific facts, on-demand retrieval and surfaces not available through system tables;
- lineage API/Catalog Explorer history only for the exact use whose source contract requires it;
- workload-owned instrumentation/manifests later for propositions native Databricks sources cannot establish.

### Collection behavior

System tables are treated as delayed publication sources, not real-time event buses. Streaming reads are accelerators and must track backlog/source-version progress. Runtime/version constraints and source-retention gaps remain capability facts.

REST collectors must understand endpoint/workspace/account rate scope and 429 behavior. High-volume collection prefers bounded system-table/query strategies over per-object REST fan-out where semantics permit.

Source schema is treated as evolvable; additive system-table fields must not break fixed parsers.

## GitHub

### Authentication

Prefer a dedicated GitHub App installation for machine acquisition where the target environment supports it, preserving app/installation/repository/organization identities separately.

### Hybrid collection

- webhook delivery for lower-latency events where useful;
- REST reconciliation for missed events, current repository/workflow/deployment state and bounded history;
- conditional ETag/Last-Modified requests where endpoints support them;
- audit/streamed audit sources where enterprise entitlement and proposition require them.

Webhook delivery ID is an idempotency/replay key, not a completeness guarantee. Failed webhooks are not assumed automatically redelivered.

The collector reads rate-limit headers and respects primary/secondary limits and Retry-After/reset guidance.

## Collibra

Collibra remains optional and environment-discovered. The adapter uses stable resource IDs and exact permissions/history surfaces available to the tenant.

Collection cadence is constrained by tenant throttle configuration, license/role permissions and any customer-specific infrastructure settings. API-throttle behavior is operational state, not absence of governance records.

## Immuta

Immuta remains optional and integration/version dependent.

For Databricks Unity Catalog query audit, acquisition respects the configured audit sync frequency and workspace filters. UAM audit export to S3/ADLS can serve as a file/export source where configured, with export batch arrival creating its own availability timing.

Missing audit records are interpreted against integration scope, user/data-source coverage, sync frequency, export state and retention before any negative proposition is considered.

## Future sources

A new source must declare:

- stable source identities;
- surfaces/modes;
- authentication/authorization behavior;
- pagination/window/cursor contract;
- rate limits and retry semantics;
- publication latency;
- retention/history limits;
- schema/version behavior;
- source-specific negative-coverage boundaries;
- operational cost signals;
- optional/required capability behavior.
