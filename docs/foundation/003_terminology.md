# 003 — Foundational Terminology

This document establishes distinctions that must remain stable. The fuller canonical glossary is [`../reference/glossary.md`](../reference/glossary.md).

## Ecosystem terms

### Data ecosystem
The connected set of repositories, Change Intents, Deployments, executions, data assets, dependencies, Lineage, governance metadata, health evidence, Investigations, Impact context, and downstream consumers relevant to monitoring.

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
Descriptive reference behavior empirically derived from comparable evidence. Typical does not automatically mean healthy.

### Observation
A provenance-bearing measured/retrieved fact. It does not declare health or cause. Missing evidence is not observed absence.

### Assessment
A dimension-scoped interpretation of Observation evidence against explicit Expectation and/or comparable Baseline context.

### Freshness / Staleness
Freshness is observed currency/timeliness. Staleness is a normative Assessment that freshness violates an applicable Expectation.

### Degradation
A meaningful worsening supported by directional/normative interpretation. A realized Change or Baseline deviation alone is insufficient.

## History, planned change, and topology

### Change Intent
A registered intended modification and anticipated effects before realization. Intent is not Observation, Change, Expectation, Baseline, or cause.

### Deployment
Attempt/activation/active-state/supersession history for source/configuration state applied to a runtime target. Deployment success does not prove data effect.

### Execution History
Actual execution-instance lifecycle history. Missing telemetry cannot create fictional missing runs.

### Lineage
Typed, directed, temporal, provenance-bearing relationships. Planned topology is not active Lineage until evidence establishes it.

### Change
A realized difference/state transition established by evidence, without health/intent/causal judgment.

### Effective/event time
When something occurred or was true.

### Recorded/knowledge time
When monitoring learned/recorded it.

## Investigation and reasoning terms

### Investigation
A bounded inquiry that links evidence, claims, Impact analysis, and human context without owning those truths.

### Causal Claim
An explicit proposition that one or more conditions caused/contributed to an outcome, carrying epistemic status plus supporting/contradicting evidence.

### Root-cause hypothesis
A Causal Claim that is proposed/supported but not confirmed.

### Confirmed cause
A Causal Claim satisfying an explicit evidence/authority standard. The exact standard remains open.

### Attribution
A contribution statement represented through Causal Claim semantics when justified; quantitative allocation is not assumed.

### Impact
Downstream consequence reasoning that distinguishes candidate/reachability, actual exposure, observed downstream effect, and evidenced business consequence.

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
Where a fact/assertion/definition/intent/relationship/evaluation/claim came from, who/what asserted or derived it, and relevant temporal/version context.

## Terms to avoid conflating

- ecosystem existence ≠ Monitoring Scope ≠ authorization;
- pipeline ≠ repository ≠ Databricks job;
- Change Intent ≠ Deployment ≠ realized Change;
- anticipated effect ≠ normative Expectation;
- planned value ≠ empirical Baseline;
- Deployment attempt ≠ activation;
- activation ≠ intended effect realized;
- successful run ≠ freshness ≠ data quality;
- Expectation ≠ Baseline;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- planned topology ≠ active Lineage;
- Lineage reachability ≠ cause ≠ confirmed Impact;
- Change ≠ degradation ≠ cause;
- Investigation ≠ causal truth;
- Causal Claim ≠ confirmed cause;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- Annotation ≠ structured operational truth;
- Explanation ≠ truth source;
- effective/event time ≠ recorded/knowledge time;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority;
- Classification ≠ Policy Context ≠ authorization ≠ compliance.
