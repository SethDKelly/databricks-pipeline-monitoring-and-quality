# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, assertion authority, authorization, planned/realized change history, causal evidence, downstream business impact, protective propagation state, optional dependency-aware execution control, disclosure, and historical evolution of knowledge** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**. A person should be able to ask what is happening, what was intended, what changed, whether timing/data behavior is acceptable, whether an upstream prerequisite was actually ready before a downstream run, where a degradation first became observable, what causal explanations are supported, what may be at risk downstream, what is actually reachable/exposed/affected, what consequences are evidenced, which assertions are authoritative, what policies/restrictions apply, who is responsible, what normative health rules govern the result, what the analyst is authorized to inspect or operate, what can be communicated to which audience, and **what was known/authoritative/authorized/controlled/disclosed at an earlier point compared with what is known now**.

## Current design state

Phase 002 originally completed with 20 retained concepts. Later requirements exposed four missing independent boundaries:

- **Propagation Safeguard** — protective hold/quarantine/release state;
- **Capability Authorization** — principal/capability/subject authorization state;
- **Execution Gate** — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness;
- **Assertion Authority** — target/context/time-scoped source/actor standing and authority-rule history for governance assertions.

The current catalog contains **24 accepted concepts**.

**Live repository phase progression is declared only in [`docs/README.md#current-state`](docs/README.md#current-state).** This README intentionally does not maintain a separate current/next phase declaration. Phase-specific documentation records accepted contracts, historical exits, and group-local progress without overriding the canonical status declaration.

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but too late, use stale inputs, lose rows through a join, experience a source-shape change, legitimately change population under planned logic, threaten downstream client delivery, or produce an output risky enough to hold while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, structural/schema compatibility, data quality, planned intent, realized change, historical topology, governance, assertion authority, normative health authority, authorization, causality, downstream consequence, human investigation, optional execution gating, protective propagation control, disclosure, and evolving knowledge over time as related but distinct concerns**.

## Evidence sufficiency is conclusion-specific

Phase 004 rejects a universal `evidence confidence` or `trust` score. Evidence is adequate only relative to a **defined proposition, context, time, grain/version, and intended conclusion strength**.

The framework separates:

1. **evidence applicability** — does the evidence bear on this subject/property/time/version proposition?;
2. **coverage** — what bounded observation opportunities, population/partitions, source/query scope, versions/consumers, and intervals were observable?;
3. **corroboration/conflict** — are multiple items independent, complementary, duplicated/common-source, non-comparable, or contradictory?;
4. **conclusion-specific sufficiency** — is that evidence set adequate for this exact conclusion under its applicable standard?

This creates deliberate asymmetry between many positive and negative claims. One directly observed qualifying output may establish that an output exists. Saying **no qualifying output exists** generally requires a mechanism capable of observing every relevant bounded output opportunity plus enough coverage to rule them out.

Accordingly:

**no telemetry ≠ no event**  
**query failure ≠ zero results**  
**evidence not found ≠ observed absence**  
**source count ≠ independent corroboration**  
**sufficient for one conclusion ≠ sufficient for every related conclusion**

Assertion Authority can resolve which governance assertion has standing, but it cannot make incomplete operational evidence sufficient. Capability Authorization and disclosure governance determine what basis/details a requester may inspect or receive; they do not change internal truth.

## Evidence and analysis become available progressively

The framework should return the **narrowest trustworthy result as soon as the evidence required for that result is known**, rather than forcing every answer to wait for the slowest evidence source.

Phase 004 distinguishes:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**.

Phase 006 refines the health side into functional evidence horizons:

**immediate operational facts → fast core/schema/current-cycle health → enriched DQ/reconciliation/distribution health → diagnostic/Investigation support → retrospective/post-operations review**.

These are not fixed time tiers. A result matures when its required evidence becomes sufficient; elapsed time alone never upgrades maturity.

Source event time, source availability time, framework collection/knowledge time, and derived evaluation time remain distinct where material. A Databricks completion record can support a fast execution-status result before schema/Metric View/DQ evidence is available, while RCA deepens later as historical Lineage, Change, consumption, governance, and analyst evidence become usable.

An early narrow answer remains scoped to its knowledge cut. `Job succeeded` never silently becomes `pipeline healthy` while quality/freshness/schema evidence is pending. An early leading hypothesis never becomes `confirmed root cause` merely because it is useful or fast.

Phase 006 also establishes that **recent recomputation does not make old evidence fresh** and that result freshness is exact-use specific rather than governed by one universal TTL. Phase 009 characterizes actual source availability/collection behavior, Phase 010 selects fast-path/asynchronous architecture and performance budgets, and Phase 011 may later convert accepted timing objectives into MVP acceptance criteria.

## Causal epistemics are explicit

Causal Claims use:

**proposed → supported / weakened / unresolved / rejected / confirmed**

with non-linear historical transitions rather than a mandatory ladder.

- **proposed** — an explicit causal proposition exists but is not yet sufficiently evaluated;
- **supported** — applicable evidence materially supports it below confirmation;
- **weakened** — material contradictions/limitations reduce support without justifying rejection;
- **unresolved** — substantive evaluation occurred but evidence remains insufficient, conflicting, unavailable, restricted, or non-discriminating;
- **rejected** — sufficient contradiction/exclusion evidence exists under the applicable claim standard;
- **confirmed** — an explicit claim-class profile/standard is satisfied with sufficient evidence, alternative/contradiction review, required negative-evidence coverage, independently resolved confirmation authority/capability, and provenance-bearing confirmation action.

Phase 004 defines confirmation evidence. Phase 005 Group 05 defines confirmation authority. Human title, model output, job ownership, or service-principal identity alone cannot promote insufficient evidence to `confirmed`.

The model does not require one root cause. Multiple compatible contributors can remain supported or confirmed. `Primary` is a stronger comparative claim requiring comparative evidence, and qualitative causal roles never imply percentage attribution.

Confirmed claims remain challengeable. Later corrected evidence can change current status while preserving who/what confirmed the earlier claim, under which standard and evidence cut.

## Exposure, readiness, and control proof are evidence-layered

For downstream exposure, the framework binds the **affected state/version/window**, downstream candidate, historical relationship, encounter mode, and consumer opportunity. Reachability, timing overlap, run, or refresh alone do not establish that the affected state was consumed.

`Not exposed` is a negative conclusion requiring sufficient coverage of relevant encounter paths. A consumer may be **not exposed to suspect V while still stale** because it used an earlier safe version. `No encounter opportunity`, `no encounter`, `safe-version encounter`, `unknown-version encounter`, unavailable/restricted evidence, and actual affected-state encounter remain distinct.

Readiness is criterion-relative. `Upstream job succeeded` is not global readiness unless completion is the entire declared criterion. A gate can require qualifying current-cycle output, freshness, version, completion, publication availability, schema compatibility, or named quality conditions. Unknown required evidence remains unknown; fallback may govern action but cannot turn the prerequisite into `ready`.

Phase 006 adds another explicit step before a health result participates in readiness: **exact-use result suitability**. A fresh, sufficiently evidenced violation may be perfectly suitable and support `not ready`, while a stale `meets` result can be unsuitable and therefore cannot support `ready`.

Control evidence remains layered:

**health Assessment ≠ evidence suitability ≠ readiness result ≠ gate decision ≠ gate enforcement ≠ actual downstream execution**

and:

**safeguard proposal/configuration/request ≠ enforced active safeguard ≠ prevented exposure**.

A reliable downstream run during an applicable unoverridden hold contradicts full hold enforcement. An admitted opportunity that never runs does not prove admission failed because the gate only removes its own barrier.

`Prevented exposure` requires more than `safeguard active + consumer not exposed`: the safeguard must have been materially operative on the encounter path, with sufficient negative consumption/version and alternate-path coverage. Blocking suspect V does not prove downstream output is current, fresh, or healthy.

Configured fallback describes intended behavior; actual fallback application/enforcement requires evidence. Missing control telemetry never proves fail-open, fail-closed, success, or failure.

## Assertion Authority is explicit and scoped

Phase 005 Group 01 accepts **Assertion Authority** as the 24th concept because multiple assertion-owning concepts require the same independent source-standing, precedence, conflict, correction, and historical-resolution behavior.

It answers:

> Which source, actor, role, or governed process has authoritative standing for this exact assertion category/facet/subject scope/context/time?

It does **not** answer whether the assertion is factually infallible, whether operational evidence is sufficient, whether the principal is permitted to act, or whether an external control enforced something.

The model distinguishes source assertions, authority targets, authority holders, provenance-bearing authority rules, authoritative/advisory assertions, resolved disagreement, authoritative assertion conflict, authority-rule conflict, and unknown/unavailable authority.

No hidden precedence is allowed. Source count/majority, recency alone, synchronization/ingestion order, source availability, repository ownership, job creator/admin/title, Responsibility Assignment, or apparent specificity do not create authority unless an explicit applicable rule says so.

Sole authority, co-authority, ordered precedence, and conditional/fallback authority are allowed only through explicit rules. Co-authoritative disagreement remains conflict unless a resolver applies. Fallback requires an explicit rule plus evidence that its activation condition holds.

Authority rules require provenance and governing basis and cannot self-promote. Authority is bitemporal: later corrections can change retrospective resolution without rewriting what source the framework considered authoritative at an earlier knowledge cut.

## Semantic and schema governance are facet-specific

Phase 005 Group 02 applies Assertion Authority to Semantic Definition, Responsibility Assignment, Classification/criticality, and Policy Context without changing their truth ownership.

Different holders can legitimately govern technical schema declaration, grain/key meaning, business definition, population semantics, responsibility type, criticality scheme, and policy applicability.

Preserve:

**declared/governed schema meaning ≠ normative schema contract ≠ realized schema state ≠ compatibility Assessment**.

A runtime schema observation does not become authoritative business meaning merely because Databricks/Unity Catalog exposes it. A declared business key does not prove uniqueness/nullability health. Local/context governance does not automatically override broader governance, and governance assertions do not recursively propagate through Lineage or containment without explicit provenance and standing.

Phase 006 refines structural compatibility further: compatibility is bound to the **consumer-visible interface/contract and version**, not merely producer physical DDL. Additive changes are not universally safe, engine cast ability does not establish compatibility, and key/grain changes can be structurally material without a conventional column diff.

## Normative health governance is layered

Phase 005 Group 03 accepts **AUTH-016–AUTH-023**.

Preserve:

**metric/schema meaning → metric-profile selection → normative Expectation → threshold/margin → severity → waiver/exception → high-consequence-use eligibility → later control capability/enforcement**.

Those layers can have different authoritative holders. A metric being easy to calculate does not justify including it in every profile. Governed inclusion should have purpose, applicability, intended use/audience, authority/owner, and lifecycle/retirement context.

Baseline remains descriptive. A Baseline-derived range becomes normative only through an authoritative Expectation. Structural/schema compatibility rules are normative and consumer-specific; governed schema meaning and realized structure do not alone decide whether a change is acceptable.

A bounded waiver changes normative applicability/required response. It does not rewrite Observation, realized schema, Baseline deviation, or historical evidence and must not become a fictional clean `pass`.

Normative conflict remains explicit. `Strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and recency are not implicit resolvers.

High-consequence use is separately governed. An authoritative/business-critical metric does not automatically become a gate/safeguard predicate. Explicit eligibility is required, and even then:

**control-use eligibility ≠ current evidence suitability ≠ readiness ≠ control capability ≠ enforcement**.

## Phase 006 completes the health model

Phase 006 accepts **HLTH-001–HLTH-066** and no new concept.

The final health chain is:

**metric/check definition and applicability → Observation/evidence → structural/interface and empirical-comparability context → Baseline-relative and/or normative component Assessment → transformation-specific reconciliation → profile-bound composite health Assessment → result freshness/maturity → exact-use readiness/control-evidence suitability → readiness**, with gate decision/enforcement/execution remaining separate.

### Measurement and metric profiles

Metric definition, metric Observation, and Assessment remain distinct. Semantic applicability, governed profile selection, technical support/computability, current evidence availability, and outcome are also distinct.

Routine monitoring follows a purposeful anti-bloat structure: a small stable core plus targeted critical/business/transformation checks and diagnostic/on-demand expansion. Technical availability alone does not justify computing every null rate, cardinality, percentile, distribution statistic, or schema check.

Canonical metric families are operational/output, temporal/freshness, structural/schema, volume/population, completeness/missingness, uniqueness/key integrity, validity/domain, distribution/shape, relational/transformation integrity, and business-semantic measurement.

### Baselines and statistical context

Baseline is a provenance-bearing descriptive reference over eligible comparable history, not all available history.

Comparability is multidimensional and conclusion-relative; Phase 006 rejects a universal comparability/confidence score. Fixed, rolling, seasonal/cadence, cohort, and post-change references are functional classes rather than selected algorithms.

Low volume, sparse references, approximation/sampling, measurement uncertainty, missing periods, and structural/method breaks remain visible. Adaptive Baselines cannot silently absorb an incident or make a chronic defect acceptable simply because it became historically typical.

### Normative Assessment

For one bound criterion preserve at least `meets`, `violates`, `indeterminate/insufficient evidence`, `conflicting`, `unavailable`, and `not applicable`.

Warning/proximity, Baseline typicality, severity/priority, and waiver/disposition remain separate axes. All of these are valid combinations where evidenced:

**typical + meets**  
**atypical + meets**  
**typical + violates**  
**atypical + violates**.

`Violates + waived response` remains a violation. A bounded exception that makes the criterion genuinely non-applicable is different.

### Transformation reconciliation

Lineage does not recursively propagate local metrics or health statuses.

For A+B→C, reconciliation is based on the exact transformation/version. Joins use eligible populations, directional match/unmatched behavior, cardinality/fan-out and key integrity; filters use explicit selection/exclusion semantics; aggregation conservation is measure-specific; dedupe, union/merge/upsert, null/default/cast/value derivation, distributions and multi-input freshness each have their own semantics.

A local upstream violation can coexist with healthy downstream criteria after isolation/repair, and healthy upstream criteria can coexist with downstream failure introduced by transformation logic.

Reconciliation can materially localize a discrepancy while remaining below causal confirmation.

### Composite health

Composite health is a bounded Assessment over an explicit subject, consumer/use/context, profile/version, component set/roles/logic and time—not a universal scalar property of an asset.

Phase 006 rejects canonical majority voting, weighted averages, severity-weighted scores, and universal numeric health scores.

For a conjunctive profile, a positive `healthy` requires all applicable required components to meet and no required unresolved state. A known violation can establish `degraded` while unresolved/unavailable qualifiers remain visible. `Healthy with warning` can represent required criteria meeting while a warning/proximity condition is active.

Consumer-specific profiles can legitimately differ because they ask different bounded propositions. Technical/business/executive/audit views remain authorized projections over the same underlying proposition and cannot strengthen its status.

### Freshness, maturity and readiness suitability

Assessment evaluation time is not underlying evidence time. A recalculation performed now over yesterday's evidence can remain stale for a current-cycle use.

There is no universal result TTL. Freshness is evaluated relative to the exact use, allowed age, evidence window and current-cycle/version requirement.

Analytical maturity follows evidence sufficiency, not elapsed time. Narrow trustworthy results should be available as soon as supportable while broader composite health remains pending if slower evidence is required.

Suitability is outcome-neutral. A fresh, well-evidenced violation can be suitable and support `not ready`; a stale `meets` result can be unsuitable and cannot support `ready`.

AUTH-023 high-consequence-use eligibility and current evidence suitability are independent prerequisites. Neither creates gate authority, a gate decision, enforcement, or execution.

### Phase 006 exit

H07-01–H07-36 replay the complete chain across execution-versus-health, metric availability, schema contracts, Baseline regime breaks, seasonal/normative behavior, low-volume/approximate evidence, waivers/conflicts, A+B→C reconciliation, transformation repair/introduction, composite disagreement, progressive result timing, stale/suitable readiness evidence, AUTH-023 eligibility, passive monitoring outage, active-control uncertainty, and historical replay.

All pass without HLTH-067, a new concept, universal score, false pass, blind propagation, causal shortcut, stale-evidence shortcut, control conflation, or architecture selection.

## Phase 007 operational Lineage foundation

Phase 007 Group 01 refines the accepted Lineage concept through **OPS-001–OPS-009** without adding a new concept.

A Lineage relationship is now treated explicitly as a **bounded relationship proposition**, not a generic edge. Material interpretation binds source/target identity, semantic relationship family/role, field/key/population/consumer/version scope, effective interval and proposition-specific evidence basis.

The accepted minimum operational relationship families are:

- `data_derivation`;
- `production`;
- `operational_dependency`;
- `publication`;
- `consumption_path`.

Repository membership, Deployment provenance, Change state, execution state, Gate/Safeguard state, authority/authorization and causality remain owned elsewhere rather than being converted into Lineage merely because they are graph-representable.

The earlier preliminary notion of Lineage edge `confidence` is superseded by Phase 004 evidence semantics. Relationship existence uses applicability, provenance, opportunity/coverage, corroboration/conflict and conclusion-specific sufficiency; there is no universal Lineage confidence or completeness score. A bounded relationship proposition may resolve `established`, `absent`, `unknown`, `conflicting` or `unavailable`, with `absent` requiring adequate negative-evidence coverage.

Graph reachability is also distinct from **operational relevance**. Relevance is evaluated for an exact traversal question and can be relevant, not relevant or indeterminate based on relationship family, semantic scope, time/version/consumer context and path composition. Reachability/relevance still do not establish encounter, Impact or cause.

Historical topology remains bitemporal and non-rewriting: planned topology belongs to Change Intent; effective Lineage is evidence-backed; specific run/consumer encounter remains separate; later topology discovery can revise retrospective views without backdating framework knowledge.

## Capability Authorization is exact and least-privilege

Phase 005 Group 04 accepts **AUTH-024–AUTH-032**.

Authorization binds exact principal, capability/action, subject, environment/purpose/tenant/consumer context, time, and material detail level. `Allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` remain distinct. A system may refuse an action without positive allow, but it must not rewrite unresolved authorization into an invented deny.

There is no universal `deny wins`, `direct user wins`, `role wins`, `latest wins`, or `most specific wins` rule. User/group/role/service-principal composition and capability inheritance require explicit provenance-bearing rules.

Least privilege is detail-specific. A requester can be denied rows while allowed a safe Assessment/RCA projection. Metric values, thresholds, Baselines, schema, Lineage identities/paths, causal basis, Impact, control state, authority/authorization metadata, and Explanation may each be restricted independently.

**Authorized Analytical Projection is not declassification.** It is a requester-capability-filtered view over the same truth. Hidden evidence remains restricted, not absent. Aggregation/redaction is not automatically safe, and the framework/service principal itself must be authorized to process evidence it counts internally.

Permission to propose/edit/approve/waive/retire a rule is separate from Assertion Authority over the resulting state. Authorization remains separate from enforcement and action success.

## High-consequence authority is lifecycle-specific

Phase 005 Group 05 accepts **AUTH-033–AUTH-043**.

Preserve:

**request/proposal → approval/authorization → action issuance → control-plane acceptance → enforcement/effect → resulting domain state → downstream outcome**.

High-consequence capabilities are action- and lifecycle-stage specific. A principal may propose without approving, approve without executing, execute an already-approved action without changing policy, or hold override/release authority only under bounded conditions. Broad labels such as `admin`, `owner`, `operator`, `on-call`, or service-account identity never become universal permission.

Causal confirmation remains jointly evidence- and authority-gated. The claim profile determines whether human confirmation is mandatory or narrowly deterministic automated confirmation may be explicitly authorized.

Job/run operations remain granular. Trigger, retry, restart, cancel, scheduling/control, or other bounded actions can be independently authorized and do not grant raw-data access, gate/safeguard authority, deployment authority, or proof the resulting run succeeded.

Execution Gate authority is decomposed across registration/configuration, readiness/fallback policy configuration, enable/disable, ordinary hold/admit execution, override, and retirement. Override never changes `not ready`, `unknown`, `conflicting`, or `unavailable` into `ready` and never proves enforcement.

Propagation Safeguard authority is decomposed across proposal, approval, activation, extension, cancellation, release, and retirement/expiry. Release is independently high consequence because it restores propagation/consumption and never proves output health.

Multi-party approval, quorum, ordering, distinct-principal/role requirements, and self-approval rules exist only through explicit conditional-authorization policy. Approval completion does not execute an action.

Delegation is separately authorized, bounded by capability/target/context/time, expiring/revocable, and non-transitive unless re-delegation is explicitly permitted. Break-glass is explicit emergency authorization with bounded scope, qualifying condition, duration, provenance, and review requirements—not universal superuser access. It cannot manufacture raw-data access, readiness, health, evidence sufficiency, causality, or enforcement.

Automated/service-principal action requires exact explicit grant. Technical ability, deployed code, scheduler ownership, or model recommendation is not authority, and required human review cannot be bypassed.

Authorization-outage fallback is action-specific. `Unknown`, `conflicting`, and `unavailable` remain truth states. A later implementation may preserve existing protective state, refuse a new action, escalate, or use an explicitly authorized fallback principal only where a rule says so. There is no universal fail-open/fail-closed/always-hold/always-release rule.

## Disclosure and audience governance preserve one truth

Phase 005 Group 06 accepts **AUTH-044–AUTH-053**.

Disclosure binds requester/audience, information/detail class, subject/context, purpose, temporal perspective, and delivery scope. Audience labels such as technical, business, executive, client, or audit do not grant permission.

A requester may be allowed to inspect a result privately without being allowed to export, forward, publish, or communicate it to a client. Result visibility can differ from exact metric, threshold, schema, source, evidence, authority, confirmer, approver, or control-basis visibility.

Safe abstraction can expose exact state, coarser category/range, redacted detail, opaque existence, or explicit limitation only when the abstraction itself is authorized and semantically valid. Opaque existence is shown only when existence itself may be disclosed.

Aggregation/redaction is not automatic declassification. Counts, topology, timing, path length, role names, prior disclosures, and repeated narrow queries can combine into restricted inference; disclosure safety must consider mosaic/differencing risk.

Technical, business, executive, and audit views are different authorized projections over one underlying truth. Simplification may reduce detail but cannot strengthen status.

High-consequence statements may require separate compose/review/approve/release/correct/retract authority. Communication approval never creates evidence sufficiency, causal confirmation, health, compliance, or enforcement.

Preserve wording distinctions such as:

**supported ≠ confirmed**  
**reachable ≠ exposed**  
**not exposed to V ≠ fresh/healthy**  
**hold decision ≠ hold enforced**  
**safeguard active ≠ prevented exposure**  
**released ≠ healthy**  
**waived ≠ clean pass**  
**authoritative standing ≠ factual infallibility**

Human attribution, authority-holder/basis, authorization membership path, confirmer/approver/operator, delegation, break-glass, service-principal, and control metadata can themselves be sensitive.

Historical retained Explanation, reconstructed `as-known-then` Explanation, retrospective Explanation, historical authorization/disclosure, and current requester disclosure remain separate. Unknown/conflicting/unavailable/unsafe-to-project disclosure state never becomes permission.

## Phase 005 consolidation confirms the authority stack composes

Phase 005 Group 07 replays **G07-01–G07-26** across metric/schema governance, threshold conflict/waiver, structural-change comparability, restricted multi-cause RCA, causal confirmation, multi-party gate override, safeguard release, break-glass/outage, automation, audience projection, and historical Explanation.

All pass without another truth owner or AUTH contract.

The final accepted stack is:

**source assertion / Assertion Authority → semantic or normative governance resolution → Capability Authorization / Authorized Analytical Projection → high-consequence authorization where applicable → disclosure / Explanation projection**

while Observation, Assessment, Change, Causal Claim, Execution Gate, Propagation Safeguard, Execution History, Impact, and other domain concepts retain actual truth ownership.

Final Phase 005 range: **AUTH-001–AUTH-053**. No AUTH-054. The catalog remains 24 concepts.

## Passive monitoring should not become production overhead

The default monitoring/quality framework should be **out-of-band and non-blocking**. Monitoring collection, analysis, Investigation, Impact reasoning, and Explanation should not add meaningful production-path latency or become a production availability dependency simply because a job is monitored.

Baseline integration should prefer Databricks/platform/source metadata and independently deployed monitoring components rather than requiring framework code/libraries or monitoring workflow steps in every production ETL repository/GitHub Actions deployment process.

This is an architectural objective, not a claim that no specialized integration will ever require source changes. Future exceptions must be explicit, minimal, and justified.

## Dependency-aware execution control is optional

A pure time-based schedule can create stale downstream output when upstream dependencies run late. The model therefore includes optional **Execution Gate** behavior.

When no gate is enabled, the framework remains observational: it can report that C started before A/B were ready and later evaluate freshness/readiness consequences, but it does not delay C.

When an explicit gate is enabled, a downstream execution opportunity can be held while prerequisites are not ready, admitted once declared readiness is satisfied, or overridden through independently authorized policy without pretending readiness was satisfied.

A readiness criterion may require more than `upstream job ran`: current output, freshness, version, completion, schema compatibility, or another eligible condition may be required.

**Execution Gate ≠ Propagation Safeguard.** Gate protects downstream start/admission; Safeguard protects output/consumption propagation. Both may intentionally create delay that remains observable and assessable.

AUTH-023 control-use eligibility is necessary governance for a high-consequence metric/schema rule but does not enable/configure a gate, grant override authority, prove evidence available/suitable, or prove enforcement.

## Restricted-data analysis is a core capability

The product must not equate **lack of direct row access** with **lack of monitoring/RCA access**.

An analyst may be denied rows/sensitive columns while permitted to inspect approved execution status, duration/readiness/freshness, aggregate health metrics/Assessments, safe Expectation/Baseline/waiver state, safe schema-compatibility status, authorized Semantic Definition, Responsibility Assignment, Classification/Policy Context summaries, authority standing/conflict, historical Lineage with opaque restricted nodes, Investigation/Causal status, downstream Impact, safeguard/gate state, and Annotation.

That **Authorized Analytical Projection** can support meaningful RCA/downstream reasoning without direct data access. It must preserve redaction, missing evidence, authority limitations, and disclosure limitations rather than pretending hidden evidence does not exist.

Metadata and derived evidence are **not automatically unrestricted**. Counts, thresholds, schemas, table names, Lineage, policy labels, responsibility, authority-holder details, business consequences, safeguard/gate detail, approval/delegation/break-glass state, causal conclusions, and disclosure-review state can themselves be sensitive.

## Capability separation

The model distinguishes:

**Assertion Authority ≠ Capability Authorization**

and at least:

**raw-data read ≠ metadata/governance visibility ≠ derived health/metric visibility ≠ Lineage/RCA participation ≠ job/run operational authority ≠ safeguard authority ≠ gate-control/override authority ≠ causal-confirmation authority ≠ disclosure/publication authority.**

A user may:

- submit/edit an assertion while it remains advisory;
- analyze health/root cause/downstream Impact without row access;
- operate/retry a job without raw-data read access;
- view health/Impact/Explanation while lacking production-control authority;
- propose a safeguard while lacking activation authority;
- inspect why a run is gated while lacking override authority;
- participate in RCA without confirmation authority;
- inspect a confirmed cause internally while lacking client-publication authority.

Responsibility Assignment, Assertion Authority, Policy Context, Classification, Monitoring Scope, repository ownership, job creator identity, analyst role, or business criticality do not silently grant capabilities.

## Downstream Impact is evidence-layered

For each downstream subject the model can distinguish:

1. **candidate/reachable** — historical Lineage shows a plausible downstream path;
2. **exposed/not exposed/unknown** — evidence shows whether relevant state was encountered;
3. **observed downstream effect** — the consumer's own Observation/Assessment/Change shows a condition/effect;
4. **technical/analytical/business consequence** — separate evidence establishes delivery/use/process/decision/client consequence;
5. **causal attribution** — if the origin/gate/safeguard is claimed to have caused/contributed, that proposition belongs in Causal Claim.

Criticality can warrant urgency while a candidate remains only reachable. A downstream effect can be observed while consumed-version evidence is insufficient. The model preserves those disagreements rather than forcing one `impact` answer.

An enforced safeguard can establish **prevented exposure** only when Phase 004 material-control plus negative-consumption/path evidence is sufficient. Preventing suspect-state exposure does not prove downstream delivery was fresh/healthy; the hold may create a separate delay/non-delivery consequence.

## Historical replay is bitemporal and non-rewriting

Historical replay uses two independent coordinates:

- **event/effective time** — when the questioned state applied;
- **recorded/knowledge cutoff** — which evidence/assertions/authority/normative/authorization/disclosure state was known for that historical view.

The same event window can support:

- what happened;
- what was known then;
- what source was considered authoritative then;
- what metric/schema/profile/Baseline/threshold/waiver applied then;
- what transformation/reconciliation/composite/freshness rule applied then;
- what was assessed/believed then;
- what was authorized then;
- what approval/delegation/break-glass state existed then;
- what gate/safeguard action actually applied then;
- what was actually disclosed/explained then;
- what is known retrospectively now.

Late/corrected evidence or authority/normative/authorization rules can change the current retrospective conclusion without rewriting contemporaneous record. Evidence/rules discovered tomorrow but effective yesterday do not belong in yesterday's `as-known-then` view unless they were known then.

A historical gate hold/admission/override, safeguard activation/release, causal confirmation, authority resolution, threshold, waiver, delegated grant, break-glass action, composite health result, readiness suitability result, or retained Explanation remains actual historical state even if later evidence shows another choice would now be preferred.

A current system may generate an `as-known-then` explanation from the historical state cut. That answer is explicitly **reconstructed** unless an actual retained Explanation/report proves what was communicated at the time.

Historical actor authorization/authority standing is reconstructable evidence, but not reusable current permission. Current applicable authority and requester Capability Authorization govern current resolution/disclosure.

## Key product questions

The system should make questions like these straightforward:

- Did this pipeline run, and how long did it take?
- What evidence coverage supports saying it ran—or did not run?
- Which metrics/checks are applicable, selected, supported, unavailable, pending, or not applicable?
- Is this metric Observation definition-compatible with the historical series being compared?
- Is current behavior normal Baseline variation, materially atypical, or normatively unacceptable?
- Which Baseline/reference regime is applicable, and is there enough comparable evidence for the intended claim?
- Is a threshold an explicit Expectation or merely a Baseline range?
- Is evidence near a threshold precise enough for a decisive result?
- Is a violation waived/suspended, and what underlying condition remains?
- Is this schema change compatible for this specific consumer?
- Did a schema/grain/key change invalidate a Baseline or only certain metrics?
- For A+B→C, did source population, join match, fan-out, filtering, dedupe, aggregation, merge behavior, null/default logic, or input-cycle alignment explain the output difference?
- Is a reconciliation mismatch localizing a deviation, or is there enough evidence for an actual causal claim?
- Which component Assessments make up this health profile, and what composition logic applies?
- Is overall health degraded with unresolved dimensions, or merely unresolved with no known failure?
- Can two consumers legitimately have different health results because their profiles/contracts differ?
- Is the latest health result based on fresh evidence for this exact use, or merely recalculated recently?
- What health result is available now and what broader evidence is still pending?
- Is a result mature/suitable enough for this readiness opportunity?
- Is a fresh violation suitable evidence for `not ready`?
- Is a stale `meets` result unsuitable for `ready`?
- Is this metric merely monitored or explicitly control-use eligible?
- Was the required upstream state actually ready before the downstream run started?
- Which readiness predicates are satisfied, failed, unknown, conflicting, unavailable, or supported only by stale/unsuitable evidence?
- Is a gate configured, did it issue a decision, and was that decision actually enforced?
- Is the job merely monitored, or is an explicit dependency gate active?
- Which source/actor is authoritative for the relevant semantic, responsibility, Classification, Policy Context, metric, threshold, schema compatibility, or disclosure rule?
- Is disagreement advisory, an authoritative assertion conflict, a normative conflict, an authorization conflict, or a disclosure conflict?
- Was the currently preferred source also authoritative at incident time?
- Was a relevant change planned, and what prospective blast radius existed?
- Which Deployment was active and what actually changed?
- Where did a relevant condition first become observable?
- Which causal explanations are proposed, supported, weakened, unresolved, rejected, or confirmed?
- What confirmation profile is required and is the confirmer authorized?
- Are multiple contributors compatible, and is any contributor demonstrably primary?
- Which downstream assets are reachable, actually exposed, visibly affected, or tied to business consequence?
- Did the consumer encounter suspect V, earlier V-1, or an unresolved version?
- Does `not exposed` have sufficient negative/path coverage or is telemetry simply missing?
- Was a safeguard proposed, activated, enforced, or materially preventive?
- Who could propose, approve, activate, release, override, delegate, or use break-glass?
- Did approvals exist before action, did the actor issue it, did the control plane accept/enforce it, and what outcome followed?
- Was automation explicitly authorized for this exact action or merely technically capable?
- What fallback was configured and what actually happened during control/authorization outage?
- What policy/restriction context applies and who is responsible?
- What can this analyst see, investigate, operate, gate, confirm, edit, approve, waive, override, or disclose without direct-data access?
- What is intentionally hidden and how does that limit the visible basis without changing internal truth?
- What was known, authoritative, applicable, authorized, approved/delegated, controlled, causally concluded, and disclosed at incident time?
- What changed after late evidence or authority/normative/authorization correction?
- Is this historical Explanation actual retained communication or a present reconstruction?

## Operating environment

Known environment facts remain deliberately small:

- Spark ETL pipelines execute in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a key execution/metadata source;
- Databricks Metric Views and DQX are strongly favored later evaluations;
- Collibra and Immuta are available but optional.

These are environmental facts, not architecture. Availability of Databricks/Unity Catalog, GitHub, Collibra, Immuta, or a human source does not make that source universally authoritative. The monitoring framework should remain independently deployed from production repositories/GitHub Actions unless a later accepted control/integration requirement explicitly needs otherwise.

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.**
3. **Time/history are first-class; event time and knowledge time remain distinct.**
4. **Evidence over narrative completion.**
5. **Evidence sufficiency is proposition- and conclusion-specific, not a universal score.**
6. **Negative evidence requires opportunity-to-observe plus bounded coverage.**
7. **Assertion Authority is scoped; no hidden universal source precedence.**
8. **Source assertion is separate from authoritative standing.**
9. **Assertion Authority is separate from Capability Authorization and Responsibility Assignment.**
10. **Authoritative standing does not imply factual infallibility, evidence sufficiency, compliance, or enforcement.**
11. **Expectation is normative; Baseline is descriptive.**
12. **Metric meaning/profile/threshold/severity/waiver/control-use eligibility remain distinct.**
13. **Metric definition is not Observation; Observation is not Assessment.**
14. **Structural compatibility is not statistical/Baseline comparability.**
15. **Successful execution is not timely execution, schema compatibility, freshness, or data quality.**
16. **Passive monitoring is non-blocking by default.**
17. **Baseline monitoring prefers production-repository independence.**
18. **Lineage does not recursively propagate metrics or health statuses.**
19. **A+B→C reconciliation is transformation-specific; generic row-count conservation is invalid.**
20. **Composite health is profile/use/context bound and dimension preserving, not a universal score.**
21. **Evaluation recency is not evidence freshness; no universal result TTL exists.**
22. **Analytical maturity follows evidence sufficiency, not elapsed time.**
23. **Readiness suitability is exact-use and outcome-neutral.**
24. **Execution gating is explicit opt-in control, not an automatic effect of monitoring, Lineage, authority, or control-use eligibility.**
25. **Execution Gate is separate from Execution History and Propagation Safeguard.**
26. **Readiness is criterion-relative; successful execution is not global readiness.**
27. **Gate decision is not gate enforcement or actual execution.**
28. **Safeguard proposal/request is not enforced active protection.**
29. **Prevented exposure requires material enforced control plus negative/path coverage.**
30. **Lineage discovers relationships/candidates, not cause.**
31. **First-observed localization is not root cause.**
32. **Causal propositions and epistemic status remain explicit.**
33. **Leading/supported hypothesis is not confirmed cause.**
34. **Multiple contributors/unresolved outcomes are valid; one root cause is not required.**
35. **Causal contribution does not imply percentage attribution; primary requires comparative evidence.**
36. **Confirmed causes require evidence profile/standard plus separately resolved confirmation authority.**
37. **Confirmed claims remain challengeable without rewriting historical confirmation.**
38. **Prospective Impact is not actual Impact or retrospective cause.**
39. **Impact is layered: candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution.**
40. **Non-exposure requires negative consumption/path evidence; missing telemetry is not reassurance.**
41. **Criticality influences priority, not evidence strength or threshold truth.**
42. **Propagation Safeguard is protective state, not defect proof.**
43. **Capability Authorization is separate from assertion authority, policy, responsibility, scope, normative authority, and enforcement.**
44. **Raw-data access is separate from analytical visibility, operational control, causal confirmation, and disclosure authority.**
45. **High-consequence proposal, approval, execution, override/release, delegation, break-glass, and automation are separately governed.**
46. **Authorization/approval does not prove action issuance, enforcement, or safe outcome.**
47. **Analyst Investigation remains first-class even with restricted evidence.**
48. **Annotation is attributed context, not a shadow truth store.**
49. **Explanation consumes the authorized projection; it is not a truth or authorization source.**
50. **Audience simplification cannot strengthen underlying status.**
51. **View permission is separate from export/publish/client disclosure.**
52. **Actual historical state remains distinct from replay-derived reconstruction.**
53. **Late evidence or authority/normative/authorization correction can revise retrospective knowledge without rewriting what was known then.**
54. **Historical authority/authorization/disclosure is not current authority/disclosure permission.**
55. **Monitoring must not broaden raw-data or production-control authority.**
56. **Databricks-native first where it fits; integrate before duplicate.**
57. **A Lineage relationship is a bounded semantic proposition, not a generic graph edge.**
58. **Lineage reachability is not question-bound operational relevance, encounter, Impact, or cause.**
59. **Lineage evidence and topology completeness are conclusion-relative; no universal edge confidence/completeness score exists.**

## Canonical A+B→C scenario

Suppose C is produced by joining A and B and materially drops in volume. Historical Lineage discovers A/B and relevant execution/deployment context. B can be the earliest monitored location where deviation appears without automatically becoming root cause.

Phase 004 requires each evidence item to match relevant output/window/grain before supporting a proposition. Evidence that B did not change requires adequate opportunity-to-observe and coverage of the proposed mechanism; absence of an alert is insufficient. Mirrored copies of one Databricks event do not become independent corroboration.

Phase 005 adds separate governance questions: which source/actor has authoritative standing for **business definition, technical schema/key/grain, responsibility, Classification, Policy Context, criticality, metric profile, threshold/schema compatibility Expectation, waiver, and control-use eligibility**? Different layers can legitimately have different authorities.

Phase 006 makes the measurement path explicit. A technical profile may include B key-null rate because it validates a known join failure mode while excluding meaningless identifier quantiles. A business authority may own C's acceptable population range while a platform team owns a technical warning band. Baseline regularity does not create either rule automatically.

If B's schema/key/grain changes, scoped review can suspend affected metric/profile/Baseline use while preserving that empirical comparability is evidence-driven. A migration waiver can suspend a response or bounded applicability without rewriting actual observed state.

For the exact A+B→C join, the framework can evaluate eligible populations, directional match/unmatched rates, matched pairs, zero/one/many-match populations and fan-out. A large C row-count drop may be localized to a collapsing B match rate even if B's raw row count is stable. Conversely, an intentional filter or dedupe can reduce output without being a defect. Generic `rows(A)+rows(B)=rows(C)` is not assumed.

Local upstream health still does not propagate. B can violate an upstream criterion while C meets its own required profile because the transformation isolates/repairs the condition; A and B can both meet while C's transformation introduces a defect.

A composite C health result is profile/use/context bound. One required violation can make a conjunctive profile degraded while an unavailable schema component remains visible as unresolved. Consumer A and Consumer B may have different bounded health results when their contracts/profiles differ.

Phase 007 Group 01 now makes the topology path itself more explicit. A and B can both be `data_derivation` sources for C while carrying different semantic roles—for example A supplying projected values and B determining join/filter population. A table-level A→C relationship does not imply every A field is relevant to every C field, and graph reachability can remain true while a particular field/population path is known not relevant or remains indeterminate.

Causal claims remain explicit. `B match degradation contributed to C row loss` and `join-key nulls contributed to C row loss` can both become supported. A recent Deployment can remain a competing claim; if sufficient evidence shows C degradation began before activation, that claim may be weakened or rejected. No one root cause is forced and no contributor is called primary without comparative evidence.

A supported claim can be useful before confirmation. `Confirmed` requires applicable profile plus separately resolved confirmation authority. A human title, model output, or service-principal identity alone cannot confirm it.

A business analyst may investigate without A/B/C row access using authorized aggregate health metrics, runtime timing, safe Lineage, policy/restriction context, responsibility, authority/normative standing, causal status, Impact, safeguard/gate state, and Annotation. Restricted nodes/evidence/authority details remain opaque rather than being summarized behind the user's permission boundary.

Before C runs, an optional Execution Gate could require current A/B outputs. If B is late, C may be held instead of joining A-current + B-stale. If the criterion requires B current output, freshness, or an eligible schema/quality condition, successful B execution alone does not satisfy the gate.

Phase 006 adds that even a `meets` health Assessment cannot be used if it is stale or otherwise unsuitable for this exact opportunity. A fresh, sufficient `violates` result can be suitable evidence for `not ready`. AUTH-023 eligibility does not itself enable the gate or make stale evidence suitable.

If override is requested, Phase 005 keeps request, approvals, authorization, action issuance, scheduler/control acceptance, enforcement, C execution, and downstream outcome separate. Break-glass can bypass only governed ordinary conditions; it does not make B ready, grant unrelated raw-data access, or prove C healthy.

Downstream, a Metric View and reports may be reachable. Version/refresh evidence can establish one report consumed affected C, another used earlier safe V-1, and another remains exposure-unknown. Safe-version report can be `not exposed to V` while stale. Report metric failure is downstream effect; client delivery/decision consequence needs separate evidence; saying C caused the effect requires Causal Claim.

If an enforced safeguard blocks suspect V before client refresh, prevented exposure requires materially operative control plus negative-consumption/alternate-path coverage. If the report never had a relevant refresh opportunity, the correct statement may be `safeguard active; consumer not exposed` rather than prevention. Older served state remains separately assessed for freshness.

Technical and business audiences can receive different authorized views of this same incident. Engineering may see exact row counts, null rate, threshold, join behavior, schema diff, and causal basis. A business user may see `completeness degraded; current delivery at risk; two supported contributors; one restricted upstream basis`. Neither view may strengthen `supported` to `confirmed`, `reachable` to `affected`, `waived` to clean pass, or `hold decided` to `hold enforced`.

If downstream consumption, enforcement, corrected timing, metric-definition/schema/Baseline/transformation/composite/freshness rules, authority, normative-rule, authorization, approval/delegation, break-glass, or disclosure evidence arrives late, the historical incident-time view remains what was known/authoritative/applicable/authorized/disclosed then while current causal/readiness/exposure/authority resolution may change. Actual historical approvals, gate/safeguard decisions, executions, rules/waivers, health Assessments and retained Explanations are never rewritten.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation navigation/system of record and canonical phase status.
- [`docs/foundation/`](docs/foundation/) — accepted foundation and roadmap.
- [`docs/foundation/011_phase_006_exit_phase_007_handoff.md`](docs/foundation/011_phase_006_exit_phase_007_handoff.md) — accepted Phase 006 exit / original Phase 007 handoff; historical handoff status does not override `docs/README.md`.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — concept specifications and four post-exit addenda.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — completed synchronization contracts/scenarios and exit review.
- [`docs/concepts/phase_004/`](docs/concepts/phase_004/) — completed evidence/time/causality refinement contracts and exit review.
- [`docs/concepts/phase_005/README.md`](docs/concepts/phase_005/README.md) — completed authority/governance/capability/disclosure phase.
- [`docs/concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md`](docs/concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md) — accepted Phase 005 exit review.
- [`docs/concepts/phase_006/README.md`](docs/concepts/phase_006/README.md) — completed health/metrics/schema/statistical/reconciliation/composite/timing phase.
- [`docs/concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`](docs/concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md) — accepted Phase 006 exit review.
- [`docs/concepts/phase_007/README.md`](docs/concepts/phase_007/README.md) — Phase 007 operational refinement plan and group-local progress.
- [`docs/concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/README.md`](docs/concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/README.md) — accepted operational Lineage/historical-topology refinement.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/reference/authority_vocabulary.md`](docs/reference/authority_vocabulary.md) — authority vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history.
- [`AGENTS.md`](AGENTS.md) and [`.cursor/rules/`](.cursor/rules/) — repository-agent guardrails.

## Phase direction

For live repository phase/group progression, use **[`docs/README.md#current-state`](docs/README.md#current-state)**. Phase-local README/AGENTS files define the active group's accepted contracts and next handoff without creating a second repository-wide status authority.
