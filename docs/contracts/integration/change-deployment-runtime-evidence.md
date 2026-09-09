# Change, Deployment, Execution, Version & Runtime Evidence

**Canonical key:** `integration.group-03`

**Kind:** INTEGRATION CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.INTG`

**Stable IDs:** INTG-051–INTG-083

**Owns current question:** What can Git/GitHub and Databricks runtime/deployment surfaces actually prove about revision, deployment, activation, execution identity, attempt continuity, sequence and input/output versions?

## Canonical source findings

Preserve the chain:

**repository revision / governed Change Intent → workflow/deployment attempt → explicit CI↔target correlation → target activation → execution/run/task identity → attempt/repair continuity → run-specific implementation facets → actual sequence → input/output version evidence → bounded historical reconstruction**.

Git commit SHA is repository-revision identity, not Change Intent without an explicit governance rule. GitHub Actions success ≠ Databricks activation. GitHub Deployment status ≠ target activation. Cross-system association requires immutable correlation/attestation evidence, not names, actors or timestamps.

For qualifying direct remote-Git Databricks runs, `git_snapshot.used_commit` can strongly bind exact code revision. Bundle/workspace-source execution has no universal out-of-box immutable run commit attestation. Exact multi-input consumed-version manifests are likewise unsupported out of the box for arbitrary workloads without source/workload-specific instrumentation. Configured dependency ≠ actual precedence ≠ waiting ≠ consumption. Successful execution ≠ output existence/currentness/health.

## Stable contracts

### INTG-051 — Repository Revision & Change-Record Identity
Use commit SHA as exact repository-revision identity while keeping a governed Change Intent association explicit rather than inferred from any commit/PR/release.

### INTG-052 — GitHub Event & Workflow-Trigger Revision Semantics
Preserve event-triggering revision/ref separately from workflow-definition revision; GitHub event semantics determine which SHA each field represents.

### INTG-053 — GitHub Workflow Run Identity & Attempt Continuity
Use workflow `run_id` as run identity and attempt metadata for re-execution continuity; a new attempt is not automatically a new source revision.

### INTG-054 — GitHub Job / Step Lifecycle & Conclusion Evidence
Treat job/step lifecycle and conclusion as GitHub workflow evidence only; successful CI does not prove target activation or downstream execution.

### INTG-055 — GitHub Re-run Revision, Actor & Privilege Semantics
Re-runs retain original event revision semantics unless explicitly changed; re-run actor/permission evidence does not manufacture a new Change Intent or target state.

### INTG-056 — GitHub Artifact, Log & Attestation Retention Evidence
Artifacts/logs/attestations support provenance only within their actual retention, mutability and association envelope; expired artifacts remain a historical gap.

### INTG-057 — GitHub Deployment & Environment Request Identity
Bind GitHub Deployment/environment requests to exact repository ref/resolved SHA and GitHub environment/request identity without treating them as Databricks activation.

### INTG-058 — GitHub Deployment Status vs Databricks Activation
GitHub deployment status is a GitHub-side assertion; exact target activation requires target evidence or an explicit reliable correlation/attestation chain.

### INTG-059 — Cross-System CI → Databricks Correlation Contract
Require a shared immutable identifier, manifest, fingerprint, target-recorded revision or equivalent evidence; names, actors and temporal proximity are insufficient joins.

### INTG-060 — Databricks Job Definition & SCD2 Configuration Identity
Treat current/SCD2 job definition evidence as configuration state for its recorded interval; it is not automatically run-specific implementation state.

### INTG-061 — Databricks External-Deployment / Bundle Provenance
External-deployment/bundle metadata supplies bounded provenance about management/origin, not universal immutable run-level Git revision.

### INTG-062 — Bundle Deployment Attempt, Apply Outcome & Target Binding
Separate bundle deployment attempt, apply outcome and target-resource binding; deploy success alone does not prove every target facet became effective.

### INTG-063 — Deployment Activation & Active-State Evidence
Establish target activation/effective state from target-appropriate evidence; requested/applied deployment state is not automatically active state.

### INTG-064 — Databricks Job Run Identity & Lifecycle
Use Databricks run identity, lifecycle, trigger/run type and timing as execution evidence within documented source coverage; partial lifecycle does not fabricate terminal outcome.

### INTG-065 — Databricks Task Run & Parent/Child Execution Identity
Preserve task/run parent-child/root/source associations from explicit fields where available; do not reconstruct missing relationships from timestamps.

### INTG-066 — Execution Opportunity, Trigger & No-Run Evidence
A configured trigger/opportunity is not an execution. `No run` requires bounded expected opportunity plus adequate run-source coverage and source health.

### INTG-067 — Retry Attempt Semantics
Retry/attempt identity follows source-specific evidence and remains distinct from rerun, repair, restart and backfill semantics.

### INTG-068 — Repair, Restart, Rerun & Backfill Continuity
Preserve each continuity mode and its relationship to the original execution; convenience must not flatten them into one retry concept.

### INTG-069 — Run-Specific Remote-Git Commit Binding
When present for a qualifying direct-Git run, `git_snapshot.used_commit` is strong evidence of the exact Git code revision used by that run.

### INTG-070 — Bundle / Workspace-Source Run-Version Gap
Generic bundle/workspace-source execution lacks a universal out-of-box immutable Git commit attestation; exact run revision remains conditional on explicit manifest/fingerprint/attestation evidence.

### INTG-071 — Composite Run-Specific Implementation-State Binding
Run implementation state can span code/build, job/task definition, parameters, libraries/runtime, schema/interface/configuration and target environment; one commit/current definition cannot own all facets.

### INTG-072 — Configured Dependency vs Actual Sequence
Configured dependency ≠ actual temporal precedence ≠ evidenced waiting/hold ≠ input/version consumption.

### INTG-073 — Run-Job Trigger & Root/Source-Task Association
Use explicit trigger/root/source-task/run identifiers to establish associations; absent historical fields remain unresolved rather than inferred.

### INTG-074 — Runtime Timing, Queue, Setup & Execution Semantics
Keep queue/setup/start/execution/end timing semantics and source clocks distinct when evaluating delay/order; timing alone does not establish cause.

### INTG-075 — Lakeflow Pipeline Update Identity & Lifecycle
Treat pipeline update identity/lifecycle as source-local execution evidence with its own timing, status, coverage and retention semantics.

### INTG-076 — Databricks API / System-Table Coverage & Retention Split
API and system-table surfaces have different fields, latency and history windows; combine them explicitly rather than assuming one uniform execution ledger.

### INTG-077 — Audit-Log Operational Event Corroboration & Coverage
Audit records may corroborate qualifying operational actions/events but retain event-class, retention, permission and completeness limitations.

### INTG-078 — Delta Output Table Commit / Version Evidence
Conditionally bind an execution to exact output table/version only when table commit and run/job provenance can be reliably correlated; output evidence remains per-output and may be partial.

### INTG-079 — Delta `readVersion` Non-Input-Manifest Boundary
Do not treat Delta history `readVersion` as a universal manifest of all exact upstream versions consumed by an arbitrary workload.

### INTG-080 — Run-Specific Input-Version Consumption Gap
Generic exact multi-input version consumption is unsupported out of the box unless workload/query/source instrumentation, explicit parameters/manifests/snapshots or equivalent evidence establishes it.

### INTG-081 — Multi-Output & Partial Output-Version Set
Represent execution→output version evidence as a possibly partial set; failed runs may commit outputs and successful runs may still have unknown output evidence.

### INTG-082 — Operational Negative Claims & Coverage Envelope
`No deployment/activation/run/retry/output/consumption` requires the exact opportunity/population/window plus sufficient source/query coverage and source health.

### INTG-083 — Group 03 Runtime Source Matrix & Group 04 Handoff
Pass run/task identity, timing, code/implementation facets and input/output versions forward only where evidenced; unresolved runtime/version gaps remain explicit and cannot become health facts.

## Architecture boundary

This contract selects no deployment-manifest format, attestation mechanism, GitHub Actions workflow design, bundle strategy, runtime agent, query instrumentation, version-manifest mechanism, ingestion architecture, persistence schema or retention service.

## Provenance

- `docs/concepts/phase_009/03_change_deployment_execution_version_runtime_evidence/README.md`
- Phase 009 Group 03 accepted INTG-051–INTG-083.
