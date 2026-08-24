# 010 — Open Questions

These questions are intentionally unresolved. Accepted Phase 002–005 boundaries constrain the answers but do not silently decide them.

**Phase 004 is complete with REF-001–REF-030 accepted. Phase 005 is active: Groups 01–05 are accepted with AUTH-001–AUTH-043; Group 06 — Disclosure, Explanation & Audience Governance is next and has not started.**

## Accepted Phase 005 authority/governance foundation — Groups 01–05 complete

The following are no longer open questions:

- authority is target/category/facet/scheme/type/subject-scope/context/effective-time scoped rather than globally source-scoped;
- source assertions remain provenance-bearing independently from their authority standing;
- no hidden authority precedence from source count, recency, synchronization order, availability, responsibility, title, repository ownership, or apparent specificity;
- Assertion Authority and Capability Authorization are independent;
- authority history is bitemporal and cannot manufacture evidence sufficiency, factual infallibility, compliance, or enforcement;
- semantic authority is facet-specific, including technical schema, grain, field/key role, business definition, population, and calculation meaning;
- responsibility authority is responsibility-type scoped;
- Classification/criticality authority is scheme/context scoped; criticality remains contextual priority, not Impact/health proof;
- policy reference authority can differ from subject/context policy-applicability authority;
- local/context governance does not automatically override broader governance and governance assertions do not implicitly propagate through Lineage/containers;
- governed schema meaning, normative structural compatibility, and realized schema state remain separate truths;
- Expectation authority is dimension/property/context/time/lifecycle-action scoped;
- metric meaning, metric-profile inclusion, threshold/margin, severity, waiver, and high-consequence-use eligibility are independently governable;
- metric profiles are governed selection/applicability structures and technical availability does not justify metric bloat;
- Baseline-derived ranges remain descriptive until an authoritative Expectation adopts a normative criterion;
- structural/schema compatibility Expectations require explicit normative authority;
- authority cannot manufacture empirical Baseline comparability after structural Change;
- bounded exceptions/waivers/suspensions do not rewrite Observations/Baselines/realized schema or create false `pass` results;
- normative conflict does not silently use strictest/business/technical/latest/highest-severity precedence;
- authoritative/business-critical metrics are not automatically eligible for active control;
- control-use eligibility remains separate from control capability, evidence readiness, and enforcement;
- Capability Authorization is exact-action/detail scoped with `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` retained distinctly;
- unresolved authorization never becomes permission, while runtime refusal without positive allow does not rewrite unresolved truth into a fabricated deny;
- user/group/role/service-principal composition and capability inheritance require explicit rules and historical evidence rather than hidden precedence;
- raw rows, schema, metrics, thresholds, Baselines, Lineage, RCA, causal/Impact/control detail, normative actions, and Explanation can be independently authorized;
- Authorized Analytical Projection is a synchronization/view over existing truth, not declassification or a new concept;
- requester visibility and framework/service-principal evidence-processing authorization are separate;
- aggregate/derived monitoring evidence may itself be sensitive or inference-leaking;
- historical authorization is non-rewriting and is not reusable as current permission;
- authorization never proves action occurrence, external enforcement, or success;
- high-consequence proposal/request, approval/authorization, execution/issuance, external acceptance, enforcement/effect, and outcome remain separate facts;
- causal confirmation remains jointly evidence- and authority-gated, with human-versus-automated confirmation governed by claim class/profile rather than a universal rule;
- job/run operational actions are granular and independent from raw-data, gate, safeguard, and deployment authority;
- Execution Gate registration/configuration/normal operation/override/fallback/retirement and Propagation Safeguard proposal/activation/release/recovery can have different authorized principals;
- multi-party approval, quorum, ordering, distinct-principal requirements, and self-approval rules are explicit conditional-authorization semantics rather than universal defaults;
- exercising a high-consequence capability does not implicitly grant delegation authority; delegated grants are bounded, historical, expiring/revocable, and non-transitive unless explicit;
- break-glass is explicit bounded emergency authorization, not universal superuser access, and cannot manufacture raw-data access, readiness, health, evidence sufficiency, causality, or enforcement;
- service/model technical ability does not create automated high-consequence authority; exact service-principal capability and any required human review remain explicit;
- authorization-outage fallback is action-specific and does not rewrite `unknown`, `conflicting`, or `unavailable` authorization truth;
- an already enforced protective state may remain actual during an authorization outage without implying that anyone has new authority to change it.

Concrete source/actor mappings, organizational approver classes, and technical realization remain later work. Metric/statistical/schema-health calculation semantics remain Phase 006 work.

