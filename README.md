# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, assertion authority, authorization, planned/realized change history, causal evidence, downstream business impact, protective propagation state, optional dependency-aware execution control, and historical evolution of knowledge** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, whether an upstream prerequisite was actually ready before a downstream run, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually reachable/exposed/affected, what consequences are evidenced, which assertions are authoritative, what policies/restrictions apply, who is responsible, what normative health rules govern the result, what the analyst is authorized to inspect or operate, and **what was known/authoritative/authorized/controlled/explained at an earlier point compared with what is known now**.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE**

Phase 002 originally completed with 20 retained concepts. Later requirements exposed four missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state;
- **Execution Gate** — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness;
- **Assertion Authority** — target/context/time-scoped source/actor standing and authority-rule history for governance assertions.

The current catalog contains **24 accepted concepts**.

**Groups 01–06 are accepted. The accepted synchronization range is SYN-001–SYN-035, and E-01–E-22 pass end-to-end historical/consolidation review.**

**Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE. Groups 01–05 are accepted with REF-001–REF-030.**

Phase 004 Group 01 defines common evidence applicability/coverage/sufficiency rules. Group 02 defines exact temporal knowledge-cut, correction, and progressive analytical-availability semantics. Group 03 defines causal proposition/status, confirmation, multiple-contributor, progressive-RCA, and post-confirmation challenge semantics. Group 04 defines exposure/non-exposure, criterion-bound readiness, gate/safeguard enforcement, prevented-exposure, degraded-control, and control-effect evidence standards. Group 05 consolidates REF-001–REF-030 across E-01–E-22 and the Phase 004 scenario suites and accepts the Phase 004 exit without another synchronization or refinement contract.

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is ACTIVE. Groups 01–03 are accepted with AUTH-001–AUTH-023. Group 04 — Capability Authorization & Restricted Analytical Visibility is next and has not started.**

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but too late, use stale inputs, lose rows through a join, experience a source-shape change, legitimately change population under planned logic, threaten downstream client delivery, or produce an output risky enough to hold while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, structural/schema compatibility, data quality, planned intent, realized change, historical topology, governance, assertion authority, normative health authority, authorization, causality, downstream consequence, human investigation, optional execution gating, protective propagation control, and evolving knowledge over time as related but distinct concerns**.

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

This evidence-strength model is internal to the product truth model. Assertion Authority can resolve which governance assertion has standing, but it cannot make insufficient operational evidence sufficient. Capability Authorization still independently determines what basis details a requester may inspect.

## Evidence and analysis become available progressively

The framework should return the **narrowest trustworthy result as soon as the evidence required for that result is known**, rather than forcing every answer to wait for the slowest evidence source.

Phase 004 distinguishes at least:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**.

Source event time, source availability time, framework collection/knowledge time, and derived evaluation time remain distinct where material. A Databricks completion record can therefore support a fast execution-status result before schema/Metric View/DQ evidence is available, and RCA can deepen later as historical Lineage, Change, consumption, and analyst evidence become usable.

An early narrow answer remains scoped to its knowledge cut. `Job succeeded` never silently becomes `pipeline healthy` while quality/freshness/schema evidence is pending. Likewise, an early leading hypothesis never becomes `confirmed root cause` merely because it is useful or fast.

Concrete latency objectives are intentionally deferred: Phase 006 defines health-result timing needs, Phase 009 characterizes actual source availability/collection behavior, Phase 010 selects fast-path/asynchronous architecture and performance budgets, and Phase 011 converts accepted timing objectives into MVP acceptance criteria.

## Causal epistemics are explicit

Causal Claims use the accepted functional statuses:

**proposed → supported / weakened / unresolved / rejected / confirmed**

with non-linear historical transitions rather than a mandatory ladder.

