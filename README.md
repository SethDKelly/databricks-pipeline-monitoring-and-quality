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

**Phase 004 — Evidence, Time, and Causality Refinement is ACTIVE. Groups 01–04 are accepted with REF-001–REF-030. Group 05 — Consolidation / Exit Review is next and has not started.**

Phase 004 Group 01 defines common evidence applicability/coverage/sufficiency rules. Group 02 defines exact temporal knowledge-cut, correction, and progressive analytical-availability semantics. Group 03 defines causal proposition/status, confirmation, multiple-contributor, progressive-RCA, and post-confirmation challenge semantics. Group 04 defines exposure/non-exposure, criterion-bound readiness, gate/safeguard enforcement, prevented-exposure, degraded-control, and control-effect evidence standards.

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

## Evidence and analysis become available progressively

The framework should return the **narrowest trustworthy result as soon as the evidence required for that result is known**, rather than forcing every answer to wait for the slowest evidence source.

Phase 004 distinguishes at least:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**.

Source event time, source availability time, framework collection/knowledge time, and derived evaluation time remain distinct where material. A Databricks completion record can therefore support a fast execution-status result before Metric View/DQ evidence is available, and RCA can deepen later as historical Lineage, Change, consumption, and analyst evidence become usable.

An early narrow answer remains scoped to its knowledge cut. `Job succeeded` never silently becomes `pipeline healthy` while quality/freshness evidence is pending. Likewise, an early leading hypothesis never becomes `confirmed root cause` merely because it is useful or fast.

Concrete latency objectives are intentionally deferred: Phase 006 defines health-result timing needs, Phase 009 characterizes actual source availability/collection behavior, Phase 010 selects fast-path/asynchronous architecture and performance budgets, and Phase 011 converts accepted timing objectives into MVP acceptance criteria.

## Causal epistemics are explicit

Causal Claims use the accepted functional statuses:

**proposed → supported / weakened / unresolved / rejected / confirmed**

with non-linear historical transitions rather than a mandatory ladder.

- **proposed** means an explicit causal proposition exists but has not been sufficiently evaluated for a stronger status;
- **supported** means applicable evidence materially supports it below confirmation;
- **weakened** means material contradiction/limitations reduce support without justifying rejection;
- **unresolved** means substantive evaluation occurred but evidence remains insufficient, conflicting, unavailable, restricted, or non-discriminating;
- **rejected** requires sufficient contradiction/exclusion evidence under the applicable claim standard—it is not simply unsupported or lower-ranked;
- **confirmed** requires an explicit claim-class confirmation profile/standard, sufficient evidence across its required dimensions, review of material contradiction/alternatives, sufficient negative-evidence coverage where relied upon, independently resolved confirmation capability/authority, and a provenance-bearing confirmation action.

Phase 004 does not grant confirmation authority. Neither a human title nor an automated process can self-authorize a confirmed cause. Phase 005 will refine who/what may confirm by subject/context without weakening the Phase 004 evidence meaning of `confirmed`.

The model does not require one root cause. B population decline and join-key degradation can both remain supported or confirmed contributors when compatible. `Primary` is a stronger comparative claim requiring comparative evidence, and qualitative causal roles never imply percentage attribution.

Confirmed claims remain challengeable. Later corrected evidence can change the current status while preserving who/what confirmed the earlier claim, under which standard and evidence cut.

## Exposure, readiness, and control proof are evidence-layered

Phase 004 Group 04 makes control and downstream encounter evidence as explicit as causal evidence.

For downstream exposure, the framework binds the **affected state/version/window**, downstream candidate, historical relationship, encounter mode, and consumer opportunity. Reachability, timing overlap, or a downstream run/refresh alone do not establish that the affected state was consumed.

`Not exposed` is a negative conclusion requiring sufficient coverage of the relevant encounter paths. A consumer may be **not exposed to the suspect version while still stale** because it refreshed from an earlier safe state. `No encounter opportunity`, `no encounter`, `safe-version encounter`, `unknown-version encounter`, unavailable/restricted evidence, and actual affected-state encounter remain distinct.

Readiness is also criterion-relative. `Upstream job succeeded` is not global readiness unless completion is the entire declared criterion. A gate can explicitly require completion, qualifying output existence, expected version/current-cycle state, freshness, publication availability, or named quality conditions. Unknown required evidence remains unknown; a fallback can govern the control response but cannot turn the prerequisite into `ready`.

Control evidence is layered:

**readiness result ≠ gate decision ≠ gate enforcement ≠ actual downstream execution**

and:

**safeguard proposal/configuration/request ≠ enforced active safeguard ≠ prevented exposure**.

