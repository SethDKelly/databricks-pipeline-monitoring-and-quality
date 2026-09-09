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

Semantic Definition, Responsibility Assignment, Classification, and Policy Context preserve source assertions, provenance, effective time, and conflict. Synchronization order is never treated as an authority rule. Missing governance metadata is also not converted into a safe default.

Whether repeated source-precedence behavior becomes an independent authority concept or an integration/metadata-category contract remains deferred.

### D-016 — Expectation is normative and Baseline is descriptive

**Status:** Accepted — Phase 002 Group 03

Expectation states what should be true or acceptable for a subject/context/time. Baseline describes reference behavior derived from comparable evidence. Historical regularity is not silently promoted into a requirement.

### D-017 — Observation is evidence and missing evidence is not observed absence

**Status:** Accepted — Phase 002 Group 03

Observation records a provenance-bearing measured/retrieved fact without interpreting health or cause. Missing telemetry must never be represented as zero, false, empty, or no event.

### D-018 — Assessment must preserve its normative/comparative basis

**Status:** Accepted — Phase 002 Group 03

Assessment interprets Observation evidence against explicit Expectation and/or comparable Baseline context. `Within Baseline` does not imply `healthy`, and `outside Baseline` does not imply `degraded`.

### D-019 — Health evaluation is dimension-scoped and reassessment is historical

**Status:** Accepted — Phase 002 Group 03

Execution, freshness, completeness, validity, volume, schema, distribution, and other dimensions are assessed independently by default. Any composite result requires an explicit aggregation rule; late/corrected evidence creates traceable reassessment.

### D-020 — Planned modification requires Change Intent separate from realized Change

**Status:** Accepted — Phase 002 Group 04

A pipeline/data modification can be registered before activation through **Change Intent**. Intent is planned context, not an Observation, Deployment, realized Change, Expectation, or causal conclusion.

### D-021 — Planned structural change may create a prospective Baseline boundary but cannot set the Baseline

**Status:** Accepted — Phase 002 Group 04 refinement of Group 03 synchronization

Change Intent may register that an existing Baseline is expected to become non-comparable if a structural modification becomes active. A new post-change Baseline must be empirically derived from sufficient comparable post-change Observations.

### D-022 — Deployment, execution, Lineage, and Change preserve distinct historical truth

**Status:** Accepted — Phase 002 Group 04

Deployment distinguishes attempt from activation and cannot prove intended data effect. Execution History reconstructs actual runs. Lineage records typed temporal relationships. Change records realized differences/transitions and does not judge health, intent conformance, or cause.

### D-023 — Adopt ledger-like historical semantics without selecting ledger technology

**Status:** Accepted — cross-cutting product principle

Material historical state should be provenance-bearing and reconstructable. Corrections/supersessions append or link new state rather than invisibly rewriting prior knowledge. Where material, effective/event time and recorded/knowledge time remain distinct.

### D-024 — Require graph-compatible relationship semantics without selecting a graph database

**Status:** Accepted — cross-cutting product principle

Entity Identity plus typed, directed, temporal, provenance-bearing Lineage forms a naturally graph-shaped reasoning model. This does not select a graph technology.

### D-025 — Investigation organizes inquiry but does not own evidence or causal truth

**Status:** Accepted — Phase 002 Group 05

Investigation is a bounded inquiry that links relevant source evidence, Causal Claims, Impact analysis, and Annotations. It may close unresolved or multi-causal.

### D-026 — Causal Claim is the explicit epistemic home for causality

**Status:** Accepted — Phase 002 Group 05

Causal statements are explicit provenance-bearing claims with supporting and contradicting evidence, contribution role where useful, uncertainty rationale, review/confirmation provenance, and status history. Correlation/Lineage/Deployment timing/intent consistency do not confirm cause.

### D-027 — Impact separates reachability, exposure, observed effect, and business consequence

**Status:** Accepted — Phase 002 Group 05

Downstream Lineage produces Impact candidates only. Impact separately records actual exposure, downstream effect evidence, and technical/analytical/business consequence evidence.

### D-028 — Annotation is human context, not a catch-all truth or confirmation mechanism

**Status:** Accepted — Phase 002 Group 05

Annotation preserves attributed human context with revision/dispute/withdrawal history. Structured operational truth belongs to its owning concept.

### D-029 — Explanation is an authorization- and time-aware projection over concept state

