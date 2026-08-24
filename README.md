# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, authorization, planned/realized change history, causal evidence, downstream business impact, protective propagation state, and optional dependency-aware execution control** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, whether an upstream prerequisite was actually ready before a downstream run, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually reachable/exposed/affected, what consequences are evidenced, what policies/restrictions apply, who is responsible, what the analyst is authorized to inspect or operate, and what evidence supports each conclusion.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: ACTIVE**

Phase 002 originally completed with 20 retained concepts. Later requirements exposed three missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state;
- **Execution Gate** — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness.

The current catalog contains **23 accepted concepts**.

**Groups 01–05 are accepted. SYN-032 — Dependency Readiness Evidence → Execution Gate Admission is accepted as a later Group 03 extension. Group 06 — Historical Replay & Phase 003 Consolidation is next and has not started.**

Group 05 formalized layered downstream Impact, evidence-backed exposure/non-exposure, observed downstream effects, consequence evidence, safeguard-prevented exposure, Annotation boundaries, Capability Authorization-based analytical projection, and audience-specific Explanation without direct-data-access assumptions. The pre-Group-06 refinement adds explicit separation between passive monitoring and optional active dependency gating.

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but too late, use stale inputs, lose rows through a join, experience a source-shape change, legitimately change population under planned logic, threaten downstream client delivery, or produce an output risky enough to hold while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, data quality, planned intent, realized change, historical topology, governance, authorization, causality, downstream consequence, human investigation, optional execution gating, and protective propagation control as related but distinct concerns**.

## Passive monitoring should not become production overhead

The default monitoring/quality framework should be **out-of-band and non-blocking**. Monitoring collection, analysis, Investigation, Impact reasoning, and Explanation should not add meaningful production-path latency or become a production availability dependency simply because a job is monitored.

Baseline integration should prefer Databricks/platform/source metadata and independently deployed monitoring components rather than requiring framework code, libraries, or monitoring workflow steps to be added to every production ETL repository or its GitHub Actions deployment process.

This is an architectural objective, not a claim that no specialized future integration will ever require source changes. If a future capability cannot be realized without production changes, that exception should be explicit, minimal, and justified.

## Dependency-aware execution control is optional

A pure time-based schedule can create stale downstream output when an upstream dependency runs late. The accepted model therefore includes an optional **Execution Gate**.

When no gate is enabled, the framework remains observational: it can report that C started before A/B were ready and later evaluate freshness/readiness consequences, but it does not delay C.

When an explicit gate is enabled, a downstream execution opportunity can be:

- **held** while a prerequisite is not ready;
- **admitted** once the declared readiness criterion is met;
- **overridden** by an independently authorized actor/control path without pretending readiness was satisfied;
- subject to an explicit timeout/fallback/escalation rule when readiness/control evidence is unavailable.

A readiness criterion may require more than `upstream job ran`. Depending on the declared gate, it may require a qualifying current-cycle output, freshness, version, completion, or another accepted readiness condition.

**Execution Gate ≠ Propagation Safeguard.** Execution Gate protects the **downstream start/admission boundary**. Propagation Safeguard protects the **output/consumption boundary**. A gate may prevent stale recomputation before execution; a safeguard may quarantine/hold suspect or missing output after or around execution. Both may create intentional delay that remains observable and assessable.

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
- Execution Gate state such as `waiting on prerequisite` where independently authorized;
- human Annotation where independently permitted.

That **Authorized Analytical Projection** can support meaningful root-cause and downstream-impact analysis without direct data access. It must preserve redaction, missing evidence, and authorization-limited confidence rather than pretending hidden evidence does not exist.

Metadata and derived evidence are **not automatically unrestricted**. Counts, thresholds, table names, Lineage, policy labels, responsibility information, business consequences, safeguard/gate details, and causal conclusions can themselves be sensitive.

## Capability separation

The accepted model distinguishes at least:

**raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard-control authority ≠ gate-control/override authority.**

A user may therefore:

- analyze health/root cause/downstream Impact without being allowed to query raw data;
- operate/retry/update a job under an explicit operational capability without receiving raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking authority to activate it;
- inspect why a downstream run is gated while lacking authority to override that gate.

Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, and job creator identity do not silently grant these capabilities.

## Downstream Impact is evidence-layered

Group 05 rejects a generic `affected` flag. For every downstream subject the model can distinguish:

