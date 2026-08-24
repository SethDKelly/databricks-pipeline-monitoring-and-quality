# Phase 004 — Evidence, Time, and Causality Refinement

**Status:** Active — Groups 01–04 accepted; Group 05 next

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
| 05 | Phase 004 Consolidation / Exit Review | cross-domain application; retained vs reconstructed state; scenario stress test; later-phase handoff | **Next** |

## Accepted Group 01 results

Group 01 is documented in [`01_evidence_sufficiency_and_coverage/README.md`](01_evidence_sufficiency_and_coverage/README.md) and accepts:

- **REF-001 — Evidence Applicability and Proposition Binding**;
- **REF-002 — Coverage Profile and Opportunity to Observe**;
- **REF-003 — Negative, Absence, and Exclusion Evidence**;
- **REF-004 — Corroboration, Conflict, and Evidence Independence**;
- **REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation**.

Key results:

- evidence is not globally `good` or `bad`; sufficiency is relative to a defined proposition, context, time, and decision standard;
- evidence must be applicable before it can support/contradict a proposition;
- coverage is bounded and multidimensional;
- negative/absence/exclusion conclusions require an adequate opportunity to observe plus sufficient bounded coverage;
- missing telemetry, unavailable queries, and unauthorized evidence are not negative evidence;
- duplicated/common-source evidence does not become independent corroboration;
- conflicts remain explicit until an accepted authority/resolution rule applies;
- no universal numeric confidence/trust score is introduced;
- evidence sufficiency does not itself grant disclosure or production-control authority.

## Accepted Group 02 results

Group 02 is documented in [`02_event_time_knowledge_cut_and_correction/README.md`](02_event_time_knowledge_cut_and_correction/README.md) and accepts:

- **REF-006 — Temporal Coordinates and Evidence Availability**;
- **REF-007 — Historical Knowledge-Cut Eligibility**;
- **REF-008 — Known By, Learned After, and Not Known By Claims**;
- **REF-009 — Progressive Evidence Availability and Analytical Maturity**;
- **REF-010 — Late Evidence, Correction, Conflict, and Reinterpretation**;
- **REF-011 — Dependent Re-evaluation and Investigation Reopen Materiality**;
- **REF-012 — Actual Retained State versus Reconstructible Historical State**.

Key results:

- event/effective time, source production/availability, framework collection/knowledge, derived evaluation, and correction time remain distinct where material;
- source evidence being available does not mean the framework knew it;
- `as-known` cuts use evidence known to the framework by the cutoff;
- `known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are separate propositions;
- monitoring/reasoning may mature progressively from immediate operational validation through enriched health, RCA, and post-operations review;
- early results remain narrowly scoped and cannot be promoted into broader health/causal conclusions merely because slower evidence is pending;
- late evidence, source correction, independent conflict, reinterpretation, and later authority resolution remain distinct;
- dependent reevaluation is basis/materiality driven; closed Investigations can become review/reopen candidates without automatic reopening;
- actual historical state requires evidence it existed then; otherwise historical answers are replay-derived/reconstructed;
- exact product latency objectives remain deferred to Phases 006/009/010/011.

## Accepted Group 03 results

Group 03 is documented in [`03_causal_epistemics_confirmation/README.md`](03_causal_epistemics_confirmation/README.md) and accepts:

- **REF-013 — Causal Proposition and Role Binding**;
- **REF-014 — Causal Epistemic Status Vocabulary and Transition Semantics**;
- **REF-015 — Causal Support, Contradiction, and Evidence-Dimension Evaluation**;
- **REF-016 — Material Alternatives and Causal Discrimination**;
- **REF-017 — Confirmation Evidence Gate and Authority Separation**;
- **REF-018 — Multiple Contributors and Qualitative Causal Roles**;
- **REF-019 — Progressive RCA Maturity and Fast-Path Causal Communication**;
- **REF-020 — Challenge, Reversal, and Historical Preservation After Confirmation**.

Key results:

- causal propositions bind cause, effect, role, context/time, and material mechanism/transmission assumptions;
- accepted epistemic vocabulary is `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, and `confirmed`;
- `unresolved` means substantive evaluation remains non-discriminating/insufficient; `rejected` requires sufficient contradiction/exclusion evidence;
- support/contradiction is multidimensional rather than a universal confidence score;
- stronger causal status considers a bounded material alternative set; compatible contributors need not be excluded;
- `confirmed` is a separate claim-class evidence gate, not `strongly supported` or `leading hypothesis`;
- confirmation requires an explicit standard/profile, required evidence dimensions, contradiction/alternative review, adequate negative-evidence coverage where relied upon, resolved confirmation authority/capability, and provenance-bearing confirmation action;
- Phase 004 does not assign confirmation authority;
- multiple contributors can coexist; qualitative roles do not imply percentage attribution and `primary` requires comparative evidence;
- RCA may mature progressively without latency-driven status inflation;
- confirmed claims remain challengeable while historical confirmation stays reconstructable.

