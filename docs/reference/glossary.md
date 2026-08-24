# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during later design, but changes must be reflected consistently across foundation, concept, synchronization, and decision documents.

## Core ecosystem

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage relationships, governance metadata, Capability Authorization state, health/quality evidence, Investigations, causal reasoning, Impact context, Propagation Safeguards, downstream consumers, Annotations, and Explanations relevant to monitoring. An entity may be known while outside Monitoring Scope.

### Logical pipeline
A logical data-processing responsibility that transforms or moves data. It may span one or more jobs/tasks and does not automatically equal a repository.

### Repository
A source-control boundary and provenance context, not the product reasoning boundary.

### Job / Task / Run
A Job is an orchestration definition; Task is a unit inside it; Run/execution instance is time-bounded actual work established by execution evidence.

## Scope, identity, and authorization

### Monitoring Scope — Accepted
The time-aware declaration of whether the product is responsible for monitoring an Entity Identity. Scope is not authorization and does not implicitly propagate through Lineage.

### Entity Identity — Accepted
Functionality for deciding when source-specific references denote the same logical entity across systems/time while preserving ambiguity, separation, validity, and correction provenance.

### Capability Authorization — Accepted post-exit addendum
Functionality for resolving whether a principal may perform a named capability on a subject/context/time, with provenance, conditions, effective interval, conflict/unknown behavior, and historical revision.

Capability classes are independently resolvable. The model must distinguish direct/raw data read, sensitive-value access, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, operational job/run actions, safeguard actions, and Explanation/report access without selecting an IAM implementation.

Responsibility Assignment, Classification, Policy Context, Monitoring Scope, repository ownership, job creator identity, and platform administration do not silently grant Capability Authorization.

### Authorized evidence view
The general set of concept/evidence state a principal is permitted to inspect for a specific context/purpose. It can vary by subject, evidence facet, time, and capability.

### Authorized Analytical Projection
The Phase 003 Group 05 synchronization result that assembles the **task-specific permitted subset/abstraction** of concept state for a requesting principal. It may expose approved aggregate health metrics, Assessment status, execution timing, redacted/opaque Lineage, policy/restriction summaries, responsibility context, Causal Claim status, Impact, safeguard state, and Annotation while withholding restricted rows, columns, thresholds, entity identities, or evidence details.

The projection is not a new truth-owning concept, persistence layer, or declassification mechanism. Derived evidence is not automatically unrestricted, and restricted evidence is not retrieved merely to synthesize a more complete summary.

### Direct/raw data access
Permission to inspect underlying rows/records/values or sensitive fields. Lack of direct-data access does not automatically prevent independently authorized monitoring, Investigation, RCA, Impact analysis, or Explanation.

### Analytical visibility
Permission to inspect approved metadata, aggregate health/Assessment state, Lineage/RCA evidence, Impact, safeguards, and Explanation. Analytical visibility does not imply raw-data access or production-control authority.

### Operational job authority
Permission to perform a named job/run operation where later defined. It is independent from raw-data read and analytical visibility. Authorization to act does not establish that the action succeeded.

## Semantics, responsibility, governance, policy

### Semantic Definition — Accepted
Provenance-bearing semantic assertions describing what an entity means in a relevant business/technical context/time.

### Responsibility Assignment — Accepted
Who bears a named responsibility for an identified subject/time. Responsibility does not imply universal authority or Capability Authorization.

### Classification — Accepted
Category membership under named governance/sensitivity vocabularies, preserving source meaning/provenance/time/conflict.

### Policy Context — Accepted
Declared policy applicability/handling context for subject/context/time without claiming enforcement, Capability Authorization, legal interpretation, or compliance.

### Criticality
Context describing how important an entity is to downstream business or operational processes. Group 05 treats criticality as priority/significance context, **not** evidence that exposure, downstream effect, business consequence, or causal Impact actually occurred. Exact representation remains deferred to later governance/Impact refinement.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational categories/context according to applicable definitions. Presence of such metadata does not itself establish compliance.

## Health evaluation

### Expectation — Accepted
A provenance-bearing normative assertion describing what should be true/acceptable for subject/dimension/context/time.

