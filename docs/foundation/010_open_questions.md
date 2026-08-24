# 010 — Open Questions

These questions are intentionally unresolved. Accepted Phase 002–004 boundaries constrain the answers but do not silently decide them.

**Phase 004 is complete with REF-001–REF-030 accepted. Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is next and has not started.**

## Accepted evidence/time/causality/control foundation — Phase 004 complete

The following are no longer open questions:

- evidence sufficiency is conclusion-relative rather than a universal score;
- evidence applicability, bounded coverage, corroboration/conflict, and conclusion sufficiency remain distinct;
- negative/absence/exclusion evidence requires adequate opportunity-to-observe and coverage;
- event/effective time, source availability, framework knowledge time, and evaluation time remain distinct;
- `as-known` cuts use evidence known to the framework by the cutoff;
- source availability does not backdate framework knowledge;
- `known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are distinct propositions;
- monitoring/reasoning may mature progressively without evidence-status inflation;
- late evidence, explicit correction, independent conflict, reinterpretation, and later authority resolution remain distinct;
- actual historical state requires evidence it existed then; otherwise replay is reconstructed;
- causal status is `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- `rejected` requires sufficient contradiction/exclusion evidence;
- `confirmed` is a separate claim-class evidence gate with independently resolved confirmation authority;
- multiple compatible causal contributors may coexist; no single root cause is required;
- exposure requires actual affected-state encounter rather than reachability/timing;
- `not exposed` requires sufficient negative consumption/path coverage;
- readiness is criterion-relative rather than a global upstream status;
- readiness result, gate decision, gate enforcement, and actual execution remain separate;
- safeguard proposal/configuration/request does not prove enforcement;
- prevented exposure requires materially operative safeguard enforcement plus negative-consumption/version and alternate-path coverage;
- configured fallback is not proof of actual fallback application/enforcement;
- late control/consumption evidence can revise retrospective conclusions without rewriting historical actions.

## Phase 005 priority — authority, governance, policy, capability

### Source/actor authority and conflict resolution

- What source/actor is authoritative for each metadata, semantic, governance, normative, authorization, and control-policy category by subject/environment/time?
- Which assertions are authoritative versus enriching/advisory?
- How are conflicting assertions resolved without deleting provenance/history?
- What correction/supersession authority is needed for each category?
- When does an unresolved source conflict remain visible rather than being resolved automatically?
- Does repeated category-specific authority behavior warrant additional structured authority semantics, or are integration contracts sufficient?

### Semantic/governance authority

- Is Collibra authoritative for Semantic Definition, Responsibility Assignment, criticality, or stewardship in the target environment?
- Is Immuta authoritative for Classification/Policy Context, or does it provide policy/enforcement context only?
- Which Unity Catalog/Databricks metadata is authoritative versus observed/enriching?
- Who may establish/revise business meaning, ownership/responsibility, criticality, and classification/policy applicability?
- How do different governance contexts/tenants/environments override or coexist without one global definition?

### Expectation and normative authority

- Who/what may establish/revise each class of Expectation?
- Which expectations may be derived from platform policy versus require human/business authority?
- How are temporary exceptions/waivers represented without changing observed health truth?
- Can policy context propose or constrain an Expectation without itself becoming the normative authority?

### Capability Authorization

- What canonical capability vocabulary is required for MVP?
- How should allow/deny/conditional/unknown/conflicting authorization states be resolved?
- Which authorization sources are authoritative for raw-data access, metadata visibility, derived health, Lineage/RCA, job operations, safeguard actions, gate actions/override, causal confirmation, and Explanation access?
- How are purpose, environment, tenant, subject, consumer, time, and emergency/break-glass conditions represented?
- How should group/role/service-principal authorization combine without creating hidden precedence rules?
- Which derived evidence/details are safe to disclose at which abstraction when underlying basis is restricted?
- What historical authorization detail can be disclosed to a current requester without inference leakage?

### Causal-confirmation authority

