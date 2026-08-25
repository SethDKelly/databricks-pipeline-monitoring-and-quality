# External Source Review — Phase 009 Group 06

**Verified:** 2026-08-25

This review records current public source facts used by Group 06. It does not substitute for environment-specific discovery of enabled audit/system tables, GitHub plan/repository settings, deployed Immuta version/integration mode, custom controls, retention extensions or organizational Assertion Authority.

## Databricks audit and Jobs controls

- [Audit log system table reference](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs) — `system.access.audit` records actor, service/action, request parameters, response, event ID and event time for qualifying events; most workspace events are regional.
- [System tables reference](https://docs.databricks.com/aws/en/admin/system-tables/) — audit system table currently has a 365-day free retention period.
- [Audit log reference](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs) — documents Jobs and governance actions including run failures/cancellation/repair and permission changes with action-specific request fields.
- [Cancel Run API](https://docs.databricks.com/api/jobs/v2/cancel-run) / Jobs API semantics — cancellation acts on a run/task and is asynchronous; request completion does not establish immediate termination.
- [Configure task dependencies](https://docs.databricks.com/gcp/en/jobs/run-if) — Lakeflow Jobs `Run if` conditions govern downstream task execution from dependency outcomes.
- [If/else condition task](https://docs.databricks.com/gcp/en/jobs/tasks/if-else) — evaluates an explicit boolean expression and exposes true/false branch outcomes in the job graph/run details.
- These Jobs control-flow features are implementation candidates for a bounded Execution Gate only when an accepted Gate criterion/readiness/opportunity contract is explicitly mapped. Native dependency success or expression truth does not itself define DMTZ readiness.

## GitHub Actions deployment protection

- [Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — environment protection rules can require reviewers, wait timers, branch/tag restrictions and custom deployment protection rules; configured rules must pass before an environment-referencing job proceeds.
- [Deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) — protection rules must pass before the job is sent to a runner; environment secrets become available only after the job proceeds.
- [Reviewing deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments) — required reviewers can approve or reject waiting jobs; rejection fails the workflow; authorized users can bypass pending protection rules unless bypass is disabled, with an optional/commented bypass action.
- [Deploying with GitHub Actions](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments) — custom deployment protection rules use GitHub Apps/webhooks and callbacks to approve/reject jobs based on external systems; protection-rule availability varies by plan/repository visibility and custom rules remain preview functionality.
- GitHub environment protection is therefore strong pre-start evidence for the exact Actions job opportunity. It is not evidence that a later Databricks run was gated unless the GitHub job is explicitly correlated to that target execution under Group 03.

## Immuta enforcement and audit

- [Understanding Immuta Audit Logs](https://documentation.immuta.com/saas/knowledge-base/implementation/audit-and-monitor/understanding-immuta-audit-logs) — application events include policy, metadata/tag, user/group attribute, access request and permission changes; query events record governed-data activity. Current SaaS guidance describes a 90-day default audit retention and recommends export for longer-term analysis.
- [Universal Audit Model](https://documentation.immuta.com/latest/detect-your-activity/audit/reference-guides/universal-audit-model-uam) — UAM provides consistent query/authentication/policy/project/tag events and supports export; integration-specific limitations include missing target data-source information for some Databricks Unity Catalog events and coverage/configuration dependencies.
- [Databricks Query Audit Logs](https://documentation.immuta.com/2024.2/detect-your-activity/audit/reference-guides/databricks) — for covered registered users/data sources, Databricks query audit can include user entitlements and the policy set applied during execution, and can record denied queries with subscription-policy context. Version-specific retention/defaults differ from current SaaS guidance, so deployed-version semantics must be verified.
- [Immuta Users and Permissions](https://documentation.immuta.com/SaaS/configuration/people/users-index/reference-guides/personas-and-permissions) — Immuta permissions govern actions within Immuta; permission changes are audited. These are not DMTZ Assertion Authority by title alone.
- Immuta query-time audit can be strong enforcement evidence for its covered population, but one denied query/path does not establish global prevention and missing audit does not establish allow/deny.

## Investigation / causality source discipline

- Databricks anomaly-monitoring `root_cause_analysis`, GitHub review/comment records, Immuta audit rationales and automated analysis can all provide leads/context/annotations.
- None is treated as automatic Causal Claim confirmation. Exact causal roles/status remain governed by REF-013–REF-020 and confirmation by REF-017 + AUTH-034.
- Remediation, rollback, rerun and policy/control interventions can create useful before/after contrasts only when source/version/exposure/effect identity and relevant confounders/coverage are sufficient for the bounded proposition.

## Environment-specific unknowns retained

- which Databricks audit/system tables and audit events are enabled/readable for the monitoring service;
- exact Jobs/runtime versions and whether conditional tasks are used as explicit Gate realizations;
- which UC privilege/policy surfaces, caches, exports and non-UC paths must be controlled for a Safeguard proposition;
- whether Immuta is deployed, integration type/version, registered user/data-source population, query-audit coverage and exported retention;
- GitHub plan/repository visibility, configured environments, reviewers, bypass rules, custom protection rules and retained deployment/review history;
- organization-owned Investigation/Annotation/case-management source and causal-confirmation Assertion Authority registry;
- concrete Propagation Safeguard activation/release workflow and evidence path;
- exact Execution Gate criterion/profile registry, override/fallback authority, multiple-Gate composition and control delivery/acceptance telemetry;
- control integration observability needed to distinguish missing telemetry from control outcome;
- long-horizon retention needed for audit, control and causal historical replay.

These remain `unknown / not yet verified`, conditional or partial support rather than assumptions.
