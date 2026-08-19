# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery

**Status:** Complete.

Established product purpose, actors, terminology, Concept Design method, architectural principles, security/policy stance, lifecycles, MVP boundary, roadmap, and initial concept catalog.

## Phase 002 — Concept Specifications

**Status:** **Complete.**

All five groups and 20 retained concepts are accepted:

1. **Scope & Identity** — Monitoring Scope, Entity Identity.
2. **Semantics, Governance & Policy** — Semantic Definition, Responsibility Assignment, Classification, Policy Context.
3. **Health Evaluation** — Expectation, Baseline, Observation, Assessment.
4. **History, Lineage & Change** — Change Intent, Execution History, Deployment, Lineage, Change.
5. **Investigation, Impact & Explanation** — Investigation, Causal Claim, Impact, Annotation, Explanation.

Key Phase 002 cross-cutting outcomes include ledger-like historical semantics, graph-compatible typed temporal Lineage, planned-change/Baseline boundaries, explicit causal-claim semantics, downstream Impact layering, and authorization/time-aware Explanation.

See `../concepts/phase_002/README.md`.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Next — not started.**

**Goal:** define how independent accepted concepts synchronize to satisfy end-to-end behavior while preserving each concept's truth boundary.

Priority scenarios:

- stale upstream with successful downstream execution;
- A+B→C join-volume degradation with one or multiple contributors;
- successful run with bad output;
- planned structural change with valid outcome;
- planned change with unintended violation;
- unregistered source/config/topology change;
- schema/distribution change;
- cross-repository dependency degradation;
- Deployment-correlated data shift;
- conflicting governance/Expectation metadata;
- downstream reachability versus actual exposure/consequence;
- restricted/sensitive asset reporting;
- contemporaneous versus retrospective historical explanation;
- recovery/reassessment/reopened investigation.

## Phase 004 — Evidence, Time, and Causality Refinement

**Goal:** deepen the accepted evidence/temporal/causal model before technical storage architecture.

Refine:

- evidence sufficiency/completeness semantics;
- event/effective versus knowledge-time query semantics;
- correction/supersession behavior;
- Causal Claim status transitions;
- evidence/authority standard for confirmed cause;
- qualitative versus quantitative attribution if required;
- confidence/uncertainty semantics;
- historical Investigation/Explanation reconstruction.

Phase 002 already established the concept boundaries; Phase 004 refines synchronization/evidence standards rather than rediscovering them.

## Phase 005 — Governance, Authority, Semantics, and Policy Refinement

**Goal:** refine source authority, conflict resolution, stewardship, criticality, Classification, Policy Context, PII/PHI/HIPAA-related transparency, expectation authority, and policy-sensitive disclosure.

Evaluate what must be native versus sourced from Collibra/Immuta/Unity Catalog or other authorities.

## Phase 006 — Health, Freshness, and Quality Refinement

**Goal:** refine expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage semantics, quality checks, and how Databricks Metric Views/DQX could realize accepted concepts.

## Phase 007 — Lineage, Change, Investigation, and Impact Refinement

**Goal:** refine Lineage type taxonomy, historical topology evidence, Change Intent realization, execution reconstruction, Causal Claim discovery/review, multiple contributors, and downstream exposure/consequence evidence.

## Phase 008 — Business Questioning and Explanation

**Goal:** define question types, audience-specific Explanation structures, visible evidence citation rules, contemporaneous/retrospective views, uncertainty communication, retained-snapshot policy, and deterministic versus generative behavior.

## Phase 009 — Integration Contracts and Source Authority

**Goal:** determine required facts and source authority for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream analytical metadata, and planned-change sources.

## Phase 010 — Technical Architecture

**Goal:** only now select implementation architecture based on validated product concepts/constraints.

Evaluate, without presumption:

- historical/evidence storage forms;
- graph-compatible Lineage realization;
- ledger/temporal history realization;
- ingestion/synchronization patterns;
- service/API boundaries;
- identity/authorization architecture;
- Databricks deployment model;
- Explanation/question interface;
- batch/event-driven behavior;
- tenancy/environment strategy;
- testing/observability.

## Phase 011 — MVP Implementation Planning

Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation

Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept. Reopen/revise the concept explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
