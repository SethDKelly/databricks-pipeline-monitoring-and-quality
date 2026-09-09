# Group 07 External Source Review

**Reviewed:** 2026-08-28

Public vendor documentation is architecture input only; Group 01 requires target-environment capability verification before use.

## GitHub Actions environments

GitHub documents deployment protection rules that must pass before an environment-referencing job can proceed. Required reviewers, wait timers, branch/tag restrictions and custom GitHub App deployment protection rules can participate in this boundary. Environment secrets are unavailable to the job until protection requirements pass.

Architecture interpretation: this is a strong pre-start enforcement candidate for the exact GitHub Actions job/deployment opportunity. It does not establish downstream Databricks Gate enforcement without Group 05 correlation.

References:
- https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
- https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments
- https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments

Custom deployment protection rules are documented with plan/deployment constraints and preview status in current GitHub documentation. DMTZ therefore treats them as a deployment-verified optional adapter, not a universal dependency.

## Databricks Lakeflow Jobs conditional control

Databricks documents task dependency `Run if` behavior and `If/else` condition tasks for branching within a job DAG.

Architecture interpretation: these mechanisms can realize a bounded DMTZ Gate only where the exact DMTZ criterion, opportunity and branch/execution semantics are explicitly mapped. Native conditions do not become DMTZ Gate truth merely because they exist.

References:
- https://docs.databricks.com/aws/en/jobs/run-if
- https://docs.databricks.com/gcp/en/jobs/control-flow
- https://docs.databricks.com/gcp/en/jobs/tasks/if-else

## Databricks job submission

Databricks `run-now` supports an idempotency token that guarantees one launched run for repeated requests using that token, subject to the documented API semantics.

Architecture interpretation: a governed pre-start trigger broker can use the token plus DMTZ opportunity/correlation identity to reduce duplicate launch ambiguity, but must separately govern other trigger paths.

Reference:
- https://docs.databricks.com/api/jobs/v2/job

## Databricks cancellation

Databricks documents run cancellation and cancel-all as asynchronous. Cancel-all also explicitly does not prevent new runs from starting.

Architecture interpretation: cancellation is post-start interruption/containment, not a pre-start Gate HOLD.

References:
- https://docs.databricks.com/api/jobs/v2/submit-run
- https://docs.databricks.com/api/workspace/jobs/cancelallruns

## Service/workload identity

Databricks documents service principals for automated tools/jobs/applications and roles allowing jobs to run under service identities.

Architecture interpretation: active-control adapters should use least-privilege workload identities where target deployments support them, while Group 03 keeps service processing authorization independent from requester permission.

Reference:
- https://docs.databricks.com/aws/en/security/auth/access-control/service-principal-acl

## No universal native Safeguard

The reviewed sources do not provide a single vendor-native mechanism that universally blocks all Databricks/GitHub/BI/export/application propagation paths. Group 07 therefore retains a pluggable path/cohort-specific Safeguard architecture rather than assigning universal prevention semantics to any one product feature.
