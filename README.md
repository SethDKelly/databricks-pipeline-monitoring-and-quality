# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, authorization, planned/realized change history, causal evidence, downstream business impact, and protective propagation state** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually exposed or affected, what policies/restrictions apply, who is responsible, what the analyst is authorized to inspect or operate, and what evidence supports each conclusion.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: ACTIVE**

Phase 002 originally completed with 20 retained concepts. Later requirements exposed two missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state.

The current catalog contains **22 accepted concepts**.

**Groups 01–04 are accepted. A pre-Group-05 Capability Authorization refinement is accepted. Group 05 — Downstream Impact, Annotation & Explanation is next and has not yet started.**

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
- downstream Impact and Propagation Safeguard state.

That authorized analytical projection can support meaningful root-cause analysis without direct data access. It must also preserve redaction, missing evidence, and authorization-limited confidence rather than pretending hidden evidence does not exist.

Metadata and derived evidence are **not automatically unrestricted**. Counts, thresholds, table names, Lineage, policy labels, responsibility information, and causal conclusions can themselves be sensitive.

## Capability separation

The accepted model distinguishes at least:

**raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard-control authority.**

A user may therefore:

- analyze health/root cause without being allowed to query raw data;
- operate/retry/update a job under an explicit operational capability without receiving raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking authority to activate it.

Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, and job creator identity do not silently grant these capabilities.

## Key product questions

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- Is a run slower than usual or violating a completion/readiness requirement?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned and what prospective blast radius exists?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, contradicted, rejected, or unresolved?
- What downstream assets are reachable, exposed, affected, or tied to business consequence?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, or operate without direct-data access?
- Is suspect output intentionally held, and is that safeguard actually active?
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
13. **Propagation Safeguard is protective state, not defect proof.**
14. **Capability Authorization is separate from policy, responsibility, scope, and enforcement.**
15. **Raw-data access is separate from analytical visibility and operational control.**
16. **Analyst Investigation remains first-class even with restricted evidence.**
17. **Explanation is an authorized projection over evidence, not a truth source.**
18. **Monitoring must not broaden raw-data or production-control authority.**
19. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause. Competing Causal Claims can remain supported or unresolved.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, causal status, Impact, and safeguard state. Restricted nodes/evidence remain opaque rather than being retrieved and summarized behind the user's permission boundary.

If the analyst also holds a separate job-operation capability, the analyst may be permitted to retry/update a job without gaining raw-data read access. Actual action success remains separately evidenced by Deployment/Execution History.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation navigation/system of record.
- [`docs/foundation/`](docs/foundation/) — accepted foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — concept specifications and post-exit addenda.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — synchronization contracts/scenarios.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) and [`.cursor/rules/`](.cursor/rules/) — repository-agent guardrails.

## Phase direction

Phase 003 remains documentation/design-first. IAM implementation, graph/causal architecture, quarantine enforcement, service decomposition, and runtime integration choices remain deferred until later refinement/technical phases.
