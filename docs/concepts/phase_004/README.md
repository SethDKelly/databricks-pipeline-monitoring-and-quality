# Phase 004 — Evidence, Time, and Causality Refinement

**Status:** Active — Groups 01–02 accepted; Group 03 next

## Purpose

Phase 004 refines the evidence, temporal, and causal standards that Phase 003 intentionally left abstract. It does **not** replace the 23 accepted concepts or SYN-001–SYN-035, and it does not select storage, orchestration, IAM, graph, DQ, statistical, LLM, or other technical architecture.

Phase 003 established which truths must remain separate. Phase 004 establishes what evidence is adequate to support those truths, how historical evidence cuts are evaluated precisely, how results can mature as evidence arrives, and what standards govern high-consequence causal statuses.

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
- remains implementation-neutral.

Refinement artifacts use `REF-###` identifiers. These identifiers are **not new synchronizations** and do not extend the Phase 003 SYN sequence.

## Review groups

| Group | Theme | Primary questions | Status |
|---|---|---|---|
| 01 | Evidence Sufficiency, Coverage & Negative Evidence | applicability; bounded coverage; opportunity-to-observe; absence/exclusion; corroboration/conflict; conclusion-specific sufficiency | **Accepted** |
| 02 | Event/Effective Time, Knowledge Cut & Correction | evidence availability; exact `as-known` semantics; progressive analytical maturity; late evidence; correction/supersession; `not known by cutoff`; dependent reassessment/reopen | **Accepted** |
| 03 | Causal Epistemics, Confirmation & Multiple Contributors | claim-status vocabulary; support/contradiction; confirmation standard; review authority boundary; challenge after confirmation; progressive RCA maturity | **Next** |
| 04 | Exposure, Consumption, Readiness & Control Evidence | exposure/non-exposure proof; gate readiness; hold/admit enforcement; safeguard enforcement/prevention evidence | Planned |
| 05 | Phase 004 Consolidation / Exit Review | cross-domain application; retained vs reconstructed state; scenario stress test; later-phase handoff | Planned |

## Accepted Group 01 results

Group 01 is documented in [`01_evidence_sufficiency_and_coverage/README.md`](01_evidence_sufficiency_and_coverage/README.md) and accepts:

- **REF-001 — Evidence Applicability and Proposition Binding**;
- **REF-002 — Coverage Profile and Opportunity to Observe**;
- **REF-003 — Negative, Absence, and Exclusion Evidence**;
- **REF-004 — Corroboration, Conflict, and Evidence Independence**;
- **REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation**.

Key results:

- evidence is not globally `good` or `bad`; sufficiency is relative to a defined proposition, context, time, and decision standard;
- an evidence item must be applicable to the proposition before it can support or contradict it;
- coverage is bounded and multidimensional rather than a universal percentage;
- negative/absence/exclusion conclusions require an adequate opportunity to observe plus sufficient bounded coverage;
- missing telemetry, unavailable queries, and unauthorized evidence are not negative evidence;
- duplicated or commonly derived evidence cannot be counted as independent corroboration merely because it appears in several systems;
- conflicts remain explicit until an accepted authority/resolution rule applies;
- no universal numeric confidence/trust score is introduced;
- evidence sufficiency does not itself grant disclosure authorization or production-control authority.

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
- `as-known` cuts use evidence known to the framework by the cutoff, not facts first retrieved later;
- `known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are separate propositions with different evidence requirements;
- monitoring/reasoning may mature progressively from immediate operational validation through enriched health, RCA, and post-operations review;
- early results remain narrowly scoped and cannot be promoted into broader health/causal conclusions merely because slower evidence is pending;
- late evidence, source correction, independent conflict, reinterpretation, and later authority resolution remain distinct;
- dependent reevaluation is basis/materiality driven; closed Investigations can become review/reopen candidates without automatic reopening;
- actual historical state requires evidence it existed then; otherwise historical answers are replay-derived/reconstructed;
- exact product latency objectives are deferred, but Phases 006/009/010/011 must define them by health output, evidence source, architecture, and MVP acceptance criteria.

## Progressive analytical availability handoff

Phase 004 establishes functional evidence-maturity horizons but does not choose service topology or performance budgets:

1. immediate operational validation;
2. enriched health evaluation;
3. investigative/RCA reasoning;
4. retrospective/post-operations review.

Later work must define how quickly each class should become available and which evidence sources are realistically capable of supporting those targets. Passive monitoring remains out-of-band/non-blocking for ungated production regardless of monitoring-result latency targets.

## Phase boundaries

Phase 004 may refine evidence standards used by Observation, Assessment, Causal Claim, Impact, Execution Gate, Propagation Safeguard, historical replay, and Explanation. It must not:

- invent source-authority rules that belong in Phase 005;
- invent statistical/anomaly models that belong in Phase 006;
- select Lineage/control implementations that belong in Phase 007/010;
- decide Explanation UX/LLM behavior that belongs in Phase 008/010;
- silently require production-repository changes or make passive monitoring blocking.

## Phase exit direction

Phase 004 exits when the project has explicit, internally consistent standards for evidence applicability/coverage/sufficiency, temporal evidence availability and historical knowledge cuts/corrections, causal epistemic transitions/confirmation, exposure/readiness/control proof, and retained-versus-reconstructed historical conclusions—without collapsing source authority, authorization, health, causality, latency objectives, or architecture.

**Group 03 — Causal Epistemics, Confirmation & Multiple Contributors is next and has not started.**