1. **candidate/reachable** — historical Lineage shows a plausible downstream path;
2. **exposed/not exposed/unknown** — consumption evidence shows whether the relevant state was actually encountered;
3. **observed downstream effect** — that consumer's own Observation/Assessment/Change shows a health or operational effect;
4. **technical/analytical/business consequence** — separate evidence establishes delivery, use, process, decision, client, or other consequence;
5. **causal attribution** — if the origin, gate, or safeguard is claimed to have caused/contributed to the effect/consequence, that proposition belongs in Causal Claim.

A high-criticality or client-facing report can warrant immediate attention while remaining only reachable. Conversely, a downstream effect can be observed while consumed-version evidence remains insufficient. The model preserves these disagreements rather than forcing one `impact` answer.

An enforced safeguard can establish **prevented exposure** when enforcement and negative-consumption evidence are sufficient. Preventing suspect-state exposure does not prove downstream delivery was fresh/healthy; the hold may itself create a separate delay/non-delivery consequence.

## Key product questions

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- Is a run slower than usual or violating a completion/readiness requirement?
- Was the required upstream state actually ready before this downstream run started?
- Is the job merely being monitored, or is an explicit dependency gate active?
- If a gate is holding the run, what prerequisite is unmet, what evidence supports that, and what timeout/fallback/override semantics apply?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned and what prospective blast radius exists?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, contradicted, rejected, or unresolved?
- Which downstream assets are merely reachable, actually exposed, visibly affected, or tied to evidenced business consequence?
- Did a safeguard actually prevent a suspect state from reaching a consumer, and did the safeguard create a separate delay?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, operate, gate, or override without direct-data access?
- What is intentionally hidden/redacted, and how does that limit confidence?
- What was known, authorized, gated, held, or explained at incident time versus what is known/allowed retrospectively?

## Operating environment

Known environment facts remain deliberately small:

- Spark ETL pipelines execute in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a key execution and metadata source;
- Databricks Metric Views and DQX are strongly favored later evaluations;
- Collibra and Immuta are available but optional.

These are environmental facts, not implementation architecture. The monitoring framework should remain independently deployed from the production repositories/GitHub Actions unless a later accepted control/integration requirement explicitly needs otherwise.

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.**
3. **Time/history are first-class.**
4. **Evidence over narrative completion.**
5. **Expectation is normative; Baseline is descriptive.**
6. **Observation is not Assessment.**
7. **Successful execution is not timely execution, freshness, or data quality.**
8. **Passive monitoring is non-blocking by default.**
9. **Baseline monitoring prefers production-repository independence.**
10. **Execution gating is explicit opt-in control, not an automatic effect of monitoring or Lineage.**
11. **Execution Gate is separate from Execution History and Propagation Safeguard.**
12. **Lineage discovers relationships/candidates, not cause.**
13. **First-observed localization is not root cause.**
14. **Causal claims remain epistemically explicit.**
15. **Multiple contributors and unresolved outcomes are valid.**
16. **Prospective Impact is not actual Impact or retrospective cause.**
17. **Actual Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
18. **Criticality influences priority, not evidence strength.**
19. **Propagation Safeguard is protective state, not defect proof; prevented exposure requires enforcement evidence.**
20. **Capability Authorization is separate from policy, responsibility, scope, and enforcement.**
21. **Raw-data access is separate from analytical visibility and operational control.**
22. **Analyst Investigation remains first-class even with restricted evidence.**
23. **Annotation is attributed context, not a shadow truth store.**
24. **Explanation consumes the authorized analytical projection; it is not a truth or authorization source.**
25. **Monitoring must not broaden raw-data or production-control authority.**
26. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause. Competing Causal Claims can remain supported or unresolved.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, causal status, Impact, safeguard/gate state, and Annotation. Restricted nodes/evidence remain opaque rather than being retrieved and summarized behind the user's permission boundary.

Before C runs, an optional Execution Gate could require the current A and B outputs to be ready. If B is late, C may be held instead of blindly joining A-current + B-stale. The hold may prevent stale recomputation while also threatening C's completion/client-delivery deadline. If no gate is enabled, monitoring remains observational and C proceeds according to its existing production schedule/orchestration.

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

Phase 003 remains documentation/design-first. **Group 06 is next and will consolidate E-01–E-22 across the 23 concepts and SYN-001–SYN-032.** IAM implementation, graph/causal architecture, quarantine enforcement, scheduler/gate implementation, service decomposition, and runtime integration choices remain deferred until later refinement/technical phases.
