# 003 — Foundational Terminology

This document establishes distinctions that must remain stable. The fuller canonical glossary is [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance metadata, health evidence, Investigations, Impact context, Propagation Safeguards, and downstream consumers relevant to monitoring.

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
Observed timing properties of executions or dependencies. Duration, queue/wait time, completion latency, and dependency readiness can materially affect ecosystem health even when table-level statistical quality is acceptable. A timing Observation becomes normatively unacceptable only through an applicable Expectation; Baseline comparison may establish typicality/atypicality.

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

## Investigation and reasoning terms

### Investigation
A bounded inquiry that links evidence, claims, Impact analysis, and human context without owning those truths. Analyst-driven research is first-class, including cases where automated evidence is insufficient to determine cause or where significance warrants prompt review despite no normative criterion.

### Evidence candidate
An entity/path/context discovered as structurally relevant to an Investigation, commonly through historical Lineage. Candidate status means **where evidence should be inspected**, not causal support.

### First-observed localization
The earliest monitored point on a relevant historical path where a related deviation is evidenced. It localizes the problem within observed coverage but is **not root cause**, especially when upstream monitoring is incomplete, restricted, unavailable, or out of scope.

### Causal Claim
An explicit proposition that one or more conditions caused/contributed/enabled/prevented an outcome, carrying epistemic status plus supporting/contradicting evidence.

### Causal support / contradiction
Relevant evidence dimensions include temporal ordering, relationship applicability, actual encounter/consumption where required, realized state/change, mechanism compatibility, contrast/intervention evidence, alternatives, and evidence coverage. Support and contradiction remain separately traceable.

### Root-cause hypothesis
A Causal Claim that is proposed/supported but not confirmed.

### Confirmed cause
A Causal Claim satisfying an explicit evidence/authority standard. The exact standard remains open for Phase 004; automated ranking, human title, Lineage reachability, and lack of known alternatives do not create confirmation authority.

### Attribution
A contribution statement represented through Causal Claim semantics when justified; quantitative allocation is not assumed.

### Analyst research
Human investigation results route to the concept owning their meaning: reproducible facts → Observation; realized difference → Change; causal proposition → Causal Claim; contextual commentary → Annotation; structured plan/norm/governance assertion → its respective concept.

### Impact
Downstream consequence reasoning that distinguishes candidate/reachability, actual exposure, observed downstream effect, and evidenced business consequence.

### Propagation Safeguard
A protective proposed/active/released state that holds or quarantines a defined output/consumption boundary to reduce downstream exposure. It is not a quality Assessment, Causal Claim, access-control grant, or proof that the data is defective or safe. Safeguard state can itself become a proposed causal condition for operational delay when enforcement/timing evidence supports that separate claim.

### Annotation
Attributed human context that cannot silently become Observation, Change Intent, Expectation, Responsibility Assignment, or causal confirmation.

### Explanation
Authorization- and time-aware evidence-grounded communication. It is not an independent truth source and can distinguish what was known then from retrospective knowledge now.

## Governance and policy terms

### Responsibility Assignment
A provenance-bearing assertion that a person/team/role bears a named responsibility for a subject/time/context. Responsibility is not universal authority or authorization.

### Semantic Definition
Provenance-bearing meaning/interpretation assertions.

### Classification
Category membership under a named governance/sensitivity vocabulary; not Policy Context or authorization.

### Policy Context
Declared policy/handling applicability without access enforcement, legal interpretation, or compliance determination.

### PII / PHI / HIPAA-related policy context
Sensitive-data/legal-organizational categories/context according to applicable definitions. Presence of such metadata does not establish compliance.

### Provenance
Where a fact/assertion/definition/intent/relationship/evaluation/claim/safeguard came from, who/what asserted or derived it, and relevant temporal/version context.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ authorization;
- pipeline ≠ repository ≠ Databricks job;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective Impact ≠ actual Impact ≠ retrospective cause;
- anticipated effect ≠ normative Expectation;
- planned value ≠ empirical Baseline;
- Deployment attempt ≠ activation;
- activation ≠ intended effect realized;
- successful run ≠ timely run ≠ freshness ≠ data quality;
- execution-duration Observation ≠ duration violation;
- Expectation ≠ Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- raw difference ≠ material Change;
- typical ≠ healthy;
- atypical ≠ degraded/defective ≠ mandatory intervention;
- planned topology ≠ active Lineage;
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- temporal proximity ≠ causal proof;
- absence of contradiction ≠ confirmation;
- Investigation closure ≠ Causal Claim confirmation;
- Causal Claim ≠ confirmed cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- safeguard release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ truth source;
- effective/event time ≠ recorded/knowledge time;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.
