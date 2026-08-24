# 010 — Open Questions

These questions are intentionally unresolved. Accepted Phase 002–005 boundaries constrain the answers but do not silently decide them.

**Phase 004 is complete with REF-001–REF-030 accepted. Phase 005 is active: Group 01 accepted Assertion Authority and AUTH-001–AUTH-008; Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**

## Accepted authority foundation — Phase 005 Group 01 complete

The following are no longer open questions:

- authority is target/category/facet/scheme/type/subject-scope/context/effective-time scoped rather than globally source-scoped;
- source assertions remain provenance-bearing independently from their authority standing;
- authoritative, advisory, explicitly non-authoritative, conditional, unknown, unavailable, authoritative-conflict, and authority-rule-conflict states remain distinct;
- assertion disagreement, resolved assertion disagreement, authoritative assertion conflict, and authority-rule conflict are different states;
- source count/majority, recency alone, synchronization/ingestion order, source availability, repository ownership, job creator/admin/title, responsibility, or apparent specificity do not create hidden precedence;
- more-specific authority does not automatically override broader authority unless an accepted rule explicitly says so;
- co-authoritative assertions that disagree remain authoritative conflict unless an explicit resolver applies;
- conditional/fallback authority requires an explicit accepted rule plus evidence that its activation condition holds;
- authority rules require provenance/governing basis and cannot self-validate merely by claiming authority;
- Assertion Authority and Capability Authorization are independent;
- Responsibility Assignment, Classification, Policy Context, Monitoring Scope, and organizational title do not automatically confer Assertion Authority;
- authority history is bitemporal; prospective revision, correction, supersession, retirement, and late discovery remain distinct;
- later authority correction may revise retrospective resolution without rewriting `as-known-then` authority;
- authoritative standing does not make evidence sufficient, establish factual infallibility, prove compliance, or prove enforcement.

## Phase 005 Group 02 priority — semantic/governance authority

### Semantic Definition

- Which semantic facets require independently resolvable authority for MVP: business definition, technical description, grain, unit, population/inclusion rules, calculation meaning, domain interpretation, others?
- Which facets permit multiple simultaneous context-specific authoritative definitions rather than conflict?
- Which facets may use local/domain/environment overrides, and what explicit authority rules govern those overrides?
- Which source/actor should be authoritative for each facet in the target environment—Collibra, Unity Catalog/Databricks, repository metadata, human steward, other?
- Which sources should remain advisory/enriching even if they are technically easier to query?
- How should semantic authority behave across migrations, renamed entities, and succession without confusing authority transfer with Entity Identity?

### Responsibility Assignment

- Which responsibility types are required for MVP: technical ownership, business accountability, stewardship, security/privacy responsibility, platform operations, others?
- Which responsibility types permit multiple concurrent authoritative assignees?
- Is inheritance from domain/pipeline/repository ever allowed, and if so under which explicit authority rule rather than implicit containment?
- Which sources/actors are authoritative for each responsibility type in the target environment?
- How should explicitly unassigned responsibility be distinguished from unknown authority or missing assignment evidence?

### Classification

- Which classification schemes/vocabularies are required for MVP?
- Which source/actor is authoritative within each scheme/context?
- How should crosswalk/normalization relate to source authority without replacing original labels?
- Which contexts allow multiple schemes to coexist versus represent a true conflict inside one scheme?
- Which entity/facet kinds need classification in MVP, including columns or metrics if they receive Entity Identity?

### Policy Context

- Which policy-context facts are required for MVP versus later enrichment?
- Which sources/actors are authoritative for policy applicability, handling restrictions, or policy references by context?
- How are jurisdiction/purpose/environment-specific policy authorities represented without universalizing one authority?
- Which policy assertions remain advisory context rather than authoritative applicability?
- How should conflicting authoritative policy applicability remain visible without turning the framework into a legal/compliance adjudicator?
- Which policy summaries can safely be exposed to business users versus governance/security users?

### Criticality

- What criticality dimensions are required: operational, client-facing, financial, regulatory-handling priority, executive reporting, other?
- Who/what is authoritative to declare criticality by subject/context/time?
- Can technical and business criticality coexist as distinct facets rather than conflict?
- How are temporary incident/event priorities distinguished from durable criticality assertions?
- How should criticality influence prioritization without becoming evidence of actual Impact or consequence?

## Phase 005 Group 03 — normative health, metric, and threshold authority

