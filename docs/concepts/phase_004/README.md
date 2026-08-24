# Phase 004 — Evidence, Time, and Causality Refinement

**Status:** COMPLETE — Groups 01–05 accepted; REF-001–REF-030 accepted

## Purpose

Phase 004 refines the evidence, temporal, causal, exposure, readiness, and control-proof standards that Phase 003 intentionally left abstract. It does **not** replace the 23 accepted concepts or SYN-001–SYN-035, and it does not select storage, orchestration, IAM, graph, DQ, statistical, LLM, causal-algorithm, or other technical architecture.

Phase 003 established which truths must remain separate. Phase 004 establishes what evidence is adequate to support those truths, how historical evidence cuts are evaluated precisely, how results can mature as evidence arrives, and what standards govern high-consequence causal and control/exposure conclusions.

## Phase method

A Phase 004 refinement:

- applies to one or more accepted concepts/synchronizations without becoming a new truth owner unless a genuine concept gap is discovered;
- names the proposition/conclusion being evaluated;
- distinguishes evidence applicability from evidence coverage and from conclusion sufficiency;
- preserves supporting, contradicting, missing, restricted, late, corrected, duplicated, and derived evidence explicitly;
- states event/effective-time, evidence-availability, recorded/knowledge-time, and evaluation-time behavior where relevant;
- never converts missing telemetry into a reassuring negative;
- never converts an evidence-strength rule into source authority or user authorization unless those semantics are explicitly in scope;
- allows narrow trustworthy results to appear before slower enrichment while preserving scope/knowledge-cut limitations;
- keeps causal status explicit and never promotes a leading/fast hypothesis into confirmation merely for operational convenience;
- keeps readiness, gate decision/enforcement, actual execution, safeguard enforcement, and exposure/prevention conclusions separate;
- remains implementation-neutral.

Refinement artifacts use `REF-###` identifiers. These identifiers are **not new synchronizations** and do not extend the Phase 003 SYN sequence.

## Review groups

| Group | Theme | Primary questions | Status |
|---|---|---|---|
| 01 | Evidence Sufficiency, Coverage & Negative Evidence | applicability; bounded coverage; opportunity-to-observe; absence/exclusion; corroboration/conflict; conclusion-specific sufficiency | **Accepted** |
| 02 | Event/Effective Time, Knowledge Cut & Correction | evidence availability; exact `as-known` semantics; progressive analytical maturity; late evidence; correction/supersession; `not known by cutoff`; dependent reassessment/reopen | **Accepted** |
| 03 | Causal Epistemics, Confirmation & Multiple Contributors | causal proposition/status; support/contradiction; alternatives; confirmation evidence/authority boundary; multiple contributors; progressive RCA; challenge after confirmation | **Accepted** |
| 04 | Exposure, Consumption, Readiness & Control Evidence | exposure/non-exposure proof; readiness criteria; gate decision/enforcement; safeguard enforcement; prevented exposure; degraded control telemetry | **Accepted** |
| 05 | Phase 004 Consolidation / Exit Review | cross-domain composition; scenario replay; retained/reconstructed state; later-phase handoff | **Accepted — Phase exit** |

## Accepted Group 01 — REF-001–REF-005

Group 01 is documented in [`01_evidence_sufficiency_and_coverage/README.md`](01_evidence_sufficiency_and_coverage/README.md).

- **REF-001 — Evidence Applicability and Proposition Binding**
- **REF-002 — Coverage Profile and Opportunity to Observe**
- **REF-003 — Negative, Absence, and Exclusion Evidence**
- **REF-004 — Corroboration, Conflict, and Evidence Independence**
- **REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation**

Key results:

- evidence sufficiency is proposition/conclusion relative, not a universal score;
- evidence must be applicable before it can support/contradict;
- coverage is bounded and multidimensional;
- negative/absence/exclusion claims require opportunity-to-observe plus sufficient bounded coverage;
- missing/unavailable/restricted telemetry is not negative evidence;
- duplicated/common-derived evidence is not independent corroboration;
- applicable conflicts remain explicit until accepted authority semantics resolve them;
- sufficiency does not grant disclosure or production-control authority.

## Accepted Group 02 — REF-006–REF-012

Group 02 is documented in [`02_event_time_knowledge_cut_and_correction/README.md`](02_event_time_knowledge_cut_and_correction/README.md).

- **REF-006 — Temporal Coordinates and Evidence Availability**
- **REF-007 — Historical Knowledge-Cut Eligibility**
- **REF-008 — Known By, Learned After, and Not Known By Claims**
- **REF-009 — Progressive Evidence Availability and Analytical Maturity**
- **REF-010 — Late Evidence, Correction, Conflict, and Reinterpretation**
- **REF-011 — Dependent Re-evaluation and Investigation Reopen Materiality**
- **REF-012 — Actual Retained State versus Reconstructible Historical State**

Key results:

- event/effective time, source production/availability, framework collection/knowledge, derived evaluation, and correction time remain distinct where material;
- source availability is not framework knowledge;
- `as-known` cuts use only evidence known by the cutoff;
- `known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are separate propositions;
- results may mature from immediate operational validation through enriched health, RCA, and post-ops review;
- faster narrow results do not inherit broader health/causal meaning;
- late evidence/correction/conflict/reinterpretation remain distinct;
- actual historical state requires evidence that it existed then; otherwise replay is reconstructed;
- exact latency objectives remain deferred to Phases 006/009/010/011.

## Accepted Group 03 — REF-013–REF-020

Group 03 is documented in [`03_causal_epistemics_confirmation/README.md`](03_causal_epistemics_confirmation/README.md).

- **REF-013 — Causal Proposition and Role Binding**
- **REF-014 — Causal Epistemic Status Vocabulary and Transition Semantics**
- **REF-015 — Causal Support, Contradiction, and Evidence-Dimension Evaluation**
- **REF-016 — Material Alternatives and Causal Discrimination**
- **REF-017 — Confirmation Evidence Gate and Authority Separation**
- **REF-018 — Multiple Contributors and Qualitative Causal Roles**
- **REF-019 — Progressive RCA Maturity and Fast-Path Causal Communication**
- **REF-020 — Challenge, Reversal, and Historical Preservation After Confirmation**

Key results:

- causal propositions bind cause, effect, role, context/time, and material mechanism/transmission assumptions;
- accepted status vocabulary is `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- `rejected` requires sufficient contradiction/exclusion evidence;
- causal evaluation is multidimensional, not a universal confidence score;
- material alternatives are bounded by Investigation context and compatible contributors may coexist;
- `confirmed` is a separate claim-class evidence gate with independently resolved confirmation authority/capability;
- no human title or automated process self-authorizes confirmation;
- `primary` requires comparative evidence and qualitative roles do not imply percentage attribution;
- RCA may mature progressively without latency-driven status inflation;
- confirmed claims remain challengeable while historical confirmation remains reconstructable.

## Accepted Group 04 — REF-021–REF-030

Group 04 is documented in [`04_exposure_consumption_readiness_control/README.md`](04_exposure_consumption_readiness_control/README.md).

- **REF-021 — Exposure Proposition and Encounter Binding**
- **REF-022 — Positive Exposure / Consumption Evidence**
- **REF-023 — Non-Exposure and Negative Consumption Coverage**
- **REF-024 — Dependency Readiness Criterion Decomposition**
- **REF-025 — Execution Gate Decision, Enforcement, and Actual Execution**
- **REF-026 — Gate Enforcement Evidence and Degraded Control State**
- **REF-027 — Propagation Safeguard Activation and Enforcement Evidence**
- **REF-028 — Prevented Exposure Evidence Standard**
- **REF-029 — Control Telemetry, Fallback, and Unavailable-State Evidence**
- **REF-030 — Control-Effect Causality and Retrospective Revision**

Key results:

- exposure is actual encounter/use of a bound affected state/version/window, not reachability/timing;
- `not exposed` requires bounded negative consumption/path coverage;
- safe prior-version use may mean non-exposure to the suspect state while freshness is still stale;
- readiness is criterion-relative and can decompose completion, output existence, version/currentness, freshness, publication availability, and named quality predicates;
- successful upstream execution is not global readiness;
- gate decision, gate enforcement, and actual execution remain separate evidence claims;
- configured/enabled gate state and fallback policy do not prove opportunity-specific enforcement;
- safeguard proposal/request/configuration does not prove active enforcement;
- prevented exposure requires materially operative safeguard enforcement plus negative-consumption/version and alternate-path coverage;
- control-effect causal claims still use REF-013–REF-020;
- late control/consumption evidence revises retrospective conclusions without rewriting historical actions.

## Accepted Group 05 — Consolidation / Exit

Group 05 is documented in [`05_consolidation_and_exit/README.md`](05_consolidation_and_exit/README.md).

The exit review adds **no new REF identifiers**. It accepts:

- [`05_consolidation_and_exit/scenario_consolidation_matrix.md`](05_consolidation_and_exit/scenario_consolidation_matrix.md) — E-01–E-22 pass under REF-001–REF-030;
- [`05_consolidation_and_exit/phase_004_exit_review.md`](05_consolidation_and_exit/phase_004_exit_review.md) — formal evidence/time/causality/control exit review;
- D-140–D-152 — durable consolidation/exit decisions.

The consolidated model confirms one common evidence burden across run/output absence, historical negative claims, causal exclusion, non-exposure, control suppression, and prevented exposure; progressive analytical availability without evidence inflation; authorization-safe restricted analysis; non-rewriting retrospective revision; and clean separation of passive monitoring from explicitly enabled active control.

## Progressive analytical availability handoff

Phase 004 establishes functional evidence-maturity horizons without choosing service topology or performance budgets:

1. **immediate operational validation**;
2. **enriched health evaluation**;
3. **investigative/RCA reasoning**;
4. **retrospective/post-operations review**.

For RCA:

**candidate/proposed claims → early supported/weakened/unresolved evaluation → deeper investigative RCA → retrospective/confirmation review**.

For control/exposure:

**readiness/output facts → gate decision state → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

Ungated production remains independent from passive-monitoring availability. Explicitly gated paths may require stronger/faster control-path availability. Exact source latency, SLO, performance, and architecture decisions remain deferred.

## Phase boundaries retained for later phases

Phase 004 intentionally does **not** decide:

- source/actor authority, conflict resolution, or capability assignment — Phase 005;
- final health/quality/statistical vocabularies or result-timing objectives — Phase 006;
- detailed Lineage/Investigation/Impact/safeguard/gate operational policy — Phase 007;
- Explanation UX and deterministic/generative behavior — Phase 008;
- actual Databricks/GitHub/DQX/Metric View/governance/consumer/control integration evidence and latency — Phase 009;
- technical architecture, orchestration/control implementation, storage, IAM, causal engine, fast-path/asynchronous topology, or performance budgets — Phase 010.

## Phase exit

**Phase 004 exit gate is satisfied. Phase 004 is complete with REF-001–REF-030 accepted.**

**Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is next and has not started.**
