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

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **COMPLETE — Groups 01–05 accepted; REF-001–REF-030 accepted.**

Phase 004 uses `REF-###` refinement contracts over accepted concepts/synchronizations. These are not new truth-owning concepts and do not extend the Phase 003 SYN sequence.

Accepted groups:

1. **Evidence Sufficiency, Coverage & Negative Evidence — REF-001–REF-005.** Proposition binding/evidence applicability, bounded coverage/opportunity-to-observe, negative/absence/exclusion evidence, corroboration/conflict/independence, conclusion-specific sufficiency.
2. **Event/Effective Time, Knowledge Cut & Correction — REF-006–REF-012.** Event/source-availability/framework-knowledge/evaluation time, exact `as-known` eligibility, negative epistemic claims, progressive analytical availability, late/corrected evidence classes, material reassessment/reopen behavior, actual-retained versus reconstructed historical state.
3. **Causal Epistemics, Confirmation & Multiple Contributors — REF-013–REF-020.** Causal proposition/status, multidimensional support/contradiction, bounded alternatives, claim-class confirmation profiles, evidence/authority separation, multiple contributors, qualitative roles, progressive RCA, post-confirmation challenge.
4. **Exposure, Consumption, Readiness & Control Evidence — REF-021–REF-030.** Encounter-bound exposure, non-exposure coverage, criterion-relative readiness, gate decision/enforcement/execution separation, safeguard enforcement/prevention, fallback evidence, control-effect causality and retrospective revision.
5. **Consolidation / Exit Review — accepted.** E-01–E-22 and all Phase 004 scenario checks pass under REF-001–REF-030. No additional Concept, synchronization, or REF contract is required.

### Progressive monitoring-result and RCA availability

Phase 004 establishes functional sequences rather than fixed SLAs:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**

Within RCA:

**candidate/proposed claim → early supported/weakened/unresolved evaluation → deeper investigative RCA → retrospective/confirmation review**

For controls/exposure:

**readiness/output facts → gate decision → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

The project should return the narrowest trustworthy result as soon as its evidence standard is satisfied. Faster job lifecycle evidence should not wait for slower Metric View/DQ/RCA evidence, while early results must not overstate health, causality, exposure, or control enforcement.

Concrete timing targets remain intentionally deferred:

- **Phase 006** defines which health/quality results need immediate, near-real-time, delayed, or post-ops availability and their evidence/result freshness objectives;
- **Phase 008** defines communication of progressive health/RCA/control maturity;
- **Phase 009** evaluates actual evidence source availability, collection latency, retention, query cost, and enforcement observability;
- **Phase 010** selects fast-path/asynchronous architecture, control-path availability strategy, and performance budgets while preserving passive-monitoring non-interference;
- **Phase 011** converts accepted timing objectives into MVP acceptance criteria.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** **NEXT — not started.**

Refine:

- source/actor authority and category/context-specific conflict resolution;
- Semantic Definition, Responsibility Assignment, Classification, Policy Context, criticality, and stewardship authority;
- Expectation/normative-setting authority;
- Capability Authorization vocabulary, conditionality, source precedence/conflict/unknown behavior;
- safe derived-evidence disclosure and opacity;
- causal-confirmation capability/authority by claim class/subject/context;
- safeguard proposal/activation/release authority;
- Execution Gate configuration/enable/override/control authority;
- policy-sensitive Explanation/disclosure governance.

Phase 005 may determine who/what is permitted to confirm, configure, operate, disclose, or resolve state. It must **not** weaken or redefine the Phase 004 evidence meaning of those conclusions or select IAM implementation.

## Phase 006 — Health, Freshness, Quality, and Result-Timing Refinement

Refine Expectation dimensions, Baseline classes/comparability, Assessment vocabularies, observed-absence coverage, execution-duration/latency dimensions, dependency-readiness criteria/classes, statistical uncertainty/significance, quality checks, downstream-health summarization, Databricks Metric Views/DQX fit, and **functional availability expectations for immediate operational checks, enriched health metrics, and health summaries**.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement

Refine Lineage taxonomy/historical topology evidence, Change Intent realization, execution reconstruction, Investigation lifecycle, prospective/actual Impact, consumer/version encounter patterns, consequence categories, safeguard placement/release, Execution Gate classes, timeout/fallback/escalation/override/recovery policy, and control-induced operational effects. Preserve Phase 004 evidence burdens.

## Phase 008 — Business Questioning and Explanation

Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction, layered Impact/control state, contemporaneous/retrospective/comparison views, reconstructed-versus-actual historical Explanation labeling, uncertainty communication, deterministic versus generative behavior, and progressive result maturity communication.

## Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

Determine required facts and actual evidence support for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, safeguard/gate enforcement, authorization sources, and causal evidence inputs.

Characterize **source production/availability time, collection latency, retention, query cost/availability, and control-enforcement observability** needed to satisfy the accepted evidence/timing semantics. Preserve the objective that baseline monitoring be independently deployed and avoid production repository/GitHub Actions changes where platform metadata is sufficient.

## Phase 010 — Technical Architecture

Only now select implementation architecture. Evaluate evidence/history storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; Capability Authorization realization; Databricks deployment model; out-of-band passive monitoring; optional dependency-gating control-plane realization/availability/fallback; safeguard/quarantine realization; Explanation interface; testing/observability; causal reasoning implementation; and **fast-path versus asynchronous/deeper analysis architecture and performance budgets**.

A key architecture criterion remains that **ungated production jobs must not depend on monitoring-framework availability**. Explicitly gated paths may require deliberate production-critical control availability under accepted policies.

## Phase 011 — MVP Implementation Planning

Convert accepted architecture into implementation phases, interfaces, test strategy, onboarding/migration strategy, acceptance criteria, and concrete availability/latency targets for selected MVP monitoring-result, health, RCA, exposure, and control classes.

## Phase 012 — MVP Implementation

Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept, synchronization, or refinement. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.
