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
