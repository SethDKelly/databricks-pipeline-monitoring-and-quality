# 006 — Security, Governance, and Policy Transparency Model

## Purpose

Define trust boundaries and non-negotiable security/privacy/governance principles before implementation. This document is a product-security model, not a detailed IAM or network design.

## Security objective

The monitoring system should increase operational and data transparency **without increasing unauthorized data exposure**.

The product has unusual risk because it aggregates metadata from many systems. Even if it avoids raw row-level data, the combined metadata may reveal sensitive facts about schemas, table names, classifications, semantics, responsibilities, incidents, business processes, policies, downstream usage, health metrics, causal conclusions, or authorization state.

## Trust boundaries

The initial ecosystem contains distinct trust/authority boundaries:

1. Git repositories;
2. GitHub Actions deployment workflows;
3. Databricks workspaces/jobs/tasks/runs;
4. Databricks catalogs/data assets/lineage/quality metadata;
5. optional governance systems such as Collibra;
6. optional policy/access systems such as Immuta;
7. the monitoring/quality framework itself;
8. human users and consuming systems.

The monitoring framework must not assume that access or authority in one boundary implies access or authority in another.

## Security principles

### SP-01 — Least privilege
Every integration and user capability should require only the authority necessary for its approved function.

### SP-02 — Monitoring does not grant raw-data access
A user who can see that a restricted table is stale should not automatically be able to see rows from that table.

### SP-03 — Metadata can be sensitive
Descriptions, business definitions, column names, lineage paths, classification labels, responsibility assignments, policy context, incident notes, quality metrics, causal claims, safeguard state, and authorization metadata may themselves reveal sensitive information and need access control.

### SP-04 — Minimize copied sensitive data
The default monitoring design should prefer metadata and aggregates over row-level values. Real PII/PHI must never be placed in repository fixtures or documentation.

### SP-05 — Preserve source authorization intent
If a source system restricts a fact, synchronizing that fact into monitoring must not intentionally bypass that restriction. The exact authorization mechanism is deferred, but the product semantics are not.

### SP-06 — Provenance is security-relevant
Users should be able to distinguish a classification asserted by a policy/governance source, a definition sourced from a catalog, an observation measured in Databricks, a human annotation, and an authorization decision supplied by an access authority.

### SP-07 — Audit material changes
Changes to expectations, semantic definitions, responsibility assignments, classification/policy overrides, incident conclusions, suppression/waiver decisions, safeguard state, authorization state, and system-of-record mappings should be attributable and historically visible.

### SP-08 — No secrets in source control
Credentials, tokens, connection strings, patient/customer values, production payloads, and environment secrets must not be committed to the repository.

### SP-09 — Safe examples
Documentation and tests created later should use synthetic assets and synthetic data unless an approved sanitized dataset is explicitly provided.

### SP-10 — Question answering is authorization-aware
A natural-language interface can create data-leakage risk by composing facts from several sources. Any future answer-generation layer must operate over an authorized evidence view and must not retrieve hidden values merely to summarize them.

### SP-11 — Separate analytical transparency from raw-data and production-control authority
The product must support independent authorization for direct/raw data access, derived health/metric visibility, governance/metadata visibility, Lineage/RCA participation, job/run operational actions, and safeguard-control actions.

A user may be denied raw rows while still being permitted to investigate approved health metrics, execution timing, redacted Lineage, policy/restriction summaries, responsibility context, and causal evidence. Conversely, permission to analyze metadata does not imply authority to modify a job or activate quarantine. Permission to operate a job does not imply permission to inspect the data it processes.

Derived or aggregate evidence is not automatically unrestricted; safe analytical projection remains authorization-aware.

## Governance model

The project distinguishes several governance/security facts rather than treating them as one field.

### Semantic definition
What an identified entity means and how it should be interpreted in a relevant business or technical context.

### Responsibility assignment
Who bears a named responsibility for an identified subject. A responsibility assignment does not grant access or operational authority.

### Criticality
How important the entity is to downstream business or operational processes. Exact representation remains deferred.

### Classification
Category membership under a named governance or sensitivity vocabulary. Classification does not itself encode policy obligations, grant access, or establish compliance.

### Policy context
A declared assertion that a policy, handling expectation, restriction, or governance obligation applies to an identified subject in a relevant context/time. Policy Context does not itself grant or deny a user capability.

### Capability authorization
A provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time. Capability Authorization is separate from Responsibility Assignment, Classification, Policy Context, Monitoring Scope, and enforcement evidence.

The model must be able to distinguish at least raw-data read, metadata/health-analysis visibility, Lineage/RCA participation, job/run operational action, and safeguard-control capability categories without selecting an IAM implementation.

