# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery

**Status:** Complete.

Established product purpose, actors, terminology, Concept Design method, architectural principles, security/policy stance, lifecycles, MVP boundary, roadmap, and initial concept catalog.

## Phase 002 — Concept Specifications

**Status:** **Complete with one accepted post-exit addendum.**

The original five groups accepted 20 concepts. Phase 003 Group 03 later exposed a missing protective-control boundary, so **Propagation Safeguard** was accepted as a narrow post-exit addendum. The current catalog contains 21 concepts.

Key outcomes include ledger-like historical semantics, graph-compatible typed temporal Lineage, planned-change/Baseline boundaries, explicit Causal Claim semantics, Impact layering, authorization/time-aware Explanation, and now separate propagation-protection state.

See `../concepts/phase_002/README.md`.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Active — Groups 01–03 accepted; Group 04 next.**

**Goal:** define how independent accepted concepts synchronize to satisfy end-to-end behavior while preserving each concept's truth boundary.

Formal review groups:

1. **Subject, Scope & Governance Context** — **Accepted**. Entity Identity → Monitoring Scope and independent semantic/responsibility/classification/policy resolution; Classification may support explicit Policy Context applicability without manufacturing policy.
2. **Planned Change & Reference Transition** — **Accepted**. Change Intent → independent prospective Expectation/Baseline preparation; evidence-backed Deployment association/transition; empirical post-transition Baseline; prospective downstream blast-radius profile without actual Impact claims.
3. **Runtime Evidence, Health & Realized Change** — **Accepted**. Active Deployment ↔ Execution History; execution-duration/dependency timing Observations; time-valid Assessment; meaningful realized Change; analyst Investigation handoff; Propagation Safeguard coordination.
4. **Lineage, Investigation & Causal Reasoning** — **Next**. Bounded Investigation → historical Lineage/evidence discovery → competing Causal Claims, including timing/safeguard evidence and analyst-added context.
5. **Downstream Impact, Annotation & Explanation** — Planned. Lineage → Impact candidates/exposure/effect/consequence; Annotation/context → authorized Explanation.
6. **Historical Replay & Phase 003 Consolidation** — Planned. Full ecosystem scenario composition, contemporaneous/retrospective reconstruction, and exit review.

Priority scenarios include stale upstream with successful downstream execution; A+B→C degradation; planned structural change with valid outcome; planned change with unintended violation; prospective blast radius; unregistered change; deployment-correlated shifts; cross-repository dependencies; conflicting governance/Expectation metadata; restricted context; long-running upstream delay; missing output with protective hold; ordinary Baseline variation without intervention; client-critical atypicality with analyst research; safeguard-induced delivery delay; downstream reachability versus actual exposure/consequence; and late historical correction.

See `../concepts/phase_003/README.md`.

## Phase 004 — Evidence, Time, and Causality Refinement

**Goal:** deepen the accepted evidence/temporal/causal model before technical storage architecture.

Refine evidence sufficiency/completeness; event/effective versus knowledge-time query semantics; correction/supersession behavior; Causal Claim status transitions; confirmed-cause evidence/authority standards; attribution/confidence semantics; and historical Investigation/Explanation reconstruction.

## Phase 005 — Governance, Authority, Semantics, and Policy Refinement

**Goal:** refine source authority, conflict resolution, stewardship, criticality, Classification, Policy Context, PII/PHI/HIPAA-related transparency, expectation authority, policy-sensitive disclosure, safeguard authority, and whether repeated response/urgency behavior warrants its own normative concept.

Evaluate what must be native versus sourced from Collibra/Immuta/Unity Catalog or other authorities.

## Phase 006 — Health, Freshness, and Quality Refinement

**Goal:** refine expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage semantics, execution-duration/latency dimensions, statistical uncertainty/significance, quality checks, and how Databricks Metric Views/DQX could realize accepted concepts.

## Phase 007 — Lineage, Change, Investigation, Impact, and Safeguard Refinement

**Goal:** refine Lineage type taxonomy, historical topology evidence, Change Intent realization, execution reconstruction, prospective/actual Impact, Causal Claim discovery/review, multiple contributors, downstream exposure/consequence evidence, and safeguard placement/authority/effect evidence.

## Phase 008 — Business Questioning and Explanation

**Goal:** define question types, audience-specific Explanation structures, visible evidence citation rules, contemporaneous/retrospective views, uncertainty communication, retained-snapshot policy, and deterministic versus generative behavior.

## Phase 009 — Integration Contracts and Source Authority

**Goal:** determine required facts and source authority for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream analytical metadata, planned-change sources, and safeguard enforcement evidence.

## Phase 010 — Technical Architecture

**Goal:** only now select implementation architecture based on validated product concepts/constraints.

Evaluate historical/evidence storage; graph-compatible Lineage realization; ledger/temporal history realization; ingestion/synchronization patterns; service/API boundaries; identity/authorization architecture; Databricks deployment model; safeguard/quarantine realization; Explanation/question interface; batch/event-driven behavior; tenancy/environment strategy; and testing/observability.

## Phase 011 — MVP Implementation Planning

Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation

Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept or synchronization. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
