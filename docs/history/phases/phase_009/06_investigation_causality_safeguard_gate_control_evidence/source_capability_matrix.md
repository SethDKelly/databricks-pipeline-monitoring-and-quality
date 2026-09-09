# Group 06 Source Capability Matrix

Support is **proposition + source set + context** bound. `Conditional` means exact proposition identity, authority, correlation, path/population coverage, enforcement evidence or retained history must be present.

| Proposition / capability | Primary evaluated surfaces | Group 06 result | Key boundary / residual gap |
|---|---|---|---|
| Investigation trigger | Alerts, DQ/health results, run failures, incidents/user reports | Supported as trigger when bound | Trigger ≠ cause |
| First observed deviation | Groups 03–05 retained Observations/Assessments/effects | Conditional | Earliest retained observation ≠ earliest real-world deviation |
| Earliest evidenced state change | Change/deployment/run/version history | Conditional / strong | Exact identity/time/coverage required; temporal order ≠ cause |
| First reconciliation/transformation boundary | Group 04 reconciliation/measurement evidence | Conditional | Boundary mismatch ≠ causal mechanism |
| First consumer effect | Group 05 exposure/effect evidence | Conditional | Effect can be known while exact exposure/cause remains unresolved |
| Investigation lead provenance | Source evidence + Annotation/ticket/issue metadata | Conditional | Lead priority/model score ≠ causal status |
| Lead exclusion | Discriminating negative evidence | Conditional / coverage-intensive | Missing support ≠ rejection |
| Human Annotation/review record | GitHub issue/PR/ticket/review or other governed record | Environment-specific / Conditional | Human title/approval ≠ truth/authority |
| Automated RCA/lead result | Vendor RCA/model/agent output | Supporting/contextual | Tool/model origin ≠ Causal Claim status |
| Causal proposition support | Runtime/version/reconciliation/exposure/effect/intervention evidence | Conditional | Claim-relative evidence roles |
| Causal contradiction | Non-consumption, after-effect timing, bypass, incompatible mechanism evidence | Conditional | Strong exclusion requires coverage |
| `confirmed` Causal Claim | Source evidence + AUTH-034 Assertion Authority | Conditional | No evaluated platform auto-confirms causality |
| Remediation/rollback contrast | Before/after version and effect evidence | Conditional / strong supporting | Successful fix ≠ confirmation by itself |
| Historical Investigation/Causal replay | Retained source facts + investigation/claim records | Partially supported | Source windows and annotation retention differ |
| Databricks control/governance action audit | `system.access.audit` | Supported for qualifying audited actions | 365-day free retention; regional/workspace considerations |
| Databricks request actor/action/params/response | `system.access.audit` | Supported where emitted | API response ≠ asynchronous effective enforcement |
| UC grant/revoke/permission change | UC state + audit | Conditional / strong | Privilege plane may not cover all access paths |
| Historical UC enforcement | audit/history + encounter evidence | Conditional | Current grant state ≠ earlier enforcement |
| Immuta policy/metadata/access-request change | Immuta application audit/UAM | Supported when Immuta deployed/retained | Policy config ≠ query-time application |
| Immuta query-time policy application | Immuta Databricks query audit | Conditional / strong | Registered user/data source/integration coverage required |
| Immuta query denial | Immuta query audit | Conditional / strong for covered attempt | Denied one path ≠ globally prevented exposure |
| Immuta long-horizon replay | UAM export / retained audit | Conditional | SaaS default retention is bounded; export needed for longer horizon |
| Safeguard proposal/authorization/request | Governed workflow/control records | Environment-specific / Conditional | No universal native DMTZ workflow assumed |
| Safeguard effective enforcement | Query-time policy/ACL/path-control + state evidence | Conditional | Configuration/API success insufficient |
| Safeguard protected state/path/cohort | Policy/control + Entity Identity/path mapping | Conditional | Asset-level state cannot cover ungoverned alternates |
| Partial Safeguard enforcement | per-user/path/cohort control evidence | Supported when exposed by source | No global success percentage |
| REF-028 prevented exposure | Group 05 opportunity + enforcement + negative encounter + alternate-path coverage | Conditional / coverage-intensive | `not exposed` + active control insufficient |
| Safeguard release/reopening | policy/grant/release action + effective state | Conditional | Release ≠ recovery/currentness |
| Safe stale/non-delivery effect | Group 04/05 result evidence | Conditional | Effect separate from control truth |
| Databricks run cancellation | Jobs API/run state/audit | Supported as post-start interruption | Cancel is asynchronous; not pre-start HOLD |
| Universal output quarantine/hold | evaluated native surfaces | Unsupported as one universal feature | Requires path-specific Phase 010 realization |
| GitHub environment pre-start gate | Actions environment protection rules | Supported for the GitHub job opportunity | Does not automatically gate Databricks execution |
| GitHub required-review approval | environment deployment review | Supported | Approval ≠ DMTZ readiness unless criterion mapping says so |
| GitHub rejection | environment deployment review | Supported | Rejection fails workflow; not causal truth |
| GitHub bypass | environment review bypass event/context | Supported as exceptional action | Bypass ≠ normal readiness/override authority unless mapped |
| GitHub wait timer | environment protection rule | Supported in GitHub semantics | Timer expiry ≠ DMTZ readiness by itself |
| GitHub custom protection rule | GitHub App deployment protection rule | Conditional / strong gate surface | External app decision ≠ source truth it consults |
| Databricks `Run if` dependency gate | Jobs task dependency result | Conditional | Native orchestration result ≠ DMTZ Gate without explicit mapping |
| Databricks `If/else` condition task | condition expression/result | Conditional / strong implementation candidate | Operand semantics/version must match exact criterion |
| Gate criterion/profile identity | governed criterion + source config/history | Environment-specific / Conditional | Name/label not criterion logic |
| Gate decision issuance/delivery/acceptance | GitHub/Databricks/custom control records | Conditional | Integrations expose different stages |
| HOLD enforcement | pre-start barrier + no-start/contradictory-start evidence | Conditional | No run alone insufficient |
| ADMIT enforcement | barrier release/permissive state | Conditional | ADMIT ≠ execution occurrence |
| Override | GitHub bypass/custom workflow or other authorized exception record | Conditional | Exception authority/scope explicit; readiness unchanged |
| Fallback | configured policy + trigger + selected action + enforcement | Environment-specific / Conditional | Configured fallback ≠ applied fallback |
| Timeout/escalation | timer/event/workflow record | Supported where emitted | Trigger ≠ admission decision |
| Multiple Gate composition | explicit configuration/control semantics | Conditional | No universal most-restrictive-wins rule |
| Gate + Safeguard coordination | independently evidenced controls | Conditional | Neither control inherits the other's action |
| Control telemetry failure | audit/API/runtime integration health | Supported as integration limitation | Missing telemetry ≠ fail-open/fail-closed |
| Historical Gate/Safeguard replay | retained configs/decisions/actions/enforcement + T/K | Partially supported | Native retention windows vary; external retention may be required |