## Accepted Group 04 results

Group 04 is documented in [`04_exposure_consumption_readiness_control/README.md`](04_exposure_consumption_readiness_control/README.md) and accepts:

- **REF-021 — Exposure Proposition and Encounter Binding**;
- **REF-022 — Positive Exposure / Consumption Evidence**;
- **REF-023 — Non-Exposure and Negative Consumption Coverage**;
- **REF-024 — Dependency Readiness Criterion Decomposition**;
- **REF-025 — Execution Gate Decision, Enforcement, and Actual Execution**;
- **REF-026 — Gate Enforcement Evidence and Degraded Control State**;
- **REF-027 — Propagation Safeguard Activation and Enforcement Evidence**;
- **REF-028 — Prevented Exposure Evidence Standard**;
- **REF-029 — Control Telemetry, Fallback, and Unavailable-State Evidence**;
- **REF-030 — Control-Effect Causality and Retrospective Revision**.

Key results:

- exposure requires an encounter proposition bound to the affected state/version/window, consumer, relationship, encounter mode, and consumer opportunity;
- actual encounter evidence is required for positive exposure; downstream timing/activity alone is insufficient;
- `not exposed` requires sufficient negative consumption/path coverage;
- no encounter opportunity, no encounter, safe-version encounter, unknown-version encounter, unavailable/restricted evidence, and affected-state encounter remain distinct;
- readiness is relative to an explicit criterion and may decompose execution completion, output existence, version/currentness, freshness, publication availability, and named quality predicates;
- successful upstream execution is not global readiness;
- readiness uncertainty may drive configured fallback but fallback does not turn the prerequisite into `ready`;
- gate decision, gate enforcement, and actual downstream execution are separate evidence claims;
- a reliable downstream run during an applicable unoverridden hold contradicts full hold enforcement, while an admitted opportunity that does not run does not by itself prove admission failed;
- configured/enabled gate state does not prove opportunity-specific enforcement;
- safeguard proposal/configuration/request is not enforced active state; safeguard enforcement is boundary/scope/time specific;
- prevented exposure requires materially operative safeguard enforcement plus negative-consumption/version and alternate-path coverage, not merely `safeguard active + consumer not exposed`;
- blocking suspect state does not imply fresh/healthy delivery;
- configured fallback is not proof actual fallback behavior occurred;
- control-effect causal claims use REF-013–REF-020, and late control/consumption evidence revises retrospective conclusions without rewriting historical actions.

## Progressive analytical availability handoff

Phase 004 establishes functional evidence-maturity horizons but does not choose service topology or performance budgets:

1. immediate operational validation;
2. enriched health evaluation;
3. investigative/RCA reasoning;
4. retrospective/post-operations review.

For RCA:

**candidate/proposed claims → early supported/weakened/unresolved evaluation → deeper investigative RCA → retrospective/confirmation review**.

For control/exposure:

**readiness/output facts → gate decision state → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

Some explicitly gated decisions may need stronger and faster evidence/control-path availability than ordinary passive monitoring. Exact availability targets and architecture remain deferred to Phases 006/009/010/011.

## Phase boundaries

Phase 004 may refine evidence standards used by Observation, Assessment, Causal Claim, Impact, Execution Gate, Propagation Safeguard, historical replay, and Explanation. It must not:

- invent source/actor authority rules that belong in Phase 005;
- grant causal-confirmation, gate-control, or safeguard authority by role/title/process identity;
- invent statistical/anomaly models that belong in Phase 006;
- select causal algorithms, Lineage/control implementations, scheduler/orchestrator, quarantine technology, or service topology;
- decide final gate timeout/fallback/override policy that belongs in later governance/control refinement;
- decide Explanation UX/LLM behavior that belongs in Phase 008/010;
- silently require production-repository changes or make passive monitoring blocking.

## Phase exit direction

Phase 004 exits when the project has explicit, internally consistent standards for evidence applicability/coverage/sufficiency, temporal evidence availability and historical knowledge cuts/corrections, causal epistemic transitions/confirmation, exposure/readiness/control proof, and retained-versus-reconstructed historical conclusions—without collapsing source authority, authorization, health, causality, latency objectives, control policy, or architecture.

**Group 05 — Consolidation / Exit Review is next and has not started.**
