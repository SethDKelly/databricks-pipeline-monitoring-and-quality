# Shared Glossary

This glossary is the canonical vocabulary reference. Terms may evolve during later design, but changes must be reflected consistently across foundation, concept, synchronization, and decision documents.

## Core ecosystem

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage relationships, governance metadata, health/quality evidence, Investigations, causal reasoning, Impact context, Propagation Safeguards, downstream consumers, and Explanations relevant to monitoring. An entity may be known while outside Monitoring Scope.

### Logical pipeline
A logical data-processing responsibility that transforms or moves data. It may span one or more jobs/tasks and does not automatically equal a repository.

### Repository
A source-control boundary and provenance context, not the product reasoning boundary.

### Job / Task / Run
A Job is a Databricks orchestration definition; Task is a unit inside it; Run/execution instance is time-bounded actual work established by execution evidence.

### Code revision
A source-controlled version of code/configuration relevant to Deployment provenance.

## Scope and identity

### Monitoring Scope — Accepted
The time-aware declaration of whether the product is responsible for monitoring an Entity Identity. Scope is not authorization and does not implicitly propagate through Lineage.

### Entity Identity — Accepted
Functionality for deciding when source-specific references denote the same logical entity across systems/time while preserving ambiguity, separation, validity, and correction provenance.

## Semantics, responsibility, governance, policy

### Semantic Definition — Accepted
Provenance-bearing semantic assertions describing what an entity means in a relevant business/technical context/time.

### Responsibility Assignment — Accepted
Who bears a named responsibility for an identified subject/time. Responsibility does not imply universal authority or authorization.

### Classification — Accepted
Category membership under named governance/sensitivity vocabularies, preserving source meaning/provenance/time/conflict.

### Policy Context — Accepted
Declared policy applicability/handling context for subject/context/time without claiming enforcement, legal interpretation, or compliance.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational categories/context according to applicable definitions. Presence of such metadata does not itself establish compliance.

## Health evaluation

### Expectation — Accepted
A provenance-bearing normative assertion describing what should be true/acceptable for subject/dimension/context/time.

A Change Intent may prompt explicit establishment/revision of a post-change Expectation, but anticipated effects do not become normative automatically.

### Quality expectation
An Expectation specifically describing acceptable data-quality behavior.

### Baseline — Accepted
Descriptive reference behavior derived from comparable Observation evidence. It preserves evidence population/window, comparison context, derivation meaning, version, and limitations.

A Change Intent can register a prospective comparability break; realization evidence is required before the break becomes effective. A new Baseline must be derived from post-change Observations rather than intended values. Ordinary variation appropriate to the comparison context should remain within the Baseline model rather than becoming alert noise simply because consecutive runs differ.

### Observation — Accepted
A provenance-bearing measured/retrieved fact. Observation preserves measurement meaning/time/provenance without declaring health, anomaly, staleness, intent conformance, or cause. Missing evidence is not observed absence.

### Assessment — Accepted
A dimension-scoped interpretation of authorized Observation evidence against explicit Expectation and/or comparable Baseline context, preserving its basis/history.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that observed freshness violates an applicable freshness Expectation.

### Execution duration
Elapsed execution time derived from compatible execution start/completion evidence. Duration is an Observation before it is compared with a Baseline or Expectation. A successful run may still violate a duration/completion requirement.

### Operational latency / readiness
Timing relationship among upstream execution/output availability and downstream execution/delivery needs. Dependency delay can materially affect ecosystem health even when row-level/statistical quality remains acceptable.

### Degradation
A meaningful worsening supported by explicit directional/normative interpretation. Baseline deviation or realized Change alone is insufficient.

## History, lineage, and change

### Change Intent — Accepted
Functionality for registering an intended modification and anticipated effects before realization. It preserves target, planned/effective context, monitoring implications, provenance, and revision/withdrawal history.

Anticipated effects are not automatically Expectations, Observations, Changes, actual Impact, or causes.

### Prospective Impact Profile
A pre-realization downstream candidate/blast-radius view built from Change Intent, active Lineage, planned-only topology, and authorized criticality/semantic/governance context. It may inform review, testing, analyst attention, or safeguard proposal. It does not establish actual exposure, downstream effect, business consequence, causal proof, or a numeric probability/severity score unless a later accepted model supports one.

### Execution History — Accepted
Functionality for reconstructing actual execution instances/lifecycle states and provenance over time. Missing telemetry does not create a fictional missing execution.

### Deployment — Accepted
Functionality for recording deployment attempts and resolving which source/configuration state was actually active for a target/time. Attempt, workflow success, and activation remain distinct; activation does not prove data effect or health.

### Lineage — Accepted
Functionality for maintaining/traversing typed, directed, temporal, provenance-bearing relationships among Entity Identities. Current topology does not overwrite historical topology; planned topology is not active until evidence establishes it.

Lineage requires graph-compatible semantics, but no graph database, query language, or graph service has been selected.

### Data lineage
How data assets derive from or flow into other data assets.

### Operational dependency lineage
How pipelines/jobs/executions depend on other availability/execution conditions.

### Deployment provenance
How repositories/revisions/configuration/Deployments/active targets/executions relate over time. It remains distinct from data derivation Lineage.

