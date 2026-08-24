# Phase 006 Group 01 — Scenario Review

All scenarios are synthetic. They test whether HLTH-001–HLTH-008 provide enough common measurement semantics before later schema/Baseline/threshold/propagation work.

| ID | Scenario | Required interpretation | Result |
|---|---|---|---|
| H01-01 | Table C reports `row_count = 12M` with no output/window/version binding | Value is ambiguous evidence until HLTH-001 binding is established | **PASS** |
| H01-02 | `customer_null_rate = 2%` changes denominator from all rows to active rows but keeps the same display name | Material definition revision/version; historical continuity cannot be assumed | **PASS** |
| H01-03 | Platform can compute p50/p95/p99 for opaque UUID identifiers | Distribution metric is semantically `not applicable`; availability does not justify computation | **PASS** |
| H01-04 | Distinct count for an account identifier is meaningful for diagnostics but not routine monitoring | `applicable + diagnostic/on-demand`; not profile-selected for routine use | **PASS** |
| H01-05 | Critical customer identifier has governed null-rate and uniqueness checks | Fits critical-field/business role; actual metric observations remain separate from Assessments | **PASS** |
| H01-06 | New table contains 180 columns | New columns do not automatically receive every available column statistic; anti-bloat selection remains explicit | **PASS** |
| H01-07 | RCA temporarily calculates category-share distributions on three fields | Diagnostic observations can support Investigation without becoming permanent profile membership | **PASS** |
| H01-08 | Same `row_count` metric is measured before and after grain changes from account to account-day | Metric binding/definition context changes; Group 03 later decides comparability | **PASS** |
| H01-09 | Profile-selected null-rate metric cannot be obtained because its telemetry source is down | `applicable + selected + supported + unavailable`; never zero/pass | **PASS** |
| H01-10 | Metric definition requires a source capability the platform cannot provide | `unsupported` is distinct from temporary `unavailable` | **PASS** |
| H01-11 | Metric is applicable but intentionally omitted from routine profile | `applicable + not selected`; absence of evaluation is not healthy/not-applicable | **PASS** |
| H01-12 | Row count is observed but no Expectation or Baseline comparison is configured | Descriptive Observation only; no normative/comparative pass/fail | **PASS** |
| H01-13 | Structural extractor observes `column customer_id exists = true` | Observation can be true while later schema-compatibility Assessment still fails on type/nullability/key contract | **PASS** |
| H01-14 | DQX and a monitoring index both expose the same underlying null-rate calculation | Provenance identifies common derivation; duplicate surfaces do not create independent evidence | **PASS** |
| H01-15 | Approximate distinct count is used with declared approximation semantics | Valid metric Observation with approximation provenance; later threshold/comparability use must account for it | **PASS** |
| H01-16 | Restricted row data is used by an authorized monitoring principal to compute a safe completeness Assessment | Internal Observation can retain restricted provenance while requester disclosure remains Phase 005 governed | **PASS** |
| H01-17 | Technical user sees exact metric and business user sees a health abstraction | Both consume the same underlying Observation/Assessment truth; audience is not a separate metric definition | **PASS** |
| H01-18 | Upstream A row count is profile-selected and A feeds C | Lineage alone does not make A row count a C metric or imply arithmetic reconciliation; Group 05 owns propagation semantics | **PASS** |
| H01-19 | Current output has no qualifying measurement yet but previous run has one | Current evaluation is pending/unavailable as appropriate; prior value must not be silently reused as current evidence | **PASS** |
| H01-20 | Both null count and null rate are available and nearly redundant for a routine question | Profile may retain one/both only where distinct purpose/evidence value justifies them; availability alone is insufficient | **PASS** |

## Findings

1. The accepted concept model is sufficient; no new Metric/Check/Profile concept is needed.
2. Metric definition and metric Observation must be distinguishable before any Baseline or threshold reasoning.
3. Semantic applicability, profile selection, source support, current availability, and Assessment outcome must remain orthogonal.
4. Metric-family taxonomy is useful only when it does not become a universal checklist.
5. Anti-bloat requires routine versus diagnostic distinction and explicit lifecycle behavior.
6. Provenance must remain strong enough to support later comparability, threshold, propagation and restricted-disclosure reasoning.
7. Group 01 deliberately leaves schema compatibility to Group 02, statistical/Baseline comparability to Group 03, threshold/Assessment semantics to Group 04, propagation to Group 05, and composite/timing behavior to Group 06.

## Result

**H01-01–H01-20 pass under HLTH-001–HLTH-008. No new concept, SYN, REF, AUTH, or additional HLTH contract is required for Group 01 exit.**