### Baseline — Accepted
Descriptive reference behavior derived from comparable Observation evidence. Ordinary variation appropriate to the comparison context should remain within the Baseline model rather than becoming alert noise simply because consecutive runs differ.

### Observation — Accepted
A provenance-bearing measured/retrieved fact. Missing evidence is not observed absence.

### Assessment — Accepted
A dimension-scoped interpretation of authorized Observation evidence against explicit Expectation and/or comparable Baseline context, preserving its basis/history.

An actor may be authorized to see an Assessment result while some underlying Observation values, thresholds, or Baseline details remain restricted.

### Execution duration
Elapsed execution time derived from compatible execution start/completion evidence. Duration is an Observation before it is compared with a Baseline or Expectation.

### Operational latency / readiness
Timing relationship among upstream execution/output availability and downstream execution/delivery needs.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that observed freshness violates an applicable freshness Expectation.

### Degradation
A meaningful worsening supported by explicit directional/normative interpretation. Baseline deviation or realized Change alone is insufficient.

## History, lineage, and change

### Change Intent — Accepted
Functionality for registering an intended modification and anticipated effects before realization. Anticipated effects are not automatically Expectations, Observations, Changes, actual Impact, or causes.

### Prospective Impact Profile
A pre-realization downstream candidate/blast-radius view built from Change Intent, active Lineage, planned-only topology, and authorized criticality/semantic/governance context. It does not establish actual exposure, downstream effect, business consequence, causal proof, or a numeric probability/severity score.

### Execution History — Accepted
Functionality for reconstructing actual execution instances/lifecycle states and provenance over time. Missing telemetry does not create a fictional execution or absence.

### Deployment — Accepted
Functionality for recording deployment attempts and resolving which source/configuration state was active for a target/time. Attempt/workflow success/activation remain distinct; activation does not prove data effect or health.

### Lineage — Accepted
Functionality for maintaining/traversing typed, directed, temporal, provenance-bearing relationships among Entity Identities. Current topology does not overwrite historical topology; planned topology is not active until evidence establishes it.

Lineage requires graph-compatible semantics, but no graph database/query language/service has been selected. A principal can receive an authorized redacted/opaque Lineage view without receiving direct-data access or every node identity.

### Change — Accepted
Functionality for identifying/describing a realized difference or state transition established by evidence. Change does not itself mean intended, healthy, degraded, valid, invalid, or causal.

### Effective/event time
When a condition was true or an event occurred.

### Recorded/knowledge time
When the monitoring ecosystem learned or recorded it.

## Investigation, causality, impact, protection, and communication

### Investigation — Accepted
Functionality for organizing a bounded inquiry into a question, symptom, unexpected outcome, or uncertainty by linking evidence, Causal Claims, Impact analysis, and Annotations without becoming the source of those facts/conclusions.

Investigation/RCA capability does not imply direct-data access or complete evidence visibility. Restricted evidence may remain opaque while the Investigation preserves the limitation.

### Evidence candidate
An entity/relationship/state identified as structurally or temporally relevant enough to inspect during Investigation. Candidate relevance is not causal support by itself.

### First-observed localization
The earliest monitored point where a related deviation becomes visible within available evidence/coverage. It narrows the problem but is not root cause.

### Causal Claim — Accepted
A provenance-bearing proposition that one or more conditions caused/contributed/enabled/materially influenced a defined outcome, with explicit epistemic status plus supporting/contradicting evidence and revision history.

### Confirmed cause
A Causal Claim satisfying an explicit accepted evidence/authority standard. The exact standard remains deferred.

### Impact — Accepted
Functionality for reasoning about downstream consequence while keeping separate candidate/reachability, actual exposure/consumption, observed downstream effect, and evidenced technical/analytical/business consequence.

### Impact candidate / reachability
A downstream Entity Identity is a plausible candidate because historical typed Lineage shows a relevant path from the originating condition/subject. Candidate status is not evidence that the downstream entity consumed the affected state, changed, or experienced business consequence.

### Exposure / consumption
Evidence that a downstream candidate actually encountered the relevant affected state/version/time window. Exposure is stronger than reachability but is not automatically downstream degradation or causal attribution.

