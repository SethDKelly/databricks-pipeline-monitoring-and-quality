# Group 05 Source Capability Matrix

Support is **proposition + source set + context** bound. `Conditional` means the required identity/version/path/coverage/retention or external instrumentation must be present.

| Proposition / capability | Primary evaluated surfaces | Group 05 result | Key boundary / residual gap |
|---|---|---|---|
| Captured table read/write lineage event | `system.access.table_lineage` | Supported when captured | Source explicitly represents only a subset of read/write events |
| Captured column lineage | `system.access.column_lineage` | Supported when inferred | UDF/path/other limitations; no-source column events omitted |
| Effective logical relationship interval | Lineage events + governed topology/config/history | Conditional | Event occurrence ≠ continuous dependency |
| Direct vs intermediate dependency | lineage `direct_access` | Supported in source semantics | Not semantic relevance/exposure strength |
| Databricks consumer entity context | lineage `entity_metadata` | Supported when populated | Source-local identity; null for some JDBC/other events |
| Historical lineage ≤ 1 year | lineage system tables | Supported within capture/retention | Rolling window and capture limitations |
| Historical lineage beyond 1 year | Catalog Explorer / lineage API after 2024-09-01 | Partially supported | Different detail/programmatic surface; no pre-cut data |
| Rename continuity | native lineage + Entity Identity mapping | Unsupported natively / Conditional | Lineage not preserved across renames |
| Path→table relationship | lineage path + explicit mapping | Conditional | Path read does not automatically identify UC table |
| Strong `no lineage` / `no dependency` | complete capture + identity/history coverage | Conditional / generally weak | Numerous documented capture limitations |
| Availability/publication | table/view/materialization/dashboard/application state | Conditional | Lineage/run success alone insufficient |
| SQL statement execution | `system.query.history` | Supported for covered SQL warehouse/serverless scope | Public Preview; 365-day system-table horizon; compute scope boundaries |
| Query actor / execution principal | query history | Supported | Principal identity still reconciled through Group 02 |
| Query client application | query history `client_application` | Supported as contextual field | Client-provided/derived; not stable report/user identity |
| Query source entity | query history `query_source` | Supported for Databricks entities | External source entity may not be represented |
| Statement→source-read association | lineage `statement_id` + query history | Supported for qualifying SQL-warehouse events | Only when lineage captured and statement ID populated |
| Query result cache origin | query history cache fields | Supported | Cached result encounter ≠ fresh source read |
| Exact table/data version read | generic lineage + query history | Unsupported generally / Conditional | No universal table-version field |
| Explicit time-travel/version read | retained statement/params + table history | Conditional | Truncation/encryption/dynamic resolution/history expiry can block proof |
| Databricks job/task source encounter | lineage entity metadata + Group 03 run identity | Conditional / strong | Exact data version still separate |
| Dashboard query execution | dashboard audit `executeQuery` + statement | Supported where audit retained | Execution ≠ view/result receipt |
| Dashboard query-result receipt | dashboard audit `getQueryResult` + statement | Supported where retained | Result receipt ≠ exact version without state binding |
| Dashboard view/access | audit `getDashboard` / `getPublishedDashboard` | Supported | Definition/view access ≠ dataset execution/exposure |
| Dashboard cached-state encounter | dashboard audit + cache/query evidence | Partially supported / Conditional | Cache can be up to 24h old; exact cache-state version not universally attested |
| Scheduled dashboard refresh | dashboard schedule/query/audit evidence | Conditional | Configured schedule ≠ execution; refresh ≠ later human view |
| Dashboard snapshot delivery | audit snapshot/send events | Supported for documented delivery event | Delivery ≠ reading/reliance |
| External BI SQL read | query history + lineage + client application | Supported for covered Databricks query | Does not prove external report view |
| External BI report view/use | Tableau/Power BI/etc telemetry | Unknown/environment-specific | Databricks alone does not establish it |
| JDBC/ODBC/application read | query history/lineage where covered | Supported at platform-read layer | App processing/display remains external |
| Refresh/materialization encounter | refresh execution + source read/version | Conditional | Refresh success alone ≠ version consumption |
| Safe prior-state/cache encounter | cache/snapshot/version evidence | Conditional | Can coexist with freshness violation |
| Positive object-level encounter | read/query/result evidence | Supported when covered | Does not automatically identify suspect version |
| Positive suspect-state exposure | encounter + state/version binding | Conditional | Exact version gap is material |
| Strong `not exposed` | all material opportunities/paths/versions + healthy coverage | Conditional | One safe path or missing telemetry insufficient |
| Multi-hop exposure | per-hop state propagation + downstream encounter | Conditional | Lineage transitivity insufficient |
| Downstream technical effect | Group 04/operational evidence bound downstream | Conditional | Exposure and effect remain independent |
| Downstream analytical effect | report/model/output comparison evidence | Conditional | Platform query alone may not prove analytical change |
| Business/process/customer consequence | business/app/decision/ticket/financial evidence | Unknown/environment-specific / Conditional | Generally outside Databricks-native evidence |
| Dashboard view → decision reliance | dashboard audit + business evidence | Unsupported by Databricks alone | View/delivery ≠ reliance |
| Table popularity/insights | Catalog Insights/popularity | Supported as recent usage context | 30-day aggregate/context, not version exposure or Impact |
| Vendor downstream-impact labels | anomaly-monitoring result | Supporting/contextual only | Not realized Impact/causal truth |
| Historical exposure replay | lineage + query + audit + external source histories | Partially supported | Retention/coverage differ per source |
| Strong `no effect` / `no consequence` | complete dimension/business coverage | Conditional / generally difficult | Missing monitored evidence is not unchanged/no consequence |

## Consolidated Group 05 gaps carried forward

1. **Unity Catalog lineage is not complete enough for universal negative topology/use claims.** Missing records cannot become no dependency/no use.
2. **Rename continuity requires explicit Entity Identity reconciliation.** Native lineage does not universally bridge renamed objects/columns.
3. **Generic exact table-version consumption remains unsupported out of the evaluated lineage/query-history pair.** Version-bound exposure needs explicit state evidence.
4. **Dashboard cache state is only partially reconstructable.** A view can use a 24-hour cache without a new SQL execution; exact cached data version may require added attestation.
5. **External BI report views and user interactions are outside Databricks query evidence.** Platform reads can be observed without proving report display/reliance.
6. **Application fetch/display/business use requires application/business telemetry where material.** JDBC/query execution is only one boundary.
7. **Multi-hop exposure requires per-hop state evidence.** Effective Lineage alone cannot propagate exposure transitively.
8. **Business consequence evidence is environment-specific.** No evaluated Databricks-native surface universally establishes decision/customer/financial consequence.
9. **Historical Impact replay is heterogeneous.** Lineage, query history, audit, dashboard/cache and external systems have different retention/coverage semantics.
10. **Strong non-exposure/no-effect/no-consequence conclusions remain expensive.** They require explicit path/population/version/dimension coverage rather than missing telemetry.
