# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with three accepted post-exit addenda.**

The original five groups accepted 20 concepts. Phase 003 later added **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate** after synchronization review exposed independent missing behavior. Current catalog: **23 concepts**.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Complete — Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass.**

Phase 003 defines end-to-end coordination for subject/governance context; planned change/reference transition; runtime timing/health/change; optional execution gating; safeguards; Investigation/causality; layered downstream Impact; Annotation; authorized analytical projection/Explanation; and bitemporal historical replay.

Group 06 establishes event/effective-time + knowledge-cut replay, late/corrected-evidence retrospective re-evaluation, current-authorization-safe historical Explanation, and the completed Phase 003 exit review.

See `../concepts/phase_003/README.md` and `../concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md`.

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **Active — Groups 01–02 accepted; Group 03 next.**

Phase 004 uses `REF-###` refinement contracts over the accepted concepts/synchronizations. These are not new truth-owning concepts and do not extend the Phase 003 SYN sequence.

Review groups:

1. **Evidence Sufficiency, Coverage & Negative Evidence** — **Accepted.** REF-001–REF-005 define proposition binding/evidence applicability, bounded Coverage Profiles/opportunity-to-observe, negative/absence/exclusion evidence, corroboration/conflict/independence, and conclusion-specific sufficiency.
2. **Event/Effective Time, Knowledge Cut & Correction** — **Accepted.** REF-006–REF-012 distinguish event/source-availability/framework-knowledge/evaluation time, exact `as-known` eligibility, epistemic negative claims, progressive analytical availability, late/corrected evidence classes, dependent reevaluation/reopen materiality, and actual-retained versus reconstructed historical state.
3. **Causal Epistemics, Confirmation & Multiple Contributors** — **Next.** Refine Causal Claim status transitions, support/contradiction, confirmation evidence/authority standards, qualitative contribution roles, progressive RCA maturity, and challenge after confirmation.
4. **Exposure, Consumption, Readiness & Control Evidence** — Planned. Specialize evidence standards for exposure/non-exposure, gate readiness, actual hold/admission enforcement, safeguard enforcement/prevented exposure, and unavailable-control evidence.
5. **Phase 004 Consolidation / Exit Review** — Planned. Apply the standards across the full Phase 003 behavior and hand remaining authority/statistical/integration/implementation questions to later phases.

### Progressive monitoring-result availability

Phase 004 Group 02 establishes a functional sequence rather than fixed SLAs:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**.

The project should return the narrowest trustworthy result as soon as the evidence required for that result is available. Faster evidence such as job lifecycle state should not wait for slower Metric View/DQ/RCA evidence, while early results must not overstate broader health or causality.

Concrete timing targets remain intentionally deferred:

- **Phase 006** defines which health/quality results need immediate, near-real-time, delayed, or post-ops availability and what freshness/latency expectations apply;
- **Phase 009** evaluates actual evidence-availability/collection characteristics for Databricks jobs, Metric Views, DQX, GitHub/deployment, Lineage, governance, consumption, and other sources;
- **Phase 010** selects architecture/performance budgets for fast-path and asynchronous/deeper analysis while preserving passive-monitoring non-interference;
- **Phase 011** converts accepted timing objectives into MVP acceptance criteria.

See `../concepts/phase_004/README.md`.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement
Refine source authority, conflict resolution, stewardship, criticality, Classification, Policy Context, PII/PHI/HIPAA-related transparency, Expectation authority, safeguard authority, Capability Authorization vocabulary/source precedence/conditional semantics, Execution Gate configuration/override authority, safe derived-evidence disclosure, and policy-sensitive Explanation.

## Phase 006 — Health, Freshness, Quality, and Result-Timing Refinement
Refine Expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage, execution-duration/latency dimensions, dependency-readiness criteria, statistical uncertainty/significance, quality checks, downstream-health summarization, Databricks Metric Views/DQX fit, and **functional availability expectations for immediate operational checks, enriched health metrics, and health summaries**. Define evidence/result freshness and latency objectives without selecting architecture.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement
Refine Lineage taxonomy, historical topology evidence, Change Intent realization, execution reconstruction, prospective/actual Impact, causal discovery/review, multiple contributors, consumer/version exposure evidence, consequence evidence, criticality prioritization, safeguard placement/prevention/effect evidence, and Execution Gate readiness/hold/admit/override/timeout behavior.

## Phase 008 — Business Questioning and Explanation
Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction, layered Impact/control state, contemporaneous/retrospective/comparison views, reconstructed-versus-actual historical Explanation labeling, uncertainty communication, retention, and deterministic versus generative behavior. Define how progressive result maturity is communicated so users can distinguish fast operational state from enriched/RCA/post-ops conclusions.

## Phase 009 — Integration Contracts, Source Authority, and Evidence Availability
Determine required facts/source authority for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, safeguard/gate enforcement, and authorization sources. Characterize **source production/availability, collection latency, historical retention, and query cost/availability** needed to support the accepted monitoring-result horizons. Preserve the objective that baseline monitoring is independently deployed and should not require production repository/GitHub Actions changes where platform metadata is sufficient.

## Phase 010 — Technical Architecture
Only now select implementation architecture. Evaluate historical/evidence storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; identity/Capability Authorization realization; service/API boundaries; Databricks deployment model; out-of-band passive monitoring; optional dependency-gating control-plane realization and availability/fallback; safeguard/quarantine realization; Explanation interface; tenancy/environment strategy; testing/observability; and **fast-path versus asynchronous/deeper analysis architecture and performance budgets**.

A key architecture criterion is that ungated production jobs should not depend on monitoring-framework availability and baseline monitoring should add as little production-path latency as practical.

## Phase 011 — MVP Implementation Planning
Convert accepted architecture into implementation phases, interfaces, test strategy, migration/onboarding strategy, acceptance criteria, and concrete availability/latency targets for the selected MVP monitoring-result classes.

## Phase 012 — MVP Implementation
Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule
A later phase may reveal a flaw in an earlier concept or synchronization. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