## Consolidated Group 06 gaps carried forward

1. **No evaluated platform automatically owns Causal Claim confirmation.** REF-017 + AUTH-034 remains mandatory.
2. **A durable Investigation/Annotation/claim-status record is environment-specific.** Databricks/GitHub/Immuta facts can support it but do not natively constitute the full Investigation model.
3. **Databricks audit is action history, not universal enforcement truth.** Async requests and path-specific controls need effective-state evidence.
4. **No universal native Propagation Safeguard covers every publication/cache/export/application path.** Safeguard realization remains path-specific.
5. **Immuta enforcement evidence is strong only within registered/instrumented population and retained audit coverage.** Missing audit is not allowed/denied proof.
6. **REF-028 prevention remains expensive.** Actual encounter opportunity, enforced protected path, non-exposure and alternate-path coverage are all required.
7. **GitHub environments are a strong Gate only for the GitHub job/deployment they protect.** Cross-system gating of Databricks needs explicit Group 03 correlation.
8. **Databricks task conditions are strong implementation candidates but not automatic DMTZ Gate semantics.** Criterion/readiness/decision mapping must be explicit.
9. **Databricks cancellation is not a pre-start Gate.** It is asynchronous post-start interruption/control evidence.
10. **Override/fallback/multi-Gate semantics require explicit organizational control contracts.** No evaluated vendor supplies universal DMTZ composition semantics.
11. **Control historical replay is source-specific.** Audit, GitHub deployment/action history, Immuta audit and custom control records have different retention/detail limits.
12. **Missing/conflicting control telemetry remains unknown.** It cannot establish success, failure, fail-open, fail-closed or control-effect causality.