A reliable downstream run during an applicable unoverridden hold contradicts full hold enforcement. By contrast, an admitted opportunity that never runs does not prove admission failed because the gate only removes its own barrier. Safeguard enforcement is specific to the protected boundary, consumer/path scope, and time; protection at one boundary does not silently prove all alternate paths were blocked.

`Prevented exposure` requires more than `safeguard active + consumer not exposed`: the safeguard must have been materially operative on the relevant encounter path, with sufficient negative consumption/version and alternate-path coverage. Blocking the suspect version does not prove the downstream result is current, fresh, or healthy.

Configured fallback behavior describes intended unavailable-state control semantics; actual fallback application/enforcement requires evidence. Missing control telemetry never proves fail-open, fail-closed, success, or failure.

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

**raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard-control authority ≠ gate-control/override authority ≠ causal-confirmation authority.**

A user may therefore:

- analyze health/root cause/downstream Impact without being allowed to query raw data;
- operate/retry/update a job under an explicit operational capability without receiving raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking authority to activate it;
- inspect why a downstream run is gated while lacking authority to override that gate;
- participate in RCA without holding authority to confirm a Causal Claim.

Responsibility Assignment, Policy Context, Classification, Monitoring Scope, repository ownership, job creator identity, and analyst role do not silently grant these capabilities.

## Downstream Impact is evidence-layered

Group 05 rejects a generic `affected` flag. For every downstream subject the model can distinguish:

1. **candidate/reachable** — historical Lineage shows a plausible downstream path;
2. **exposed/not exposed/unknown** — consumption evidence shows whether the relevant state was actually encountered;
3. **observed downstream effect** — that consumer's own Observation/Assessment/Change shows a health or operational effect;
4. **technical/analytical/business consequence** — separate evidence establishes delivery, use, process, decision, client, or other consequence;
5. **causal attribution** — if the origin, gate, or safeguard is claimed to have caused/contributed to the effect/consequence, that proposition belongs in Causal Claim.

A high-criticality or client-facing report can warrant immediate attention while remaining only reachable. Conversely, a downstream effect can be observed while consumed-version evidence remains insufficient. The model preserves these disagreements rather than forcing one `impact` answer.

An enforced safeguard can establish **prevented exposure** when the Group 04 material-control and negative-consumption/path evidence standard is satisfied. Preventing suspect-state exposure does not prove downstream delivery was fresh/healthy; the hold may itself create a separate delay/non-delivery consequence.

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

Historical causal confirmation is also reconstructable. A claim that was confirmed at incident time can later be challenged/rejected without erasing the fact that confirmation existed under the earlier evidence cut and standard.

Historical actor authorization is reconstructable evidence, but it is not reusable permission: the current requester's applicable Capability Authorization still governs current disclosure.

## Key product questions

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- What evidence coverage supports saying it ran—or did not run?
- Is a run slower than usual or violating a completion/readiness requirement?
- Was the required upstream state actually ready before this downstream run started?
- Which readiness predicates are satisfied, failed, or still unknown?
- Is the evidence sufficient for `upstream job completed` only, or also for `current qualifying output was available`?
- Is a gate merely configured, did it issue a decision, and was that decision actually enforced for this execution opportunity?
- Is the job merely being monitored, or is an explicit dependency gate active?
- If a gate is holding the run, what prerequisite is unmet, what evidence supports that, and what timeout/fallback/override semantics apply?
- What monitoring/health result is available now, what evidence is still pending, and what later analytical horizon should enrich it?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned and what prospective blast radius existed **using what was known at planning time**?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, weakened, unresolved, rejected, or confirmed?
- What confirmation profile/standard would be required to move a supported claim to confirmed, and is the confirmer actually authorized?
- Are multiple contributors compatible, and is there enough comparative evidence to call any contributor primary?
- What evidence is truly independent corroboration versus copied/common-source telemetry?
- Which downstream assets are merely reachable, actually exposed, visibly affected, or tied to evidenced business consequence?
- Did this consumer actually encounter the affected version, an earlier safe version, or an unresolved version?
- Does `not exposed` have sufficient negative consumption and alternate-path coverage, or is consumer telemetry simply missing?
- Was a safeguard merely proposed/requested or actually enforced at the relevant boundary?
- Did a safeguard materially prevent exposure, or did non-exposure occur for another reason/no encounter opportunity?
- Did protection block the suspect version while still leaving an older stale version served?
- What control/fallback behavior was configured, and what evidence shows what actually happened during a control outage?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, operate, gate, confirm, or override without direct-data access?
- What is intentionally hidden/redacted, and how does that limit the visible basis without changing internal evidence sufficiency?
- What was known, believed, authorized, gated/held/safeguarded, causally concluded, and explained at incident time?
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
14. **Readiness is criterion-relative; successful execution is not global readiness.**
15. **Gate decision is not gate enforcement or actual execution.**
16. **Safeguard proposal/request is not enforced active protection.**
17. **Prevented exposure requires material enforced control plus sufficient negative/path coverage.**
18. **Lineage discovers relationships/candidates, not cause.**
19. **First-observed localization is not root cause.**
20. **Causal propositions and epistemic status remain explicit.**
21. **Leading/supported hypothesis is not confirmed cause.**
22. **Multiple contributors and unresolved outcomes are valid; one root cause is not required.**
23. **Causal contribution does not imply percentage attribution; primary cause requires comparative evidence.**
24. **Confirmed causes require an explicit evidence profile/standard plus separately resolved confirmation authority.**
25. **Confirmed claims remain challengeable without rewriting historical confirmation.**
26. **Prospective Impact is not actual Impact or retrospective cause.**
27. **Actual Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
28. **Non-exposure requires negative consumption/path evidence; missing telemetry is not reassurance.**
29. **Criticality influences priority, not evidence strength.**
30. **Propagation Safeguard is protective state, not defect proof.**
31. **Capability Authorization is separate from policy, responsibility, scope, and enforcement.**
32. **Raw-data access is separate from analytical visibility, operational control, and causal-confirmation authority.**
33. **Analyst Investigation remains first-class even with restricted evidence.**
34. **Annotation is attributed context, not a shadow truth store.**
35. **Explanation consumes the authorized analytical projection; it is not a truth or authorization source.**
36. **Actual historical state remains distinct from replay-derived reconstruction.**
37. **Late evidence can revise retrospective knowledge without rewriting what was known then.**
38. **Actual historical control actions are not counterfactually rewritten.**
39. **Historical authorization is not current disclosure permission.**
40. **Monitoring must not broaden raw-data or production-control authority.**
41. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause.

