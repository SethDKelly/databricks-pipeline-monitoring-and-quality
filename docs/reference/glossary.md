# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during later design, but changes must be reflected consistently across foundation, concept, synchronization, and decision documents.

## Core ecosystem

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage relationships, governance metadata, Capability Authorization state, health/quality evidence, Execution Gates, Investigations, causal reasoning, Impact context, Propagation Safeguards, downstream consumers, Annotations, Explanations, and historical knowledge evolution relevant to monitoring. An entity may be known while outside Monitoring Scope.

### Logical pipeline
A logical data-processing responsibility that transforms or moves data. It may span one or more jobs/tasks and does not automatically equal a repository.

### Repository
A source-control boundary and provenance context, not the product reasoning boundary.

### Job / Task / Run
A Job is an orchestration definition; Task is a unit inside it; Run/execution instance is time-bounded actual work established by execution evidence.

### Execution opportunity
A prospective downstream start context such as a schedule window, trigger opportunity, or other identifiable admission context that may be subject to an Execution Gate. It is not itself an actual Run and need not become a first-class domain entity in the eventual implementation.

## Scope, identity, and authorization

### Monitoring Scope — Accepted
The time-aware declaration of whether the product is responsible for monitoring an Entity Identity. Scope is not authorization and does not implicitly propagate through Lineage.

### Entity Identity — Accepted
Functionality for deciding when source-specific references denote the same logical entity across systems/time while preserving ambiguity, separation, validity, and correction provenance.

### Capability Authorization — Accepted post-exit addendum
Functionality for resolving whether a principal may perform a named capability on a subject/context/time, with provenance, conditions, effective interval, conflict/unknown behavior, and historical revision.

Capability classes are independently resolvable. The model distinguishes direct/raw data read, sensitive-value access, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, operational job/run actions, safeguard actions, Execution Gate control/override, and Explanation/report access without selecting an IAM implementation.

Responsibility Assignment, Classification, Policy Context, Monitoring Scope, repository ownership, job creator identity, and platform administration do not silently grant Capability Authorization.

### Authorized evidence view
The general set of concept/evidence state a principal is permitted to inspect for a specific context/purpose. It can vary by subject, evidence facet, time, and capability.

### Authorized Analytical Projection
The Phase 003 Group 05 synchronization result that assembles the **task-specific permitted subset/abstraction** of concept state for a requesting principal. It may expose approved aggregate health metrics, Assessment status, execution timing, redacted/opaque Lineage, policy/restriction summaries, responsibility context, Causal Claim status, Impact, safeguard state, Execution Gate state, and Annotation while withholding restricted rows, columns, thresholds, entity identities, or evidence details.

The projection is not a new truth-owning concept, persistence layer, or declassification mechanism. Derived evidence is not automatically unrestricted, and restricted evidence is not retrieved merely to synthesize a more complete summary.

### Direct/raw data access
Permission to inspect underlying rows/records/values or sensitive fields. Lack of direct-data access does not automatically prevent independently authorized monitoring, Investigation, RCA, Impact analysis, or Explanation.

### Analytical visibility
Permission to inspect approved metadata, aggregate health/Assessment state, Lineage/RCA evidence, Impact, safeguards, Execution Gate state, and Explanation. Analytical visibility does not imply raw-data access or production-control authority.

### Operational job authority
Permission to perform a named job/run operation where later defined. It is independent from raw-data read and analytical visibility. Authorization to act does not establish that the action succeeded.

### Gate-control authority
Capability Authorization to configure, enable, operate, or override an Execution Gate. It is independent from raw-data read, ordinary analytical visibility, responsibility assignment, and generic job-operation authority unless an explicit capability rule says otherwise.

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
Context describing how important an entity is to downstream business or operational processes. Criticality is priority/significance context, **not** evidence that exposure, downstream effect, business consequence, or causal Impact actually occurred.

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

### Dependency readiness
Evidence-backed state describing whether an explicitly relevant upstream prerequisite satisfies the readiness criterion required for a downstream context. The criterion may involve execution completion, current-cycle output availability, freshness, expected version, or another accepted condition. Dependency readiness is not automatically an Execution Gate decision.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that observed freshness violates an applicable freshness Expectation.

