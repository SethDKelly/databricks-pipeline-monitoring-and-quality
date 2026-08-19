# 006 — Security, Governance, and Policy Transparency Model

## Purpose

Define trust boundaries and non-negotiable security/privacy/governance principles before implementation. This document is a product-security model, not a detailed IAM or network design.

## Security objective

The monitoring system should increase operational and data transparency **without increasing unauthorized data exposure**.

The product has unusual risk because it aggregates metadata from many systems. Even if it avoids raw row-level data, the combined metadata may reveal sensitive facts about schemas, table names, classifications, incidents, business processes, or downstream usage.

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

The monitoring framework must not assume that access in one boundary implies access in another.

## Security principles

### SP-01 — Least privilege

Every integration should require only the authority necessary to retrieve or perform its approved function.

### SP-02 — Monitoring does not grant raw-data access

A user who can see that a restricted table is stale should not automatically be able to see rows from that table.

### SP-03 — Metadata can be sensitive

Descriptions, column names, lineage paths, classification labels, ownership, incident notes, and quality metrics may themselves reveal sensitive information and need access control.

### SP-04 — Minimize copied sensitive data

The default monitoring design should prefer metadata and aggregates over row-level values. Real PII/PHI must never be placed in repository fixtures or documentation.

### SP-05 — Preserve source authorization intent

If a source system restricts a fact, synchronizing that fact into monitoring must not intentionally bypass that restriction.

The exact authorization mechanism is deferred, but the product semantics are not.

### SP-06 — Provenance is security-relevant

Users should be able to distinguish a classification asserted by Immuta, a definition sourced from Collibra, an observation measured in Databricks, and a human annotation made in the monitoring system.

### SP-07 — Audit material changes

Changes to expectations, classification/ownership overrides, incident conclusions, suppression/waiver decisions, and system-of-record mappings should be attributable and historically visible.

### SP-08 — No secrets in source control

Credentials, tokens, connection strings, patient/customer values, production payloads, and environment secrets must not be committed to the repository.

### SP-09 — Safe examples

Documentation and tests created later should use synthetic assets and synthetic data unless an approved sanitized dataset is explicitly provided.

### SP-10 — Question answering is authorization-aware

A natural-language interface can create data-leakage risk by composing facts from several sources. Any future answer-generation layer must operate over an authorized evidence view and must not retrieve hidden values merely to summarize them.

## Governance model

The project distinguishes several governance facts rather than treating "governance" as one field.

### Description

What the technical/data asset is and how it is intended to be understood.

### Business definition / semantics

What business meaning, calculation, population, grain, or interpretation applies.

### Ownership

Who is technically responsible and who is accountable for business fitness.

### Stewardship

Who maintains or validates governance metadata and expectations.

### Criticality

How important the asset is to downstream business or operational processes.

### Classification

Sensitivity or policy-relevant categories such as PII/PHI or organizational classifications.

### Policy expectation

A declared handling/retention/access/monitoring requirement that may apply to the asset.

### Control/evidence state

Evidence that a policy-related control or check operated, where available. This is still not equivalent to a legal compliance conclusion.

## PII, PHI, and HIPAA-related transparency

The product should make policy context visible in a careful vocabulary:

- `classified as PII` means a source or authorized actor has assigned a PII classification;
- `classified as PHI` means a source or authorized actor has assigned a PHI classification;
- `HIPAA-related policy context applies` means organizational/legal handling expectations may be relevant;
- `control evidence present` means a particular control/check produced evidence;
- none of the above, by itself, means `HIPAA compliant`.

The product should avoid broad legal conclusions unless an authorized compliance process explicitly supplies them.

## Authority and conflict

Different systems may disagree about description, ownership, or classification.

The product must therefore eventually support:

- source provenance;
- authority ranking or selection by metadata category;
- conflict visibility;
- last-observed/last-asserted time;
- explicit overrides with ownership and audit history;
- an `unknown` or `conflicting` state rather than silent last-write-wins semantics.

The authority rules themselves are a later design decision.

## Threat themes to carry forward

### Unauthorized inference

Combining harmless metadata may reveal a restricted fact.

### Metadata poisoning

Incorrect ownership, classification, expected cadence, or lineage can cause incorrect operational decisions.

### Evidence tampering

If historical metrics or incident evidence can be silently rewritten, root-cause reports become untrustworthy.

### Over-broad integration credentials

A monitoring connector with unnecessary privileges creates an attractive escalation path.

### Stale policy metadata

A classification copied once and never refreshed can provide false confidence.

### Root-cause overstatement

An automated explanation that presents a correlation as a confirmed cause can lead to unsafe engineering or business action.

### Cross-domain leakage through reporting

Business reports or conversational answers can reveal restricted asset names, column meanings, or incident details even when raw data is hidden.

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
