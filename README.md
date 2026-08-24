# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, authorization, planned/realized change history, causal evidence, downstream business impact, and protective propagation state** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually reachable/exposed/affected, what consequences are evidenced, what policies/restrictions apply, who is responsible, what the analyst is authorized to inspect or operate, and what evidence supports each conclusion.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: ACTIVE**

Phase 002 originally completed with 20 retained concepts. Later requirements exposed two missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state.

The current catalog contains **22 accepted concepts**.

**Groups 01–05 are accepted. Group 06 — Historical Replay & Phase 003 Consolidation is next.**

Group 05 formalized layered downstream Impact, evidence-backed exposure/non-exposure, observed downstream effects, consequence evidence, safeguard-prevented exposure, Annotation boundaries, Capability Authorization-based analytical projection, and audience-specific Explanation without direct-data-access assumptions.

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but too late, use stale inputs, lose rows through a join, experience a source-shape change, legitimately change population under planned logic, threaten downstream client delivery, or produce an output risky enough to hold while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, data quality, planned intent, realized change, historical topology, governance, authorization, causality, downstream consequence, human investigation, and protective control as related but distinct concerns**.

## Restricted-data analysis is a core capability

The product must not equate **lack of direct row access** with **lack of monitoring or RCA access**.

An analyst may be denied Table C rows or sensitive columns while being permitted to inspect approved:

- pipeline/job execution status, duration, readiness, and freshness;
- aggregate table/pipeline health metrics and Assessments;
- safe Expectation/Baseline result state;
- Semantic Definition at an authorized abstraction;
- Responsibility Assignment/team contact;
- Classification and Policy Context/restriction summaries;
- historical Lineage with redacted or opaque restricted nodes;
- Investigation and Causal Claim status/evidence limitations;
- downstream Impact and Propagation Safeguard state;
- human Annotation where independently permitted.

That **Authorized Analytical Projection** can support meaningful root-cause and downstream-impact analysis without direct data access. It must preserve redaction, missing evidence, and authorization-limited confidence rather than pretending hidden evidence does not exist.

Metadata and derived evidence are **not automatically unrestricted**. Counts, thresholds, table names, Lineage, policy labels, responsibility information, business consequences, safeguard details, and causal conclusions can themselves be sensitive.

## Capability separation

The accepted model distinguishes at least:

**raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard-control authority.**

A user may therefore:

- analyze health/root cause/downstream Impact without being allowed to query raw data;
- operate/retry/update a job under an explicit operational capability without receiving raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking authority to activate it.

Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, and job creator identity do not silently grant these capabilities.

## Downstream Impact is evidence-layered

Group 05 rejects a generic `affected` flag. For every downstream subject the model can distinguish:

1. **candidate/reachable** — historical Lineage shows a plausible downstream path;
2. **exposed/not exposed/unknown** — consumption evidence shows whether the relevant state was actually encountered;
3. **observed downstream effect** — that consumer's own Observation/Assessment/Change shows a health or operational effect;
4. **technical/analytical/business consequence** — separate evidence establishes delivery, use, process, decision, client, or other consequence;
5. **causal attribution** — if the origin is claimed to have caused/contributed to the effect/consequence, that proposition belongs in Causal Claim.

A high-criticality or client-facing report can warrant immediate attention while remaining only reachable. Conversely, a downstream effect can be observed while consumed-version evidence remains insufficient. The model preserves these disagreements rather than forcing one `impact` answer.

An enforced safeguard can also establish **prevented exposure** when enforcement and negative-consumption evidence are sufficient. Preventing suspect-state exposure does not prove downstream delivery was fresh/healthy; the hold may itself create a separate delay/non-delivery consequence.

## Key product questions

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- Is a run slower than usual or violating a completion/readiness requirement?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned and what prospective blast radius exists?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, contradicted, rejected, or unresolved?
- Which downstream assets are merely reachable, actually exposed, visibly affected, or tied to evidenced business consequence?
- Did a safeguard actually prevent a suspect state from reaching a consumer, and did the safeguard create a separate delay?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, or operate without direct-data access?
- What is intentionally hidden/redacted, and how does that limit confidence?
- What was known and authorized at incident time versus what is known/allowed retrospectively?

## Operating environment

Known environment facts remain deliberately small:

- Spark ETL pipelines execute in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a key execution and metadata source;
- Databricks Metric Views and DQX are strongly favored later evaluations;
- Collibra and Immuta are available but optional.

These are environmental facts, not implementation architecture.

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.**
3. **Time/history are first-class.**
4. **Evidence over narrative completion.**
5. **Expectation is normative; Baseline is descriptive.**
6. **Observation is not Assessment.**
7. **Successful execution is not timely execution, freshness, or data quality.**
8. **Lineage discovers relationships/candidates, not cause.**
9. **First-observed localization is not root cause.**
10. **Causal claims remain epistemically explicit.**
11. **Multiple contributors and unresolved outcomes are valid.**
12. **Prospective Impact is not actual Impact or retrospective cause.**
13. **Actual Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
14. **Criticality influences priority, not evidence strength.**
15. **Propagation Safeguard is protective state, not defect proof; prevented exposure requires enforcement evidence.**
16. **Capability Authorization is separate from policy, responsibility, scope, and enforcement.**
17. **Raw-data access is separate from analytical visibility and operational control.**
18. **Analyst Investigation remains first-class even with restricted evidence.**
19. **Annotation is attributed context, not a shadow truth store.**
20. **Explanation consumes the authorized analytical projection; it is not a truth or authorization source.**
21. **Monitoring must not broaden raw-data or production-control authority.**
22. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause. Competing Causal Claims can remain supported or unresolved.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, causal status, Impact, safeguard state, and Annotation. Restricted nodes/evidence remain opaque rather than being retrieved and summarized behind the user's permission boundary.

Downstream, a Metric View and two reports may all be reachable. Version/refresh evidence can establish that one report consumed the affected C output, another did not, and a third remains exposure-unknown. A report's own metric failure is observed downstream effect; a client delivery/decision consequence requires separate evidence; saying C caused that effect requires Causal Claim.

If an enforced safeguard blocks the suspect version before a client report refreshes, Impact may establish prevented exposure while still assessing any delivery lateness caused by the hold. If the analyst also holds a separate job-operation capability, the analyst may be permitted to retry/update a job without gaining raw-data read access. Actual action success remains separately evidenced by Deployment/Execution History.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation navigation/system of record.
- [`docs/foundation/`](docs/foundation/) — accepted foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — concept specifications and post-exit addenda.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — synchronization contracts/scenarios.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) and [`.cursor/rules/`](.cursor/rules/) — repository-agent guardrails.

## Phase direction

Phase 003 remains documentation/design-first. Group 06 now performs historical replay and consolidation across E-01–E-20 before Phase 004 refinement. IAM implementation, graph/causal architecture, quarantine enforcement, service decomposition, and runtime integration choices remain deferred until later refinement/technical phases.
