# Phase 010 Group 04 — External Source Acquisition Review

**Verified:** 2026-08-28

These are current public vendor facts used as architecture inputs. They do not establish that a particular enterprise deployment has the documented feature, entitlement, runtime version, permission or limit.

## Databricks

Databricks documents system tables as non-real-time: data is updated throughout the day and recent events may not yet appear. System-table schemas can gain new columns/struct fields, and queries may require selective predicates. Databricks also documents streaming system-table constraints: DBR 16.4+ for streaming, 17.3+ for CDF, 18.0+ for native `Trigger.AvailableNow`, `skipChangeCommits=true`, and risk of stream failure when lag exceeds the underlying default 7-day VACUUM horizon.

Databricks REST rate limits are endpoint/workspace scoped and excess requests return 429. Current AWS resource-limit documentation lists explicit limits for selected surfaces, including table/column lineage hourly/daily limits and Jobs API endpoint limits. Generic adapter code therefore must discover/encode the exact endpoint envelope rather than assume one REST requests-per-second value.

Architecture consequence: system tables are preferred bulk/reconciliation sources where propositionally sufficient; streams/API calls are targeted accelerators; lag, runtime/version, schema drift, selectivity and quota are integration-health inputs.

References:
- https://docs.databricks.com/aws/en/admin/system-tables
- https://docs.databricks.com/aws/en/resources/limits
- https://docs.databricks.com/api/workspace/
- https://docs.databricks.com/api/workspace/errors

## GitHub

GitHub REST primary rate limits depend on authentication mode; GitHub App installation tokens have installation-scoped budgets and Enterprise Cloud installations receive higher primary limits. GitHub also applies secondary limits. Rate-limit headers and Retry-After/reset guidance are available, and GitHub recommends conditional ETag/Last-Modified requests; qualifying authenticated `304 Not Modified` responses do not consume primary rate limit.

GitHub webhooks can fail, GitHub does not automatically redeliver failed deliveries, and documented redelivery is limited to deliveries from the past three days. GitHub recommends tracking `X-GitHub-Delivery` and recovering missed/failed deliveries.

Architecture consequence: use webhooks for freshness plus REST reconciliation/conditional polling for repair/completeness; never treat webhook silence as no-event evidence.

References:
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api
- https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
- https://docs.github.com/en/webhooks/using-webhooks/handling-failed-webhook-deliveries
- https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/redelivering-webhooks

## Collibra

Current Collibra configuration documentation exposes API throttling controls and currently states a default throttling limit of 100 API requests/second for the documented service setting, with tenant/configuration behavior remaining material.

Architecture consequence: the adapter cannot bake the public default in as a tenant fact. It records discovered throttle/license/role/deployment conditions and treats throttling as integration health.

Reference:
- https://productresources.collibra.com/docs/collibra/latest/Content/Console/Infrastructure/DGCService/Configuration/ref_environment-settings.htm

## Immuta

Current Immuta 2026.1 documentation for Databricks Unity Catalog integration says query audit is enabled by default when configured and lets the operator restrict ingestion to workspace IDs and configure the audit sync schedule from 1 to 24 hours. Current SaaS documentation supports periodic UAM audit export to S3 or ADLS with configured intervals; those exports form separate arrival/availability events. Databricks Spark audit coverage can depend on Immuta-registered data sources/users.

Architecture consequence: Immuta audit ingestion latency and coverage are integration configuration facts, not universal source behavior. Export availability, integration scope and retention must be preserved in the acquisition manifest.

References:
- https://documentation.immuta.com/2026.1/configuration/integrations/databricks/databricks-unity-catalog/how-to-guides/configure
- https://documentation.immuta.com/SaaS/governance/detect-your-data/audit/reference-guides/query-audit-logs/databricks
- https://documentation.immuta.com/SaaS/governance/detect-your-data/audit/how-to-guides/export-adls

## Consolidated result

The vendor set validates a hybrid, source-specific acquisition architecture. No one collection mechanism is universally real-time, complete, unthrottled, immutable, indefinitely retained or deployment-independent.
