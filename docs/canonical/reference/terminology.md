# Foundational Terminology

**Canonical key:** `foundation.terminology`

**Kind:** REFERENCE

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `foundation.terminology`

**Owns current question:** Which foundational DMTZ terms and non-equivalences must remain stable across concepts, contracts, architecture, implementation, and Explanation?

**Stable IDs:** N/A

## Current semantics

This resource defines **foundational naming discipline**. It does not replace the detailed semantics of the 24 accepted concepts or the SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract families. Those retain their inventory-selected current owners until their later CKR cutovers.

The [shared glossary](glossary.md) is the compact lookup surface for individual terms. This document emphasizes the distinctions that must survive implementation.

## Ecosystem terms

- **Data ecosystem** — the connected repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance/authorization state, health evidence, controls, Investigations, causal/Impact state, Annotations, Explanations, consumers, and historical knowledge relevant to monitoring.
- **Logical pipeline** — a named data-processing responsibility that may span jobs/tasks/repositories; it is not automatically any one of them.
- **Repository** — a source-control/provenance boundary, not the product reasoning boundary.
- **Job / Task / Run** — orchestration definition / unit within a definition / time-bounded actual execution instance established by evidence.
- **Execution opportunity** — prospective downstream admission context such as a schedule/trigger opportunity; not an actual Run.

## Evaluation terms

- **Expectation** — normative statement of what should be acceptable.
- **Baseline** — descriptive reference behavior from comparable evidence; typical does not mean healthy.
- **Observation** — provenance-bearing measured/retrieved fact; missing evidence is not observed absence.
- **Assessment** — interpretation of applicable authorized Observation evidence against an Expectation and/or comparable Baseline.
- **Freshness** — observed currency/timeliness.
- **Staleness** — normative Assessment that applicable freshness Expectation is violated.
- **Degradation** — meaningful worsening supported by directional/normative interpretation; Change or atypicality alone is insufficient.
- **Dependency readiness** — evidence-backed satisfaction of an explicit prerequisite criterion for a particular downstream context; not automatically gate admission.

## Change, history, topology, and control terms

- **Change Intent** — registered intended modification and anticipated effects before realization.
- **Deployment** — attempt/activation/active-state/supersession history for source/configuration state applied to a runtime target.
- **Execution History** — evidence-backed actual execution lifecycle history; missing telemetry cannot create fictional missing runs.
- **Lineage** — typed, directed, temporal, provenance-bearing relationship state. Planned topology is not active Lineage until evidence establishes it.
- **Change** — realized difference/state transition established by evidence without automatically implying intent, health, materiality, or cause.
- **Execution Gate** — optional start-admission control for a downstream execution opportunity based on explicit readiness criteria and authority.
- **Propagation Safeguard** — optional output/consumption protection at a defined propagation boundary.
- **Passive monitoring** — observational mode where monitoring is out-of-band and is not a hidden production start dependency.
- **Active execution gating** — explicit opt-in control mode where a downstream opportunity may be held, admitted, or overridden under accepted policy.

## Time and replay terms

- **Effective/event time** — when a condition was true or event occurred.
- **Source availability time** — when source evidence became queryable from that source.
- **Framework collection/retrieval time** — when DMTZ received/retrieved the evidence.
- **Framework recorded/knowledge time** — when evidence entered the DMTZ knowledge state usable for reasoning/replay.
- **Derived evaluation time** — when a derived Assessment/claim/Impact/control/Explanation result was produced.
- **Historical state cut** — accepted synchronization view for an event/effective-time question under a specified knowledge cutoff; not a new concept.
- **Contemporaneous view** — historical state cut approximating what was known at the historical time.
- **Retrospective view** — same historical event/window evaluated using a later knowledge cutoff.
- **Replay-derived interpretation** — current computation over a historical cut; not proof the same result was recorded/believed then.
- **Actual historical state** — state/action/assertion evidence establishes was actually recorded/effective by the cutoff.
- **Reconstructed historical Explanation** — present Explanation generated from a historical cut and explicitly labeled reconstructed when no retained historical communication proves it existed then.

## Authorization and authority terms

- **Capability Authorization** — provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time.
- **Assertion Authority** — authority determining whether a source/actor may establish a proposition/category as authoritative for the applicable subject/context/time.
- **Authorized Analytical Projection** — task-specific permitted subset/abstraction of concept/evidence state used for analysis/Explanation; not a new truth source or declassification mechanism.
- **Direct/raw data access** — permission to inspect underlying values; not a prerequisite for every independently authorized analytical capability.
- **Analytical visibility** — permission to inspect approved metadata/health/Lineage/RCA/Impact/control/Explanation evidence; not raw-data or production-control authority.
- **Operational job authority** — permission to perform a named job/run operation; does not prove execution success.
- **Gate-control authority** — permission to configure/operate/override an Execution Gate; independent from ordinary analytical visibility or raw-data access.
- **Causal-confirmation authority** — authority/capability required, alongside the applicable confirmation evidence standard, to record a Causal Claim as confirmed.

