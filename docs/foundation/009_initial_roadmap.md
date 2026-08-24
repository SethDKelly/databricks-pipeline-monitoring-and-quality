# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with two accepted post-exit addenda.**

The original five groups accepted 20 concepts. Phase 003 Group 03 later added **Propagation Safeguard** after protective-control behavior exposed a missing concept boundary. Before Group 05, **Capability Authorization** was added after restricted-data analysis and separated operational authority exposed another missing boundary. The current catalog contains **22 concepts**.

See `../concepts/phase_002/README.md`.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Active — Groups 01–05 accepted; Group 06 next.**

**Goal:** define how independent accepted concepts synchronize to satisfy end-to-end behavior while preserving each concept's truth boundary.

Formal review groups:

1. **Subject, Scope & Governance Context** — **Accepted**.
2. **Planned Change & Reference Transition** — **Accepted**.
3. **Runtime Evidence, Health & Realized Change** — **Accepted**.
4. **Lineage, Investigation & Causal Reasoning** — **Accepted**.
5. **Downstream Impact, Annotation & Explanation** — **Accepted**. Historical downstream Lineage → candidates; consumption evidence → exposure/non-exposure; downstream health → observed effect; separate consequence evidence; Causal Claim for attribution; safeguard-prevented exposure; Annotation; Capability Authorization → Authorized Analytical Projection → Explanation.
6. **Historical Replay & Phase 003 Consolidation** — **Next**. Compose E-01–E-20 across event/effective time, knowledge time, authorization history, corrections, opacity, and the full Phase 003 exit gate.

Priority scenarios include stale upstream with successful downstream execution; A+B→C degradation; planned structural change; prospective blast radius; unregistered change; deployment-correlated shifts; cross-repository dependencies; conflicting governance metadata; restricted context; long-running upstream delay; missing output with protective hold; ordinary Baseline variation; client-critical atypicality with analyst research; safeguard-induced delivery delay; restricted-data analyst RCA; job-operation authority without raw-data read; safeguard-prevented exposure; critical-but-unexposed consumer; downstream effect with unknown business consequence; and historical authorization without current access.

See `../concepts/phase_003/README.md`.

## Phase 004 — Evidence, Time, and Causality Refinement
Refine evidence sufficiency/completeness; event/effective versus knowledge-time query semantics; correction/supersession; Causal Claim status transitions; confirmed-cause evidence/authority standards; attribution/confidence; negative evidence/coverage; exposure proof; and historical Investigation/Impact/Explanation reconstruction.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement
Refine source authority, conflict resolution, stewardship, criticality, Classification, Policy Context, PII/PHI/HIPAA-related transparency, Expectation authority, safeguard authority, **Capability Authorization vocabulary/source precedence/conditional semantics**, safe derived-evidence disclosure, and policy-sensitive explanation. Evaluate what must be native versus sourced from Collibra/Immuta/Unity Catalog/IAM systems.

## Phase 006 — Health, Freshness, and Quality Refinement
Refine Expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage, execution-duration/latency dimensions, statistical uncertainty/significance, quality checks, downstream-health summarization, and Databricks Metric Views/DQX fit.

## Phase 007 — Lineage, Change, Investigation, Impact, and Safeguard Refinement
Refine Lineage taxonomy, historical topology evidence, Change Intent realization, execution reconstruction, prospective/actual Impact, Causal Claim discovery/review, multiple contributors, consumer/version exposure evidence, technical/analytical/business consequence evidence, criticality prioritization, and safeguard placement/prevention/effect evidence.

## Phase 008 — Business Questioning and Explanation
Define question types, audience-specific Explanation structures, visible evidence citation rules, **Authorized Analytical Projection/redaction behavior**, layered Impact presentation, contemporaneous/retrospective views, uncertainty communication, retention, and deterministic versus generative behavior.

## Phase 009 — Integration Contracts and Source Authority
Determine required facts and source authority for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream analytical metadata, consumption/version evidence, planned-change sources, safeguard enforcement evidence, and authorization/entitlement sources.

## Phase 010 — Technical Architecture
Only now select implementation architecture. Evaluate historical/evidence storage; graph-compatible Lineage; ledger/temporal history; ingestion/synchronization; identity/authentication/Capability Authorization realization; service/API boundaries; Databricks deployment model; safeguard/quarantine realization; Explanation interface; tenancy/environment strategy; and testing/observability.

## Phase 011 — MVP Implementation Planning
Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation
Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule
A later phase may reveal a flaw in an earlier concept or synchronization. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