## Phase 005 Group 06 priority — disclosure / Explanation governance

- Which policy/restriction/metric/schema/threshold/waiver/authority/authorization/causal/Impact/control details may be disclosed by audience and capability?
- When may a restricted entity/path, authoritative source, approver, confirmer, delegate, break-glass actor, or service principal be acknowledged as existing but remain opaque?
- Which high-consequence statements require additional review before business/client-facing Explanation?
- How should authorization-limited basis affect wording without turning hidden evidence into absence?
- How should technical versus business projections differ without creating separate truth?
- Which authority-rule/holder, approval-chain, delegation, break-glass, gate/safeguard configuration, or control-service details are sensitive and may require opaque disclosure?
- How should the product communicate `confirmed`, `overridden`, `held`, `released`, `break-glass`, or `automated action` without implying broader health, safety, compliance, or causal certainty than the underlying state supports?
- When is it safe to disclose that multiple approvals occurred while hiding actor identities or role structure?
- What historical authority/authorization/normative/high-consequence-action detail can be disclosed without revealing restricted governance or security hierarchy?
- How should unresolved/conflicting authorization or authority be explained when the rule/source detail itself is restricted?

## Monitoring result, authorization, and control-path availability — Phases 006/009/010/011

Phase 004 accepts progressive analytical availability and Group 05 accepts action-specific authorization fallback, but exact targets remain open:

- Which validations belong on an **immediate operational** path: job start/completion/success/failure, queue/duration, direct output existence, dependency state, gate state, simple schema-contract state?
- Which health results can be **near-real-time/enriched** versus delayed because they depend on Metric Views, DQX, Baseline comparison, semantic context, schema evidence, or source refresh?
- What evidence is required before **RCA** begins automatically, and which RCA outputs should be incremental versus post-ops?
- What belongs specifically in **post-operations review** because it depends on late/corrected consumption, consequence, authority, authorization, or historical evidence?
- What maximum evidence age/result age is acceptable for each health dimension and audience?
- Which source availability/collection latencies are inherent to Databricks job/schema metadata, Metric Views, DQX, GitHub/deployment evidence, Lineage, consumption evidence, governance systems, and authority/authorization sources?
- Which analyses can be precomputed/cached versus reconstructed on demand without violating historical truth?
- What latency budgets preserve useful near-real-time monitoring without placing passive monitoring on the ungated production critical path?
- Which AUTH-023 control-eligible decisions require synchronous evidence/control behavior and what availability objectives apply?
- Which high-consequence authorization/approval sources must meet production-critical availability objectives for gate/safeguard operations?
- Which action classes may preserve current protective state, escalate, refuse action, or use an explicitly authorized fallback principal when authorization resolution is unavailable?
- How quickly must revocation, expiry, delegated-grant changes, and break-glass termination become effective on production control paths?

## Historical time, retention, authority, authorization, and replay — later phases

- Which historical states require retained events/snapshots versus reconstructible version history in MVP?
- Which authority rules/assertions and normative rule/waiver/profile states need retained snapshots/events versus reconstructible history?
- Which Capability Authorization, approval, delegation, break-glass, service-principal authorization, action issuance, control-plane acceptance, and enforcement states must be retained rather than reconstructed?
- What source/integration evidence establishes source-availability time when it differs from framework knowledge time?
- What retention/coverage is needed before `not recorded by` or `not known by` is safely answerable for each evidence class?
- What evidence establishes authority/authorization-source availability time separately from framework knowledge time?
- What notification/escalation behavior should occur when retrospective conclusions, authority/normative resolutions, or authorization/action history materially change?
- What retention/audit requirements apply to actual historical Explanation versus reconstructed Explanation?
- What immutable or append-only audit properties, if any, are required for high-consequence approvals/actions in the eventual implementation?

## Causal profiles and quantitative reasoning — Phases 007/010+

Group 05 establishes the generic authority framework; concrete causal-profile design remains open:

- Which claim classes need distinct confirmation profiles for MVP: deterministic control mechanism, version-mediated propagation, data transformation, Deployment causation, business consequence causation, others?
- Which causal evidence dimensions are mandatory versus optional for each profile?
- Which concrete claim classes must require human confirmation, and which narrowly deterministic classes may permit explicitly authorized automated confirmation?
- Which principal classes or governed processes should be eligible confirmers for each deployment-specific claim profile?
- When does quantitative attribution become necessary, and what model/evidence standard would justify percentages?
- How should causal chains among several claims be represented/displayed if simple claim references become insufficient?
- What notification/escalation follows a materially challenged/reversed previously confirmed claim?

