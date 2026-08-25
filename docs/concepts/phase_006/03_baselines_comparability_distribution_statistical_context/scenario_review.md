# Phase 006 Group 03 — Baselines, Comparability, Distribution & Statistical Context Scenario Review

All scenarios are synthetic and test functional semantics rather than Databricks/statistical implementation.

| ID | Scenario | Expected reasoning | Result |
|---|---|---|---|
| H03-01 | C row count has 90 comparable ordinary weekdays | Eligible history can support an ordinary-weekday descriptive Baseline | **PASS** |
| H03-02 | Month-end C volume is 3x ordinary weekdays | Use month-end context; recent weekday history is not automatically comparable | **PASS** |
| H03-03 | Only two month-end runs exist | Literal history is known, but stable distribution/tail reference can remain insufficient | **PASS** |
| H03-04 | Metric display name unchanged but denominator changed | New definition/version; do not join the series silently | **PASS** |
| H03-05 | Additive optional schema field does not affect execution duration semantics | Execution-duration Baseline can remain comparable | **PASS** |
| H03-06 | Grain changes account → account/day | Row-count/uniqueness/distribution references segment at realized break | **PASS** |
| H03-07 | Same grain change; freshness definition unchanged | Freshness Baseline may remain comparable if other context is stable | **PASS** |
| H03-08 | Rename has authoritative identity mapping; metric binds same semantic field | Identity continuity can preserve candidate comparability, subject to other dimensions | **PASS** |
| H03-09 | Field keeps same name but meaning changes | Same name cannot preserve historical reference continuity | **PASS** |
| H03-10 | Proposed grain change never deploys | Prospective break does not activate; old Baseline remains eligible | **PASS** |
| H03-11 | Unplanned population change is realized | Realized Change can segment affected reference without prior intent | **PASS** |
| H03-12 | First three runs after change have no stable history | New regime remains `insufficient reference`; Expectations can still be assessed separately | **PASS** |
| H03-13 | Current value is included in the rolling window before comparison without declared semantics | Reject silent self-comparison/reference leakage | **PASS** |
| H03-14 | Five-day incident enters a rolling reference automatically | Do not silently normalize incident through adaptation | **PASS** |
| H03-15 | Known incident window excluded by explicit reference-population rule | Exclusion is valid when provenance/rule is retained | **PASS** |
| H03-16 | Historical values look unusual but no independent exclusion basis exists | `Looks anomalous` alone cannot circularly exclude them | **PASS** |
| H03-17 | Long-standing 12% null rate becomes historically typical; Expectation is ≤2% | Typical and normatively violating can coexist | **PASS** |
| H03-18 | Current row count is outside historical range but no normative volume rule exists | Report atypical, not failed quality | **PASS** |
| H03-19 | Current value is within historical range but violates an explicit later Expectation | Typical does not imply acceptable | **PASS** |
| H03-20 | Error count doubles because eligible volume doubles; error rate per million is stable | Raw counts can be non-comparable while explicit normalized rate remains comparable | **PASS** |
| H03-21 | Analyst rescales row count after seeing an outlier with no prior metric definition | Ad-hoc post-hoc normalization does not create valid comparability | **PASS** |
| H03-22 | Approximate distinct-count method changes algorithm/error behavior | Method change can create definition/comparability break | **PASS** |
| H03-23 | Approximate current distinct count differs by less than material method uncertainty | Do not assert precise shift beyond evidence | **PASS** |
| H03-24 | Three systems expose copies of same approximate metric | Mirroring does not narrow uncertainty or create corroboration | **PASS** |
| H03-25 | p95 transaction amount shifts with sufficient comparable history | Descriptive distribution shift can be assessed | **PASS** |
| H03-26 | p95 requested for opaque UUID | Semantically inapplicable despite technical computability | **PASS** |
| H03-27 | New category appears in a categorical distribution | Report shape/category change with context; not automatically defect | **PASS** |
| H03-28 | Histogram bin definitions changed | Historical bin summaries can become non-comparable | **PASS** |
| H03-29 | Tail/p99 reference has too few observations while median reference is sufficient | Sufficiency is conclusion-relative; central and tail claims can differ | **PASS** |
| H03-30 | Month-end Tuesday matches both weekday and month-end Baselines with no composition rule | Preserve ambiguous reference context rather than choose newest/cleanest | **PASS** |
| H03-31 | Restricted historical metric is usable by authorized monitoring service but hidden from analyst | Baseline can support safe projected Assessment without declassification | **PASS** |
| H03-32 | Baseline refreshed today; historical incident Assessment used prior Baseline version | Preserve historical Assessment/reference version rather than substituting current Baseline | **PASS** |

## Review result

**H03-01–H03-32 pass.**

The existing Baseline, Observation and Assessment concepts remain sufficient. `HLTH-019–HLTH-029` refine reference membership, comparability, baseline class/context, regime segmentation, evidence sufficiency, approximation, distribution shape, normalization, adaptation and ambiguity without creating a new statistical truth owner.

No anomaly algorithm, universal comparability/confidence score, statistical library, Metric Views/DQX realization, persistence strategy or compute architecture is selected.