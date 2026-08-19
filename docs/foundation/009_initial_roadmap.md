# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery

**Status:** Complete.

Established product purpose, actors, terminology, Concept Design method, architectural principles, security/policy stance, lifecycles, MVP boundary, roadmap, and initial concept catalog.

## Phase 002 — Concept Specifications

**Status:** **Complete.**

All five groups and 20 retained concepts are accepted. Key outcomes include ledger-like historical semantics, graph-compatible typed temporal Lineage, planned-change/Baseline boundaries, explicit Causal Claim semantics, Impact layering, and authorization/time-aware Explanation.

See `../concepts/phase_002/README.md`.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Active — Group 01 accepted; Group 02 next.**

**Goal:** define how independent accepted concepts synchronize to satisfy end-to-end behavior while preserving each concept's truth boundary.

Formal review groups:

1. **Subject, Scope & Governance Context** — **Accepted**. Entity Identity → Monitoring Scope and independent semantic/responsibility/classification/policy resolution; Classification may support explicit Policy Context applicability without manufacturing policy.
2. **Planned Change & Reference Transition** — **Next**. Change Intent → prospective Expectation review/Baseline comparability boundary → realization evidence/post-change reference transition.
3. **Runtime Evidence, Health & Realized Change** — Planned. Deployment activation → Execution History → Observation → Assessment and realized Change.
4. **Lineage, Investigation & Causal Reasoning** — Planned. Assessment/Change/question → Investigation; historical Lineage/evidence → competing Causal Claims.
5. **Downstream Impact, Annotation & Explanation** — Planned. Lineage → Impact candidates/exposure/effect/consequence; Annotation/context → authorized Explanation.
6. **Historical Replay & Phase 003 Consolidation** — Planned. Full ecosystem scenario composition, contemporaneous/retrospective reconstruction, and exit review.

Priority scenarios include stale upstream with successful downstream execution; A+B→C degradation; planned structural change with valid outcome; planned change with unintended violation; unregistered change; Deployment-correlated shifts; cross-repository dependencies; conflicting governance/Expectation metadata; restricted context; downstream reachability versus actual exposure/consequence; and late historical correction.

See `../concepts/phase_003/README.md`.

## Phase 004 — Evidence, Time, and Causality Refinement

**Goal:** deepen the accepted evidence/temporal/causal model before technical storage architecture.

Refine evidence sufficiency/completeness; event/effective versus knowledge-time query semantics; correction/supersession behavior; Causal Claim status transitions; confirmed-cause evidence/authority standards; attribution/confidence semantics; and historical Investigation/Explanation reconstruction.

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

Evaluate historical/evidence storage; graph-compatible Lineage realization; ledger/temporal history realization; ingestion/synchronization patterns; service/API boundaries; identity/authorization architecture; Databricks deployment model; Explanation/question interface; batch/event-driven behavior; tenancy/environment strategy; and testing/observability.

## Phase 011 — MVP Implementation Planning

Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation

Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept or synchronization. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
