# External Source Review — Phase 009 Group 05

**Verified:** 2026-08-25

This review records current public source facts used by Group 05. It does not substitute for environment-specific discovery of enabled system tables, permissions, BI/application telemetry, retention extensions or dashboard configuration.

## Unity Catalog lineage

- [Lineage system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/lineage) — `system.access.table_lineage` and `system.access.column_lineage` expose captured read/write lineage. Databricks explicitly states these tables are a subset of all read/write events and records are emitted only when lineage can be inferred.
- The table-lineage schema exposes source/target table/path/type, actor, event time, `record_id`, `event_id`, entity metadata and `direct_access`.
- For SQL-warehouse events, lineage `statement_id` is a foreign key to `system.query.history`.
- Entity metadata can identify jobs/job runs, dashboards, notebooks, SQL queries, pipelines/updates, Genie spaces and alerts. Null entity metadata can accompany JDBC/sample-data or other events.
- Lineage system tables retain a rolling one-year window. Catalog Explorer/lineage API indefinitely retain captured lineage after 2024-09-01, subject to documented capture limitations.
- [Unity Catalog lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) documents limitations including missing pre-2024-09-01 history, incomplete/absent links for some `runs submit`/spark-submit patterns, rename continuity not preserved, RDD/checkpoint limitations, incomplete PRIVATE-pipeline lineage, path/UDF column-lineage limitations and transaction lineage persisting even when a transaction is rolled back.
- Lineage visibility is permission-aware; workspace object details can also be masked across workspaces.

## Query history

- [Query history system table](https://docs.databricks.com/aws/en/admin/system-tables/query-history) — Public Preview `system.query.history` records covered SQL warehouse and serverless-compute notebook/job statements account-wide within the region.
- The schema exposes `statement_id`, execution status/timing, `executed_by`, `executed_as`, statement text, client application/driver, read/produced row/file/byte metrics, result-cache fields, parameters and `query_source`.
- `query_source` can identify dashboard, SQL query, Genie, notebook and job/job-run/task-run context for Databricks entities. Values are not an execution-order list.
- `client_application` may identify applications such as Tableau and Power BI but is derived from client-provided information and is contextual rather than a stable consumer identity.
- `from_result_cache` and `cache_origin_statement_id` expose query-result-cache use/origin. Cached receipt is not a fresh source read.
- System-table reference currently lists a 365-day free retention horizon for query history. Exact accessible history and any retained copies remain environment-specific.

## AI/BI dashboard usage and caching

- [Monitor dashboard usage](https://docs.databricks.com/gcp/en/dashboards/monitor-usage) demonstrates audit-log use for `getDashboard` and `getPublishedDashboard` view/access events, including per-user counts.
- [Audit log reference](https://docs.databricks.com/gcp/en/admin/account-settings/audit-logs) documents dashboard events including `executeQuery`, `getQueryResult`, `triggerDashboardSnapshot` and `sendDashboardSnapshot`, with dashboard/statement/recipient context where applicable.
- `getPublishedDashboard` means a user accessed the published dashboard by UI or requested its definition using the API; it is therefore not identical to a proven human visual encounter with every dataset/widget.
- [Dataset optimization and caching](https://docs.databricks.com/aws/en/dashboards/caching) documents a best-effort 24-hour dashboard cache. Underlying data changes do not automatically invalidate it; cached results can be served without starting the SQL warehouse or running a new query.
- For multi-page dashboards, published-dashboard opening runs/caches only datasets supporting the active page. Scheduled refreshes run all dataset SQL and populate cache.
- [Scheduled dashboard updates and subscriptions](https://docs.databricks.com/aws/en/dashboards/share/schedule-subscribe) documents scheduled refresh and email/Slack/Teams snapshot delivery. Delivery remains distinct from human reading/business reliance.

## Insights / popularity

- [View table insights and popularity](https://docs.databricks.com/aws/en/discover/table-insights) provides recent usage trends, frequent queries/users/dashboards/notebooks and table/column popularity.
- The frequent-query portion is limited to Databricks SQL and is permission-aware; frequent sections can be workspace-scoped while the usage graph is metastore-scoped.
- Popularity is based on recent query activity (30-day context) and is useful prioritization/context evidence, not version-bound exposure or realized Impact.

## Environment-specific unknowns retained

- which lineage/query/audit system tables are enabled and readable by the monitoring service;
- whether lineage API/Catalog Explorer long-horizon data can be programmatically retained with sufficient detail for the required historical questions;
- which workloads use unsupported lineage patterns or storage-path access;
- whether exact table/data versions read are emitted through workload-specific metadata, query parameters, custom tags or explicit manifests;
- dashboard publication model, shared-vs-individual data permissions, schedules, cache behavior and retained audit coverage in the target environment;
- Tableau/Power BI/other external-BI workspace telemetry for report views, extracts, refreshes and user interactions;
- application/API fetch/processing/display telemetry and exact source-state bindings;
- business-process, decision, customer, ticket, incident and financial systems required for consequence evidence;
- extended retention/copying of query history, lineage system tables and audit logs;
- disclosure/authorization rules for user query text, query parameters, dashboard viewers and downstream consumer identities.

These remain `unknown / not yet verified`, conditional or partial support rather than assumptions.
