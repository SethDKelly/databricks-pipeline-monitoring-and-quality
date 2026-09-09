# Shared Glossary

**Canonical key:** `reference.glossary`

**Kind:** REFERENCE

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `reference.glossary`

**Owns current question:** What do the shared DMTZ terms mean at a compact reference level today?

**Stable IDs:** N/A

## Use

This glossary provides compact current vocabulary. It does not replace the detailed current owners of accepted concepts or stable-ID contracts; use the CKR ownership inventory for those until later domains are canonicalized.

## Core ecosystem

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance/authority/authorization state, health/quality evidence, controls, Investigations, causal/Impact state, consumers, Annotations, Explanations, and historical knowledge relevant to monitoring.

### Logical pipeline
A logical data-processing responsibility that may span multiple jobs/tasks/repositories and is not automatically any one of them.

### Repository
A source-control/provenance boundary, not the product reasoning boundary.

### Job / Task / Run
Job is an orchestration definition; Task is a unit within it; Run/execution instance is time-bounded actual work established by execution evidence.

### Execution opportunity
A prospective downstream start/admission context such as a schedule window or trigger opportunity; not an actual Run.

## Scope, identity, authority, and authorization

### Monitoring Scope
Time-aware declaration of whether DMTZ is responsible for monitoring an Entity Identity. Scope is not authorization and does not automatically propagate through Lineage.

### Entity Identity
Functionality for deciding when source-specific references denote the same logical entity across systems/time while preserving ambiguity, separation, validity, and correction provenance.

### Assertion Authority
Provenance-bearing authority determining whether an assertion source/actor may establish a proposition/category as authoritative for the applicable subject/context/time. Technical privilege or source availability alone does not confer it.

### Capability Authorization
Provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time, including conditions, conflicts/unknowns, effective interval, and revision history.

### Authorized evidence view
The set of concept/evidence state a principal may inspect for a particular subject/context/purpose.

### Authorized Analytical Projection
Task-specific permitted subset/abstraction of DMTZ evidence/concept state assembled for analysis or Explanation. It is not a new truth source, persistence layer, or declassification mechanism.

### Direct/raw data access
Permission to inspect underlying rows/records/values or sensitive fields. Lack of raw-data access does not automatically prohibit independently authorized monitoring/RCA/Impact/Explanation.

### Analytical visibility
Permission to inspect approved metadata, aggregate health/Assessment, Lineage/RCA, Impact, control, or Explanation state; not raw-data or production-control authority.

### Operational job authority
Permission to perform a named job/run operation. Authorization to act does not establish that the action occurred or succeeded.

### Safeguard-control authority
Capability Authorization to configure/operate/release/override a Propagation Safeguard as applicable. It is distinct from analytical visibility and raw-data access.

### Gate-control authority
Capability Authorization to configure/enable/operate/override an Execution Gate. It is independent from raw-data access, ordinary analytical visibility, responsibility, and generic job authority unless an explicit rule says otherwise.

### Causal-confirmation authority
Authority/capability required, in addition to the applicable confirmation evidence standard, to record a Causal Claim as confirmed.

## Semantics, responsibility, governance, and policy

### Semantic Definition
Provenance-bearing assertion describing what an identified entity means in a relevant business/technical context/time.

### Responsibility Assignment
Provenance-bearing assertion that a person/team/role bears a named responsibility for a subject/time/context. Responsibility is not universal authority or Capability Authorization.

### Classification
Category membership under a named governance/sensitivity vocabulary, preserving source/provenance/time/conflict.

### Policy Context
Declared policy/handling applicability for a subject/context/time without itself claiming enforcement, authorization, legal interpretation, or compliance.

### Criticality
Importance/priority context about an entity or downstream use. It is not evidence that exposure, effect, consequence, or causal Impact occurred.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational classification/context according to applicable definitions. Such metadata does not itself establish compliance or violation.

## Health evaluation

### Expectation
Provenance-bearing normative assertion describing what should be true/acceptable for a subject/dimension/context/time.

### Baseline
Descriptive reference behavior derived from comparable Observation evidence. Typical does not automatically mean healthy.

### Observation
Provenance-bearing measured/retrieved fact. Missing evidence is not observed absence.

