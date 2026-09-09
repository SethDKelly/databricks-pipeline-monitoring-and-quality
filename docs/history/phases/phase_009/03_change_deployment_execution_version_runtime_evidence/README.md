# Phase 009 Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence

**Status:** Review complete — accepted

## Result

Group 03 accepts **INTG-051–INTG-083** and **RTE03-01–RTE03-54**. No new product concept is required.

The group maps concrete GitHub/GitHub Actions and Databricks operational surfaces to the accepted Change Intent, Deployment and Execution History semantics without turning a CI/CD or runtime platform into a new truth owner.

The central evidence chain is:

**exact repository revision / governed Change Intent → GitHub workflow/deployment attempt → explicit CI↔target correlation → Databricks target activation evidence → execution/run/task identity → attempt/repair continuity → run-specific implementation facets → actual sequence → input/output version evidence → bounded historical reconstruction**.

No link automatically creates the next.

## Accepted contracts

1. **INTG-051** — Repository Revision & Change-Record Identity
2. **INTG-052** — GitHub Event & Workflow-Trigger Revision Semantics
3. **INTG-053** — GitHub Workflow Run Identity & Attempt Continuity
4. **INTG-054** — GitHub Job / Step Lifecycle & Conclusion Evidence
5. **INTG-055** — GitHub Re-run Revision, Actor & Privilege Semantics
6. **INTG-056** — GitHub Artifact, Log & Attestation Retention Evidence
7. **INTG-057** — GitHub Deployment & Environment Request Identity
8. **INTG-058** — GitHub Deployment Status vs Databricks Activation
9. **INTG-059** — Cross-System CI → Databricks Correlation Contract
10. **INTG-060** — Databricks Job Definition & SCD2 Configuration Identity
11. **INTG-061** — Databricks External-Deployment / Bundle Provenance
12. **INTG-062** — Bundle Deployment Attempt, Apply Outcome & Target Binding
13. **INTG-063** — Deployment Activation & Active-State Evidence
14. **INTG-064** — Databricks Job Run Identity & Lifecycle
15. **INTG-065** — Databricks Task Run & Parent/Child Execution Identity
16. **INTG-066** — Execution Opportunity, Trigger & No-Run Evidence
17. **INTG-067** — Retry Attempt Semantics
18. **INTG-068** — Repair, Restart, Rerun & Backfill Continuity
19. **INTG-069** — Run-Specific Remote-Git Commit Binding
20. **INTG-070** — Bundle / Workspace-Source Run-Version Gap
21. **INTG-071** — Composite Run-Specific Implementation-State Binding
22. **INTG-072** — Configured Dependency vs Actual Sequence
23. **INTG-073** — Run-Job Trigger & Root/Source-Task Association
24. **INTG-074** — Runtime Timing, Queue, Setup & Execution Semantics
25. **INTG-075** — Lakeflow Pipeline Update Identity & Lifecycle
26. **INTG-076** — Databricks API / System-Table Coverage & Retention Split
27. **INTG-077** — Audit-Log Operational Event Corroboration & Coverage
28. **INTG-078** — Delta Output Table Commit / Version Evidence
29. **INTG-079** — Delta `readVersion` Non-Input-Manifest Boundary
30. **INTG-080** — Run-Specific Input-Version Consumption Gap
31. **INTG-081** — Multi-Output & Partial Output-Version Set
32. **INTG-082** — Operational Negative Claims & Coverage Envelope
33. **INTG-083** — Group 03 Runtime Source Matrix & Group 04 Handoff

## GitHub revision and workflow evidence

Git commit SHA is the exact repository-revision identity. GitHub Actions workflow execution adds event-bound revision/ref context, workflow-definition revision, workflow-run identity, job/step lifecycle and attempt identity.

Preserve:

- `github.sha` / `GITHUB_SHA` as event-semantic triggering revision;
- `github.workflow_sha` as workflow-definition revision;
- `run_id` as workflow-run identity;
- `run_attempt` as re-execution attempt identity;
- re-runs using the original event SHA/ref rather than creating a new source revision by default.

A pull request/commit/release becomes **Change Intent** only under an explicit governance rule. GitHub Actions success proves its own workflow result, not target activation.

## Deployment evidence and cross-system association

GitHub Deployment objects can bind a repository ref/resolved SHA to an environment/request. Their statuses remain GitHub-side deployment-state assertions.