### Control/evidence state
Evidence that a policy-related or authorization-related control operated, where available. This remains separate from policy applicability, authorization intent/decision, and legal compliance conclusions.

## PII, PHI, and HIPAA-related transparency

The product should make policy context visible in careful vocabulary:

- `classified as PII` means a source or authorized actor assigned a PII classification under a relevant vocabulary;
- `classified as PHI` means a source or authorized actor assigned a PHI classification;
- `HIPAA-related policy context applies` means an authoritative policy-context assertion says related handling expectations are relevant;
- `capability permitted/denied/conditional` means an applicable authorization source resolved a named principal capability for the relevant subject/context;
- `control evidence present` means a particular control/check produced evidence;
- none of the above, by itself, means `HIPAA compliant`.

The product should avoid broad legal conclusions unless an authorized compliance process explicitly supplies them.

## Authority and conflict

Different systems may disagree about semantic definitions, responsibility assignments, classifications, policy context, or capability authorization.

The product must preserve source provenance, metadata category/capability, context, conflict visibility, assertion/decision time, relevant effective time, attributable overrides/corrections, and explicit unknown/conflicting/stale/unavailable states where appropriate.

**Synchronization order is never an authority rule.** Until an accepted source-precedence/authority rule exists for a category or capability, incompatible applicable assertions remain conflicting rather than silently collapsing to the most recently synchronized value.

## Unknown is not a safe default

Governance and authorization gaps must not be converted into reassuring assumptions:

- missing semantics does not authorize inferred business meaning;
- missing responsibility does not prove intentional unassignment;
- missing classification does not mean non-sensitive;
- missing policy context does not mean unrestricted;
- missing capability authorization does not mean permitted;
- stale policy/classification/authorization metadata must not be presented as current certainty.

## Restricted-data analysis principle

A restricted-data analyst should be able to perform as much monitoring/RCA work as their explicit capabilities permit without requiring direct row access as a prerequisite.

An authorized analytical projection may include, independently and at safe abstraction levels:

- pipeline/job execution state, timing, duration, and readiness;
- table/pipeline freshness and health Assessments;
- aggregate quality/volume/distribution indicators where allowed;
- Expectation/Baseline result state while hiding restricted thresholds/raw values when required;
- Semantic Definition appropriate to the audience;
- Responsibility Assignment/contact context;
- Classification and Policy Context summaries;
- redacted/opaque Lineage and dependency context;
- Investigation and Causal Claim status/evidence limitations;
- Impact and Propagation Safeguard state.

The product must clearly identify redaction, opacity, missing evidence, and authorization-limited confidence. It must not convert an unavailable restricted fact into a reassuring negative.

## Operational authority principle

Authorization to retry, update, reconfigure, or otherwise control a job/run is independent from analytical and data-read capabilities. A later technical design must enforce these separately.

The monitoring model may show that an actor is permitted to perform a job operation while being denied raw-data read, or may allow an analyst to investigate while denying all production-control actions. Actual operational action success remains evidence in Deployment/Execution History rather than being implied by permission.

## Threat themes to carry forward

### Unauthorized inference
Combining harmless metadata may reveal a restricted fact.

### Metadata poisoning
Incorrect responsibility, classification, expected cadence, semantics, lineage, health metrics, or authorization state can cause incorrect operational decisions.

### Evidence tampering
If historical metrics, authorization, or incident evidence can be silently rewritten, root-cause reports become untrustworthy.

### Over-broad integration credentials
A monitoring connector with unnecessary privileges creates an attractive escalation path.

### Stale policy/authorization metadata
A policy or capability assertion copied once and never refreshed can provide false confidence.

### Authority confusion
Treating synchronization order, repository ownership, technical ownership, platform administration, or responsibility as universal authorization can silently grant inappropriate access/control.

### Root-cause overstatement
An automated explanation that presents a correlation as a confirmed cause can lead to unsafe action.

### Cross-domain leakage through reporting
Reports or conversational answers can reveal restricted asset names, definitions, classifications, policy context, thresholds, incident details, authorization state, or causal conclusions even when raw data is hidden.

## Security design questions deferred to technical design

- identity provider and authentication method;
- RBAC/ABAC/entitlement mechanism;
- authoritative source(s) by capability category;
- row/column-level authorization mechanics for monitoring metadata;
- safe metric/threshold/Lineage disclosure levels;
- operational action enforcement and audit;
- secret storage and rotation;
- encryption architecture;
- network topology;
- service identities;
- audit-log storage/retention;
- detailed threat model and abuse cases;
- whether raw/sampled values are ever required.