### Assessment
Dimension-scoped interpretation of applicable authorized Observation evidence against explicit Expectation and/or comparable Baseline context, preserving basis/history.

### Execution duration
Elapsed execution time derived from compatible start/completion evidence. It is an Observation until evaluated against a Baseline/Expectation.

### Operational latency / readiness
Timing relationship among upstream execution/output availability and downstream execution/delivery needs.

### Dependency readiness
Evidence-backed state describing whether a relevant prerequisite satisfies the explicit readiness criterion for a downstream context. It is not automatically an Execution Gate decision.

### Readiness criterion / profile
Explicit set of prerequisite conditions required for a particular downstream/gate context. No upstream subject is globally `ready` independent of criterion and opportunity.

### Readiness predicate
One independently evaluable condition within a readiness criterion, such as qualifying execution completion, output existence, version/currentness, freshness, or named Assessment state.

### Freshness
Observed currency/timeliness.

### Staleness
Normative Assessment that observed freshness violates an applicable freshness Expectation.

### Degradation
Meaningful worsening supported by directional/normative interpretation. Baseline deviation or realized Change alone is insufficient.

## Evidence sufficiency and availability

### Evidence applicability
Whether evidence actually bears on a bounded proposition given subject identity, property/semantics, event time/window, grain/version, derivation, and relationship context.

### Coverage profile
Bounded description of what population/opportunities/time/source/query/version/measurement/instrumentation was observable. Coverage is proposition/context specific, not globally complete.

### Opportunity to observe
Whether the evidence mechanism/query/source could detect the relevant event/state if it occurred in the bounded context.

### Conclusion-specific evidence sufficiency
Whether an applicable evidence set is adequate for a particular bounded conclusion under its applicable standard. Sufficiency is not an intrinsic universal evidence score.

### Observed absence
Negative fact supported by sufficient applicable coverage and opportunity to observe. Missing telemetry is not observed absence.

### Source production/observation time
When a source produced or directly observed a fact/event.

### Source availability time
When evidence became queryable/available from its source. Availability does not imply DMTZ knew it.

### Framework collection/retrieval time
When DMTZ retrieved/received the evidence.

### Framework recorded/knowledge time
When evidence/assertion entered the DMTZ knowledge state usable for reasoning/replay.

### Derived evaluation time
When a derived Assessment, causal/Impact/readiness/control/Explanation result was produced.

### Progressive analytical availability
Expose the narrowest trustworthy result when the evidence required for that result is known rather than forcing early operational answers to wait for slower enrichment. Functional horizons are immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review.

## Change, deployment, Lineage, history, and control

### Change Intent
Registered intended modification and anticipated effects before realization. Intent is not Observation, realized Change, Expectation, actual Impact, or cause.

### Prospective Impact Profile
Pre-realization downstream candidate/blast-radius context using Change Intent, active/planned topology, and authorized semantic/governance context. It does not establish actual exposure/effect/consequence/cause or numeric harm probability.

### Deployment
Functionality/history for deployment attempts and resolving which source/configuration state was active for a target/time. Attempt/workflow success/activation remain distinct; activation does not prove data effect or health.

### Execution History
Functionality for reconstructing actual execution-instance/lifecycle history. Missing telemetry does not create fictional execution or absence.

### Lineage
Typed, directed, temporal, provenance-bearing relationships among Entity Identities. Current topology does not overwrite historical topology; planned topology is not active until evidence establishes it.

### Change
Realized difference/state transition established by evidence. Change does not itself mean intended, healthy, degraded, valid, material, or causal.

### Passive monitoring
Default observational mode in which monitoring does not place DMTZ on the production start critical path.

### Active execution gating
Explicit opt-in control mode in which a downstream execution opportunity may be held until prerequisites are evidenced or an accepted fallback/override applies.

### Execution Gate
Optional active-control concept governing whether a downstream execution opportunity is held, admitted, or explicitly overridden based on declared prerequisite readiness and authority.

### Gate hold
Gate state in which an opportunity is intentionally not admitted. A hold is not an execution failure because a Run may not have started.

### Gate admission
Gate state indicating permission to proceed. Admission is not evidence that the Run actually occurred or every health dimension is healthy.

