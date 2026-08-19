# 009 — Initial Roadmap

This roadmap intentionally delays implementation until product concepts, synchronizations, and trust boundaries are stable enough to guide technical design.

## Phase 001 — Product Foundation and Concept Discovery

**Goal:** establish product purpose, actors, terminology, Concept Design method, architectural principles, security/policy stance, lifecycles, MVP boundary, and open questions.

**Deliverables:** this `docs/foundation/` set, concept catalog seed, Codex/Cursor rules.

**No coding.**

## Phase 002 — Concept Specifications

**Goal:** turn the candidate catalog into explicit specifications using a strategic group-by-group review order.

Active groups:

1. **Scope & Identity** — Monitored Scope, Asset Identity.
2. **Semantics, Governance & Policy** — Semantic Definition, Ownership, Classification, Policy Context.
3. **Health Evaluation** — Expectation, Baseline, Observation, Assessment.
4. **History, Lineage & Change** — Execution History, Deployment, Lineage, Change.
5. **Investigation, Impact & Explanation** — Investigation, Causal Claim, Impact, Annotation, Explanation.

Each candidate may be accepted, revised, split, merged, renamed, or rejected during review.

**Key output:** for each retained concept, purpose, operational principle, state, actions, invariants, ambiguity behavior, synchronizations, security/provenance considerations, scenarios, and non-goals.

See `../concepts/phase_002/README.md`.

**No implementation mapping yet.**

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Goal:** define how independent concepts synchronize to satisfy end-to-end scenarios.

Stress-test:

- stale upstream;
- join-volume degradation;
- successful run with bad output;
- schema change;
- cross-repository dependency degradation;
- deployment-correlated data shift;
- conflicting governance metadata;
- restricted/sensitive asset reporting;
- recovery and historical replay.

## Phase 004 — Evidence, Time, and Causality Semantics

**Goal:** define product-level semantics for evidence, temporal validity, baselines, change, hypotheses, attribution, confidence, confirmation, and historical topology.

This is essential before choosing a storage/graph/time-series architecture.

## Phase 005 — Governance, Semantics, Ownership, and Policy Refinement

**Goal:** refine authority, provenance, conflicts, stewardship, criticality, classification, PII/PHI/HIPAA-related transparency, and policy-sensitive presentation.

Evaluate what must be native versus sourced from Collibra/Immuta.

## Phase 006 — Health, Freshness, and Quality Semantics

**Goal:** define expected execution, freshness/staleness, quality dimensions, quality rules/checks, trend/degradation semantics, and how Databricks Metric Views/DQX could realize accepted concepts.

## Phase 007 — Lineage, Change Attribution, and Root-Cause Analysis

**Goal:** refine typed lineage families, historical topology, upstream investigation, downstream blast radius, multiple contributing causes, and evidence chains.

## Phase 008 — Business Questioning and Reporting

**Goal:** define question types, layered explanations, report semantics, uncertainty communication, authorized detail levels, and business-facing trust requirements.

## Phase 009 — Integration Contracts and Source Authority

**Goal:** determine required facts and source authority for:

- Databricks;
- Git repositories;
- GitHub Actions;
- DQX;
- Metric Views;
- Collibra (optional);
- Immuta (optional);
- downstream analytical metadata.

This phase defines integration contracts conceptually before implementation.

## Phase 010 — Technical Architecture

**Goal:** only now select implementation architecture based on validated product concepts and constraints.

Questions may include:

- storage forms for historical observations and lineage;
- ingestion/synchronization patterns;
- API/service boundaries;
- identity and authorization architecture;
- Databricks deployment model;
- UI/question interface;
- batch versus event-driven behavior;
- tenancy/environment strategy;
- testing and observability.

No choice is implied by the current roadmap.

## Phase 011 — MVP Implementation Planning

**Goal:** convert the accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation

**Goal:** implement the minimum vertical slices required to prove the canonical scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept. The project should revise the concept rather than preserve a bad foundation merely to maintain sequence.