### Not exposed
A negative Impact exposure determination supported by sufficient consumption/refresh/version coverage. Missing consumer telemetry is not `not exposed`.

### Observed downstream effect
Downstream Observation/Assessment/Change evidence showing a condition at the candidate itself. The effect may be known while exposure to the originating state remains unknown; exposure may also be proven while monitored downstream health remains acceptable.

### Consequence evidence
Provenance-bearing evidence of a technical, analytical, or business consequence such as delayed publication, application behavior, report/metric use, client delivery, process interruption, decision use, or other established outcome. Criticality, client-facing status, exposure, or policy sensitivity alone is not consequence evidence.

### Prevented exposure
An evidence-backed statement that an otherwise reachable downstream consumer did not encounter the relevant suspect state because an **active/enforced Propagation Safeguard** blocked the applicable path/boundary, with sufficient negative-consumption coverage. A proposed safeguard is insufficient.

Prevented exposure does not mean the downstream state was fresh/healthy. A safeguard can prevent suspect-version exposure while separately causing lateness or non-delivery.

### Propagation Safeguard — Accepted post-exit addendum
Functionality for representing a protective proposed/active/released hold or quarantine at a defined output/consumption boundary. Safeguard action authority is separately resolved through Capability Authorization.

### Analyst intervention
Human research through Investigation or an authorized operational/safeguard decision. It is not a separate concept.

### Annotation — Accepted
Attributed human-authored context attached to ecosystem state without mutating source evidence or silently substituting for structured truth or authorization. Human consequence context can inform Impact while retaining its human-source provenance and dispute/withdrawal state.

### Explanation — Accepted
Authorization- and time-aware communication composed from concept state/evidence. Group 05 formalizes that Explanation consumes the Authorized Analytical Projection rather than hidden evidence directly. Different audiences may receive different safe detail/abstraction, but epistemic status, Impact layering, human-source status, and material statement-to-basis traceability remain intact.

### Statement-to-basis traceability
The requirement that each material Explanation statement be internally traceable to the authorized concept state/evidence, epistemic status, and authorization/redaction context supporting it. Visible citation UI is deferred, but internal traceability is required.

## Evidence and provenance

### Evidence
A provenance-bearing fact/assertion used to support Assessment, Investigation, Causal Claim, Impact, safeguard decisions, or Explanation.

### Observed absence
A negative fact supported by sufficient source/query coverage. Missing telemetry is not observed absence.

### Provenance
Information describing where a fact/assertion/definition/classification/intent/deployment/relationship/Expectation/Baseline/Observation/Assessment/Change/claim/annotation/impact/safeguard/authorization state came from and its temporal/version context.

### Authority / source precedence
Rules determining which source/actor is authoritative for a category/capability/subject/context/time. The project has no universal authority rule; unresolved conflicts remain conflicts until accepted category-specific semantics exist.

## Key non-equivalences

- Monitoring Scope ≠ Capability Authorization;
- Responsibility Assignment ≠ Capability Authorization;
- Policy Context ≠ Capability Authorization;
- raw-data access ≠ analytical visibility ≠ job-operation authority ≠ safeguard authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- permission to act ≠ action succeeded;
- successful execution ≠ timely execution ≠ freshness ≠ data quality;
- raw difference ≠ material Change;
- atypicality ≠ normative violation ≠ mandatory intervention;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- Impact candidate/reachability ≠ exposure;
- exposure ≠ observed downstream effect;
- observed downstream effect ≠ consequence;
- consequence ≠ causal attribution;
- `not exposed` ≠ missing telemetry;
- criticality ≠ actual Impact;
- policy sensitivity ≠ policy breach/compliance failure;
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- safeguard proposal ≠ active/enforced safeguard;
- prevented exposure ≠ fresh/healthy delivery;
- quarantine ≠ defect proof;
- release ≠ health proof;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth/authorization source;
- historical authorization ≠ current disclosure permission;
- missing telemetry ≠ missing run/output.

## Concept Design

### Concept
An independently understandable unit of functionality with a clear purpose, operational principle, state, and actions, composed via synchronizations.

### Synchronization
Defined coordination between independent concepts without collapsing their purposes/state into one concept or selecting technical architecture.