**Status:** Accepted — Phase 002 Group 05

Explanation is not an independent truth source. It preserves material epistemic labels, statement-to-basis traceability, and the distinction between `what was known then` and `what we know now`.

### D-030 — Phase 002 concept specification exit gate is satisfied

**Status:** Accepted

All five groups and 20 retained concepts have reviewed specifications and can express the canonical/adversarial scenarios without hidden functionality or selected technical architecture.

### D-031 — Review Phase 003 as six synchronization groups

**Status:** Accepted — Phase 003 foundation

Phase 003 is organized as: (1) Subject, Scope & Governance Context; (2) Planned Change & Reference Transition; (3) Runtime Evidence, Health & Realized Change; (4) Lineage, Investigation & Causal Reasoning; (5) Downstream Impact, Annotation & Explanation; and (6) Historical Replay & Phase 003 Consolidation.

The order is a reasoning/review dependency, not an implementation dependency. Group 06 explicitly composes the whole system and performs the exit review rather than treating historical replay as an incidental concern.

### D-032 — Synchronizations coordinate concept results without becoming hidden architecture

**Status:** Accepted — Phase 003 foundation

A synchronization specifies participating concept actions/results, trigger, semantic preconditions, necessary ordering/independence, ambiguity/failure propagation, temporal/provenance/security behavior, and invariants. It does not imply a service call, workflow engine, transaction, event bus, database relation, API, or deployment architecture.

Synchronization order is never authority, and a synchronization trigger never implies causation.

### D-033 — Subject-specific synchronization starts from Entity Identity and preserves independent context branches

**Status:** Accepted — Phase 003 Group 01

Subject-specific synchronization first resolves Entity Identity rather than attaching state to raw names. Monitoring Scope then resolves independently. Semantic Definition, Responsibility Assignment, Classification, and Policy Context resolve as independent context branches against the common identity/time/context.

An unresolved branch must not erase independently valid branches. Scope does not imply authorization/evidence availability. Synchronization order cannot resolve governance authority conflicts.

### D-034 — Classification can support Policy Context applicability but cannot manufacture policy

**Status:** Accepted — Phase 003 Group 01

Where an explicit Policy Context assertion depends on a Classification predicate, the Classification result may provide supporting/contradicting/uncertain applicability evidence. Classification alone never creates Policy Context, grants authorization, proves enforcement, or establishes compliance. Missing Classification also cannot be converted into policy non-applicability.

### D-035 — Planned change prepares Expectation and Baseline references through independent branches

**Status:** Accepted — Phase 003 Group 02

A registered Change Intent may independently prompt explicit prospective Expectation establishment/revision and register a prospective Baseline comparability break. Anticipated effects do not become normative criteria, intended values do not become empirical Baseline values, and one unresolved branch does not erase a valid result in the other.

### D-036 — Intent-to-Deployment association and activation do not prove intended effect

**Status:** Accepted — Phase 003 Group 02

Change Intent ↔ Deployment association requires provenance-bearing target/revision/configuration/change linkage evidence rather than timing/name similarity. Deployment attempt, intent association, activation, intended-effect realization, health, and causation remain separate. Associations may be many-to-many and target/context specific.

### D-037 — Reference transition follows sufficient realization evidence, not workflow success or planned time

**Status:** Accepted — Phase 003 Group 02

A prospective reference boundary becomes effective only when evidence sufficiently establishes that the changed operating context became active for the relevant subject/dimension/context. Trustworthy Deployment activation may establish the structural/configuration boundary; realized Change evidence may do so where Deployment evidence is absent/insufficient. Workflow success and planned activation time alone are not enough.

### D-038 — Baseline non-comparability is contextual and rollback requires re-resolution

**Status:** Accepted — Phase 003 Group 02

A structural transition makes an old Baseline non-comparable for the changed context/interval without deleting it. Rollback/restoration creates another context boundary; prior Baseline or Expectation versions may become candidates again only when their own comparability/applicability semantics justify it. Rollback never blindly restores historical references.

### D-039 — Post-transition Baselines are empirical and late knowledge preserves contemporaneous history

**Status:** Accepted — Phase 003 Group 02

New Baselines require sufficient comparable post-transition Observations; an explicit Expectation can support immediate normative evaluation before that history exists. Late intent, activation, or correction evidence may improve retrospective reference interpretation without rewriting what the monitoring ecosystem knew or which references it actually used earlier.