- **proposed** means an explicit causal proposition exists but has not yet received enough evaluation to justify a stronger status;
- **supported** means applicable evidence materially supports it below confirmation;
- **weakened** means material contradiction/limitations reduce support without justifying rejection;
- **unresolved** means substantive evaluation occurred but evidence remains insufficient, conflicting, unavailable, restricted, or non-discriminating;
- **rejected** requires sufficient contradiction/exclusion evidence under the applicable claim standard—it is not simply unsupported or lower-ranked;
- **confirmed** requires an explicit claim-class confirmation profile/standard, sufficient evidence across its required dimensions, review of material contradiction/alternatives, sufficient negative-evidence coverage where relied upon, independently resolved confirmation capability/authority, and a provenance-bearing confirmation action.

Phase 004 defines the evidence meaning of confirmation but does not grant confirmation authority. Phase 005 later groups refine who/what may confirm by subject/context without weakening that evidence meaning.

The model does not require one root cause. B population decline and join-key degradation can both remain supported or confirmed contributors when compatible. `Primary` is a stronger comparative claim requiring comparative evidence, and qualitative causal roles never imply percentage attribution.

Confirmed claims remain challengeable. Later corrected evidence can change the current status while preserving who/what confirmed the earlier claim, under which standard and evidence cut.

## Exposure, readiness, and control proof are evidence-layered

Phase 004 Group 04 makes control and downstream encounter evidence as explicit as causal evidence.

For downstream exposure, the framework binds the **affected state/version/window**, downstream candidate, historical relationship, encounter mode, and consumer opportunity. Reachability, timing overlap, or a downstream run/refresh alone do not establish that the affected state was consumed.

`Not exposed` is a negative conclusion requiring sufficient coverage of the relevant encounter paths. A consumer may be **not exposed to the suspect version while still stale** because it refreshed from an earlier safe state. `No encounter opportunity`, `no encounter`, `safe-version encounter`, `unknown-version encounter`, unavailable/restricted evidence, and actual affected-state encounter remain distinct.

Readiness is also criterion-relative. `Upstream job succeeded` is not global readiness unless completion is the entire declared criterion. A gate can explicitly require completion, qualifying output existence, expected version/current-cycle state, freshness, publication availability, schema compatibility, or named quality conditions. Unknown required evidence remains unknown; a fallback can govern the control response but cannot turn the prerequisite into `ready`.

Control evidence is layered:

**readiness result ≠ gate decision ≠ gate enforcement ≠ actual downstream execution**

and:

**safeguard proposal/configuration/request ≠ enforced active safeguard ≠ prevented exposure**.

A reliable downstream run during an applicable unoverridden hold contradicts full hold enforcement. By contrast, an admitted opportunity that never runs does not prove admission failed because the gate only removes its own barrier. Safeguard enforcement is specific to the protected boundary, consumer/path scope, and time; protection at one boundary does not silently prove all alternate paths were blocked.

`Prevented exposure` requires more than `safeguard active + consumer not exposed`: the safeguard must have been materially operative on the relevant encounter path, with sufficient negative consumption/version and alternate-path coverage. Blocking the suspect version does not prove the downstream result is current, fresh, or healthy.

Configured fallback behavior describes intended unavailable-state control semantics; actual fallback application/enforcement requires evidence. Missing control telemetry never proves fail-open, fail-closed, success, or failure.

## Assertion Authority is explicit and scoped

Phase 005 Group 01 accepts **Assertion Authority** as the 24th concept because multiple assertion-owning concepts repeatedly required the same independent source-standing, precedence, conflict, correction, and historical-resolution behavior.

It answers:

> Which source, actor, role, or governed process has authoritative standing for this exact assertion category/facet/subject scope/context/time?

It does **not** answer whether the assertion is factually infallible, whether operational evidence is sufficient, whether the principal is permitted to perform an action, or whether an external control actually enforced something.

The model distinguishes:

- **source assertion** — a provenance-bearing contribution regardless of standing;
- **authority target** — the bounded concept/category/facet/scheme/type + subject scope/context/time being resolved;
- **authority holder** — source/actor/role/governed process referenced by an authority rule;
- **authority rule** — provenance-bearing standing/condition/precedence/fallback rule;
- **authoritative assertion** — assertion from a holder with authoritative standing for the target;
- **advisory assertion** — useful context/challenge that cannot displace authoritative state;
- **resolved assertion disagreement** — disagreement remains recorded but authority rules yield an authoritative resolution;
- **authoritative assertion conflict** — simultaneously authoritative assertions disagree and no resolver applies;
- **authority-rule conflict** — authority rules themselves disagree and no accepted governing rule resolves them;
- **authority unknown/unavailable** — no applicable accepted rule can be established or required authority-rule evidence is unavailable.

No hidden precedence is allowed. The following do not make a source authoritative unless an explicit applicable rule says so:

**source count/majority, recency alone, synchronization or ingestion order, source availability, repository ownership, job creator/admin/title, Responsibility Assignment, or apparent scope specificity.**

Sole authority, co-authority, ordered precedence, and conditional/fallback authority are allowed only through explicit accepted rules. Co-authoritative disagreement remains conflict unless another resolver applies. Fallback authority requires both an explicit rule and evidence that its activation condition holds.

Authority rules themselves require provenance and an accepted governing basis; a source or rule cannot self-promote merely by asserting its own authority. Authority history is bitemporal: a later correction can change current retrospective resolution without changing what source the framework considered authoritative at an earlier knowledge cutoff.

## Semantic and schema governance are facet-specific

Phase 005 Group 02 applies Assertion Authority to Semantic Definition, Responsibility Assignment, Classification/criticality, and Policy Context without changing their truth ownership.

A governed technical schema declaration, key/grain meaning, business definition, responsibility assignment, criticality label, and policy-applicability assertion can legitimately have different authoritative holders. The project preserves:

**declared/governed schema meaning ≠ normative schema contract ≠ realized schema state ≠ compatibility Assessment**.

A runtime schema observation does not become authoritative business meaning merely because Databricks/Unity Catalog can expose it. Likewise, a declared business key does not prove uniqueness/nullability health. Local/context governance does not automatically override broader governance, and governance assertions do not recursively propagate through Lineage or containment without explicit provenance and standing.

## Normative health governance is layered

Phase 005 Group 03 accepts **AUTH-016–AUTH-023** without adding a new concept.

It preserves:

**metric/schema meaning → metric-profile selection → normative Expectation → threshold/margin → severity → waiver/exception → high-consequence-use eligibility → later control capability/enforcement**.

Those layers may have different authoritative holders. A metric being easy to compute does not justify placing it in every asset profile; governed inclusion should have purpose, applicability, intended use/audience, authority/owner, and lifecycle/retirement context.

Baseline remains descriptive. A Baseline-derived range becomes normative only through an explicit authoritative Expectation. Structural/schema compatibility rules are likewise normative: governed schema meaning and realized structure do not by themselves decide whether an additive field, type change, nullability change, or key/grain transition is acceptable for a particular consumer.

A bounded waiver/exception changes normative applicability or required response. It does not rewrite the Observation, realized schema, Baseline deviation, or historical evidence, and should not be presented as a fictional clean `pass`.