### Degradation
A meaningful worsening supported by explicit directional/normative interpretation. Baseline deviation or realized Change alone is insufficient.

## History, lineage, change, and execution control

### Change Intent — Accepted
Functionality for registering an intended modification and anticipated effects before realization. Anticipated effects are not automatically Expectations, Observations, Changes, actual Impact, or causes.

### Prospective Impact Profile
A pre-realization downstream candidate/blast-radius view built from Change Intent, active Lineage, planned-only topology, and authorized criticality/semantic/governance context. It does not establish actual exposure, downstream effect, business consequence, causal proof, or a numeric probability/severity score.

### Execution History — Accepted
Functionality for reconstructing actual execution instances/lifecycle states and provenance over time. Missing telemetry does not create a fictional execution or absence.

### Execution Gate — Accepted post-exit addendum
Functionality for explicit downstream execution admission control based on declared prerequisite readiness. An enabled gate may evaluate readiness, hold an execution opportunity, admit it when criteria are satisfied, record an authorized override, or preserve unknown/conflicting/unavailable gate state.

Execution Gate is **optional active control**. Passive monitoring and readiness Assessment do not automatically create a gate. `held` is not a failed execution, `admitted` is not proof that a run actually occurred, and `override` does not mean the prerequisite became ready.

### Passive monitoring
The default observational mode in which monitoring collects/interprets evidence without placing the framework in the production execution critical path. Monitoring degradation must not itself delay ungated jobs merely because they are monitored.

### Active execution gating
An explicitly enabled control mode in which a downstream execution opportunity can be intentionally held until prerequisite readiness is evidenced or an explicit fallback/override applies. Active gating may intentionally create latency and therefore requires traceable authority, readiness criteria, fallback/timeout behavior, and control evidence.

### Gate hold
An Execution Gate state in which a downstream execution opportunity is not admitted because the applicable gate rule requires waiting. A hold is not an execution failure because the downstream execution may not have started.

### Gate admission
An Execution Gate state indicating the gate permits the downstream execution to proceed. Admission does not establish that the run actually started or that every upstream health dimension is healthy.

### Gate override
An authorized bypass of the normal gate readiness outcome. The underlying prerequisite remains not-ready/unknown/conflicting as applicable; override records permission to proceed despite that state.

### Gate fallback behavior
Explicit configured behavior for unavailable/unknown readiness or control evidence, such as hold, allow, expire, or escalate where later accepted. The project has **no universal fail-open or fail-closed rule**.

### Production-repository independence
The architectural objective that baseline monitoring be independently deployed/versioned and prefer no required ETL-code/library/GitHub Actions changes when the necessary evidence is available through Databricks/platform/source metadata. It is an objective rather than an absolute guarantee for every future specialized integration.

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

## Historical replay and evolving knowledge

### Historical state cut
The Group 06 replay result that resolves relevant accepted concept histories for an event/effective-time question under a specified recorded/knowledge-time cutoff. It is a synchronization view, **not a 24th concept** or persistence requirement.

### Contemporaneous view
A historical state cut using a knowledge cutoff representative of what the ecosystem knew at the historical event/decision time.

### Retrospective view
The same historical event/window evaluated using a later knowledge cutoff that may include late/corrected evidence.

### Replay-derived interpretation
A current computation over a historical state cut. It does not prove the same Assessment, claim, Impact conclusion, decision, or Explanation was actually recorded/believed then.

### Actual historical state
Concept state/action/assertion established as actually recorded/effective by the historical cutoff, such as an Assessment, gate hold, safeguard activation, claim status, Annotation, or retained Explanation.

### Historical correction / retrospective re-evaluation
Late/corrected evidence is recorded at its real knowledge time and may cause new derived state about an earlier event. Prior contemporaneous state remains reconstructable rather than silently overwritten.

### Counterfactual control rewrite
Replacing an actual historical gate/safeguard action with what later evidence suggests should have happened. **Not historical replay and prohibited as a substitute for actual history.** Counterfactual analysis, if later supported, is a separate behavior.

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
A Causal Claim satisfying an explicit accepted evidence/authority standard. The exact standard remains deferred to Phase 004.

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