Phase 004 requires the reasoning to state what each evidence item can actually support. A B row-count Observation must match the relevant B output/window/grain before it bears on the hypothesis. Evidence that B did not change requires adequate opportunity-to-observe and coverage of the proposed B mechanism; absence of an alert is insufficient. Mirrored copies of one Databricks event do not become independent corroboration.

Causal claims are explicit. `B's reduced population contributed to C row loss` and `elevated join-key nulls contributed to C row loss` can both become supported when their evidence warrants it. A recent Deployment can remain a competing claim; if sufficiently covered evidence shows C degradation began before Deployment activation, that claim may be weakened or rejected. No single root cause is forced, and neither contributor is called primary without comparative evidence.

A supported claim can be useful before confirmation. `Confirmed` requires the applicable claim-class confirmation profile plus separately resolved confirmation authority; an analyst, administrator, or automated process does not gain confirmation authority merely by participating in RCA.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, causal status, Impact, safeguard/gate state, and Annotation. Restricted nodes/evidence remain opaque rather than being retrieved and summarized behind the user's permission boundary.

Before C runs, an optional Execution Gate could require the current A and B outputs to be ready. If B is late, C may be held instead of blindly joining A-current + B-stale. If the criterion requires B's current output and freshness, a successful B run alone does not satisfy the gate. A hold decision is still distinct from evidence that the external control actually suppressed C. If reliable Execution History shows C started during an unoverridden hold, full hold enforcement is contradicted. If the gate admits C but C never starts, admission can still be valid because another scheduler/compute condition may have prevented execution.

Downstream, a Metric View and two reports may all be reachable. Version/refresh evidence can establish that one report consumed the affected C output, another refreshed from an earlier safe version, and a third remains exposure-unknown. The safe-version report can be `not exposed to affected V` while still stale. A report's own metric failure is observed downstream effect; a client delivery/decision consequence requires separate evidence; saying C caused that effect requires Causal Claim.

If an enforced safeguard blocks the suspect version before a client report refreshes, Impact may establish prevented exposure only when the safeguard was materially operative on the encounter path and negative-consumption/alternate-path coverage is sufficient. If the report never had a relevant refresh opportunity, the correct statement may instead be `safeguard active; consumer not exposed`, without claiming the safeguard prevented exposure. Any older state still being served remains separately assessed for freshness.

If downstream consumption, enforcement, or corrected timing evidence arrives late, the historical incident-time view remains what was known then while current readiness/exposure/prevention/causal status may change. Actual historical gate/safeguard decisions and executions are never rewritten.

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

**Phase 004 is active. Groups 01–04 are accepted with REF-001–REF-030. Group 05 — Consolidation / Exit Review is next and has not started.** Group 05 will verify that evidence applicability/coverage, temporal replay, causal confirmation, exposure/non-exposure, criterion-bound readiness, gate/safeguard enforcement, degraded-control, and progressive-result semantics compose across the accepted ecosystem scenarios before Phase 004 exits.