Normative conflict remains explicit. `Strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and recency are not implicit resolvers.

High-consequence use is separately governed. An authoritative or business-critical metric does not automatically become an Execution Gate/safeguard predicate. Explicit eligibility is required, and even then:

**control-use eligibility ≠ control capability ≠ evidence readiness ≠ enforcement**.

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

A readiness criterion may require more than `upstream job ran`. Depending on the declared gate, it may require a qualifying current-cycle output, freshness, version, completion, schema compatibility, or another accepted readiness condition.

**Execution Gate ≠ Propagation Safeguard.** Execution Gate protects the **downstream start/admission boundary**. Propagation Safeguard protects the **output/consumption boundary**. A gate may prevent stale recomputation before execution; a safeguard may quarantine/hold suspect or missing output after or around execution. Both may create intentional delay that remains observable and assessable.

Group 03 adds one prerequisite governance layer: a metric/Expectation must be explicitly eligible for high-consequence use before it can be used as a control predicate. That eligibility still does not enable/configure the gate, grant override authority, prove evidence availability, or prove enforcement.

## Restricted-data analysis is a core capability

The product must not equate **lack of direct row access** with **lack of monitoring or RCA access**.

An analyst may be denied Table C rows or sensitive columns while being permitted to inspect approved:

- pipeline/job execution status, duration, readiness, and freshness;
- aggregate table/pipeline health metrics and Assessments;
- safe Expectation/Baseline/waiver result state;
- safe schema-compatibility status;
- Semantic Definition at an authorized abstraction;
- Responsibility Assignment/team contact;
- Classification and Policy Context/restriction summaries;
- authorized Assertion Authority standing or safe authority-conflict state;
- historical Lineage with redacted or opaque restricted nodes;
- Investigation and Causal Claim status/evidence limitations;
- downstream Impact and Propagation Safeguard state;
- Execution Gate state such as `waiting on prerequisite` where independently authorized;
- human Annotation where independently permitted.

That **Authorized Analytical Projection** can support meaningful root-cause and downstream-impact analysis without direct data access. It must preserve redaction, missing evidence, authority limitations, and authorization-limited confidence rather than pretending hidden evidence does not exist.

Metadata and derived evidence are **not automatically unrestricted**. Counts, thresholds, schemas, table names, Lineage, policy labels, responsibility information, authority-holder/basis details, business consequences, safeguard/gate details, and causal conclusions can themselves be sensitive.

## Capability separation

The accepted model distinguishes:

**Assertion Authority ≠ Capability Authorization**

and at least:

**raw-data read authorization ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard-control authority ≠ gate-control/override authority ≠ causal-confirmation authority.**

A user may therefore:

- submit/edit an assertion under an explicit capability while the assertion remains advisory;
- analyze health/root cause/downstream Impact without being allowed to query raw data;
- operate/retry/update a job under an explicit operational capability without receiving raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking authority to activate it;
- inspect why a downstream run is gated while lacking authority to override that gate;
- participate in RCA without holding authority to confirm a Causal Claim.

Responsibility Assignment, Assertion Authority, Policy Context, Classification, Monitoring Scope, repository ownership, job creator identity, and analyst role do not silently grant capabilities. Likewise, Capability Authorization to edit does not silently grant Assertion Authority.

Group 04 will further refine permission to view/propose/edit/approve/waive/retire normative metric/schema state without conflating those capabilities with the authoritative standing accepted in Group 03.

## Downstream Impact is evidence-layered

For every downstream subject the model can distinguish:

1. **candidate/reachable** — historical Lineage shows a plausible downstream path;
2. **exposed/not exposed/unknown** — consumption evidence shows whether the relevant state was actually encountered;
3. **observed downstream effect** — the consumer's own Observation/Assessment/Change shows a health or operational effect;
4. **technical/analytical/business consequence** — separate evidence establishes delivery, use, process, decision, client, or other consequence;
5. **causal attribution** — if the origin, gate, or safeguard is claimed to have caused/contributed to the effect/consequence, that proposition belongs in Causal Claim.

A high-criticality or client-facing report can warrant immediate attention while remaining only reachable. Conversely, a downstream effect can be observed while consumed-version evidence remains insufficient. The model preserves these disagreements rather than forcing one `impact` answer.

An enforced safeguard can establish **prevented exposure** when the Phase 004 material-control and negative-consumption/path evidence standard is satisfied. Preventing suspect-state exposure does not prove downstream delivery was fresh/healthy; the hold may itself create a separate delay/non-delivery consequence.

## Historical replay is bitemporal and non-rewriting

Historical replay is organized around two independent coordinates:

- **event/effective time** — when the questioned condition/event/state applied;
- **recorded/knowledge cutoff** — which evidence/assertions/authority/normative rules the ecosystem was allowed to know for that historical view.

The same event window can therefore support multiple valid perspectives:

- **what happened**;
- **what was known then**;
- **what assertion/source was considered authoritative then**;
- **what normative threshold/waiver/profile state applied then**;
- **what was actually assessed/believed then**;
- **what was authorized then**;
- **what gate/safeguard control state or action actually applied then**;
- **what was actually explained then**;
- **what is known retrospectively now**.

Late or corrected evidence or authority/normative rules can change the current retrospective conclusion without rewriting the contemporaneous record. Evidence or a rule discovered tomorrow but effective yesterday does not belong in yesterday's `as-known-then` view.

A historical gate hold, admission, override, safeguard activation/release, causal confirmation, authority resolution, threshold, or waiver remains the actual state/action/rule used at the time even if later evidence shows a different decision or governing source would now be preferred.

A current system may generate an `as-known-then` explanation from the historical state cut. That answer is explicitly **reconstructed** unless an actual retained Explanation/report proves what was communicated at the time.

Historical actor authorization and authority standing are reconstructable evidence, but they are not reusable permission/current standing: current applicable authority and requester Capability Authorization govern current resolution/disclosure.

Phase 003 Group 06 correctly concluded that historical replay itself was **not** a new concept. The later 24th concept is Assertion Authority, discovered in Phase 005 Group 01.

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
- Which metrics/checks are actually part of the governed profile for this asset, and why?
- Is a threshold an explicit Expectation or merely a descriptive Baseline range?
- Is a violation currently waived/suspended, and what underlying evidence remains visible?
- Is this schema change normatively compatible for this specific downstream consumer?
- Is this metric/Expectation merely monitored, or explicitly eligible for high-consequence control use?
- Which source/actor is authoritative for the relevant business definition, responsibility, classification, policy context, criticality, metric/threshold, or other assertion—and under what rule?
- Are conflicting assertions merely advisory disagreement, an authoritative assertion conflict, or an authority-rule conflict?
- Was the currently preferred source also authoritative at incident time, or only after a later authority correction?
- Was a relevant change planned and what prospective blast radius existed using what was known at planning time?
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
- What can this analyst see, investigate, operate, gate, confirm, edit, approve, waive, or override without direct-data access?
- What is intentionally hidden/redacted, and how does that limit the visible basis without changing internal evidence sufficiency?
- What was known, authoritative, normatively applicable, authorized, gated/held/safeguarded, causally concluded, and explained at incident time?
- What changed in the retrospective conclusion after late/corrected evidence or authority/normative changes arrived?
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

These are environmental facts, not implementation architecture. Availability of Databricks/Unity Catalog, GitHub, Collibra, Immuta, or a human source does not make that source universally authoritative. The monitoring framework should remain independently deployed from production repositories/GitHub Actions unless a later accepted control/integration requirement explicitly needs otherwise.

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.**
3. **Time/history are first-class; event time and knowledge time remain distinct.**
4. **Evidence over narrative completion.**
5. **Evidence sufficiency is proposition- and conclusion-specific, not a universal score.**
6. **Negative evidence requires opportunity-to-observe plus sufficient bounded coverage.**
7. **Assertion Authority is scoped; no hidden universal source precedence.**
8. **Source assertion is separate from authoritative standing.**
9. **Assertion Authority is separate from Capability Authorization and Responsibility Assignment.**
10. **Authoritative standing does not imply factual infallibility, evidence sufficiency, compliance, or enforcement.**
11. **Expectation is normative; Baseline is descriptive.**
12. **Metric meaning/profile/threshold/severity/waiver/control-use eligibility remain distinct.**
13. **Observation is not Assessment.**
14. **Successful execution is not timely execution, schema compatibility, freshness, or data quality.**
15. **Passive monitoring is non-blocking by default.**
16. **Baseline monitoring prefers production-repository independence.**
17. **Execution gating is explicit opt-in control, not an automatic effect of monitoring, Lineage, authority, or control-use eligibility.**
18. **Execution Gate is separate from Execution History and Propagation Safeguard.**
19. **Readiness is criterion-relative; successful execution is not global readiness.**
20. **Gate decision is not gate enforcement or actual execution.**
21. **Safeguard proposal/request is not enforced active protection.**
22. **Prevented exposure requires material enforced control plus sufficient negative/path coverage.**
23. **Lineage discovers relationships/candidates, not cause.**
24. **First-observed localization is not root cause.**
25. **Causal propositions and epistemic status remain explicit.**
26. **Leading/supported hypothesis is not confirmed cause.**
27. **Multiple contributors and unresolved outcomes are valid; one root cause is not required.**
28. **Causal contribution does not imply percentage attribution; primary cause requires comparative evidence.**
29. **Confirmed causes require an explicit evidence profile/standard plus separately resolved confirmation authority.**
30. **Confirmed claims remain challengeable without rewriting historical confirmation.**
31. **Prospective Impact is not actual Impact or retrospective cause.**
32. **Actual Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
33. **Non-exposure requires negative consumption/path evidence; missing telemetry is not reassurance.**
34. **Criticality influences priority, not evidence strength or threshold truth.**
35. **Propagation Safeguard is protective state, not defect proof.**
36. **Capability Authorization is separate from assertion authority, policy, responsibility, scope, normative authority, and enforcement.**
37. **Raw-data access is separate from analytical visibility, operational control, and causal-confirmation authority.**
38. **Analyst Investigation remains first-class even with restricted evidence.**
39. **Annotation is attributed context, not a shadow truth store.**
40. **Explanation consumes the authorized analytical projection; it is not a truth or authorization source.**
41. **Actual historical state remains distinct from replay-derived reconstruction.**
42. **Late evidence or authority/normative correction can revise retrospective knowledge without rewriting what was known then.**
43. **Historical authority/authorization is not current authority/disclosure permission.**
44. **Monitoring must not broaden raw-data or production-control authority.**
45. **Databricks-native first where it fits; integrate before duplicate.**

## Canonical A+B→C scenario

Suppose Table C is produced by joining A and B. C materially drops in volume. Investigation uses historical Lineage to discover A/B and relevant operational/deployment evidence. B may be the earliest monitored location where a deviation appears without automatically becoming root cause.

Phase 004 requires the reasoning to state what each evidence item can actually support. A B row-count Observation must match the relevant B output/window/grain before it bears on the hypothesis. Evidence that B did not change requires adequate opportunity-to-observe and coverage of the proposed B mechanism; absence of an alert is insufficient. Mirrored copies of one Databricks event do not become independent corroboration.

Phase 005 adds separate governance questions: which source/actor has authoritative standing for the **business definition, technical definition/schema/key/grain, responsibility, classification, policy context, criticality, metric profile, threshold/schema compatibility Expectation, waiver, and control-use eligibility** relevant to A/B/C? Different layers can legitimately have different authorities.

A technical profile may include B key-null rate because it validates a known join failure mode while excluding meaningless identifier quantiles. A business authority may own C's acceptable population range while a platform team owns a technical warning band. Baseline regularity does not create either rule automatically.

If B's schema/key/grain changes, Group 03 permits scoped review of affected metric/profile/Baseline use while preserving that empirical comparability is evidence-driven. A migration waiver can suspend a normative rule for a bounded interval without rewriting the actual observed state.

Causal claims remain explicit. `B's reduced population contributed to C row loss` and `elevated join-key nulls contributed to C row loss` can both become supported when their evidence warrants it. A recent Deployment can remain a competing claim; if sufficiently covered evidence shows C degradation began before Deployment activation, that claim may be weakened or rejected. No single root cause is forced, and neither contributor is called primary without comparative evidence.

