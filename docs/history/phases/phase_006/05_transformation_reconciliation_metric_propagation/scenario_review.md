# Phase 006 Group 05 Scenario Review

All scenarios must preserve local measurement identity, transformation-specific reconciliation, evidence limitations, and causal separation.

| ID | Scenario | Expected result | Result |
|---|---|---|---|
| H05-01 | A and B feed C; only asset-level Lineage is known | A/B metrics are relevant candidates only; no row-count formula/status propagation | PASS |
| H05-02 | Inner join A+B→C with 1:1 keys and complete match | Bound matched-pair/output reconciliation may be established | PASS |
| H05-03 | Same join has 8% unmatched A keys | Directional A unmatched/match Observation; downstream failure only under explicit Expectation | PASS |
| H05-04 | A 100% matched, B 70% matched | Preserve directional match-rate difference | PASS |
| H05-05 | Many-to-many join produces more C rows than A+B individually | Amplification can be valid; no generic row-count violation | PASS |
| H05-06 | Duplicate B keys cause unexpected fan-out | Fan-out/key-integrity reconciliation localizes mismatch; cause remains separate | PASS |
| H05-07 | B local uniqueness criterion violates but C dedupes before join | B violation does not automatically become C violation | PASS |
| H05-08 | B null join keys rise but affected B rows are filtered out before C join | Upstream condition can be non-material to bound C path | PASS |
| H05-09 | Pure filter removes 20% under intended predicate | Input/output/excluded reconciliation can explain row drop | PASS |
| H05-10 | Change Intent predicts 20% filter reduction but realized predicate differs | Intent does not substitute for realized reconciliation semantics | PASS |
| H05-11 | Filter changes category distribution | Output distribution is newly observed; input distribution not inherited | PASS |
| H05-12 | Aggregation groups 10M rows into 100k accounts | Row-count conservation is not expected | PASS |
| H05-13 | Additive transaction amount should conserve through grouping | Explicit total reconciliation can be evaluated | PASS |
| H05-14 | Filter precedes aggregation | Sum conservation must account for excluded population; naïve input/output equality invalid | PASS |
| H05-15 | Upstream averages 10 and 20; output average requested | Do not average summaries absent weights/raw relationship | PASS |
| H05-16 | Quantiles from two partitions are available | Do not combine quantiles generically | PASS |
| H05-17 | Distinct customer counts from overlapping A/B | Counts are not additive without overlap evidence | PASS |
| H05-18 | Pure dedupe removes 12k rows | Removal/survivor reconciliation valid under exact duplicate rule | PASS |
| H05-19 | Dedupe output unique but source non-unique | Output uniqueness does not rewrite upstream health | PASS |
| H05-20 | Dedupe survivor picks newest row, changing null rate | Survivor semantics explain downstream metric change; no inheritance | PASS |
| H05-21 | Bag union A+B with disjoint aligned populations | Additive source contribution/output count can reconcile | PASS |
| H05-22 | DISTINCT union over overlapping sources | A+B row-count sum is invalid; overlap semantics required | PASS |
| H05-23 | MERGE has inserts and updates | Output population depends on action classes/target state, not input count | PASS |
| H05-24 | Source A local criterion waived before union | Waiver does not transfer to C reconciliation/criterion | PASS |
| H05-25 | Left join introduces nulls for unmatched B | Downstream nulls can be transformation-induced and expected | PASS |
| H05-26 | COALESCE removes physical nulls using UNKNOWN | Completeness can improve while validity/business criterion violates | PASS |
| H05-27 | Cast failures become null | Derived null introduction requires observed/evidenced cast behavior | PASS |
| H05-28 | C finishes at 07:00 using current A and yesterday's B | C completion does not prove current-cycle alignment | PASS |
| H05-29 | B is intentionally daily while A hourly | Alignment uses explicit cadence criterion, not timestamp equality | PASS |
| H05-30 | Input version consumption telemetry unavailable | Alignment remains unresolved/unavailable, not current | PASS |
| H05-31 | C uses safe earlier B version avoiding suspect B-v2 | Can be not exposed to v2 while still stale | PASS |
| H05-32 | Celsius→Fahrenheit deterministic value transform | Versioned transformed measurement relationship can be valid | PASS |
| H05-33 | Join changes value distribution by selection | Do not propagate upstream quantile/drift status | PASS |
| H05-34 | Approximate upstream distinct count feeds reconciliation | Carry method/uncertainty; no false precision | PASS |
| H05-35 | Required upstream evidence unavailable | Derived reconciliation cannot substitute zero/pass | PASS |
| H05-36 | Restricted B metric contributes to reconciliation | Framework may derive authorized result; derivation is not declassification | PASS |
| H05-37 | A→B reconciliation and B→C reconciliation both valid | No automatic direct A→C conservation rule | PASS |
| H05-38 | Asset-level A→C exists but relevant A field is unused by C | Do not mark A field anomaly material solely from asset Lineage | PASS |
| H05-39 | A violates locally while C meets because transformation repairs condition | Preserve both states; no blind propagation | PASS |
| H05-40 | A/B meet locally but C violates due faulty transformation | Upstream success does not guarantee downstream success | PASS |
| H05-41 | C reconciliation violation first appears at join boundary | Localization is not root cause | PASS |
| H05-42 | A and B both abnormal and both materially relevant | Preserve multiple contributors/candidates without forced attribution | PASS |
| H05-43 | Join logic changed last month | Historical replay uses then-effective transformation/reconciliation version | PASS |
| H05-44 | Later Lineage correction reveals extra input D | Retrospective reconciliation may change; earlier Assessment remains preserved | PASS |

## Exit

H05-01–H05-44 pass under HLTH-041–HLTH-054. No Reconciliation concept, blind metric propagation, causal shortcut, or implementation architecture is required.