### Gate override
Authorized bypass of normal readiness result. Override does not convert not-ready/unknown/conflicting into ready.

### Gate decision
Selected/requested gate action/state for a specific opportunity after readiness/fallback/override evaluation. Decision is not enforcement proof.

### Gate enforcement
Evidence-backed conclusion that a gate decision actually affected the specific downstream execution opportunity at the relevant control boundary/time.

### Gate fallback behavior
Explicit configured behavior for unavailable/unknown readiness/control state. DMTZ has no universal fail-open/fail-closed rule.

### Control fallback application
Evidence that configured fallback behavior was actually recognized/applied/enforced for a specific opportunity.

### Control evidence state
Evidence status of an active-control path, such as decision known, delivery unknown, enforcement known/unknown/contradicted, source unavailable, fallback configured/application known/unknown.

### Production-repository independence
Architectural objective that baseline monitoring be independently deployable/versioned and prefer no required ETL-code/library/CI changes where source/platform metadata can satisfy evidence needs.

## Historical replay and evolving knowledge

### Effective/event time
When a condition was true or event occurred.

### Historical state cut
Synchronization view resolving relevant accepted state for an event/effective-time question under a specified recorded/knowledge cutoff. It is not a separate truth-owning concept.

### Contemporaneous view
Historical state cut using a knowledge cutoff representative of what was known at or near the historical time.

### Retrospective view
Same historical event/window considered with a later knowledge cutoff that may include late/corrected evidence.

### Replay-derived interpretation
Current computation over a historical state cut. It does not prove the same Assessment/claim/Impact/control/Explanation was actually recorded or believed then.

### Actual historical state
Concept state/action/assertion established as actually recorded/effective by the historical cutoff.

### Historical correction / retrospective re-evaluation
Late/corrected evidence is recorded at its real knowledge time and may create new derived state about an earlier event while prior contemporaneous state remains reconstructable.

### Counterfactual control rewrite
Replacing an actual historical gate/safeguard action with what later evidence suggests should have happened. This is not historical replay and cannot substitute for actual history.

## Investigation and causality

### Investigation
Bounded inquiry into a question, symptom, unexpected outcome, or uncertainty by linking evidence, Causal Claims, Impact, and Annotations without becoming the source of those facts/conclusions.

### Evidence candidate
Entity/relationship/state structurally or temporally relevant enough to inspect. Candidate relevance is not causal support.

### First-observed localization
Earliest monitored point where a related deviation is visible within available evidence/coverage. It narrows inquiry but is not root cause.

### Causal Claim
Provenance-bearing proposition that one or more conditions caused/contributed/enabled/materially influenced a defined outcome, with explicit epistemic status, supporting/contradicting evidence, and revision history.

### Proposed causal claim
Explicit causal proposition not yet evaluated enough for a stronger status.

### Supported causal claim
Applicable evidence materially supports the proposition, but separate confirmation requirements are not satisfied.

### Weakened causal claim
Support has materially reduced through contradiction, limitations, gaps, or alternatives without sufficient evidence to reject.

### Unresolved causal claim
Substantively evaluated claim for which evidence remains materially insufficient, conflicting, non-discriminating, unavailable, or restricted.

### Rejected causal claim
Evidence is sufficient under the applicable rejection standard to reject the proposition; stronger than merely unsupported/lower-ranked.

### Confirmed cause
Causal Claim satisfying the applicable claim-class confirmation evidence profile/standard **and** independently resolved causal-confirmation authority, with provenance-bearing confirmation action/history.

### Confirmation profile / standard
Named/versioned claim-class evidence/decision standard defining the required causal dimensions and evidence conditions for confirmation. There is no universal causal-confidence score.

### Material alternative
Competing explanation relevant enough that ignoring it would materially overstate a focal claim within the bounded scope/evidence cut.

### Causal role
Qualitative role such as direct, contributing, enabling, triggering, preventing, primary, or unresolved where supported. Qualitative role is not percentage attribution.

### Progressive RCA maturity
Candidate/proposed claims → early supported/weakened/unresolved evaluation → deeper Investigation → retrospective/confirmation review. Speed never upgrades epistemic status by itself.

