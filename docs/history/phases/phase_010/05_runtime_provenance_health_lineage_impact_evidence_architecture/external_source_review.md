# Phase 010 Group 05 — External Source Review

**Verified:** 2026-08-28

Public vendor documentation is architecture input only. Group 01 target-deployment verification remains mandatory.

## Databricks — Jobs / run provenance

Current Jobs API documentation exposes `git_source.git_snapshot.used_commit` on run data for qualifying remote-Git tasks. Databricks also documents that all tasks in a remote-Git job use the same snapshotted commit for the run.

Implications:

- strong run-specific code revision is available for qualifying direct-Git jobs;
- that value does not cover workspace-sourced code or non-code implementation facets;
- bundle/workspace deployments still need DMTZ deployment/content/run attestation where exact Git/content provenance is required.

References:
- https://docs.databricks.com/api/jobs/v2/get-run
- https://docs.databricks.com/aws/en/jobs/git
- https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-types

## Databricks — jobs system tables

`system.lakeflow.job_run_timeline` provides immutable run timeline records after production, including workspace/job/run identity and time slices. Job/task tables provide configuration history with their own retention/availability semantics.

Reference:
- https://docs.databricks.com/gcp/en/admin/system-tables/jobs

## Databricks — table history

Delta/Iceberg table history records write versions, operation timestamps and operation metadata. Databricks cautions that table history/time travel is not a long-term backup contract; default log retention is finite.

Implication: table history can bind output/write versions when correlated exactly, but it is not a generic exact input-version consumption source.

References:
- https://docs.databricks.com/aws/en/tables/history
- https://docs.databricks.com/gcp/en/tables/history-schema

## Databricks — Lineage + query history

`system.access.table_lineage`/`column_lineage` retain read/write lineage events and may provide `statement_id`, which is a foreign key to `system.query.history` for qualifying SQL warehouse statements. Databricks explicitly states lineage tables represent a subset of read/write events because lineage cannot always be inferred.

Implications:

- lineage is strong positive topology/encounter evidence when present;
- missing lineage cannot support universal `no dependency/no encounter`;
- query-history join is mode-specific, not universal;
- lineage does not expose a generic exact consumed Delta version for every read.

References:
- https://docs.databricks.com/aws/en/admin/system-tables/lineage
- https://docs.databricks.com/gcp/en/admin/system-tables/query-history

## Databricks — Lakeflow expectations/event logs

Pipeline event logs include update/flow identity and `flow_progress` metrics. Expectation data can include passed/failed counts and dropped records for the relevant pipeline update/dataset.

Implication: these are valuable run/update-bound quality observations, while rule authority/profile semantics remain organization governed.

References:
- https://docs.databricks.com/gcp/en/ldp/monitor-event-logs
- https://docs.databricks.com/gcp/en/ldp/monitor-event-log-schema

## Databricks — data quality monitoring

`system.data_quality_monitoring.table_results` currently stores freshness/completeness and vendor downstream-impact/RCA fields. The downstream-impact and RCA fields are documented as being deprecated; downstream-impact is based on dependency graph and recent query activity.

Implication: retain vendor status/counts as bounded source Assessments. Do not convert them into DMTZ actual exposure, realized consequence, or confirmed cause.

Reference:
- https://docs.databricks.com/aws/en/admin/system-tables/data-quality-monitoring

## GitHub — deployments

GitHub Deployments are requests to deploy a specific resolved ref/SHA and have stable deployment IDs plus environment/status history. They are strong GitHub-side deployment-process evidence but do not prove Databricks target activation/run without cross-system correlation.

GitHub currently documents finite retention for previous deployment statuses, reinforcing Group 02 product-side provenance where long replay matters.

References:
- https://docs.github.com/en/rest/deployments/deployments
- https://docs.github.com/en/rest/deployments/statuses

## Consolidated conclusion

No evaluated native source generically provides the full chain:

**Git revision → deployment activation → exact run implementation → exact multi-input versions → exact output versions → all health dimensions → complete lineage → external consumer state → realized business consequence**.

Group 05 therefore composes native evidence with selective DMTZ deployment/runtime/consumer attestation, while preserving unsupported/partial propositions explicitly.