### Change — Accepted
Functionality for identifying/describing a realized difference or state transition established by evidence, preserving before/after or source-event basis, time, magnitude, provenance, comparability, and uncertainty.

Change does not by itself mean intended, unintended, healthy, degraded, valid, invalid, or causal. Raw numerical difference need not become a durable Change record unless later significance semantics justify it.

### Evidence-ledger semantics
A cross-cutting requirement that material historical facts/assertions remain provenance-bearing, reconstructable, and corrected through append/supersede relationships rather than invisible mutation.

This is not a blockchain, event-sourcing, temporal-database, or persistence selection.

### Effective/event time
When a condition was true or an event occurred.

### Recorded/knowledge time
When the monitoring ecosystem learned or recorded it. Historical replay may need both.

## Investigation, causality, impact, protection, and communication

### Investigation — Accepted
Functionality for organizing a bounded inquiry into a question, symptom, unexpected outcome, or uncertainty by linking evidence, Causal Claims, Impact analysis, and Annotations without becoming the source of those facts/conclusions.

An Investigation can close unresolved or multi-causal. Analysts may open Investigation manually when evidence is material, suspicious, atypical, violated, or unresolved; automatic initiation requires explicit accepted response criteria rather than hidden severity rules.

### Causal Claim — Accepted
A provenance-bearing proposition that one or more conditions caused, contributed to, enabled, or materially influenced a defined outcome, with explicit epistemic status plus supporting/contradicting evidence and revision history.

Correlation, Lineage, Deployment timing, realized Change, safeguard state, and intent consistency are not confirmed causation by themselves.

### Root-cause hypothesis
A Causal Claim in a proposed/supported but not confirmed epistemic state.

### Attribution
A causal contribution statement represented through Causal Claim role/status where the available evidence supports it. Quantitative percentage allocation is not assumed.

### Confirmed cause
A Causal Claim that satisfies an explicit accepted evidence/authority standard. The exact standard remains deferred; human title alone is not universal confirmation authority.

### Impact — Accepted
Functionality for reasoning about downstream consequences while keeping separate:

- candidate/reachability through authorized Lineage;
- actual exposure/consumption of an affected state;
- observed downstream effect/condition evidence;
- evidenced technical, analytical, or business consequence.

Reachability is not exposure; exposure is not automatically degradation; business consequence is not assumed from criticality or report existence. A Prospective Impact Profile uses only candidate/risk context before realization and must not be presented as actual Impact.

### Propagation Safeguard — Accepted post-exit addendum
Functionality for representing a protective proposed/active/released hold or quarantine at a defined output/consumption boundary. A safeguard may be precautionary; active quarantine does not prove the data is defective. `proposed` is distinct from `active`, activation requires accepted authority/enforcement evidence, and release does not prove health.

If no qualifying output exists, a safeguard can hold downstream advancement/current-cycle publication rather than fabricating a quarantined data object. Safeguard state may itself cause operational delay/non-delivery that remains observable and assessable.

### Analyst intervention
Human research through Investigation or an authorized safeguard decision. It is not a separate accepted concept at this stage.

### Annotation — Accepted
Attributed human-authored context attached to ecosystem state without mutating source evidence or silently substituting for structured Change Intent, Expectation, Responsibility Assignment, Classification, Policy Context, or Causal Claim confirmation.

### Explanation — Accepted
Authorization- and time-aware communication composed from concept state/evidence. Explanation preserves material statement epistemic labels, source traceability, redaction/omission context, and the distinction between what was known at an earlier knowledge time and what a later retrospective view knows now.

Explanation is not an independent truth source.

## Evidence and provenance

### Evidence
A provenance-bearing fact or assertion used to support Assessment, Investigation, Causal Claim, Impact, safeguard decisions, or Explanation. Observation is the primary accepted concept for measured/retrieved facts; other concepts provide their own provenance-bearing assertions/state.

### Observed absence
A negative fact supported by sufficient source/query coverage. Missing telemetry is not observed absence and cannot establish a missing run/output.

### Provenance
Information describing where a fact/assertion/definition/classification/intent/deployment/relationship/Expectation/Baseline/Observation/Assessment/Change/claim/annotation/impact/safeguard state came from, who/what asserted or derived it, and relevant temporal/version context.

### Authority / source precedence
Rules determining which source/actor is authoritative for a category/subject/context/time. The project has no universal authority rule; unresolved conflicts remain conflicts until accepted category-specific semantics exist.

## Governance roles/metadata

### Technical owner / Business accountable party / Data steward
Distinct Responsibility Assignment types.

## Key non-equivalences

- successful execution ≠ timely execution ≠ freshness ≠ data quality;
- execution-duration Observation ≠ duration violation;
- raw difference ≠ material Change;
- atypicality ≠ normative violation ≠ mandatory intervention;
- prospective Impact ≠ actual exposure/effect/consequence;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ defect proof;
- release ≠ health proof;
- missing telemetry ≠ missing run/output;
- reachability ≠ exposure ≠ downstream effect ≠ business consequence;
- correlation ≠ confirmed cause.

## Concept Design

### Concept
An independently understandable unit of functionality with a clear purpose, operational principle, state, and actions, composed via synchronizations.

### Synchronization
Defined coordination between independent concepts without collapsing their purposes/state into one concept or selecting technical architecture.
