# Phase 006 Group 07 — Consolidation Scenario Matrix

**Status:** Accepted — H07-01–H07-36 pass

| ID | Scenario | Expected result |
|---|---|---|
| H07-01 | Databricks run succeeds, but required completeness criterion violates | Execution success remains true; local health is degraded; no `run succeeded → healthy` shortcut |
| H07-02 | Metric is applicable and selected but current source is unavailable | Preserve unavailable current evidence; do not convert to zero, pass, or not-applicable |
| H07-03 | Diagnostic metric is applicable but intentionally not selected in routine profile | Routine composite unchanged; diagnostic remains available for Investigation/on-demand use |
| H07-04 | Optional column added; name-based consumer tolerates it while positional export does not | Compatibility differs by consumer/interface contract; no global breaking/non-breaking label |
| H07-05 | Grain changes from account to account-day | Row-count/uniqueness/distribution Baselines require scoped regime review; unrelated execution-duration history may remain comparable |
| H07-06 | `customer_id` renamed with explicit identity mapping | Structural identity can persist under evidence-backed rename mapping; mere drop/add would not be enough |
| H07-07 | Month-end volume is much higher than ordinary weekday history but inside explicit business threshold | Seasonal Baseline can mark ordinary-for-month-end while normative criterion still independently meets |
| H07-08 | Null rate has been ~12% for months while authoritative Expectation requires ≤2% | Descriptively typical + normatively violates |
| H07-09 | Planned transformation creates new population regime with little post-change history but explicit 13–15M requirement | Baseline insufficient; explicit criterion can still resolve meets/violates from sufficient current evidence |
| H07-10 | Approximate null rate near 2% threshold has uncertainty spanning boundary | Criterion remains indeterminate/insufficient; no false precision |
| H07-11 | 0% defects observed over population of two records | Observation remains valid; reference/claim strength reflects low-volume limitation |
| H07-12 | Completeness violation has bounded alert waiver | Underlying criterion remains violates; composite cannot become clean healthy solely because response is waived |
| H07-13 | Two co-authoritative thresholds conflict for same proposition | Normative conflict remains explicit absent governed resolver |
| H07-14 | A+B→C join output drops because B directional match rate falls sharply | Reconciliation localizes material deviation at join relationship; does not by itself establish B as root cause |
| H07-15 | A violates upstream completeness but C filters affected rows and all C required criteria meet | Upstream violation remains upstream; C can legitimately meet its own bound health profile |
| H07-16 | A and B meet local criteria but C transformation introduces nulls | C can violate downstream criteria despite healthy inputs; transformation-specific evidence identifies introduction point |
| H07-17 | Many-to-many join amplifies output because duplicate business keys are expected by contract | Fan-out is observable reconciliation evidence but not automatically a defect |
| H07-18 | Intentional filter reduces C by 40% | Population drop is reconciled through eligible/included/excluded semantics; no inherited upstream failure |
| H07-19 | DISTINCT union combines overlapping A/B populations | Input row counts are not simply additive; overlap semantics are required |
| H07-20 | C finishes now using A-current and B-previous-cycle | Output completion remains true; multi-input alignment can fail current-cycle readiness/freshness |
| H07-21 | Reconciliation uses restricted B evidence but analyst is authorized only to see safe summary | Internal derived result may support authorized projection; restriction remains and derivation is not declassification |
| H07-22 | One of ten required composite components violates while nine meet | Composite degraded under conjunctive profile; no majority-green override |
| H07-23 | Required completeness violates and required schema component is unavailable | Composite degraded with unavailable/incomplete qualifier; known failure and unresolved state coexist |
| H07-24 | Explicit OR profile allows either of two alternative sources; one branch violates, other meets | Composite can meet because accepted profile logic is OR; no generic worst-child rule |
| H07-25 | Consumer A contract meets while Consumer B-specific schema requirement violates | Healthy for A and degraded for B can both be true as different bound propositions |
| H07-26 | Engineer sees exact metrics/thresholds; executive sees summary only | Both views preserve one underlying health status with authorized detail differences |
| H07-27 | Run-success fact available immediately while full DQ/reconciliation profile is pending | Emit run success now; broader composite remains pending/indeterminate |
| H07-28 | Later enriched DQ shows violation | Broader composite becomes degraded; earlier run-success fact remains historically and currently true |
| H07-29 | Completeness Assessment meets but evidence is from prior day and current opportunity requires same-cycle data | Result is stale/unsuitable; cannot support ready |
| H07-30 | Completeness Assessment violates with fresh sufficient same-cycle evidence | Result can be suitable evidence and support not-ready |
| H07-31 | Metric is AUTH-023 control-use eligible but current result is stale | Eligibility does not make stale evidence suitable |
| H07-32 | Result is fresh/sufficient but metric lacks AUTH-023 eligibility for an active gate use | Health evidence can remain valid for monitoring; it cannot be used for that high-consequence control merely because it is fresh |
| H07-33 | Passive monitoring source fails for ungated C | Monitoring is degraded/unavailable; production is not blocked solely by monitoring failure |
| H07-34 | Active gate requires a health predicate whose evidence is unavailable | Readiness remains unresolved per criterion; fallback/hold/admit behavior remains separately governed |
| H07-35 | Consumer uses earlier safe V-1 rather than suspect V but current-cycle requirement expects V | Not exposed to V can coexist with stale/not-ready state |
| H07-36 | Historical incident used earlier metric definition, Baseline, transformation, composite and freshness rules; current rules differ | Replay uses then-effective versions and knowledge cut; later rules/evidence support retrospective reassessment without rewriting historical result |

## Result

All H07-01–H07-36 pass under HLTH-001–HLTH-066 without:

- a new concept;
- HLTH-067;
- a universal health/confidence/comparability/anomaly score;
- hidden threshold or composition precedence;
- false pass from waiver, missing evidence or stale evidence;
- blind Lineage metric/status propagation;
- causal promotion from reconciliation/localization;
- readiness/control conflation;
- architecture selection.

Phase 006 exit criteria are satisfied.
