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

### D-016 — Expectation is normative and Baseline is descriptive

**Status:** Accepted — Phase 002 Group 03

Expectation states what should be true or acceptable for a subject/context/time. Baseline describes reference behavior derived from comparable evidence. Historical regularity is not silently promoted into a requirement, and repeated abnormal behavior does not become acceptable merely because it is common.

A Baseline-only comparison may establish typicality/atypicality but does not by itself establish normative health, degradation, defect, or acceptability.

### D-017 — Observation is evidence and missing evidence is not observed absence

**Status:** Accepted — Phase 002 Group 03

Observation records a provenance-bearing measured/retrieved fact without interpreting health or cause. Missing telemetry must never be represented as zero, false, empty, or no event.

A negative/absence Observation is valid only when the evidence collection/query has sufficient coverage to positively establish absence over a defined interval. This prevents monitoring outages from being mislabeled as pipeline failures.

### D-018 — Assessment must preserve its normative/comparative basis

**Status:** Accepted — Phase 002 Group 03

Assessment interprets Observation evidence against explicit Expectation and/or comparable Baseline context. Every Assessment retains which reference basis and versions were used.

`Within Baseline` does not imply `healthy`, and `outside Baseline` does not imply `degraded`. A normative health/requirement result needs a normative basis. Conflicting or insufficient evidence/reference context remains unresolved rather than being forced into green/red status.

### D-019 — Health evaluation is dimension-scoped and reassessment is historical

**Status:** Accepted — Phase 002 Group 03

Execution, freshness, completeness, validity, volume, schema, distribution, and other dimensions are assessed independently by default. Success in one dimension does not mask failure or uncertainty in another.

Any composite/overall health result must identify component Assessments and an explicit aggregation rule. Late/corrected evidence produces a new linked Assessment rather than silently rewriting the conclusion previously reached from earlier evidence.

### D-020 — Planned modification requires Change Intent separate from realized Change

**Status:** Accepted — Phase 002 Group 04

A pipeline/data modification can be registered before activation through **Change Intent**, including anticipated effects and monitoring implications. Intent is planned context, not an Observation, Deployment, realized Change, Expectation, or causal conclusion.

A registered change may activate and behave as intended, activate with unintended side effects, differ materially from anticipated magnitude, never activate, or be absent even when a deployment/change occurs.

### D-021 — Planned structural change may create a prospective Baseline boundary but cannot set the Baseline

**Status:** Accepted — Phase 002 Group 04 refinement of Group 03 synchronization

Change Intent may register that an existing Baseline is expected to become non-comparable if a structural modification becomes active. Intent alone does not end current Baseline applicability. Deployment/realized Change evidence establishes the transition.

A new post-change Baseline must be empirically derived from sufficient comparable post-change Observations. Planned values are never inserted as Baseline values. Immediate post-change normative validation should use an explicitly established/revised Expectation when appropriate.

### D-022 — Deployment, execution, Lineage, and Change preserve distinct historical truth

**Status:** Accepted — Phase 002 Group 04

Deployment distinguishes attempt from activation and cannot prove intended data effect. Execution History reconstructs actual runs and cannot fabricate missing runs from missing telemetry. Lineage records typed temporal relationships and cannot convert planned topology into active topology without evidence. Change records realized differences/transitions and does not judge health, intent conformance, or cause.

### D-023 — Adopt ledger-like historical semantics without selecting ledger technology

**Status:** Accepted — cross-cutting product principle

Material historical state should be provenance-bearing and reconstructable. Corrections/supersessions append or link new state rather than invisibly rewriting prior knowledge. Where material, effective/event time and recorded/knowledge time remain distinct.

This decision does **not** select blockchain, event sourcing, append-only database, temporal-table technology, or any persistence architecture. Technical realization belongs to later architecture design.

### D-024 — Require graph-compatible relationship semantics without selecting a graph database

**Status:** Accepted — cross-cutting product principle

Entity Identity plus typed, directed, temporal, provenance-bearing Lineage forms a naturally graph-shaped reasoning model. Product semantics must support upstream/downstream traversal, historical subgraphs, uncertainty, scope boundaries, and authorized opaque/redacted nodes.

This does **not** select Neo4j, RDF, property graphs, GraphFrames, a graph query language, or any other technical graph architecture. Those are later evaluation candidates.
