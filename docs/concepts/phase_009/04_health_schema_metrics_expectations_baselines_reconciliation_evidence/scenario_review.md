# Group 04 Scenario Review — HME04-01–HME04-56

All scenarios pass the Group 04 source-contract boundaries.

| ID | Scenario | Required result |
|---|---|---|
| HME04-01 | Current UC schema visible | Current structural Observation only; no historical/compatibility promotion |
| HME04-02 | Column hidden by permissions | Non-return is restricted/observer-relative, not absent |
| HME04-03 | Schema changed before history window | Historical change unresolved rather than `no change` |
| HME04-04 | Same column name after recreate | No automatic field-identity continuity |
| HME04-05 | Renamed column with explicit mapping | Preserve identity only under accepted mapping evidence |
| HME04-06 | PK declared, duplicates present | Declaration remains informational; empirical integrity fails independently |
| HME04-07 | CHECK enforced | Enforcement behavior retained; declaration not universal health state |
| HME04-08 | Engine can cast changed type | Cast support does not create consumer compatibility |
| HME04-09 | Consumer A accepts change, B does not | Compatibility remains consumer/interface specific |
| HME04-10 | DQX installed but version unknown | Capability/version status remains partially verified |
| HME04-11 | DQX YAML rule exists | Availability does not create Expectation authority |
| HME04-12 | DQX generated rule not reviewed | Candidate only, not normative |
| HME04-13 | DQX rule accepted by governed authority | Can implement exact framework Expectation |
| HME04-14 | DQX row warning emitted | Evidence of exact rule issue, not business severity |
| HME04-15 | DQX error action fails pipeline | Action does not become Gate decision or causal truth |
| HME04-16 | DQX summary count lacks input version | Run quality result cannot be bound to exact input version by guess |
| HME04-17 | DQX metrics persisted with run/rule provenance | Historical Observation supported within retained coverage |
| HME04-18 | Lakeflow warn expectation | Pass/fail counts are source-local Observation |
| HME04-19 | Lakeflow drop expectation | Dropped-record count remains action/result evidence, not severity |
| HME04-20 | Lakeflow fail expectation stops update | Violation may be known while detailed counts remain unavailable |
| HME04-21 | Completed flow has no expectation metrics | Apply documented metric-availability limitations; no clean inference |
| HME04-22 | View expectation evaluated in several downstream flows | Keep flow/update-specific result sets separate |
| HME04-23 | Metric View exists for revenue | Semantic metric candidate; no profile/normative health membership by existence |
| HME04-24 | Metric View YAML `version: 1.1` | Treat as spec version, not business metric revision 1.1 |
| HME04-25 | Metric View measure queried by region | Observation binds region grouping/filter/definition context |
| HME04-26 | Metric View definition changes materially | Require new governed metric-definition revision/comparability review |
| HME04-27 | Materialized metric view last refreshed hours ago | Assess exact-use freshness; schedule alone not SLA truth |
| HME04-28 | Metric View `rely` cardinality incorrect | Do not treat declaration as key integrity; measure may be invalid |
| HME04-29 | Profiling emits null/count/quantile metrics | Descriptive Observations only |
| HME04-30 | Profiling baseline table configured | Candidate/reference source, not automatic framework Baseline |
| HME04-31 | Baseline schema partially mismatches | Preserve source best-effort behavior and framework comparability limitation |
| HME04-32 | Consecutive drift high | Descriptive drift does not automatically violate Expectation |
| HME04-33 | Baseline drift low but explicit SLA violated | Normative violation and descriptive typicality coexist |
| HME04-34 | Custom aggregate metric | Retain exact metric definition/input-column/version context |
| HME04-35 | Derived custom metric | Preserve dependency on aggregate basis; no independent corroboration |
| HME04-36 | Anomaly detector marks table stale | Vendor learned-pattern Assessment; not explicit SLA violation by default |
| HME04-37 | Table meets SLA but is anomaly-stale | Keep two different propositions/results |
| HME04-38 | Table violates SLA but anomaly detector Healthy | Do not let vendor label override governed Expectation |
| HME04-39 | Anomaly detector Training | Insufficient model maturity, not healthy/unhealthy fallback |
| HME04-40 | Intelligent scan skipped table | Missing current result does not mean no anomaly |
| HME04-41 | Commit freshness good, event latency bad | Commit freshness cannot answer event freshness |
| HME04-42 | Vendor consolidated Healthy | Do not substitute for HLTH-055 profile without explicit composition |
| HME04-43 | Vendor root-cause field names upstream job | Investigation lead/context only; no causal confirmation |
| HME04-44 | Vendor impact says High | Do not convert to realized consumer Impact/severity |
| HME04-45 | Reference history has recent abnormal runs | Baseline membership/exclusion remains governed, not newest-history wins |
| HME04-46 | Structural regime changes | Segment affected Baseline/metric applicability rather than global reset |
| HME04-47 | Whole-table metric used for region question | Reject grain/population mismatch |
| HME04-48 | Region slice used for global claim | Reject transitive/global coverage |
| HME04-49 | Metric queried after run from latest table state | Cannot attribute to that run/output absent exact binding |
| HME04-50 | Output version explicitly bound then metric computed AS OF version | Exact-version Observation can be supported within retained data/history |
| HME04-51 | Upstream/downstream row counts happen to match | No reconciliation without exact transformation/population rule |
| HME04-52 | DQX relational rule binds exact source/output | Reconciliation candidate if HLTH-041–054 context is complete |
| HME04-53 | Multi-input run lacks consumed versions | Exact current-cycle alignment remains unresolved |
| HME04-54 | Older result exists but rule definition was overwritten | Historical Assessment cannot be reconstructed exactly without rule version |
| HME04-55 | No failed checks returned during failed DQX job | Integration failure is limitation, not clean pass |
| HME04-56 | DQX says pass, anomaly says Unhealthy, SLA meets | Preserve distinct propositions/bases; no universal winner/score |

**Result:** HME04-01–HME04-56 PASS.