### Confirmation challenge / reversal
Material late/corrected evidence can require reevaluation of a current confirmed claim while preserving the historical confirmation event/evidence cut/authority/standard.

## Impact and protection

### Impact
Downstream reasoning preserving candidate/reachability, exposure/encounter, observed effect, consequence evidence, and causal attribution as distinct strengths.

### Impact candidate / reachability
Downstream Entity Identity plausibly connected through relevant historical typed Lineage. Candidate status is not exposure, effect, consequence, or cause.

### Exposure proposition
Bounded proposition asking whether a specified downstream consumer encountered a specified affected state/version/window through a relevant relationship/encounter mode during a defined opportunity/window.

### Encounter mode
Functional way a downstream subject can encounter/use state, such as execution input, refresh/materialization, publication/serving, query/application use, or business-process use.

### Exposure / consumption
Evidence that a downstream candidate actually encountered the relevant affected state/version/time window.

### Safe-version encounter
Evidence a consumer encountered a sufficiently identified non-affected earlier/alternate state. It can support not-exposed-to-affected-state while still being stale/unhealthy for another reason.

### Not exposed
Negative exposure conclusion supported by sufficient consumption/refresh/version and material-path coverage. Missing consumer telemetry is not not-exposed.

### No encounter opportunity
Consumer had no relevant run/refresh/use opportunity for the bounded exposure proposition. Distinct from an observed opportunity with no encounter.

### Observed downstream effect
Observation/Assessment/Change evidence showing a condition at the downstream candidate. Effect can be known while exposure remains unresolved and does not itself establish upstream cause.

### Consequence evidence
Provenance-bearing evidence of technical, analytical, or business outcome such as delayed/non-delivery, application behavior, report/metric use, client delivery, process interruption, or decision use.

### Propagation Safeguard
Optional protective proposed/active/released hold or quarantine at a defined output/consumption boundary. It is separate from quality Assessment, Causal Claim, Capability Authorization, Execution Gate, and proof the state is defective/safe.

### Safeguard enforcement
Evidence-backed conclusion that the safeguard actually placed the protected subject/output/missing-output context into the intended state at the relevant propagation/consumption boundary, scope, and interval.

### Prevented exposure
Evidence that an otherwise reachable consumer did not encounter the relevant suspect state because an active/enforced safeguard was materially operative on the relevant encounter path, with sufficient applicable negative/path coverage.

### Analyst intervention
Human research via Investigation or an authorized operational/safeguard/gate action; not a separate concept.

## Human context and Explanation

### Annotation
Attributed human-authored context attached to ecosystem state without mutating source evidence or silently substituting for structured intent, Expectation, governance, authorization, Impact proof, or causal confirmation.

### Explanation
Authorization- and time-aware evidence-grounded communication composed from permitted concept/evidence state. It is not an independent truth or authorization source.

### Actual retained historical Explanation
Explanation/report evidence establishes was actually generated/retained at the historical knowledge time; current disclosure still applies.

### Reconstructed historical Explanation
Present-day Explanation generated from a historical state cut and labeled reconstructed when no retained historical snapshot proves the same communication existed then.

### Statement-to-basis traceability
Each material Explanation statement is internally traceable to authorized supporting concept/evidence state, epistemic status, temporal perspective, and disclosure/redaction context.

## Evidence, provenance, and source authority

### Evidence
Provenance-bearing fact/assertion used to support evaluation, Investigation, Causal Claim, Impact, control reasoning, or Explanation.

### Provenance
Information describing where a fact/assertion/definition/intent/deployment/relationship/evaluation/control/claim/Impact/authorization/Explanation came from and its relevant temporal/version/derivation/correction context.

### Authority / source precedence
Rules determining which source/actor is authoritative for a proposition/category/capability/subject/context/time. DMTZ has no universal authority rule; unresolved applicable conflicts remain conflicts until accepted category-specific semantics resolve them.

## Historical replay questions

Where evidence permits, DMTZ distinguishes:

1. What happened?
2. What was known then?
3. What was believed/interpreted then?
4. What was authorized then?
5. What control state/action applied then?
6. What enforcement/exposure conclusion was known then?
7. What causal status existed then?
8. What was actually explained then?
9. What do we know now?

## Key non-equivalences

