# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, authorization, planned/realized change history, causal evidence, downstream business impact, protective propagation state, optional dependency-aware execution control, and historical evolution of knowledge** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, whether an upstream prerequisite was actually ready before a downstream run, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually reachable/exposed/affected, what consequences are evidenced, what policies/restrictions apply, who is responsible, what the analyst is authorized to inspect or operate, and **what was known/authorized/controlled/explained at an earlier point compared with what is known now**.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE**

Phase 002 originally completed with 20 retained concepts. Later requirements exposed three missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state;
- **Execution Gate** — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness.

The current catalog contains **23 accepted concepts**.

**Groups 01–06 are accepted. The accepted synchronization range is SYN-001–SYN-035, and E-01–E-22 pass end-to-end historical/consolidation review.**

**Phase 004 — Evidence, Time, and Causality Refinement is ACTIVE. Group 01 — Evidence Sufficiency, Coverage & Negative Evidence is accepted with REF-001–REF-005. Group 02 — Event/Effective Time, Knowledge Cut & Correction is next and has not started.**

Group 05 formalized layered downstream Impact, evidence-backed exposure/non-exposure, observed downstream effects, consequence evidence, safeguard-prevented exposure, Annotation boundaries, Capability Authorization-based analytical projection, and audience-specific Explanation without direct-data-access assumptions. The pre-Group-06 refinement added explicit separation between passive monitoring and optional active dependency gating. Group 06 completed bitemporal historical replay and the Phase 003 exit review. Phase 004 Group 01 now defines the common evidence-applicability/coverage/sufficiency standard used to refine those conclusions safely.

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but too late, use stale inputs, lose rows through a join, experience a source-shape change, legitimately change population under planned logic, threaten downstream client delivery, or produce an output risky enough to hold while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, data quality, planned intent, realized change, historical topology, governance, authorization, causality, downstream consequence, human investigation, optional execution gating, protective propagation control, and evolving knowledge over time as related but distinct concerns**.

## Evidence sufficiency is conclusion-specific

Phase 004 rejects a universal `evidence confidence` or `trust` score. Evidence is adequate only relative to a **defined proposition, context, time, grain/version, and intended conclusion strength**.

The framework therefore separates:

1. **evidence applicability** — does the evidence actually bear on this subject/property/time/version proposition?;
2. **coverage** — what bounded observation opportunities, population/partitions, source/query scope, versions/consumers, and intervals were actually observable?;
3. **corroboration/conflict** — are multiple items independent, complementary, duplicated/common-source, non-comparable, or contradictory?;
4. **conclusion-specific sufficiency** — is that evidence set adequate for this exact conclusion under its applicable standard?

This creates deliberate asymmetry between many positive and negative claims. One directly observed qualifying output may establish that an output exists. Saying **no qualifying output exists** generally requires a mechanism capable of observing every relevant bounded output opportunity plus enough coverage to rule them out.

Accordingly:

**no telemetry ≠ no event**  
**query failure ≠ zero results**  
**evidence not found ≠ observed absence**  
**source count ≠ independent corroboration**  
**sufficient for one conclusion ≠ sufficient for every related conclusion**

This evidence-strength model is internal to the product truth model. Capability Authorization still independently determines what basis details a requester may inspect.

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

## Historical replay is bitemporal and non-rewriting

Group 06 formalizes historical replay around two independent coordinates:

- **event/effective time** — when the questioned condition/event/state applied;
- **recorded/knowledge cutoff** — which evidence/assertions the ecosystem was allowed to know for that historical view.

The same event window can therefore support multiple valid perspectives:

- **what happened**;
- **what was known then**;
- **what was actually assessed/believed then**;
- **what was authorized then**;
- **what gate/safeguard control state or action actually applied then**;
- **what was actually explained then**;
- **what is known retrospectively now**.

Late or corrected evidence can change the current retrospective conclusion without rewriting the contemporaneous record. Evidence discovered tomorrow but effective yesterday does not belong in yesterday's `as-known-then` view.

A historical gate hold, admission, override, safeguard activation, or release remains the actual action that occurred even if later evidence shows a different action would now be preferred. Historical replay is not a counterfactual rewrite.

Similarly, later realized Lineage, exposure, Impact, or causal evidence cannot be backfilled into an earlier Prospective Impact Profile as though it was known before deployment.

A current system may generate an `as-known-then` explanation from the historical state cut. That answer is explicitly **reconstructed** unless an actual retained Explanation/report proves what was communicated at the time.

Historical actor authorization is reconstructable evidence, but it is not reusable permission: the current requester's applicable Capability Authorization still governs current disclosure.