- Who/what may establish/revise each class of Expectation?
- Which expectations may be derived from platform policy versus require human/business authority?
- Who may approve a table/pipeline metric profile or mark a metric business-critical?
- Who may set/revise warning/failure thresholds, margins, tolerance bands, severity, or bounded exceptions?
- How do technical and business threshold authorities interact when both apply?
- How are temporary exceptions/waivers represented without changing observed health truth?
- Who may retire a metric/Expectation and what historical state must remain?
- Which metric/Expectation authority is required before a condition may participate in an Execution Gate or other high-consequence decision?
- How are conflicting authoritative thresholds represented without collapsing into majority vote or hidden composite rules?
- Can Policy Context constrain/propose an Expectation without becoming the normative authority itself?

Phase 006 remains responsible for metric taxonomy, statistical/Baseline semantics, propagation/reconciliation, and health aggregation.

## Phase 005 Group 04 — Capability Authorization

- What canonical capability vocabulary is required for MVP?
- How should allow/deny/conditional/unknown/conflicting authorization states resolve?
- Which authorization sources are authoritative for raw-data access, metadata visibility, derived health, Lineage/RCA, job operations, safeguards, gates, causal confirmation, Annotation, and Explanation?
- How are purpose, environment, tenant, subject, consumer, time, and emergency/break-glass conditions represented?
- How should group/role/service-principal authorization combine without hidden precedence?
- Does capability inheritance exist across domains/pipelines/assets and under which explicit rules?
- Which derived evidence/details are safe to disclose at which abstraction when underlying basis is restricted?
- What historical authorization detail can safely be disclosed to a current requester without inference leakage?
- How should authorization decisions and external enforcement evidence be audited/retained?

## Phase 005 Group 05 — causal-confirmation and high-consequence action authority

- Which principals/processes may hold causal-confirmation capability for each claim class, subject, context, and environment?
- Which claim classes require explicit human confirmation even if automation meets the evidence standard?
- Under what narrowly defined conditions, if any, may automated confirmation be explicitly authorized?
- Who assigns/approves the applicable confirmation profile/standard for a claim class?
- How are confirmation-authority conflicts/revocations handled while preserving historical confirmation provenance?
- Who may configure/enable/retire an Execution Gate?
- Who may override/expire/cancel a gate decision by target/environment/context?
- Who may propose, activate, release, cancel, or expire a Propagation Safeguard?
- Which control actions may be pre-authorized/automatic and under what explicit rule/authority?
- Which job/run operational actions require distinct capability from gate/safeguard authority?
- How do emergency/break-glass operations affect capability without granting raw-data access?
- What delegation, multi-party approval, expiry, revocation, or separation-of-duties semantics are needed?

## Phase 005 Group 06 — disclosure / Explanation governance

- Which policy/restriction/metric/threshold/authority/causal/Impact/control details may be disclosed by audience/capability?
- When may a restricted entity/path or authoritative source be acknowledged as existing but remain opaque?
- Which high-consequence statements require additional review before business/client-facing Explanation?
- How should authorization-limited basis affect wording without turning hidden evidence into absence?
- How should technical versus business projections differ without creating separate truth?
- Which authority-rule/holder details are themselves sensitive and may need opaque disclosure?
- What historical authority/authorization detail can be disclosed without revealing restricted governance hierarchy?

## Monitoring result availability and execution timing — Phases 006/009/010/011

Phase 004 accepts progressive analytical availability, but exact targets remain open:

- Which validations belong on an **immediate operational** path: job start/completion/success/failure, queue/duration, direct output existence, dependency state, gate state?
- Which health results can be **near-real-time/enriched** versus delayed because they depend on Metric Views, DQX, Baseline comparison, semantic context, or source refresh?
- What evidence is required before **RCA** begins automatically, and which RCA outputs should be incremental versus post-ops?
- What belongs specifically in **post-operations review** because it depends on late/corrected consumption, consequence, authority, or historical evidence?
- What maximum evidence age/result age is acceptable for each health dimension and audience?
- Which source availability/collection latencies are inherent to Databricks job metadata, Metric Views, DQX, GitHub/deployment evidence, Lineage, consumption evidence, governance systems, and authority sources?
- Which analyses can be precomputed/cached versus reconstructed on demand without violating historical truth?
- What latency budgets preserve useful near-real-time monitoring without placing passive monitoring on the ungated production critical path?
- Which explicitly gated decisions require synchronous evidence/control behavior and what availability objectives apply?

## Historical time, retention, authority, and replay — later phases

