# External Source Review — Phase 009 Group 04

**Verified:** 2026-08-25

This review records current public source facts used by Group 04. It does not substitute for environment-specific discovery of enabled features, versions, permissions, schedules, retention settings or deployed DQX configuration.

## Unity Catalog / table structure / Delta history

- [Information schema](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-information-schema) — privilege-aware current catalog metadata. Results are automatically filtered to objects the querying principal can access.
- [Schema evolution](https://docs.databricks.com/aws/en/data-engineering/schema-evolution) and [Update table schemas](https://docs.databricks.com/gcp/en/tables/update-schema) — Databricks supports additive, rename/reorder and type-evolution operations under documented conditions; engine support does not define consumer compatibility.
- [Constraints on Databricks](https://docs.databricks.com/aws/en/tables/constraints) and Information Schema constraint relations — NOT NULL/CHECK are enforced integrity constraints; primary/foreign-key relationship constraints are informational, and feature/runtime status for unique constraints must be recorded where used.
- [Work with table history](https://docs.databricks.com/aws/en/tables/history) — table versions and operation history support bounded structural/data replay; `logRetentionDuration` defaults to 30 days while default data-file retention for time travel is 7 days unless extended.
- [Table history schema](https://docs.databricks.com/gcp/en/tables/history-schema) — history can expose operation, timestamp, job/notebook/cluster provenance, `readVersion`, operation metrics and optional user metadata.

## Databricks Labs DQX

- [DQX documentation](https://databrickslabs.github.io/dqx/) — optional Databricks Labs Spark data-quality framework with row/dataset rules, profiling/rule generation, summary metrics, actions and monitoring surfaces.
- [Applying Quality Checks](https://databrickslabs.github.io/dqx/docs/guide/quality_checks_apply/) — row/dataset checks can emit detailed warning/error issue columns and save checked/quarantine outputs.
- [DQX User Guide](https://databrickslabs.github.io/dqx/docs/guide/) — summary metrics can include input/error/warning/valid counts and custom metrics and can be stored in Delta tables across runs.
- [DQX releases](https://github.com/databrickslabs/dqx/releases) — the public release page showed v0.15.0 as latest when this review was performed; production semantics must pin/test an exact deployed version rather than assuming latest behavior.
- [AI-assisted quality-check generation](https://databrickslabs.github.io/dqx/docs/guide/ai_assisted_quality_checks_generation/) — profiler/AI-assisted generation can create rule candidates from observed statistics and business context; generated rules remain governance candidates rather than authoritative framework Expectations by origin.

## Lakeflow pipeline expectations / event logs

- [Manage data quality with pipeline expectations](https://docs.databricks.com/aws/en/ldp/expectations) — named SQL Boolean expectations support warn, drop and fail-update behavior on supported pipeline datasets.
- The same documentation states tracking metrics are available for warn/drop expectations but fail-update expectations do not record the same tracking metrics after violation-induced failure; some flow/query forms may also lack metrics.
- [Pipeline event log schema](https://docs.databricks.com/aws/en/ldp/monitor-event-log-schema) — structured event records include stable/evolving maturity classification, update/flow identifiers and data-quality objects.
- [Pipeline event log](https://docs.databricks.com/gcp/en/ldp/monitor-event-logs) — expectation metrics include passed/failed/dropped record counts when emitted.
- [Monitor pipelines in the UI](https://docs.databricks.com/aws/en/ldp/monitoring-ui) — the UI retains 60 days of update history; older updates can remain in the event log, so UI-history and event-log-history capability differ.

## Unity Catalog Metric Views

- [Metric Views](https://docs.databricks.com/aws/en/uc-semantics/metric-views) and [Model metric views](https://docs.databricks.com/aws/en/uc-semantics/metric-views/basic-modeling) — centralized semantic definitions for sources, fields/dimensions, measures, joins and filters.
- [Metric-view YAML reference](https://docs.databricks.com/aws/en/uc-semantics/metric-views/yaml-reference) — YAML `version` is the specification version, not an organization-assigned revision number for the metric definition.
- [Feature availability](https://docs.databricks.com/aws/en/uc-semantics/metric-views/feature-availability) — metric-view behavior is runtime/YAML-version dependent; newer join/materialization/parameter features require later runtimes.
- [Materialization](https://docs.databricks.com/aws/en/uc-semantics/metric-views/materialization) — optional precomputation uses managed materialized views/Lakeflow and has policy/feature limitations; refresh configuration is not automatically a framework freshness SLA.
- Metric-view join documentation warns that some cardinality/rely assumptions are not validated at runtime and incorrect assumptions can produce incorrect measures; declared relationship semantics are therefore not empirical key-integrity evidence.

## Databricks data profiling

- [Data profiling](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling) — computes descriptive metrics for Delta tables across snapshot/time-series/inference configurations, with configurable windows/slices/custom metrics and optional baseline table.
- [Data profiling metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output) — writes profile and drift metrics as queryable Delta tables; metrics carry window/slice/column context.
- [Custom metrics](https://docs.databricks.com/gcp/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/custom-metrics) — aggregate, derived and drift custom metrics have different source-dependency semantics.
- A configured baseline table is used to compute drift; the product documentation describes expected-quality use cases, but framework Baseline membership/comparability/authority remains governed by HLTH-019–029 rather than inherited from configuration alone.

## Databricks anomaly detection / data-quality monitoring

- [Anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/) — Public Preview; learns commit-timing patterns for freshness and recent row-count patterns for completeness, with intelligent scanning and feature-specific preview/beta detail.
- Current anomaly-detection documentation states event freshness based on event-time/ingestion latency is not supported in the current version.
- [Data-quality monitoring results system table](https://docs.databricks.com/aws/en/admin/system-tables/data-quality-monitoring) — Public Preview `system.data_quality_monitoring.table_results` stores freshness/completeness results and table-level status; system-table documentation currently lists indefinite retention for this table.
- [Review anomaly detection results](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/results) — results can include vendor `root_cause_analysis` and downstream-impact fields. These retain their Databricks semantics and are not automatically DMTZ Causal Claim or Impact truth.
- Intelligent scanning can delay evaluation/population for skipped tables, so an absent/recently missing scan is not evidence that no quality issue exists.

## Environment-specific unknowns retained

- exact Unity Catalog/Databricks Runtime and SQL warehouse versions used for schema/constraint/Metric View features;
- exact DQX release, installation mode, rule storage, result storage, schedules, action configuration and retention;
- whether Lakeflow expectations are used and which datasets/operators emit complete quality metrics;
- whether data profiling or anomaly detection is enabled, and for which schemas/tables;
- profiling/anomaly scan schedules and intelligent-scan behavior for the target environment;
- authoritative location/versioning of framework Expectations, metric profiles, Baselines, warning/severity/waiver policy and composite-health profiles;
- whether Metric View definitions are governed/versioned outside current Unity Catalog state;
- retention policies for DQX result tables, profiling metric tables and pipeline event logs;
- what explicit measurement→run/output-version association will be emitted where current/latest table state is insufficient;
- what explicit input-version instrumentation is available for current-cycle/reconciliation propositions affected by the Group 03 multi-input gap.

These remain `unknown / not yet verified`, conditional or partial support rather than assumptions.
