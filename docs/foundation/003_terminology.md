# 003 — Foundational Terminology

This document establishes distinctions that must remain stable. The fuller canonical glossary is [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance metadata, authorization state, health evidence, Investigations, Impact context, Propagation Safeguards, and downstream consumers relevant to monitoring.

### Logical pipeline
A named data-processing responsibility that may span multiple Databricks tasks/jobs and must not automatically equal one repository.

### Repository
A source-control/provenance boundary, not the product reasoning boundary.

### Job / Task / Run
Job is an orchestration definition; Task is a unit within it; Run/execution instance is time-bounded actual work established by execution evidence.

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

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that freshness violates an applicable Expectation.

### Degradation
A meaningful worsening supported by directional/normative interpretation. A realized Change or Baseline deviation alone is insufficient.

## History, planned change, and topology

### Change Intent
A registered intended modification and anticipated effects before realization. Intent is not Observation, Change, Expectation, Baseline, actual Impact, or cause.

### Prospective Impact Profile
Pre-realization downstream candidate/blast-radius context produced from Change Intent, current Lineage, planned-only topology, and authorized business/governance context. It does not establish actual exposure, downstream effect, business consequence, causal proof, or quantified probability of harm.

### Deployment
Attempt/activation/active-state/supersession history for source/configuration state applied to a runtime target. Deployment success does not prove data effect.

### Execution History
Actual execution-instance lifecycle history. Missing telemetry cannot create fictional missing runs.

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
The subset/abstraction of concept state and evidence a principal may inspect for a particular analytical task. It may include derived/aggregate/redacted/opaque health, timing, governance, Lineage, Investigation, Causal Claim, Impact, and safeguard context while excluding restricted raw values or identities.

### Direct/raw data access
Permission to inspect underlying row/record/value data or sensitive columns. This is not a prerequisite for every monitoring/RCA capability.

### Analytical visibility
Permission to inspect approved metadata, aggregate health/Assessment state, Lineage/RCA evidence, and Explanation. Analytical visibility does not imply raw-data access or production-control authority.

### Operational job authority
Permission to perform a named job/run operation where later defined, such as retry/update/control. Operational authority does not imply raw-data access, and permission itself does not prove the action succeeded.

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

### Impact
Downstream consequence reasoning that distinguishes candidate/reachability, actual exposure, observed downstream effect, and evidenced business consequence.

### Propagation Safeguard
A protective proposed/active/released state that holds or quarantines a defined output/consumption boundary. It is not a quality Assessment, Causal Claim, Capability Authorization, or proof that the data is defective or safe.

### Annotation
Attributed human context that cannot silently become Observation, Change Intent, Expectation, Responsibility Assignment, authorization, or causal confirmation.

### Explanation
Authorization- and time-aware evidence-grounded communication. It is not an independent truth source and can distinguish what was known then from retrospective knowledge now.

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
Where a fact/assertion/definition/intent/relationship/evaluation/claim/safeguard/authorization came from, who/what asserted or derived it, and relevant temporal/version context.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ Capability Authorization;
- responsibility ≠ authorization;
- Policy Context ≠ Capability Authorization;
- raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority;
- authorized derived evidence ≠ unrestricted evidence;
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
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- safeguard release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ truth source;
- effective/event time ≠ recorded/knowledge time;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.