## Entity identity and scope realization

- Which entity kinds require first-MVP Entity Identity beyond pipelines, jobs/tasks, data assets, repositories, consumers, and deployment-related entities?
- How are logical pipeline identities established when one pipeline spans multiple jobs or one job hosts multiple logical pipelines?
- Which cross-source identity associations may be inferred versus requiring authoritative assertion?
- Which intermediate/external assets are independently included in Monitoring Scope for MVP?
- How does Assertion Authority scope reference domains/sets without creating implicit Entity Identity or authority inheritance?

## Expectations, Baselines, health, metrics, schema, and quality — Phase 006

- Which first-MVP Expectation dimensions and bounded-exception states are required?
- Which first-MVP metric families and per-table/pipeline metric-profile semantics are required?
- Which metrics belong in a small core versus critical-field/business, transformation-specific, and diagnostic/on-demand tiers?
- Which Baseline classes are required: ranges, distributions, cadence/duration profiles, seasonal cohorts, others?
- What evidence establishes Baseline non-comparability after structural Change?
- What statistical/anomaly behavior is needed beyond transparent comparisons?
- What threshold/margin/tolerance semantics are required: absolute, relative, asymmetric, warning/failure bands, low-volume/sample-size rules?
- How should a bounded waiver/exception be represented in Assessment/overall-health output without creating a false pass?
- What schema/DDL compatibility taxonomy is needed for add/drop/rename/type/nullability/key/grain/nested-field and consumer-specific compatibility?
- What Assessment status vocabulary is appropriate for normative versus comparative results?
- Does composite/overall health warrant dedicated behavior or only explicit aggregation?
- Which health Assessments are expected immediately, near-real-time, delayed, or post-ops?
- Which dependency-readiness criterion classes belong in the health model versus control policy?
- How do Metric Views and DQX align with accepted Expectation/Observation/Assessment semantics?
- What selective transformation-aware metric propagation/reconciliation is valid across A+B→C joins, filters, aggregations, deduplication, and other patterns?
- How should technical and business health projections remain one truth while showing different metric detail?
- For AUTH-023 control-eligible conditions, what evidence freshness/availability/computation characteristics make them safe inputs to readiness/control evaluation?

## Change Intent, Deployment, execution, and control policy — Phases 007/009/010

- Which source/actor may register authoritative Change Intent?
- What minimum anticipated-effect/monitoring-implication fields are required for MVP?
- How should Change Intent relate to pull requests, tickets, configuration changes, release metadata, or other planning systems?
- What evidence proves Deployment activation rather than attempt/workflow success for representative patterns?
- How are configuration-only changes related when source revision is unchanged?
- What minimum logical execution reconstruction is needed when pipelines span jobs/tasks?
- Which dependency/readiness criteria are safe for automatic gating after AUTH-023 eligibility and Group 05 control authority are resolved?
- Which concrete gate/safeguard action classes require one approver, multiple approvers, separation of duties, delegated authority, or break-glass in the target deployment?
- What gate classes need explicit hold/allow/escalate/expire behavior for unavailable readiness or authorization evidence?
- What maximum wait, timeout, escalation, expiry, and override semantics are required?
- What recovery/audit behavior applies if the control integration or authorization source itself is degraded?
- Which service principals should execute ordinary gate/safeguard actions, and which actions must remain human-executed or human-approved?

## Lineage and historical topology — Phase 007/009

- What minimal Lineage relationship taxonomy is required for MVP?
- What Lineage is already trustworthy/historical in Databricks for relevant Spark patterns?
- Which relationships must repositories/integrations assert explicitly?
- Which Lineage sources are authoritative versus inferred/advisory by relationship type?
- How should inferred relationship confidence/topology completeness be represented without a universal evidence score?
- Which graph-compatible technical realization is appropriate later, if any?

## Investigation — Phase 007

- What Investigation lifecycle/status vocabulary is required for MVP?
- Are related/nested Investigations needed or are references sufficient?
- Which Assessments/change mismatches automatically open Investigation versus surface a prompt?
- What closure/reopen/retention rules are appropriate?
- What workflow follows a Causal Claim becoming confirmed, challenged, or rejected without making Investigation own causal truth?

## Downstream Impact — Phase 007

- What exact first-MVP vocabulary represents candidate/reachability, exposure, downstream effect, and business consequence?
- Which consumer/encounter patterns must have evidence adapters for first MVP?
- Which business processes/decisions need first-class Entity Identity?
- How should criticality prioritize Impact without being mistaken for consequence evidence?
- Which alternate-path coverage is realistically required for high-confidence non-exposure/prevention by consumer class?

