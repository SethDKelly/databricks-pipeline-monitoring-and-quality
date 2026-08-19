# Decision Records

This directory records durable product/design choices that should not live only in chat history.

## Current foundational decisions

### D-001 — Use Concept Design for functional design

**Status:** Accepted

The project will use Daniel Jackson's Concept Design approach for product functionality before technical architecture is selected.

See `../foundation/004_concept_design_method.md`.

### D-002 — Remain documentation-only through Concept Specification work

**Status:** Accepted

No application code, infrastructure code, data schemas, deployment workflows, notebooks, package scaffolding, or implementation architecture should be introduced during Phase 001 or Phase 002 unless explicitly requested as a change into technical design.

### D-003 — Treat the multi-repository environment as one reasoning ecosystem

**Status:** Accepted

Repository boundaries are preserved for provenance/ownership but are not product reasoning boundaries.

### D-004 — Databricks Metric Views and DQX are favored evaluations, not predetermined architecture

**Status:** Accepted

The product concepts will be defined first. Databricks-native capabilities should be preferred where they satisfy those concepts cleanly.

### D-005 — Collibra and Immuta are optional integrations

**Status:** Accepted

They may be authoritative for selected metadata categories if discovery establishes that role, but core product concepts must not assume their presence.

### D-006 — Policy classifications are not compliance claims

**Status:** Accepted

PII, PHI, HIPAA-related handling, and other labels provide context. The framework must not convert them into ungrounded legal/compliance conclusions.

### D-007 — Treat this repository as a standalone product domain

**Status:** Accepted

Do not import actors, lifecycle terminology, product concepts, or assumptions from unrelated projects. Shared design methods may be reused deliberately; domain models may not be carried over implicitly.

### D-008 — Review Phase 002 as five strategic concept groups

**Status:** Accepted

Concept specifications will be iterated in the order Scope & Identity; Semantics/Governance/Policy; Health Evaluation; History/Lineage/Change; Investigation/Impact/Explanation. The order improves review effectiveness but does not imply implementation coupling.

See `../concepts/phase_002/README.md`.

### D-009 — Monitoring Scope applies to identified entities and does not implicitly propagate

**Status:** Accepted — Phase 002 Group 01

`Monitored Scope` is refined to **Monitoring Scope**. The concept states whether the product is responsible for monitoring an identified entity at a relevant time. An entity may be known while excluded from monitoring or while scope is unknown. Lineage/dependency relationships may cross the monitoring boundary without automatically changing scope.

Monitoring Scope is not authorization, does not guarantee evidence collection, and does not automatically inherit upstream, downstream, across repositories, or across logical pipeline boundaries.

### D-010 — Identity is ecosystem-wide and distinct from replacement or succession

**Status:** Accepted — Phase 002 Group 01

`Asset Identity` is refined to **Entity Identity** because identity behavior is required for more than data assets. The concept determines when source-specific references denote the same logical entity across systems and time.

Rename continuity requires evidence. Name equality alone is insufficient. Environment-specific instances remain distinct by default. Delete/recreate, split, merge, replacement, migration, and succession do not imply identity; relationships among those distinct entities belong to Change and/or Lineage.

### D-011 — Identity and scope preserve historical interpretation

**Status:** Accepted — Phase 002 Group 01

Identity-reference validity, identity corrections, and scope assertions retain provenance and relevant effective-time context. Historical incident reasoning must be able to reconstruct what entity references and monitoring responsibility applied at the incident time rather than projecting only current state backward.

### D-012 — Semantic definitions are facet-, context-, and time-aware

**Status:** Accepted — Phase 002 Group 02

Semantic Definition is not one canonical description string. Technical description, business definition, grain, units, population/calculation meaning, and other semantic facets may coexist with provenance and effective-time context. Multiple context-specific assertions can be valid; incompatible assertions in the same relevant context remain conflicts until authority is established.

### D-013 — Responsibility Assignment replaces the overloaded Ownership concept

**Status:** Accepted — Phase 002 Group 02

`Ownership` is refined to **Responsibility Assignment**. Technical ownership, business accountability, stewardship, policy/security responsibility, and similar roles are named responsibility types attached to a subject and time.

Responsibility does not grant access and does not make the responsible party universally authoritative for semantics, classification, policy, expectations, or other metadata categories.

### D-014 — Classification and Policy Context are separate concepts

**Status:** Accepted — Phase 002 Group 02

Classification records category membership under a named governance/sensitivity vocabulary. Policy Context records declared policy applicability/handling expectations for a subject/context/time. Classification may be evidence for policy applicability, but it is not the policy itself and does not grant access or prove compliance.

### D-015 — Governance conflicts remain conflicts until authority is explicitly defined

**Status:** Accepted — Phase 002 Group 02

Semantic Definition, Responsibility Assignment, Classification, and Policy Context preserve source assertions, provenance, effective time, and conflict. Synchronization order is never treated as an authority rule. Missing governance metadata is also not converted into a safe default: missing semantics are not inferred meaning, missing responsibility is not explicit unassignment, missing classification is not non-sensitive, and missing policy context is not unrestricted.

Whether repeated source-precedence behavior becomes an independent authority concept or an integration/metadata-category contract remains deferred.
