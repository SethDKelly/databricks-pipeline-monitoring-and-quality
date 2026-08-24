# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with three accepted post-exit addenda.**

The original five groups accepted 20 concepts. Phase 003 later added **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate** after synchronization review exposed independent missing behavior. Current catalog: **23 concepts**.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Complete — Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass.**

Phase 003 now defines end-to-end coordination for subject/governance context; planned change/reference transition; runtime timing/health/change; optional execution gating; safeguards; Investigation/causality; layered downstream Impact; Annotation; authorized analytical projection/Explanation; and bitemporal historical replay.

Group 06 establishes event/effective-time + knowledge-cut replay, late/corrected-evidence retrospective re-evaluation, current-authorization-safe historical Explanation, and the completed Phase 003 exit review.

See `../concepts/phase_003/README.md` and `../concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md`.

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **Next — not started.**

Refine:

- evidence sufficiency/completeness and source-coverage semantics;
- event/effective versus recorded/knowledge-time query semantics and `not known by cutoff` standards;
- correction/supersession and dependent reassessment/reopen materiality;
- Causal Claim status transitions, confirmation evidence/authority standards, attribution/confidence, multiple contributors, and challenge after confirmation;
- positive/negative/absence evidence;
- exposure/non-exposure proof;
- gate readiness/hold/admission/enforcement evidence sufficiency;
- historical Investigation/Impact/Explanation retention versus reconstruction.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement
Refine source authority, conflict resolution, stewardship, criticality, Classification, Policy Context, PII/PHI/HIPAA-related transparency, Expectation authority, safeguard authority, Capability Authorization vocabulary/source precedence/conditional semantics, Execution Gate configuration/override authority, safe derived-evidence disclosure, and policy-sensitive Explanation.

## Phase 006 — Health, Freshness, and Quality Refinement
Refine Expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage, execution-duration/latency dimensions, dependency-readiness criteria, statistical uncertainty/significance, quality checks, downstream-health summarization, and Databricks Metric Views/DQX fit.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement
Refine Lineage taxonomy, historical topology evidence, Change Intent realization, execution reconstruction, prospective/actual Impact, causal discovery/review, multiple contributors, consumer/version exposure evidence, consequence evidence, criticality prioritization, safeguard placement/prevention/effect evidence, and Execution Gate readiness/hold/admit/override/timeout behavior.

## Phase 008 — Business Questioning and Explanation
Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction, layered Impact/control state, contemporaneous/retrospective/comparison views, reconstructed-versus-actual historical Explanation labeling, uncertainty communication, retention, and deterministic versus generative behavior.

## Phase 009 — Integration Contracts and Source Authority
Determine required facts/source authority for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, safeguard/gate enforcement, and authorization sources. Preserve the objective that baseline monitoring is independently deployed and should not require production repository/GitHub Actions changes where platform metadata is sufficient.

## Phase 010 — Technical Architecture
Only now select implementation architecture. Evaluate historical/evidence storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; identity/Capability Authorization realization; service/API boundaries; Databricks deployment model; out-of-band passive monitoring; optional dependency-gating control-plane realization and availability/fallback; safeguard/quarantine realization; Explanation interface; tenancy/environment strategy; testing/observability.

A key architecture criterion is that ungated production jobs should not depend on monitoring-framework availability and baseline monitoring should add as little production-path latency as practical.

## Phase 011 — MVP Implementation Planning
Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, and acceptance criteria.

## Phase 012 — MVP Implementation
Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule
A later phase may reveal a flaw in an earlier concept or synchronization. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