- Monitoring Scope ≠ Capability Authorization;
- Responsibility Assignment ≠ Capability Authorization ≠ Assertion Authority;
- Policy Context ≠ Capability Authorization;
- source availability/technical privilege ≠ Assertion Authority;
- raw-data access ≠ analytical visibility ≠ job-operation authority ≠ safeguard authority ≠ gate-control authority ≠ causal-confirmation authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- passive monitoring ≠ active execution gating;
- dependency readiness ≠ gate decision ≠ gate enforcement ≠ actual execution;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- gate hold ≠ execution failure;
- gate admission ≠ actual Run occurrence;
- gate override ≠ prerequisite ready;
- configured fallback ≠ actual fallback application;
- missing readiness/control evidence ≠ ready/enforced/fail-open/fail-closed;
- permission to act ≠ action succeeded;
- successful execution ≠ timely execution ≠ freshness ≠ structural compatibility ≠ data quality;
- evidence applicability ≠ coverage ≠ conclusion-specific sufficiency;
- evidence not found ≠ observed absence;
- source availability ≠ framework knowledge ≠ derived evaluation;
- raw difference ≠ material Change;
- atypicality ≠ normative violation ≠ mandatory intervention;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- no encounter opportunity ≠ no encounter ≠ safe-version encounter ≠ unknown-version encounter;
- not-exposed-to-suspect-state ≠ fresh/current/healthy;
- criticality/policy sensitivity ≠ actual Impact/consequence/compliance failure;
- first-observed localization ≠ root cause;
- leading/supported Causal Claim ≠ confirmed cause;
- unresolved claim ≠ merely proposed/unevaluated;
- rejected claim ≠ merely unsupported/lower-ranked;
- Investigation closure ≠ confirmation;
- confirmation evidence sufficiency ≠ confirmation authority;
- one contributor ≠ exclusion of other compatible contributors;
- safeguard proposal/configuration/request ≠ enforcement;
- safeguard enforcement at one boundary ≠ every route;
- active safeguard + non-exposure ≠ automatically prevented exposure;
- prevented exposure ≠ fresh/healthy delivery;
- quarantine ≠ defect proof;
- release ≠ health proof;
- Annotation ≠ structured operational truth;
- Explanation ≠ truth/authorization source;
- effective/event time ≠ source availability ≠ framework knowledge ≠ derived evaluation;
- current state ≠ historical state cut;
- later evidence ≠ evidence known then;
- actual historical state ≠ replay-derived interpretation;
- actual historical gate/safeguard action ≠ counterfactual preferred action;
- actual retained historical Explanation ≠ reconstructed historical Explanation;
- historical authorization/control state ≠ current disclosure permission.

## Concept Design

### Concept
Independently understandable unit of functionality with a clear purpose, operational principle, state, actions, invariants/ambiguity behavior, and composition through synchronizations.

### Synchronization
Defined coordination between independent concepts without collapsing their purposes/state/authority or selecting technical architecture.

### Refinement contract
Accepted `REF-###` contract constraining how evidence/time/causal/exposure/readiness/control conclusions may be evaluated. A refinement contract is not a new truth-owning concept.

## Synchronizations / related canonical resources

- [Foundational terminology](terminology.md)
- [Concept Design method](concept-design-method.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Security and governance policy](../policies/security-governance.md)

## Provenance

- Original glossary owner: [`../../reference/glossary.md`](../../reference/glossary.md)
- Foundational terminology: [`../../foundation/003_terminology.md`](../../foundation/003_terminology.md)
- Evidence/time/causality refinements: [`../../concepts/phase_004/README.md`](../../concepts/phase_004/README.md)
- Authority/governance refinements: [`../../concepts/phase_005/README.md`](../../concepts/phase_005/README.md)
- Health/operations refinements: [`../../concepts/phase_006/README.md`](../../concepts/phase_006/README.md), [`../../concepts/phase_007/README.md`](../../concepts/phase_007/README.md)
- Explanation/integration/architecture refinements: [`../../concepts/phase_008/README.md`](../../concepts/phase_008/README.md), [`../../concepts/phase_009/README.md`](../../concepts/phase_009/README.md), [`../../concepts/phase_010/README.md`](../../concepts/phase_010/README.md)