Execution Gate and Propagation Safeguard protect different control boundaries: Execution Gate controls **whether a downstream execution starts**; Propagation Safeguard controls **whether output/current state propagates or is consumed**.

### Analyst intervention
Human research through Investigation or an authorized operational/safeguard/gate decision. It is not a separate concept.

### Annotation — Accepted
Attributed human-authored context attached to ecosystem state without mutating source evidence or silently substituting for structured truth or authorization. Human consequence context can inform Impact while retaining its human-source provenance and dispute/withdrawal state.

### Explanation — Accepted
Authorization- and time-aware communication composed from concept state/evidence. Explanation consumes the Authorized Analytical Projection rather than hidden evidence directly. Different audiences may receive different safe detail/abstraction, but epistemic status, Impact layering, human-source status, control state, and material statement-to-basis traceability remain intact.

### Actual retained historical Explanation
An Explanation/report that evidence establishes was actually generated/retained at the historical knowledge time. Current disclosure authorization still applies.

### Reconstructed historical Explanation
A present-day Explanation generated from a historical state cut. It must be labeled `reconstructed` when no historical snapshot proves the same answer/report actually existed then.

### Statement-to-basis traceability
The requirement that each material Explanation statement be internally traceable to the authorized concept state/evidence, epistemic status, temporal perspective, and authorization/redaction context supporting it. Visible citation UI is deferred, but internal traceability is required.

## Evidence and provenance

### Evidence
A provenance-bearing fact/assertion used to support Assessment, Execution Gate decisions, Investigation, Causal Claim, Impact, safeguard decisions, or Explanation.

### Observed absence
A negative fact supported by sufficient source/query coverage. Missing telemetry is not observed absence.

### Provenance
Information describing where a fact/assertion/definition/classification/intent/deployment/relationship/Expectation/Baseline/Observation/Assessment/Change/gate/claim/Annotation/Impact/safeguard/authorization/Explanation came from and its temporal/version context.

### Authority / source precedence
Rules determining which source/actor is authoritative for a category/capability/subject/context/time. The project has no universal authority rule; unresolved conflicts remain conflicts until accepted category-specific semantics exist.

## Historical replay questions

Group 06 treats these as independently answerable where evidence permits:

1. **What happened?** — actual event/effective-time facts/actions.
2. **What was known then?** — evidence/state available under the historical knowledge cutoff.
3. **What was believed/interpreted then?** — actually recorded Assessment/claim/Impact/Annotation/etc., not merely what could now be computed.
4. **What was authorized then?** — historical Capability Authorization.
5. **What control state/action applied then?** — actual gate/safeguard state/action.
6. **What was actually explained then?** — retained Explanation if it exists.
7. **What do we know now?** — later/current retrospective state.

## Key non-equivalences

- Monitoring Scope ≠ Capability Authorization;
- Responsibility Assignment ≠ Capability Authorization;
- Policy Context ≠ Capability Authorization;
- raw-data access ≠ analytical visibility ≠ job-operation authority ≠ safeguard authority ≠ gate-control authority;
- authorized derived evidence ≠ unrestricted evidence;
- Authorized Analytical Projection ≠ new truth/declassification mechanism;
- passive monitoring ≠ active execution gating;
- monitoring availability ≠ ungated production-job availability;
- dependency readiness Assessment ≠ Execution Gate admission state;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- gate hold ≠ execution failure;
- gate admission ≠ actual run occurrence;
- gate override ≠ prerequisite ready;
- successful upstream run ≠ current qualifying output unless the gate criterion defines it so;
- missing readiness evidence ≠ ready;
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
- **effective/event time ≠ recorded/knowledge time**;
- **current state ≠ historical state cut**;
- **later evidence ≠ evidence known then**;
- **actual historical state ≠ replay-derived interpretation**;
- **actual gate/safeguard action ≠ counterfactual preferred action**;
- **actual retained historical Explanation ≠ reconstructed historical Explanation**;
- **historical authorization/control state ≠ current disclosure permission**;
- missing telemetry ≠ missing run/output.

## Concept Design

### Concept
An independently understandable unit of functionality with a clear purpose, operational principle, state, and actions, composed via synchronizations.

### Synchronization
Defined coordination between independent concepts without collapsing their purposes/state into one concept or selecting technical architecture.