The GitHub→Databricks transition requires explicit correlation evidence such as a shared immutable identifier, deployment manifest, artifact/content fingerprint, target-recorded revision or equivalent mapping. Repository/job/environment names, actors and timestamps cannot establish the join.

Bundle/CI deploy success likewise does not universally prove Databricks activation. Exact target effective state must be established from target evidence appropriate to the resource and deployment pattern.

## Databricks execution evidence

Jobs Runs APIs and Lakeflow system tables provide strong source-local run/task identity, trigger/run type, lifecycle, timing and configuration-history evidence within their documented coverage.

Preserve:

**configured trigger/opportunity ≠ actual run → partial lifecycle ≠ terminal result → attempt/repair continuity ≠ new/independent execution by convenience**.

Retry, repair, restart, rerun and backfill retain source-specific semantics. Explicit parent/root/source task/run identifiers are used when available; absent historical fields are not reconstructed from timestamp proximity.

## Direct Git versus bundle/workspace-source provenance

This is the major source-pattern distinction discovered by Group 03.

For Lakeflow Jobs configured directly with remote Git, Databricks snapshots the configured branch/tag/commit at run start and qualifying Runs API results expose **`git_snapshot.used_commit`**. That is strong evidence for the exact Git code revision used by that run.

Bundle-deployed workspace-source execution is materially different. Documented bundle/job deployment metadata can identify external bundle management and repository origin/branch context, but Group 03 found no universal documented immutable Git commit attestation for every bundle/workspace-source run.

Therefore exact bundle/workspace-source run Git revision is **unsupported out of the box / conditional** on an explicit deploy/run revision manifest, immutable artifact/content fingerprint or equivalent attestation.

## Composite implementation state

Even when the exact Git commit is known, run-specific implementation state can still be composite across:

- code/build/notebook revision;
- job/task definition;
- parameters and configuration;
- libraries/runtime;
- schema/interface/configuration facets;
- target/environment state.

No single commit or current active job definition automatically owns all facets.

## Dependency and sequence

Databricks configured task dependencies support expected/configured order. Run/task timelines support actual temporal precedence.

Preserve the accepted ladder:

**configured dependency ≠ actual precedence ≠ evidenced waiting/hold ≠ input/version consumption**.

Timeline representation must be correctly assembled because one execution can span multiple timeline rows. Clock/time-source limits remain material to exact ordering.

## Input and output versions

Delta history can conditionally support an execution→output-table-version association when the exact table commit and run/job provenance can be correlated. Output evidence remains per output and can be partial; failed executions may have committed outputs and successful runs can have unknown output evidence.

Group 03 explicitly rejects treating Delta history `readVersion` as a universal multi-input manifest. For arbitrary Spark/SQL workloads the evaluated out-of-box sources do **not** universally expose the exact set of upstream entities/versions consumed by a run.

Exact input-version consumption is therefore **unsupported out of the box / conditional** on workload/query/source-specific telemetry, explicit source-version parameters, manifests, snapshots or equivalent evidence.

## Historical replay and negative claims

Recent Jobs API history and longer Lakeflow system-table history provide different fields and history windows. Historical reconstruction is therefore source-set/time-window specific rather than one uniform replay capability.

Strong claims such as `no deployment`, `no activation`, `no run`, `no retry`, `no output` and `no consumption` require the exact opportunity/population/window plus sufficient source/query coverage and source health. Retention expiry, deleted workflow evidence, regional limits, permission failures, source outages or missing input instrumentation remain limitations.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — RTE03-01–RTE03-54 pass.
- [`../../../decisions/phase_009_group_03_change_deployment_execution_runtime_sources.md`](../../../decisions/phase_009_group_03_change_deployment_execution_runtime_sources.md) — D-975–D-1021.

## Architecture boundary

Group 03 does not choose a deployment-manifest format, attestation mechanism, GitHub Actions workflow design, bundle strategy, runtime agent, query instrumentation, input-version manifest mechanism, ingestion architecture, persistence schema, polling/streaming design or retention service. Phase 010 owns technical realization.

## Handoff

**Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence is next.**

Group 04 may consume exact run/task identity, execution timing, run-specific code/implementation facets and input/output versions only where Group 03 established them. It must preserve unresolved provenance/input/output gaps and may not convert execution success into schema compatibility, metric quality, freshness, currentness or health.