- Which historical states require retained events/snapshots versus reconstructible version history in MVP?
- Which authority rules/assertions need retained snapshots/events versus reconstructible history?
- What source/integration evidence establishes source-availability time when it differs from framework knowledge time?
- What retention/coverage is needed before `not recorded by` or `not known by` is safely answerable for each evidence class?
- What evidence establishes authority-rule source availability time separately from framework knowledge time?
- What notification/escalation behavior should occur when retrospective conclusions or authority resolutions materially change?
- What retention/audit requirements apply to actual historical Explanation versus reconstructed Explanation?
- Which high-consequence historical authority/authorization/control states must be retained rather than merely reconstructible?

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
- How does Assertion Authority scope reference domains/sets without creating implicit Entity Identity or authority inheritance?

## Expectations, Baselines, health, metrics, and quality — Phase 006

- Which first-MVP Expectation dimensions and bounded-exception states are required?
- Which first-MVP metric families and per-table/pipeline metric profiles are required?
- Which metrics belong in a small core versus critical-field/business, transformation-specific, and diagnostic/on-demand tiers?
- Which Baseline classes are required: ranges, distributions, cadence/duration profiles, seasonal cohorts, others?
- What evidence establishes Baseline non-comparability after structural Change?
- What statistical/anomaly behavior is needed beyond transparent comparisons?
- What threshold/margin/tolerance semantics are required: absolute, relative, asymmetric, warning/failure bands, low-volume/sample-size rules?
- What Assessment status vocabulary is appropriate for normative versus comparative results?
- Does composite/overall health warrant dedicated behavior or only explicit aggregation?
- Which health Assessments are expected immediately, near-real-time, delayed, or post-ops?
- Which dependency-readiness criterion classes belong in the health model versus control policy?
- How do Metric Views and DQX align with accepted Expectation/Observation/Assessment semantics?
- What selective transformation-aware metric propagation/reconciliation is valid across A+B→C joins, filters, aggregations, deduplication, and other patterns?
- How should technical and business health projections remain one truth while showing different metric detail?

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
- How should UI distinguish candidate/exposure/effect/consequence and decision/enforcement/action?
- How should UI distinguish authoritative/advisory/conflicting/unknown authority without implying factual certainty?
- How should UI distinguish contemporaneous, retrospective, comparison, actual-retained, and reconstructed historical Explanation?
- How should `available now`, `pending evidence`, `enriched`, `RCA in progress`, and `retrospectively updated` be communicated?

## Security and privacy

- Which monitoring metadata, authority rules/holders, intent, topology, causal claims, Impact details, control state, or Annotations are sensitive by themselves?
- May users know a restricted entity/path or authority holder exists if they cannot inspect it?
- Will any Investigation require row-level examples, and if so how are they minimized/redacted/authorized?
- What audit/retention requirements apply to evidence, authority resolutions, Investigations, causal status/confirmation, Annotations, questions, control state, and retained Explanations?

## Integration scope — Phase 009

- Which Databricks/Unity Catalog capabilities provide required job/run/schema/Lineage/history evidence today?
- Which DQX capabilities align with accepted health concepts?
- Where do Metric Views add semantic/measurement value?
- What can GitHub Actions reliably prove about Deployment attempt and activation?
- Which systems can provide Change Intent?
- Which concrete authority targets should Collibra, Immuta, Unity Catalog/Databricks, GitHub/repository metadata, or human governance actors satisfy in the deployment environment?
- Which sources are authoritative versus advisory for each category, and what evidence/governing basis establishes those mappings?
- Which sources provide sufficiently historical evidence for event-time + knowledge-cut replay, including authority-rule history?
- What are production-to-queryable and queryable-to-framework latency characteristics of each evidence/authority source?
- Which sources provide version/refresh/consumer-use evidence for representative downstream classes?
- Which sources provide trustworthy gate/safeguard decision and enforcement evidence?
- Can optional Execution Gate semantics be realized without modifying production repositories/GitHub Actions, and where would exceptions be unavoidable?

## MVP pilot

- Which 2–5 representative pipelines exercise cross-repository dependencies, A+B→C, planned change, unintended side effect, downstream Impact, and optional gating?
- Which business analyst/report/Metric View provides a meaningful exposure/consequence case?
- Which assets carry useful governance/policy context without unsafe real data in development?
- Which pilot validates authoritative versus advisory semantics, co-authoritative conflict, and an authority correction over time?
- Which pilot validates contemporaneous/retrospective replay with intentionally late/corrected synthetic evidence?
- Which pilot validates progressive result availability from job validation through health metrics, RCA, and post-ops review?
- Which pilot validates multiple simultaneous causal contributors and later challenge/reversal?
- Which pilot validates gate decision versus actual enforcement and safeguard active versus materially prevented exposure?