- Which principals/processes may hold **causal-confirmation capability** for each claim class, subject, context, and environment?
- Which claim classes require explicit human confirmation even if automated evidence conditions are met?
- Under what narrowly defined conditions, if any, may an automated process be authorized to confirm a Causal Claim?
- Who assigns/approves the applicable confirmation profile/standard for a claim class?
- How are confirmation-authority conflicts/revocations handled while preserving historical confirmation provenance?

### Execution Gate / Propagation Safeguard authority

- Who may configure/enable/retire an Execution Gate?
- Who may override/expire/cancel a gate decision by target/environment/context?
- Who may propose, activate, release, cancel, or expire a Propagation Safeguard?
- Which control actions may be pre-authorized/automatic and under what explicit rule/authority?
- How do emergency operations affect capability without granting raw-data access?
- How do gate/safeguard policy authority and actual enforcement evidence remain separate?

### Explanation/disclosure governance

- Which policy/restriction/causal/Impact/control details may be disclosed by audience/capability?
- When may a restricted entity/path be acknowledged as existing but remain opaque?
- Which high-consequence statements require additional review before business-facing Explanation?
- How should authorization-limited basis affect wording without turning hidden evidence into absence?

## Monitoring result availability and execution timing — Phases 006/009/010/011

Phase 004 accepts progressive analytical availability, but exact targets remain open:

- Which validations belong on an **immediate operational** path: job start/completion/success/failure, queue/duration, direct output existence, dependency state, gate state?
- Which health results can be **near-real-time/enriched** versus delayed because they depend on Metric Views, DQX, Baseline comparison, semantic context, or source refresh?
- What evidence is required before **RCA** begins automatically, and which RCA outputs should be incremental versus post-ops?
- What belongs specifically in **post-operations review** because it depends on late/corrected consumption, consequence, or historical evidence?
- What maximum evidence age/result age is acceptable for each health dimension and audience?
- Which source availability/collection latencies are inherent to Databricks job metadata, Metric Views, DQX, GitHub/deployment evidence, Lineage, consumption evidence, and governance systems?
- Which analyses can be precomputed/cached versus reconstructed on demand without violating historical truth?
- What latency budgets preserve useful near-real-time monitoring without placing passive monitoring on the ungated production critical path?
- Which explicitly gated decisions require synchronous evidence/control behavior and what availability objectives apply?

## Historical time, retention, and replay — later phases

- Which historical states require retained events/snapshots versus reconstructible version history in MVP?
- What source/integration evidence establishes source-availability time when it differs from framework knowledge time?
- What retention/coverage is needed before `not recorded by` or `not known by` is safely answerable for each evidence class?
- What notification/escalation behavior should occur when retrospective conclusions materially change?
- What retention/audit requirements apply to actual historical Explanation versus reconstructed Explanation?
- Which high-consequence historical states must be retained rather than merely reconstructible?

## Causal profiles and quantitative reasoning — Phases 005/007/010+

- Which claim classes need distinct confirmation profiles for MVP: deterministic control mechanism, version-mediated propagation, data transformation, Deployment causation, business consequence causation, others?
- Which causal evidence dimensions are mandatory versus optional for each profile?
- Which statuses/confirmation actions require human review even if automation can evaluate the evidence?
- When does quantitative attribution become necessary, and what model/evidence standard would justify percentages?
- How should causal chains among several claims be represented/displayed if simple claim references become insufficient?
- What notification/escalation follows a materially challenged/reversed previously confirmed claim?

## Entity identity and scope realization

- Which entity kinds require first-MVP Entity Identity beyond pipelines, jobs/tasks, data assets, repositories, consumers, and deployment-related entities?
- How are logical pipeline identities established when one pipeline spans multiple jobs or one job hosts multiple logical pipelines?
- Which cross-source identity associations may be inferred versus requiring authoritative assertion?
- Which intermediate/external assets are independently included in Monitoring Scope for MVP?

## Expectations, Baselines, health, quality — Phase 006

