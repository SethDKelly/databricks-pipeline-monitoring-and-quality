# Group 04 Source Capability Matrix

Support is **proposition + source set + context** bound. `Conditional` means the source can satisfy the proposition only when the required governance, version, coverage, association or retention contract is present.

| Proposition / capability | Primary evaluated surfaces | Group 04 result | Key boundary / residual gap |
|---|---|---|---|
| Current realized table/column structure | UC Information Schema / table metadata | Supported for visible current state | Principal-filtered; not historical or consumer compatibility |
| Historical structural change | Delta/Iceberg table history + retained versions | Partially supported | Default history/time-travel retention limits; field continuity may remain ambiguous |
| Column rename/recreate continuity | Table history + explicit Entity Identity mapping | Conditional | Name/ordinal equality alone is insufficient |
| Declared constraints | UC/Delta constraint metadata | Supported in documented feature scope | Declaration ≠ observed integrity |
| Empirical PK/FK/unique integrity | DQX/query measurements | Conditional | Informational relationship constraints do not prove data conformance |
| Consumer-specific structural compatibility | Governed consumer/interface contract + realized schema | Conditional | Engine cast/evolution support is not compatibility truth |
| DQX rule definition | DQX rule metadata/config | Supported if DQX deployed | Exact DQX version and stored definition required |
| DQX rule as governed Expectation | DQX definition + Assertion Authority/governance | Conditional | Availability/generated origin gives no authority |
| DQX detailed row issue evidence | DQX output/quarantine issue columns | Supported for exact checked execution | Population/run/input/rule-set coverage must be retained |
| DQX summary metrics | DQX metrics observer/table | Supported when enabled | Exact run/rule/input binding and storage semantics matter |
| DQX generated/profiler rule | DQX profiler/generator | Supported as candidate | Not normative until approved/governed |
| DQX criticality/action | DQX rule/action configuration | Supported in DQX semantics | Not framework severity/waiver/Gate/control by default |
| Lakeflow expectation definition | Pipeline source/config | Supported | Framework authority/version mapping still required |
| Lakeflow warn/drop expectation metrics | Pipeline event log | Supported when emitted | Dataset/operator/config coverage limits apply |
| Lakeflow fail-expectation violation | Pipeline failure/error evidence | Partially supported | Same detailed pass/fail metrics may be absent after fail action |
| Metric View semantic measure definition | UC Metric View YAML | Conditional / strong candidate | YAML spec version ≠ metric-definition revision; authority explicit |
| Metric View query metric Observation | Metric View query result | Supported | Must bind fields/filters/parameters/window/definition/source context |
| Metric View definition history | Current UC definition + external/versioned source if available | Partially supported / Conditional | No universal organizational metric-revision history assumed |
| Metric View materialization freshness | Materialization/Lakeflow state | Partially supported | Optimization refresh schedule ≠ framework freshness SLA |
| Data-profiling descriptive metrics | Profile metrics Delta table | Supported | Observation only; not normativity/health by existence |
| Data-profiling drift | Drift metrics Delta table | Supported | Descriptive comparison; reference comparability still governed |
| Profiling baseline table as reference source | Monitor config + baseline table | Supported as source reference | Framework Baseline membership/authority conditional |
| Profiling custom metric | Monitor config + metric tables | Supported | Definition/provenance/dependency identity required |
| Anomaly-detection commit freshness | DQ monitoring results | Supported as vendor model Assessment | Not explicit SLA or event freshness |
| Anomaly-detection completeness | DQ monitoring results | Supported as vendor model Assessment | Learned expected range ≠ governed Expectation by default |
| Event-time freshness | Current anomaly-detection surface | Unsupported by this source | Separate event-time/ingestion-latency evidence required |
| Vendor table-level health status | `system.data_quality_monitoring.table_results` | Supported in vendor semantics | Not DMTZ composite health without explicit profile composition |
| Vendor root-cause field | DQ monitoring result | Supporting/contextual only | Does not satisfy Causal Claim confirmation |
| Vendor downstream-impact field | DQ monitoring result | Supporting/contextual only | Reachability/query summary ≠ exposure/effect/consequence |
| Framework Baseline membership/version | Governed reference registry + retained observations | Conditional | Vendor baseline/history does not self-authorize membership |
| Window/slice/cohort metric binding | DQX/profiling/Metric View/query predicates | Supported when explicit | Sliced/sample result cannot become whole-population evidence |
| Measurement→specific run/output version | Group 03 run/output evidence + measurement provenance | Conditional | Current/latest table query is insufficient for exact-run proposition |
| Transformation reconciliation | Exact transformation/version + measurements/checks | Conditional | Generic related row counts are not reconciliation |
| Metric-view join/cardinality integrity | Metric View definition + empirical key/cardinality checks | Partially supported | `rely`/declared cardinality is not empirical proof |
| Multi-input current-cycle alignment | Exact consumed-version evidence + HLTH-049 | Unsupported generally / Conditional | Inherits Group 03 generic input-version gap |
| Result freshness / exact-use suitability | Source evaluation/scan/refresh time + evidence timestamps | Conditional | Retrieval time/last dashboard state is insufficient |
| Historical health replay | Retained definitions + results + source state + Baseline membership | Partially supported | Source-specific retention and definition-history gaps |
| Strong `no schema change` | Complete relevant history + source health | Conditional | Retention/visibility gaps prevent strong negative |
| Strong `no failed check` / `no anomaly` | Expected evaluation + complete results/scan coverage | Conditional | Disabled/skipped/failed evaluation is not a clean negative |
| Framework composite health | Explicit HLTH-055 profile over bounded component Assessments | Conditional | No vendor-wide health label is accepted as universal substitute |

## Consolidated Group 04 gaps carried forward

1. **Consumer-specific compatibility is not supplied by structural metadata alone.** Governed interface/consumer contracts remain necessary.
2. **Key/relationship declarations do not universally prove empirical integrity.** Informational PK/FK/unique metadata needs separate observed conformance where health depends on it.
3. **DQX rule authority/versioning is environment/governance dependent.** Generated/profile-derived checks remain proposals until accepted.
4. **Metric View YAML specification version is not metric-definition revision history.** Material semantic revisions need explicit governance/provenance.
5. **Vendor profiling/anomaly baselines are not automatically framework Baselines or Expectations.** Reference membership/comparability/authority remains explicit.
6. **Anomaly detection commit freshness does not provide event-time freshness.** Separate source/event-time evidence is needed where that dimension matters.
7. **Vendor health/root-cause/impact labels remain source-owned assertions.** They cannot bypass DMTZ composite-health, Causal Claim or Impact evidence requirements.
8. **Exact current-cycle/multi-input alignment inherits the Group 03 input-version gap.** Generic workloads need explicit input-version instrumentation where this proposition matters.
9. **Exact measurement→run/output attribution is conditional.** Current/latest state is not enough for a run-specific health claim.
10. **Historical replay is source-specific.** Table history, DQX tables, pipeline event logs, profiling tables and anomaly-monitoring history have different retention/version semantics.
11. **Strong health negatives remain opportunity/coverage bound.** Disabled/skipped/failed scans/checks or missing history cannot become `no issue`.
