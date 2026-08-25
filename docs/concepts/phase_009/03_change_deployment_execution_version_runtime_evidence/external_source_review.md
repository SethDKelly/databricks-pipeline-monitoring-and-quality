# External Source Review — Phase 009 Group 03

**Verified:** 2026-08-25

This review records current public vendor/documentation facts used by Group 03. It is not a substitute for environment-specific feature/configuration discovery.

## GitHub / GitHub Actions

- [Workflow runs REST API](https://docs.github.com/en/rest/actions/workflow-runs) — workflow-run instances expose run identity and revision/ref context; APIs support filtering/querying by commit SHA and attempt-aware log access.
- [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts) and [variables reference](https://docs.github.com/en/actions/reference/workflows-and-actions/variables) — `github.run_id` remains stable across re-runs; `github.run_attempt` increments; `github.sha` is event-specific triggering SHA; `github.workflow_sha` identifies the workflow-file revision; `github.triggering_actor` can differ on re-run.
- [Re-running workflows and jobs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs) — GitHub re-runs use the same `GITHUB_SHA` and `GITHUB_REF` as the original event; re-run/attempt limits and time windows are documented.
- [Workflow syntax / events](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — workflow execution is associated with event/ref/revision semantics; event type must be preserved when interpreting the triggering SHA.
- [Artifact and log retention](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts) and [artifact/log retention settings](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization) — Actions evidence is retention/configuration bounded; retained artifacts are not implied by workflow success.
- [Deployments REST API](https://docs.github.com/en/rest/deployments/deployments) — deployment requests bind repository, ref/resolved SHA and environment; deployments/deployment statuses remain GitHub-side deployment records.
- [Deployment environments](https://docs.github.com/en/actions/reference/deployments-and-environments) — jobs referencing an environment can create deployment/deployment-status records.

## Databricks Jobs / Lakeflow

- [Lakeflow system tables](https://docs.databricks.com/aws/en/admin/system-tables/jobs) — `system.lakeflow.jobs`, `job_tasks`, `job_run_timeline`, `job_task_run_timeline`, pipeline tables and their documented 365-day history/region/schema behavior. Job/task configuration tables use SCD2-style history; timeline tables represent execution intervals.
- [Jobs Runs API](https://docs.databricks.com/api/workspace/jobs) — run records expose `run_id`, job/task/lifecycle detail, attempt/repair information and Git source/snapshot information when applicable.
- [Use Git with jobs](https://docs.databricks.com/aws/en/jobs/how-to/use-git-with-jobs) — for remote-Git Jobs, Databricks snapshots the configured branch/tag/commit at run start and all tasks use the same Git commit.
- [Jobs API run Git snapshot](https://docs.databricks.com/api/workspace/jobs/getrun) — qualifying run responses expose `git_snapshot.used_commit`, the commit used for the run.
- [Jobs run history](https://docs.databricks.com/aws/en/jobs/monitor) — Jobs UI/API run history is automatically removed after the documented recent-history window, so longer replay requires other retained evidence.
- [Declarative Automation Bundles Git metadata](https://docs.databricks.com/aws/en/dev-tools/bundles/settings) — bundle Git metadata automatically records origin/branch context but does not document a universal immutable commit field for each deployed resource/run.
- [Bundle job resources](https://docs.databricks.com/aws/en/dev-tools/bundles/resources) — bundle-managed job resources can expose deployment metadata such as external-management kind/metadata-file context.
- [Bundle job source guidance](https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-override) — bundle-deployed source commonly uses workspace source; job-level Git source is a separate execution model.

## Databricks operational/audit evidence

- [Databricks audit log reference](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs) — job create/update/run/repair and related operational actions can be represented in audit evidence subject to event/verbosity/retention/region/permission constraints.
- [Lakeflow Jobs system-table reference](https://docs.databricks.com/aws/en/admin/system-tables/jobs) — run types and newer ancestry/source fields have data-vintage limitations; timeline rows can represent slices of one execution rather than one-row-per-run.

## Delta output/version evidence

- [Delta table history](https://docs.databricks.com/aws/en/delta/history) — `DESCRIBE HISTORY` exposes table version, commit timestamp, operation and supporting provenance such as job/notebook context when available, plus `readVersion` with transaction-specific semantics.
- `readVersion` is treated only with its documented transaction meaning. Group 03 found no documented basis to interpret it as a generic manifest of every upstream entity/version consumed by arbitrary Spark/SQL workloads.

## Lakeflow pipelines

- [Lakeflow pipeline system tables](https://docs.databricks.com/aws/en/admin/system-tables/pipelines) — pipeline configuration/update history is a distinct execution/evidence surface with its own preview/retention/coverage characteristics.

## Environment-specific unknowns retained

- exact deployment pattern: direct remote-Git Jobs, bundle/workspace-source Jobs, pipeline resources or combinations;
- whether the deployment workflow emits an immutable commit/content manifest and target-side correlation identifier;
- whether target activation is independently verified after deploy;
- which Jobs/system-table/audit regions and permissions are available;
- whether verbose audit events are enabled where required;
- whether output tables are Delta and retain sufficient transaction history;
- whether workloads emit explicit input-version manifests, source snapshots or query-level consumption evidence;
- which run/task/pipeline APIs are retained externally beyond native history windows.

These remain `unknown / not yet verified`, `partially supported`, or conditional rather than assumed capabilities.
