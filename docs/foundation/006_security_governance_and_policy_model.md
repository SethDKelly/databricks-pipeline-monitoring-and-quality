# 006 — Security, Governance, and Policy Transparency Model

## Purpose

Define trust boundaries and non-negotiable security/privacy/governance principles before implementation. This document is a product-security model, not a detailed IAM or network design.

## Security objective

The monitoring system should increase operational and data transparency **without increasing unauthorized data exposure**.

The product has unusual risk because it aggregates metadata from many systems. Even if it avoids raw row-level data, the combined metadata may reveal sensitive facts about schemas, table names, classifications, semantics, responsibilities, incidents, business processes, policies, or downstream usage.

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

Every integration should require only the authority necessary to retrieve or perform its approved function.

### SP-02 — Monitoring does not grant raw-data access

A user who can see that a restricted table is stale should not automatically be able to see rows from that table.

### SP-03 — Metadata can be sensitive

Descriptions, business definitions, column names, lineage paths, classification labels, responsibility assignments, policy context, incident notes, and quality metrics may themselves reveal sensitive information and need access control.

### SP-04 — Minimize copied sensitive data

The default monitoring design should prefer metadata and aggregates over row-level values. Real PII/PHI must never be placed in repository fixtures or documentation.

### SP-05 — Preserve source authorization intent

If a source system restricts a fact, synchronizing that fact into monitoring must not intentionally bypass that restriction.

The exact authorization mechanism is deferred, but the product semantics are not.

### SP-06 — Provenance is security-relevant

Users should be able to distinguish a classification asserted by a policy/governance source, a definition sourced from a catalog, an observation measured in Databricks, and a human annotation made in the monitoring system.

### SP-07 — Audit material changes

Changes to expectations, semantic definitions, responsibility assignments, classification/policy overrides, incident conclusions, suppression/waiver decisions, and system-of-record mappings should be attributable and historically visible.

### SP-08 — No secrets in source control

Credentials, tokens, connection strings, patient/customer values, production payloads, and environment secrets must not be committed to the repository.

### SP-09 — Safe examples

Documentation and tests created later should use synthetic assets and synthetic data unless an approved sanitized dataset is explicitly provided.

### SP-10 — Question answering is authorization-aware

A natural-language interface can create data-leakage risk by composing facts from several sources. Any future answer-generation layer must operate over an authorized evidence view and must not retrieve hidden values merely to summarize them.

## Governance model

The project distinguishes several governance facts rather than treating "governance" as one field.

### Semantic definition

What an identified entity means and how it should be interpreted in a relevant business or technical context. Business definition, technical description, grain, units, population/calculation meaning, and similar facets may coexist with independent provenance and effective time.

### Responsibility assignment

Who bears a named responsibility for an identified subject, such as technical ownership, business accountability, semantic stewardship, or privacy/security responsibility. A responsibility assignment does not grant access and does not make the assignee authoritative for every governance category.

### Criticality

How important the entity is to downstream business or operational processes. During Group 02 this remains a governance facet/question; whether criticality is represented as a Classification scheme or deserves a separate concept is deferred until Impact is reviewed.

### Classification

Category membership under a named governance or sensitivity vocabulary, such as PII, PHI, confidentiality tier, or another organizational classification. Classification is descriptive categorical metadata; it does not itself encode policy obligations, grant access, or establish compliance.

### Policy context

A declared assertion that a policy, handling expectation, restriction, or governance obligation applies to an identified subject in a relevant context/time. Policy Context may reference Classification as applicability evidence, but classification and policy applicability remain distinct.

### Control/evidence state

Evidence that a policy-related control or check operated, where available. This is separate from Policy Context and is still not equivalent to a legal compliance conclusion.

## PII, PHI, and HIPAA-related transparency

The product should make policy context visible in careful vocabulary:

- `classified as PII` means a source or authorized actor has assigned a PII classification under a relevant vocabulary;
- `classified as PHI` means a source or authorized actor has assigned a PHI classification;
- `HIPAA-related policy context applies` means an authoritative policy-context assertion says HIPAA-related obligations/handling expectations are relevant in that subject/context/time;
- `control evidence present` means a particular control/check produced evidence;
- none of the above, by itself, means `HIPAA compliant`.

The product should avoid broad legal conclusions unless an authorized compliance process explicitly supplies them.

## Authority and conflict

Different systems may disagree about semantic definitions, responsibility assignments, classifications, or policy context.

The product must preserve:

- source provenance;
- metadata category/facet and context;
- conflict visibility;
- assertion/observation time and relevant effective time;
- explicit overrides/corrections with attributable history;
- `unknown`, `conflicting`, `stale`, `unauthorized`, or `unavailable` states where appropriate.

**Synchronization order is never an authority rule.** Until an accepted source-precedence/authority rule exists for a metadata category, conflicting applicable assertions remain conflicting rather than silently collapsing to the most recently synchronized value.

Authority may later be modeled as an independent concept if its purpose/state/actions warrant that boundary, or through explicit integration/metadata-category contracts. Group 02 does not decide that implementation/concept boundary prematurely.

## Unknown is not a safe default

Governance gaps must not be converted into reassuring assumptions:

- missing semantics does not authorize inferred business meaning;
- missing responsibility does not prove a subject is intentionally unassigned;
- missing classification does not mean non-sensitive;
- missing policy context does not mean unrestricted;
- stale policy/classification metadata must not be presented as current certainty.

## Threat themes to carry forward

### Unauthorized inference

Combining harmless metadata may reveal a restricted fact.

### Metadata poisoning

Incorrect responsibility, classification, expected cadence, semantics, or lineage can cause incorrect operational decisions.

### Evidence tampering

If historical metrics or governance/incident evidence can be silently rewritten, root-cause reports become untrustworthy.

### Over-broad integration credentials

A monitoring connector with unnecessary privileges creates an attractive escalation path.

### Stale policy metadata

A classification or policy-context assertion copied once and never refreshed can provide false confidence.

### Authority confusion

Treating source synchronization order, repository ownership, platform administration, or technical ownership as universal governance authority can silently select incorrect definitions, classifications, or policy context.

### Root-cause overstatement

An automated explanation that presents a correlation as a confirmed cause can lead to unsafe engineering or business action.

### Cross-domain leakage through reporting

Business reports or conversational answers can reveal restricted asset names, semantic definitions, classification labels, policy context, or incident details even when raw data is hidden.

## Security design questions deferred to technical design

- identity provider and authentication method;
- role/attribute model;
- row/column-level authorization mechanics for monitoring metadata;
- secret storage and rotation;
- encryption architecture;
- network topology;
- service identities;
- audit-log storage/retention;
- detailed threat model and abuse cases;
- whether raw/sampled values are ever required.