## Key product questions

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- What evidence coverage supports saying it ran—or did not run?
- Is a run slower than usual or violating a completion/readiness requirement?
- Was the required upstream state actually ready before this downstream run started?
- Is the evidence sufficient for `upstream job completed` only, or also for `current qualifying output was available`?
- Is the job merely being monitored, or is an explicit dependency gate active?
- If a gate is holding the run, what prerequisite is unmet, what evidence supports that, and what timeout/fallback/override semantics apply?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned and what prospective blast radius existed **using what was known at planning time**?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, contradicted, rejected, or unresolved?
- What evidence is truly independent corroboration versus copied/common-source telemetry?
- Which downstream assets are merely reachable, actually exposed, visibly affected, or tied to evidenced business consequence?
- Does `not exposed` have sufficient negative consumption coverage, or is consumer telemetry simply missing?
- Did a safeguard actually prevent a suspect state from reaching a consumer, and did the safeguard create a separate delay?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, operate, gate, or override without direct-data access?
- What is intentionally hidden/redacted, and how does that limit the visible basis without changing internal evidence sufficiency?
- What was known, believed, authorized, gated/held/safeguarded, and explained at incident time?
- What changed in the retrospective conclusion after late/corrected evidence arrived?
- Is this historical Explanation an actual retained artifact or a present reconstruction?

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
3. **Time/history are first-class; event time and knowledge time remain distinct.**
4. **Evidence over narrative completion.**
5. **Evidence sufficiency is proposition- and conclusion-specific, not a universal score.**
6. **Negative evidence requires opportunity-to-observe plus sufficient bounded coverage.**
7. **Expectation is normative; Baseline is descriptive.**
8. **Observation is not Assessment.**
9. **Successful execution is not timely execution, freshness, or data quality.**
10. **Passive monitoring is non-blocking by default.**
11. **Baseline monitoring prefers production-repository independence.**
12. **Execution gating is explicit opt-in control, not an automatic effect of monitoring or Lineage.**
13. **Execution Gate is separate from Execution History and Propagation Safeguard.**
14. **Lineage discovers relationships/candidates, not cause.**
15. **First-observed localization is not root cause.**
16. **Causal claims remain epistemically explicit.**
17. **Multiple contributors and unresolved outcomes are valid.**
18. **Prospective Impact is not actual Impact or retrospective cause.**
19. **Actual Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
20. **Criticality influences priority, not evidence strength.**
21. **Propagation Safeguard is protective state, not defect proof; prevented exposure requires enforcement evidence.**
22. **Capability Authorization is separate from policy, responsibility, scope, and enforcement.**
23. **Raw-data access is separate from analytical visibility and operational control.**
24. **Analyst Investigation remains first-class even with restricted evidence.**
25. **Annotation is attributed context, not a shadow truth store.**
26. **Explanation consumes the authorized analytical projection; it is not a truth or authorization source.**
27. **Actual historical state remains distinct from replay-derived reconstruction.**
28. **Late evidence can revise retrospective knowledge without rewriting what was known then.**
29. **Actual historical control actions are not counterfactually rewritten.**
30. **Historical authorization is not current disclosure permission.**
31. **Monitoring must not broaden raw-data or production-control authority.**
32. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause. Competing Causal Claims can remain supported or unresolved.

Phase 004 requires the reasoning to state what each evidence item can actually support. A B row-count Observation must match the relevant B output/window/grain before it bears on the hypothesis. Evidence that B did not change requires adequate opportunity-to-observe and coverage of the proposed B mechanism; absence of an alert is insufficient. Mirrored copies of one Databricks event do not become independent corroboration.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, causal status, Impact, safeguard/gate state, and Annotation. Restricted nodes/evidence remain opaque rather than being retrieved and summarized behind the user's permission boundary.

Before C runs, an optional Execution Gate could require the current A and B outputs to be ready. If B is late, C may be held instead of blindly joining A-current + B-stale. The hold may prevent stale recomputation while also threatening C's completion/client-delivery deadline. If no gate is enabled, monitoring remains observational and C proceeds according to its existing production schedule/orchestration.

Downstream, a Metric View and two reports may all be reachable. Version/refresh evidence can establish that one report consumed the affected C output, another did not, and a third remains exposure-unknown. A report's own metric failure is observed downstream effect; a client delivery/decision consequence requires separate evidence; saying C caused that effect requires Causal Claim.

If an enforced safeguard blocks the suspect version before a client report refreshes, Impact may establish prevented exposure while still assessing any delivery lateness caused by the hold. If the analyst also holds a separate job-operation capability, the analyst may be permitted to retry/update a job without gaining raw-data read access. Actual action success remains separately evidenced by Deployment/Execution History.

If downstream consumption evidence arrives late, the historical 08:15 view may correctly remain `exposure unknown` while the current retrospective view becomes `exposed`. Both are valid because they answer different knowledge-cut questions. The later evidence does not rewrite what responders knew or what the system actually explained at 08:15.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation navigation/system of record.
- [`docs/foundation/`](docs/foundation/) — accepted foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — concept specifications and post-exit addenda.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — completed synchronization contracts/scenarios and exit review.
- [`docs/concepts/phase_004/`](docs/concepts/phase_004/) — active evidence/time/causality refinement contracts.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) and [`.cursor/rules/`](.cursor/rules/) — repository-agent guardrails.

## Phase direction

**Phase 004 is active. Group 01 — Evidence Sufficiency, Coverage & Negative Evidence is accepted. Group 02 — Event/Effective Time, Knowledge Cut & Correction is next and has not started.** Later Phase 004 groups will refine causal confirmation and exposure/readiness/control proof before Phase 004 consolidation and handoff to governance, health, Lineage/Impact/control, Explanation, integration, and technical phases.
