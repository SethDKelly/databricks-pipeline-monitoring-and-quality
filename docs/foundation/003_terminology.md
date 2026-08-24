# 003 — Foundational Terminology

This document establishes distinctions that must remain stable. The fuller canonical glossary is [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance metadata, authorization state, health evidence, Execution Gates, Investigations, Causal Claims, Impact context, Propagation Safeguards, Annotations, and downstream consumers relevant to monitoring.

### Logical pipeline
A named data-processing responsibility that may span multiple Databricks tasks/jobs and must not automatically equal one repository.

### Repository
A source-control/provenance boundary, not the product reasoning boundary.

### Job / Task / Run
Job is an orchestration definition; Task is a unit within it; Run/execution instance is time-bounded actual work established by execution evidence.

### Execution opportunity
A prospective downstream start context such as a schedule window or trigger opportunity that may be evaluated by an Execution Gate. It is not itself an actual Run.

## Monitoring and quality terms

### Expectation
A normative assertion describing what should be acceptable for a subject/dimension/context/time.

### Baseline
Descriptive reference behavior empirically derived from comparable evidence. Typical does not automatically mean healthy. Ordinary run-to-run variability should be represented by the Baseline comparison context rather than treated as a violation merely because values differ.

### Observation
A provenance-bearing measured/retrieved fact. It does not declare health or cause. Missing evidence is not observed absence.

### Assessment
A dimension-scoped interpretation of Observation evidence against explicit Expectation and/or comparable Baseline context.

### Execution duration / operational latency
Observed timing properties of executions or dependencies. Duration, queue/wait time, completion latency, and dependency readiness can materially affect ecosystem health even when table-level statistical quality is acceptable.

### Dependency readiness
Evidence-backed state describing whether an explicitly relevant upstream prerequisite satisfies the criterion required for a downstream context. The criterion may involve completion, current-cycle output availability, freshness, expected version, or another accepted condition. Readiness is not automatically gate admission.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that freshness violates an applicable Expectation.

### Degradation
A meaningful worsening supported by directional/normative interpretation. A realized Change or Baseline deviation alone is insufficient.

## History, planned change, topology, and execution control

### Change Intent
A registered intended modification and anticipated effects before realization. Intent is not Observation, Change, Expectation, Baseline, actual Impact, or cause.

### Prospective Impact Profile
Pre-realization downstream candidate/blast-radius context produced from Change Intent, current Lineage, planned-only topology, and authorized business/governance context. It does not establish actual exposure, downstream effect, business consequence, causal proof, or quantified probability of harm.

### Deployment
Attempt/activation/active-state/supersession history for source/configuration state applied to a runtime target. Deployment success does not prove data effect.

### Execution History
Actual execution-instance lifecycle history. Missing telemetry cannot create fictional missing runs.

### Execution Gate
An accepted optional active-control concept that owns whether a downstream execution opportunity is admitted, held, admitted after readiness, or explicitly overridden based on declared prerequisite readiness. It is separate from passive monitoring, Assessment, Execution History, Capability Authorization, and Propagation Safeguard.

### Passive monitoring
Observation/analysis mode in which the framework is not a production start-admission dependency. Monitoring degradation should not delay ungated production jobs merely because they are monitored.

### Active execution gating
Explicit opt-in control in which a downstream execution opportunity can be intentionally held until prerequisite readiness is evidenced or an explicit fallback/override applies.

### Gate hold
A downstream execution opportunity is intentionally not admitted. A hold is not an execution failure because the execution may not have started.

### Gate admission
The gate permits the downstream execution to proceed. Admission is not evidence that the run actually occurred or that every upstream health dimension is healthy.

### Gate override
An authorized bypass of the normal readiness result. Override does not transform `not ready` or `unknown` into `ready`.

### Production-repository independence
The architectural objective that baseline monitoring be independently deployed/versioned and prefer no required ETL-code/library/GitHub Actions changes when Databricks/platform/source metadata can satisfy evidence requirements.

### Lineage
Typed, directed, temporal, provenance-bearing relationships. Planned topology is not active Lineage until evidence establishes it.

### Change
A realized difference/state transition established by evidence, without health/intent/causal judgment. Raw numerical difference is not automatically a material Change record.

### Effective/event time
When something occurred or was true.

### Recorded/knowledge time
When monitoring learned/recorded it.

## Authorization and access terms

### Capability Authorization
A provenance-bearing resolution of whether a principal may perform a named capability on an identified subject/context/time. Capability Authorization is separate from Responsibility Assignment, Policy Context, Classification, Monitoring Scope, and enforcement proof.

### Authorized evidence view
The general evidence/concept state a principal may inspect under applicable Capability Authorization.

### Authorized Analytical Projection
The task-specific Phase 003 synchronization result that assembles only the permitted concept state/abstractions needed for monitoring, Impact, RCA, or Explanation. It is not a new truth concept or declassification mechanism.

### Direct/raw data access
Permission to inspect underlying row/record/value data or sensitive columns. This is not a prerequisite for every monitoring/RCA capability.

### Analytical visibility
Permission to inspect approved metadata, aggregate health/Assessment state, Lineage/RCA evidence, Impact, safeguards, Execution Gate state, and Explanation. Analytical visibility does not imply raw-data access or production-control authority.

### Operational job authority
Permission to perform a named job/run operation where later defined, such as retry/update/control. Operational authority does not imply raw-data access, and permission itself does not prove the action succeeded.

### Gate-control authority
Permission to configure/operate/override an Execution Gate where later defined. Gate-control authority is independent from raw-data read and ordinary analytical visibility.

## Investigation and reasoning terms

### Investigation
A bounded inquiry that links evidence, claims, Impact analysis, and human context without owning those truths. Analyst-driven research remains first-class even when direct data is restricted.

### Causal Claim
An explicit proposition that one or more conditions caused/contributed to an outcome, carrying epistemic status plus supporting/contradicting evidence.

### First-observed localization
The earliest monitored point where a related deviation is observed within available evidence/coverage. It narrows investigation but is not root cause.

### Root-cause hypothesis
A Causal Claim that is proposed/supported but not confirmed.

### Confirmed cause
A Causal Claim satisfying an explicit evidence/authority standard. The exact standard remains open.

## Downstream Impact terms

### Impact candidate / reachability
A downstream subject identified through historical typed Lineage as plausibly connected to the originating condition. Reachability does not prove the candidate consumed the affected state.

### Exposure / consumption
Evidence that a downstream candidate actually encountered the relevant affected state/version/time window.

### Not exposed
An exposure conclusion supported by sufficient negative consumption/refresh/version coverage. Missing consumer telemetry is not non-exposure.

### Observed downstream effect
Observation/Assessment/Change evidence describing what happened at the downstream candidate. Effect can be known while exposure remains unresolved and does not establish upstream causation.

### Consequence evidence
Evidence of a technical, analytical, or business outcome such as delay, non-delivery, application behavior, report/metric use, client delivery, process interruption, or decision use. Criticality, client-facing status, exposure, or policy sensitivity alone is not consequence.

### Prevented exposure
Evidence that an active/enforced Propagation Safeguard blocked the relevant suspect state from an otherwise reachable consumer, with sufficient negative-consumption coverage. Prevented suspect-state exposure does not prove fresh/healthy delivery.

### Impact
Downstream reasoning that preserves candidate/reachability, exposure, observed effect, consequence evidence, and causal attribution as distinct strengths. Causal attribution belongs in Causal Claim.

### Criticality
Priority/significance context about downstream importance. It may affect urgency but is not evidence that actual Impact occurred.

### Propagation Safeguard
A protective proposed/active/released state that holds or quarantines a defined output/consumption boundary. It is not a quality Assessment, Causal Claim, Capability Authorization, Execution Gate, or proof that the data is defective or safe.

### Annotation
Attributed human context that cannot silently become Observation, Change Intent, Expectation, Responsibility Assignment, authorization, Impact proof, or causal confirmation.

### Explanation
Authorization- and time-aware evidence-grounded communication composed from the Authorized Analytical Projection. It is not an independent truth or authorization source and can distinguish what was known then from retrospective knowledge now.

## Governance and policy terms

### Responsibility Assignment
A provenance-bearing assertion that a person/team/role bears a named responsibility for a subject/time/context. Responsibility is not universal authority or Capability Authorization.

### Semantic Definition
Provenance-bearing meaning/interpretation assertions.

### Classification
Category membership under a named governance/sensitivity vocabulary; not Policy Context or authorization.

### Policy Context
Declared policy/handling applicability without access enforcement, legal interpretation, Capability Authorization, or compliance determination.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational categories/context according to applicable definitions. Presence of such metadata does not establish compliance.

### Provenance
Where a fact/assertion/definition/intent/relationship/evaluation/gate/claim/impact/safeguard/authorization came from, who/what asserted or derived it, and relevant temporal/version context.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ Capability Authorization;
- responsibility ≠ authorization;
- Policy Context ≠ Capability Authorization;
- raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority ≠ gate-control authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- passive monitoring ≠ active execution gating;
- monitoring availability ≠ ungated production-job availability;
- dependency readiness Assessment ≠ Execution Gate admission state;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- gate hold ≠ execution failure;
- gate admission ≠ actual run occurrence;
- gate override ≠ prerequisite ready;
- missing readiness evidence ≠ ready;
- permission to act ≠ evidence action succeeded;
- pipeline ≠ repository ≠ Databricks job;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- successful run ≠ timely run ≠ freshness ≠ data quality;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- planned topology ≠ active Lineage;
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ consequence ≠ causal attribution;
- `not exposed` ≠ missing telemetry;
- criticality ≠ actual Impact;
- policy sensitivity ≠ compliance consequence;
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- safeguard proposal ≠ active/enforced safeguard;
- prevented exposure ≠ fresh/healthy delivery;
- quarantine ≠ proof of defect;
- safeguard release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ truth/authorization source;
- historical authorization/control state ≠ current disclosure permission;
- effective/event time ≠ recorded/knowledge time;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.