- Which first-MVP Expectation dimensions and bounded-exception states are required?
- Which Baseline classes are required: ranges, distributions, cadence/duration profiles, seasonal cohorts, others?
- What evidence establishes Baseline non-comparability after structural Change?
- What statistical/anomaly behavior is needed beyond transparent comparisons?
- What Assessment status vocabulary is appropriate for normative versus comparative results?
- Does composite/overall health warrant dedicated behavior or only explicit aggregation?
- Which health Assessments are expected immediately, near-real-time, delayed, or post-ops?
- Which dependency-readiness criterion classes belong in the health model versus control policy?
- How do Metric Views and DQX align with accepted Expectation/Observation/Assessment semantics?

## Change Intent, Deployment, execution, and control policy — Phases 005/007

- Which source/actor may register authoritative Change Intent?
- What minimum anticipated-effect/monitoring-implication fields are required for MVP?
- How should Change Intent relate to pull requests, tickets, configuration changes, release metadata, or other planning systems?
- What evidence proves Deployment activation rather than attempt/workflow success for representative patterns?
- How are configuration-only changes related when source revision is unchanged?
- What minimum logical execution reconstruction is needed when pipelines span jobs/tasks?
- Which dependency/readiness criteria are safe for automatic gating?
- What gate classes need explicit hold/allow/escalate/expire behavior for unavailable evidence?
- What maximum wait, timeout, escalation, expiry, and override semantics are required?
- What recovery/audit behavior applies if the control integration itself is degraded?

## Lineage and historical topology — Phase 007/009

- What minimal Lineage relationship taxonomy is required for MVP?
- What Lineage is already trustworthy/historical in Databricks for relevant Spark patterns?
- Which relationships must repositories/integrations assert explicitly?
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
- How should UI distinguish candidate/exposure/effect/consequence and decision/enforcement/action?
- How should UI distinguish contemporaneous, retrospective, comparison, actual-retained, and reconstructed historical Explanation?
- How should `available now`, `pending evidence`, `enriched`, `RCA in progress`, and `retrospectively updated` be communicated?

## Security and privacy

- Which monitoring metadata, intent, topology, causal claims, Impact details, control state, or Annotations are sensitive by themselves?
- May users know a restricted entity/path exists if they cannot inspect it?
- Will any Investigation require row-level examples, and if so how are they minimized/redacted/authorized?
- What audit/retention requirements apply to evidence, Investigations, causal status/confirmation, Annotations, questions, control state, and retained Explanations?

## Integration scope — Phase 009

- Which Databricks capabilities provide required job/run/Lineage/history evidence today?
- Which DQX capabilities align with accepted health concepts?
- Where do Metric Views add semantic/measurement value?
- What can GitHub Actions reliably prove about Deployment attempt and activation?
- Which systems can provide Change Intent?
- Are Collibra/Immuta necessary for MVP or later enrichment?
- Which sources provide sufficiently historical evidence for event-time + knowledge-cut replay?
- What are production-to-queryable and queryable-to-framework latency characteristics of each evidence source?
- Which sources provide version/refresh/consumer-use evidence for representative downstream classes?
- Which sources provide trustworthy gate/safeguard decision and enforcement evidence?
- Can optional Execution Gate semantics be realized without modifying production repositories/GitHub Actions, and where would exceptions be unavoidable?

## MVP pilot

- Which 2–5 representative pipelines exercise cross-repository dependencies, A+B→C, planned change, unintended side effect, downstream Impact, and optional gating?
- Which business analyst/report/Metric View provides a meaningful exposure/consequence case?
- Which assets carry useful governance/policy context without unsafe real data in development?
- Which pilot validates contemporaneous/retrospective replay with intentionally late/corrected synthetic evidence?
- Which pilot validates progressive result availability from job validation through health metrics, RCA, and post-ops review?
- Which pilot validates multiple simultaneous causal contributors and later challenge/reversal?
- Which pilot validates gate decision versus actual enforcement and safeguard active versus materially prevented exposure?
