# Decision Records — Phase 009 Group 03 Change / Deployment / Execution / Runtime Sources

Continues after D-974.

### D-975 — Group 03 vendor facts require current documentation verification
**Status:** Accepted
Exact source surface/version/feature/retention context is part of each capability claim.

### D-976 — Git commit SHA is the repository-revision identity
**Status:** Accepted
Branch/tag/PR labels do not replace the immutable revision.

### D-977 — Repository change records become Change Intent only under explicit governance
**Status:** Accepted
PR/issue/commit metadata does not own Change Intent by origin.

### D-978 — GitHub triggering SHA is event-semantic
**Status:** Accepted
The event/ref context must accompany `github.sha` / `GITHUB_SHA`.

### D-979 — Workflow-definition revision is distinct from triggering revision
**Status:** Accepted
`github.workflow_sha` must not be collapsed into the source-under-test revision.

### D-980 — GitHub workflow-run identity and attempt identity remain distinct
**Status:** Accepted
`run_id` identifies the run and `run_attempt` identifies its re-execution attempt.

### D-981 — GitHub re-runs retain the original triggering SHA/ref
**Status:** Accepted
A re-run is not a new source revision by default.

### D-982 — GitHub Actions success does not prove Databricks activation
**Status:** Accepted
CI outcome remains a CI-local proposition absent explicit target verification.

### D-983 — GitHub job/step conclusions remain CI-local lifecycle evidence
**Status:** Accepted
They do not prove downstream run/output/health.

### D-984 — Artifact/manifest evidence exists only when explicitly produced and retained
**Status:** Accepted
Workflow success cannot manufacture an attestation artifact.

### D-985 — GitHub Actions history is retention/configuration bounded
**Status:** Accepted
Expired/deleted evidence becomes unavailable, not negative proof.

### D-986 — GitHub Deployment can bind repository SHA/ref/environment request
**Status:** Accepted
This is GitHub deployment-request identity, not universal target activation.

### D-987 — GitHub deployment status is not target activation by default
**Status:** Accepted
Target activation requires accepted target verification semantics/evidence.

### D-988 — CI → Databricks association requires explicit correlation evidence
**Status:** Accepted
Use shared immutable IDs, manifests, fingerprints or target-recorded provenance.

### D-989 — Names and timestamp proximity cannot establish operational joins
**Status:** Accepted
They remain candidate/context evidence only.

### D-990 — Databricks job identity is workspace/job scoped
**Status:** Accepted
Job ID is not repository/business identity by itself.

### D-991 — Databricks job/task system tables support time-bounded configuration history
**Status:** Accepted
SCD2 state constrains possible configuration; it does not prove execution/version use.

### D-992 — Databricks deployment metadata establishes external-management context only
**Status:** Accepted
`BUNDLE`/metadata path does not itself prove a Git commit.

### D-993 — Bundle Git origin/branch metadata is not immutable commit attestation
**Status:** Accepted
Repository context is weaker than exact deployed revision.

### D-994 — Bundle/workspace-source runs have an out-of-box exact Git revision gap
**Status:** Accepted
Exact revision requires explicit deploy/run attestation or equivalent immutable evidence.

### D-995 — Bundle/CI deploy success is not activation by convenience
**Status:** Accepted
Target-side acceptance/effective state remains independently evidenced.

### D-996 — Active job configuration is not run-specific implementation state
**Status:** Accepted
Run binding is required for material implementation facets.

### D-997 — Databricks run IDs/timelines can establish actual execution occurrence
**Status:** Accepted
Run occurrence is evidence-backed rather than schedule-backed.

### D-998 — Execution lifecycle can remain partial
**Status:** Accepted
Missing terminal evidence does not imply running/failed/cancelled.

### D-999 — Databricks run-type/source coverage differences remain explicit
**Status:** Accepted
JOB_RUN, SUBMIT_RUN, WORKFLOW_RUN and other supported classes are not assumed equally visible everywhere.

### D-1000 — Task/parent/root/source run identities use explicit platform relationships
**Status:** Accepted
No timestamp/name reconstruction when identifiers are absent.

### D-1001 — Trigger/schedule configuration is not execution occurrence
**Status:** Accepted
It supplies opportunity/expected context only.

### D-1002 — `No run` requires opportunity, coverage and source health
**Status:** Accepted
Missing/expired operational history cannot establish non-execution.

### D-1003 — Retry attempt continuity follows source-owned identifiers
**Status:** Accepted
Attempts remain distinct and later success does not rewrite earlier failure.

### D-1004 — Repair, retry, rerun and backfill remain distinct
**Status:** Accepted
Repeated activity is not normalized into one generic retry lifecycle.

### D-1005 — `git_snapshot.used_commit` is strong run-specific Git code evidence
**Status:** Accepted
For qualifying remote-Git Jobs it binds the run to the commit used.

### D-1006 — Workspace-source execution cannot infer exact Git revision from branch/deploy time
**Status:** Accepted
Explicit attestation/fingerprint evidence is required.

### D-1007 — Run-specific implementation state is composite
**Status:** Accepted
Code, job definition, configuration, libraries/runtime and environment facets can differ in evidence source.

### D-1008 — Configured dependency is not actual sequence
**Status:** Accepted
`depends_on`-style configuration remains expected relationship evidence.

### D-1009 — Actual precedence is not waiting or consumption
**Status:** Accepted
Each stronger proposition requires its own evidence.

### D-1010 — Newer run-ancestry fields cannot be backfilled into older evidence by assumption
**Status:** Accepted
Data-vintage limits remain visible.

### D-1011 — Timeline slicing must be assembled before duration/sequence claims
**Status:** Accepted
Multiple timeline rows can represent one run/task.

### D-1012 — Lakeflow pipeline update identity remains separate from Jobs execution identity
**Status:** Accepted
Pipeline success/version/output claims retain their own evidence.

### D-1013 — Recent Jobs API history and longer system-table history are different replay surfaces
**Status:** Accepted
Recent detailed fields cannot be assumed available throughout the longer history window.

### D-1014 — Audit operational events are supporting/contextual evidence with derivation limits
**Status:** Accepted
Audit + system/job telemetry is not automatically independent corroboration.

### D-1015 — Delta output commit/version binding is conditional per output
**Status:** Accepted
Explicit run/job correlation and retained table history are required.

### D-1016 — Delta `readVersion` is not a generic upstream input-version manifest
**Status:** Accepted
Use only its documented transaction semantics.

### D-1017 — Exact generic multi-input version consumption is unsupported out of the box
**Status:** Accepted
Workload/query/source-specific instrumentation or manifests are required when exact input versions matter.

### D-1018 — Multi-output executions require per-output evidence
**Status:** Accepted
Partial output sets remain partial rather than globally passed/failed.

### D-1019 — `No output` and `no consumption` retain strong negative-evidence burdens
**Status:** Accepted
Run lifecycle alone cannot establish either conclusion.

### D-1020 — Historical runtime reconstruction is retention/source-set bounded and non-rewriting
**Status:** Accepted
Later retained evidence can improve retrospective reconstruction without pretending it was available then.

### D-1021 — INTG-051–INTG-083 and RTE03-01–RTE03-54 are accepted
**Status:** Accepted — Phase 009 Group 03
Group 03 is complete; Group 04 is next.
