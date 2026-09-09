# Group 06 Scenario Review — ICE06-01–ICE06-72

All scenarios pass the Group 06 source-contract boundaries.

| ID | Scenario | Required result |
|---|---|---|
| ICE06-01 | Failed DQ check opens inquiry | Trigger only; no presumed cause |
| ICE06-02 | Alert fires after issue existed | First alert is first observed in that source, not first real deviation |
| ICE06-03 | Earlier retained metric shows deviation | Earliest evidenced state can move retrospectively |
| ICE06-04 | First reconciliation mismatch at transform B | Boundary localized; mechanism/cause unresolved |
| ICE06-05 | First consumer KPI degradation at C | Consumer-effect localization only |
| ICE06-06 | Graph-nearest upstream chosen as lead | Lead allowed; no causal rank from distance |
| ICE06-07 | Model ranks deployment as likely cause | Model output is lead/context, not causal status |
| ICE06-08 | Senior analyst marks root cause | Annotation/claim proposal; authority/evidence still required |
| ICE06-09 | Lead has no supporting telemetry | Unresolved/weakened as justified; not rejected merely for absence |
| ICE06-10 | Exact version proved never consumed | Valid discriminating evidence when coverage sufficient |
| ICE06-11 | Proposed cause occurred after effect | Temporal contradiction can weaken/reject exact causal proposition if clocks/identity sufficient |
| ICE06-12 | Same event occurs before and after unaffected runs | Preserve mixed evidence; no forced winner |
| ICE06-13 | Rollback removes downstream effect | Strong supporting intervention contrast, not automatic confirmation |
| ICE06-14 | Rollback succeeds but unrelated config also changed | Confounding limitation retained |
| ICE06-15 | Rerun without code change recovers | Causal inference remains bounded; transient alternatives stay open |
| ICE06-16 | Vendor root-cause field names job X | Supporting lead/context only |
| ICE06-17 | GitHub review says change is cause | Human assertion; Causal Claim status independent |
| ICE06-18 | Multiple compatible contributors | Preserve multiple causal propositions/roles |
| ICE06-19 | Investigation closes operationally | Causal status does not strengthen |
| ICE06-20 | Late evidence arrives after closure | Retrospective claim/localization may change; earlier knowledge preserved |
| ICE06-21 | Databricks audit records permission-change request | Control action/request established |
| ICE06-22 | Audit response is success but propagation delayed | Effective enforcement remains separately evidenced |
| ICE06-23 | Current UC privilege absent | Current denial state only; historical denial unresolved without history |
| ICE06-24 | UC revoke applies to one table | Do not generalize to cache/export/API alternate paths |
| ICE06-25 | Immuta policy created | Configured policy, not query-time enforcement |
| ICE06-26 | Immuta audit shows policy applied to query | Strong bounded enforcement evidence |
| ICE06-27 | Immuta audit shows denied query | Denied encounter opportunity on that path; global prevention separate |
| ICE06-28 | Immuta user not registered/instrumented | Audit/enforcement coverage limitation |
| ICE06-29 | No Immuta audit record | Not evidence of allowed or denied access |
| ICE06-30 | Safeguard proposal approved | Authorization only; no enforcement |
| ICE06-31 | Safeguard API call succeeds | Request/acceptance evidence; effective protection still separate |
| ICE06-32 | Protected query path denies affected state | Path-specific enforcement supported |
| ICE06-33 | Another export path remains open | No global protection/prevention conclusion |
| ICE06-34 | Safeguard active but no consumer opportunity | Valid control state; no prevented-exposure credit |
| ICE06-35 | Consumer attempts affected read and is denied | Opportunity + path enforcement evidence available |
| ICE06-36 | Denied path plus all material alternates covered | REF-028 prevented exposure may be established |
| ICE06-37 | Consumer not exposed but never attempted access | Not prevented exposure by Safeguard |
| ICE06-38 | Consumer remains on safe stale cache | Safe-state result and possible freshness violation remain separate |
| ICE06-39 | Safeguard blocks current state and causes non-delivery | Non-delivery is Impact/result evidence; broader causal effect separately evaluated |
| ICE06-40 | Safeguard released | Release/reopening only; no health/recovery inference |
| ICE06-41 | Two safeguards overlap | Independent enforcement histories; no first-control attribution |
| ICE06-42 | Control telemetry missing during interval | Enforcement unknown; no fail-open/fail-closed inference |
| ICE06-43 | Databricks cancel request accepted | Post-start interruption request, not pre-start HOLD |
| ICE06-44 | Run continues briefly after cancel | Consistent with asynchronous cancel; final state separately evidenced |
| ICE06-45 | Output table lacks universal quarantine mechanism | Explicit integration gap; do not weaken Safeguard semantics |
| ICE06-46 | GitHub environment required reviewer waits | Pre-start Gate barrier for exact Actions job |
| ICE06-47 | Reviewer approves and other protection rules pass | GitHub barrier removed; GitHub job may proceed |
| ICE06-48 | Reviewer rejects | GitHub workflow fails; no DMTZ readiness inference |
| ICE06-49 | Admin bypasses pending protection rule | Explicit exceptional action; readiness unchanged |
| ICE06-50 | Wait timer expires | Timer condition satisfied, not generic readiness |
| ICE06-51 | Custom protection app approves based on health service | App Gate decision established; health source truth remains separate |
| ICE06-52 | Custom protection app unavailable | Gate/control telemetry unavailable; fallback behavior only if explicit/evidenced |
| ICE06-53 | GitHub deployment job approved but Databricks run uncorrelated | Cannot say Databricks opportunity was gated |
| ICE06-54 | GitHub deployment job explicitly maps to Databricks run | Cross-system Gate relevance can compose under Group 03 join |
| ICE06-55 | Databricks `Run if=ALL_SUCCESS` blocks task | Native orchestration condition result; DMTZ Gate only if explicit criterion mapping exists |
| ICE06-56 | `If/else` evaluates quality flag false | Exact condition result available; readiness/authority still separately mapped |
| ICE06-57 | Condition label says `quality_gate` but rule version unknown | Gate proposition incomplete |
| ICE06-58 | HOLD decision recorded but downstream start occurs | Full HOLD enforcement contradicted absent supersession |
| ICE06-59 | HOLD decision and no start, scheduler telemetry missing | HOLD enforcement unresolved rather than proven |
| ICE06-60 | HOLD decision delivered/accepted and opportunity remains blocked | Strong bounded HOLD enforcement evidence |
| ICE06-61 | ADMIT issued and job never starts | ADMIT/barrier removal can be true without execution |
| ICE06-62 | Job starts after ADMIT | Sequence evidence; admission does not automatically cause start |
| ICE06-63 | Override approved for one opportunity | Exception scoped to that opportunity; readiness unchanged |
| ICE06-64 | Unauthorized bypass attempt fails | Attempt/action result retained; no effective override |
| ICE06-65 | Fallback configured but trigger never occurs | No fallback application |
| ICE06-66 | Timeout occurs | Trigger only; separate fallback/decision/action required |
| ICE06-67 | Timeout triggers fallback ADMIT | Fallback admission recorded; prerequisite can remain not ready |
| ICE06-68 | Escalation sent to operator | Escalation is not HOLD/ADMIT |
| ICE06-69 | Two Gates apply and one admits | Overall admission unresolved until explicit composition/other Gate state known |
| ICE06-70 | Gate admits while Safeguard remains active | Run can proceed while output path remains protected |
| ICE06-71 | Current control config differs from incident-time config | Historical replay uses time-valid config/decision/enforcement records |
| ICE06-72 | Safe outcome plus active Gate/Safeguard, but effect attribution unclear | Preserve control facts; broader prevention/delay attribution remains Causal Claim |

**Result:** ICE06-01–ICE06-72 PASS.