A supported claim can be useful before confirmation. `Confirmed` requires the applicable claim-class confirmation profile plus separately resolved confirmation authority; an analyst, administrator, or automated process does not gain confirmation authority merely by participating in RCA.

A business analyst may conduct that investigation without being allowed to inspect A/B/C rows. The analyst can use authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility metadata, safe authority/normative standing, causal status, Impact, safeguard/gate state, and Annotation. Restricted nodes/evidence/authority details remain opaque rather than being retrieved and summarized behind the user's permission boundary.

Before C runs, an optional Execution Gate could require the current A and B outputs to be ready. If B is late, C may be held instead of blindly joining A-current + B-stale. If the criterion requires B's current output, freshness, or an eligible schema/quality condition, a successful B run alone does not satisfy the gate. AUTH-023 eligibility is necessary governance for a high-consequence metric/schema rule but does not itself enable the gate or prove the evidence ready. A hold decision remains distinct from evidence that the external control actually suppressed C.

Downstream, a Metric View and two reports may all be reachable. Version/refresh evidence can establish that one report consumed the affected C output, another refreshed from an earlier safe version, and a third remains exposure-unknown. The safe-version report can be `not exposed to affected V` while still stale. A report's own metric failure is observed downstream effect; a client delivery/decision consequence requires separate evidence; saying C caused that effect requires Causal Claim.