## Investigation, causality, and Impact terms

- **Investigation** — bounded inquiry linking evidence, claims, Impact, and human context without owning those truths.
- **Causal Claim** — explicit provenance-bearing causal proposition with epistemic state, support/contradiction, and revision history.
- **First-observed localization** — earliest monitored point where a related deviation is observed within available evidence/coverage; not root cause.
- **Impact candidate / reachability** — downstream subject structurally connected by relevant historical Lineage; not exposure.
- **Exposure / consumption** — evidence a consumer encountered the relevant affected state/version/window.
- **Observed downstream effect** — downstream Observation/Assessment/Change state; not necessarily upstream-caused.
- **Consequence evidence** — evidence of technical, analytical, or business outcome.
- **Prevented exposure** — evidence an enforced Propagation Safeguard materially prevented the relevant affected-state encounter with sufficient negative/path coverage.
- **Impact** — downstream reasoning that preserves candidate, exposure, effect, consequence, and causal attribution as separate strengths.
- **Annotation** — attributed human context that cannot silently become structured source truth, authorization, or causal confirmation.
- **Explanation** — authorization- and time-aware evidence-grounded communication; not an independent truth/authorization source.

## Governance terms

- **Semantic Definition** — provenance-bearing meaning assertion.
- **Responsibility Assignment** — assertion that a person/team/role bears a named responsibility; not universal authority.
- **Classification** — category membership under a named vocabulary; not Policy Context or authorization.
- **Policy Context** — policy/handling applicability assertion; not enforcement, authorization, legal interpretation, or compliance determination.
- **Criticality** — importance/priority context; not evidence of actual exposure, effect, consequence, or Impact.
- **Provenance** — source, actor/process, temporal/version, derivation, and correction context sufficient to interpret a material fact/assertion/result.

## Non-equivalences that must not collapse

- ecosystem existence ≠ Monitoring Scope ≠ Capability Authorization;
- Entity Identity ≠ source-local identifier/name;
- repository ≠ logical pipeline ≠ Databricks job;
- Responsibility Assignment ≠ Capability Authorization ≠ Assertion Authority;
- source availability ≠ Assertion Authority;
- authentication ≠ Capability Authorization;
- Expectation ≠ Baseline;
- Observation ≠ Assessment;
- successful execution ≠ timely execution ≠ freshness ≠ structural compatibility ≠ data quality;
- missing evidence ≠ observed absence/negative truth;
- evidence applicability ≠ coverage ≠ conclusion-specific sufficiency;
- Change Intent ≠ Deployment ≠ realized Change;
- planned topology ≠ active Lineage;
- Lineage ≠ encounter/exposure ≠ Impact ≠ cause;
- first-observed localization ≠ root cause;
- Investigation/leading hypothesis ≠ confirmed cause;
- proposed/supported/weakened/unresolved/rejected Causal Claim ≠ confirmed cause;
- causal evidence sufficiency ≠ causal-confirmation authority;
- reachability ≠ exposure ≠ downstream effect ≠ consequence ≠ causal attribution;
- criticality/policy sensitivity ≠ actual Impact/consequence;
- passive monitoring ≠ active Execution Gate;
- readiness result ≠ gate decision ≠ enforcement ≠ actual execution;
- gate hold ≠ execution failure;
- gate override ≠ prerequisite ready;
- Execution Gate ≠ Propagation Safeguard;
- safeguard configuration/request ≠ enforcement ≠ prevented exposure ≠ release/recovery;
- current state ≠ historical/as-known state;
- later evidence ≠ evidence known then;
- actual historical state/action/Explanation ≠ replay-derived reconstruction;
- historical authorization/control state ≠ current disclosure permission;
- model/search output ≠ truth, authority, evidence sufficiency, causal confirmation, Impact, or control decision.

## Synchronizations / related canonical resources

- [Shared glossary](glossary.md)
- [Concept Design method](concept-design-method.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Security and governance policy](../policies/security-governance.md)

## Provenance

- Original owner: [`../../foundation/003_terminology.md`](../../foundation/003_terminology.md)
- Prior glossary owner: [`../../reference/glossary.md`](../../reference/glossary.md)
- Material temporal/evidence refinements: [`../../concepts/phase_004/README.md`](../../concepts/phase_004/README.md)
- Material authority/governance refinements: [`../../concepts/phase_005/README.md`](../../concepts/phase_005/README.md)
- Material operational/control refinements: [`../../concepts/phase_007/README.md`](../../concepts/phase_007/README.md)
- Explanation/integration/architecture refinements: [`../../concepts/phase_008/README.md`](../../concepts/phase_008/README.md), [`../../concepts/phase_009/README.md`](../../concepts/phase_009/README.md), [`../../concepts/phase_010/README.md`](../../concepts/phase_010/README.md)