## Annotation

- Which actors may annotate which referents?
- Are structured Annotation types needed in addition to free text?
- What moderation/retention rules prevent unsafe or low-quality sensitive notes?
- Which Annotations may appear in business-facing Explanation without explicit review?

## Explanation and question answering — Phase 008

- Is natural-language interaction required in MVP or is a structured question surface sufficient?
- Which question types must be deterministic versus generative?
- Which material statements require visible evidence citations/links by audience?
- Should generated Explanations be dynamically resolved, retained snapshots, or both?
- How should authorization differences across a path be explained without inference leakage?
- How should UI distinguish causal statuses without implying numeric confidence?
- How should UI distinguish candidate/exposure/effect/consequence and authorization/approval/decision/enforcement/action?
- How should UI distinguish authoritative/advisory/conflicting/unknown authority without implying factual certainty?
- How should UI distinguish threshold conflict, waived/suspended rule state, and actual metric/Assessment result?
- How should UI distinguish ordinary, delegated, break-glass, and automated high-consequence actions without implying broader authority?
- How should UI distinguish contemporaneous, retrospective, comparison, actual-retained, and reconstructed historical Explanation?
- How should `available now`, `pending evidence`, `enriched`, `RCA in progress`, and `retrospectively updated` be communicated?

## Security and privacy

- Which monitoring metadata, authority rules/holders, normative metric/schema/threshold/waiver state, intent, topology, causal claims, Impact details, control state, approval chains, delegation/break-glass state, service-principal identity, or Annotations are sensitive by themselves?
- May users know a restricted entity/path, authority holder, approver, confirmer, delegate, or control service exists if they cannot inspect it?
- Will any Investigation require row-level examples, and if so how are they minimized/redacted/authorized?
- What audit/retention requirements apply to evidence, authority/normative resolutions, authorization, approvals/delegations/break-glass actions, Investigations, causal confirmation, questions, control state, and retained Explanations?

## Integration scope — Phase 009

- Which Databricks/Unity Catalog capabilities provide required job/run/schema/Lineage/history evidence today?
- Which DQX capabilities align with accepted health concepts?
- Where do Metric Views add semantic/measurement value?
- What can GitHub Actions reliably prove about Deployment attempt, proposed schema compatibility, and activation?
- Which systems can provide Change Intent?
- Which concrete authority targets should Collibra, Immuta, Unity Catalog/Databricks, GitHub/repository metadata, or human governance actors satisfy in the deployment environment?
- Which sources are authoritative versus advisory for each category, and what evidence/governing basis establishes those mappings?
- Which sources can authoritatively resolve Capability Authorization, approval/delegation/break-glass state, and service-principal high-consequence capability for each action class?
- Which sources provide sufficiently historical evidence for event-time + knowledge-cut replay, including authority/normative/authorization/action history?
- What are production-to-queryable and queryable-to-framework latency characteristics of each evidence/authority/authorization source?
- Which sources provide version/refresh/consumer-use evidence for representative downstream classes?
- Which sources provide trustworthy gate/safeguard action-issuance, control-plane acceptance, and enforcement evidence?
- Can optional Execution Gate semantics be realized without modifying production repositories/GitHub Actions, and where would exceptions be unavoidable?

## MVP pilot

- Which 2–5 representative pipelines exercise cross-repository dependencies, A+B→C, planned/schema change, unintended side effect, downstream Impact, and optional gating?
- Which business analyst/report/Metric View provides a meaningful exposure/consequence case?
- Which assets carry useful governance/policy context without unsafe real data in development?
- Which pilot validates authoritative versus advisory semantics, co-authoritative conflict, and an authority correction over time?
- Which pilot validates normative threshold conflict, a bounded waiver, metric-profile anti-bloat, and schema compatibility by consumer?
- Which pilot validates restricted-data RCA with result visibility while threshold/raw/schema/Lineage basis remains partly opaque?
- Which pilot validates high-consequence request → approval → action → enforcement → outcome separation, including a delegated or break-glass path?
- Which pilot validates a service-principal normal gate action while override remains human-authorized?
- Which pilot validates contemporaneous/retrospective replay with intentionally late/corrected synthetic evidence?
- Which pilot validates progressive result availability from job validation through health metrics, RCA, and post-ops review?
- Which pilot validates multiple simultaneous causal contributors and later challenge/reversal?
- Which pilot validates gate decision versus actual enforcement and safeguard active versus materially prevented exposure?