If an enforced safeguard blocks the suspect version before a client report refreshes, Impact may establish prevented exposure only when the safeguard was materially operative on the encounter path and negative-consumption/alternate-path coverage is sufficient. If the report never had a relevant refresh opportunity, the correct statement may instead be `safeguard active; consumer not exposed`, without claiming the safeguard prevented exposure. Any older state still being served remains separately assessed for freshness.

If downstream consumption, enforcement, corrected timing, authority, or normative-rule evidence arrives late, the historical incident-time view remains what was known/authoritative/applicable then while current readiness/exposure/prevention/causal/authority resolution may change. Actual historical gate/safeguard decisions, executions, rules/waivers, and retained Explanations are never rewritten.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation navigation/system of record.
- [`docs/foundation/`](docs/foundation/) — accepted foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — concept specifications and four post-exit addenda.
- [`docs/concepts/phase_002/addenda/assertion_authority.md`](docs/concepts/phase_002/addenda/assertion_authority.md) — accepted Assertion Authority concept.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — completed synchronization contracts/scenarios and exit review.
- [`docs/concepts/phase_004/`](docs/concepts/phase_004/) — completed evidence/time/causality refinement contracts and exit review.
- [`docs/concepts/phase_005/README.md`](docs/concepts/phase_005/README.md) — active authority/governance refinement phase.
- [`docs/concepts/phase_005/01_authority_vocabulary_and_conflict/`](docs/concepts/phase_005/01_authority_vocabulary_and_conflict/) — accepted Group 01 AUTH-001–AUTH-008.
- [`docs/concepts/phase_005/02_semantic_governance_authority/`](docs/concepts/phase_005/02_semantic_governance_authority/) — accepted Group 02 AUTH-009–AUTH-015.
- [`docs/concepts/phase_005/03_normative_health_metric_threshold_governance/`](docs/concepts/phase_005/03_normative_health_metric_threshold_governance/) — accepted Group 03 AUTH-016–AUTH-023.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/reference/authority_vocabulary.md`](docs/reference/authority_vocabulary.md) — Group 01 authority vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) and [`.cursor/rules/`](.cursor/rules/) — repository-agent guardrails.

## Phase direction

**Phase 005 is active. Groups 01–03 are accepted with AUTH-001–AUTH-023. Group 04 — Capability Authorization & Restricted Analytical Visibility is next and has not started.**