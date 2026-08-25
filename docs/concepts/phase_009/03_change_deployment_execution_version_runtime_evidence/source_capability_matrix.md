# Group 03 Source Capability Matrix

Support remains **proposition + source set + context** bound. `Conditional` means the proposition can be established only when the named correlation/attestation/instrumentation exists and is retained.

| Proposition / capability | Primary evaluated surfaces | Group 03 result | Key boundary / residual gap |
|---|---|---|---|
| Exact repository revision | Git commit SHA / GitHub commit object | Supported | Branch/tag/PR labels do not replace immutable revision |
| Registered Change Intent | PR/change record/repository metadata | Conditional | Requires an explicit governance rule defining which record/facet owns Change Intent |
| Actions triggering revision | Workflow run/context `head_sha` / `github.sha` | Supported with event semantics | Event type changes SHA/ref meaning |
| Workflow-definition revision | `github.workflow_sha` | Supported | Distinct from triggering revision |
| GitHub workflow run identity | `run_id`, `run_number`, workflow identity | Supported | CI-local execution only |
| GitHub re-run attempt identity | `run_id` + `run_attempt` | Supported | Same triggering SHA/ref; not new source revision by default |
| GitHub job/step lifecycle | Jobs/steps/status/conclusion | Supported in CI scope | Does not prove Databricks activation/runtime success |
| Actions artifacts/logs/manifest | Artifact/log APIs + configured retention | Partially supported | Must be explicitly produced and retained; workflow deletion/retention can remove evidence |
| GitHub deployment request | Deployment object `sha`/`ref`/environment | Supported in GitHub scope | Request/status is not Databricks Deployment activation |
| GitHub deployment status | Deployment status records | Supported in GitHub scope | `success` remains source-local unless target verification semantics are explicitly sufficient |
| GitHub → Databricks deployment correlation | Shared immutable identifier/manifest/fingerprint | Unsupported out of box / Conditional | Names, environment and timestamps are insufficient |
| Databricks job definition identity | Workspace + job ID | Supported | Not repository or business identity by itself |
| Databricks job/task config history | `system.lakeflow.jobs` / `job_tasks` SCD2 | Supported within documented history | Effective config constrains possible run state; does not prove run-specific code/version |
| Bundle-managed job provenance | Job `deployment` metadata / bundle metadata path | Supported as management context | Does not expose universal immutable Git commit for each run |
| Bundle repository origin/branch context | Bundle Git metadata | Supported as contextual provenance | Branch/origin are not commit attestation |
| Bundle deployment attempt | CI/bundle command + explicit target | Partially supported | Client success ≠ verified target activation |
| Databricks target activation | Target config/history/audit evidence | Partially supported / Conditional | Exact activation semantics depend on resource and retained target evidence |
| Job run occurrence | Jobs Runs API + `system.lakeflow.job_run_timeline` | Supported | Coverage/run-type/history boundaries apply |
| Task run occurrence/lifecycle | Runs API + `job_task_run_timeline` | Supported | Parent/root/source fields are data-vintage dependent |
| Retry continuity | Runs API `attempt_number` / `original_attempt_run_id` | Supported for qualifying recent records | Longer-horizon detail may require independent retention |
| Repair continuity | Runs API `repair_history` / related run IDs | Supported for qualifying recent records | Repair ≠ rerun/backfill; history window matters |
| Run-job/root ancestry | parent/root/source run identifiers | Partially supported | Newer fields are unavailable for older history |
| Remote-Git run commit | Runs API `git_snapshot.used_commit` | Supported | Strong for Git code facet only |
| Bundle/workspace-source run Git commit | Bundle/job metadata + run | Unsupported out of box / Conditional | Requires explicit immutable deploy/run attestation or content fingerprint |
| Composite run implementation state | Code + job config + params + libraries/runtime + target facets | Partially supported | No single native field owns all facets |
| Configured task dependency | `depends_on_keys` / job task configuration | Supported | Intended/configured dependency only |
| Actual temporal precedence | Task/run timeline | Supported within timeline coverage | Precedence ≠ waiting ≠ consumption |
| Evidenced waiting/hold | Source-specific lifecycle/timing fields | Partially supported | Temporal gap alone is not waiting proof |
| Trigger/opportunity | Effective trigger/schedule/run-job configuration | Partially supported | Opportunity must account for control/schedule/config effective interval |
| Strong `no run` | Opportunity + complete run coverage + healthy sources | Conditional | API/system retention and source availability constrain negative |
| Lakeflow pipeline/update identity | Pipeline config/update system surfaces | Partially supported | Pipeline update is distinct from job run; preview/history limits apply |
| Databricks recent detailed run replay | Jobs Runs API/UI | Partially supported | Databricks documents automatic removal after 60 days |
| Databricks longer operational replay | Lakeflow system tables | Partially supported | Typically 365-day free retention; not every recent API detail is present |
| Databricks audit operational events | `system.access.audit` / audit event records | Partially supported | Coverage/verbosity/retention and common derivation remain material |
| Delta output table version | `DESCRIBE HISTORY` + explicit job/run correlation | Conditional / Partially supported | Job/notebook fields vary by operation/task/surface; history retention matters |
| Delta history `readVersion` | Delta transaction history | Supported for its documented transaction meaning | Not a generic upstream input-version manifest |
| Exact generic multi-input version set | Evaluated out-of-box Jobs/Delta/system surfaces | Unsupported out of box / Conditional | Requires workload/query/source-specific instrumentation or manifest |
| Multi-output version set | Per-output Delta/history/commit evidence | Partially supported | Outputs can be partial; every output needs its own association |
| Strong `no output` | Execution opportunity + output population + complete commit coverage | Conditional | Run success/failure alone is insufficient |
| Strong `no consumption` | Exact expected input/path + complete consumption telemetry | Unsupported generally / Conditional | Generic source set lacks universal consumption manifest |

## Consolidated Group 03 gaps carried forward

1. **CI → Databricks association is not universal out of the box.** A shared immutable correlation/manifest/fingerprint is required when platform-native linkage is absent.
2. **Bundle/workspace-source runs do not provide universal run-specific Git commit attestation.** Direct remote-Git Jobs are materially stronger because `git_snapshot.used_commit` can bind the run to the executed commit.
3. **Run-specific implementation state is composite.** Code, job config, parameters, libraries/runtime and environment may need separate evidence.
4. **Exact generic multi-input version consumption remains unsupported out of the box.** Explicit instrumentation/manifest evidence is required where the product needs this proposition.
5. **Output version binding is conditional and per output.** Run success is not output evidence.
6. **Historical precision degrades across source windows.** Recent Runs API detail and longer system-table history are not semantically identical.
7. **Strong operational negatives remain coverage dependent.** Retention/source failure/pagination/permission gaps cannot become `no run`, `no output` or `no consumption`.
