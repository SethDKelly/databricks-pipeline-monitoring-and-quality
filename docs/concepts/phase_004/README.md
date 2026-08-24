# Phase 004 — Evidence, Time, and Causality Refinement

**Status:** Active — Group 01 accepted; Group 02 next

## Purpose

Phase 004 refines the evidence, temporal, and causal standards that Phase 003 intentionally left abstract. It does **not** replace the 23 accepted concepts or SYN-001–SYN-035, and it does not select storage, orchestration, IAM, graph, DQ, statistical, LLM, or other technical architecture.

Phase 003 established which truths must remain separate. Phase 004 establishes what evidence is adequate to support those truths, how historical evidence cuts are evaluated precisely, and what standards govern high-consequence causal statuses.

## Phase method

A Phase 004 refinement:

- applies to one or more accepted concepts/synchronizations without becoming a new truth owner unless a genuine concept gap is discovered;
- names the proposition/conclusion being evaluated;
- distinguishes evidence applicability from evidence coverage and from conclusion sufficiency;
- preserves supporting, contradicting, missing, restricted, late, corrected, duplicated, and derived evidence explicitly;
- states event/effective-time and recorded/knowledge-time behavior where relevant;
- never converts missing telemetry into a reassuring negative;
- never converts an evidence-strength rule into source authority or user authorization unless those semantics are explicitly in scope;
- remains implementation-neutral.

Refinement artifacts use `REF-###` identifiers. These identifiers are **not new synchronizations** and do not extend the Phase 003 SYN sequence.

## Review groups

| Group | Theme | Primary questions | Status |
|---|---|---|---|
| 01 | Evidence Sufficiency, Coverage & Negative Evidence | applicability; bounded coverage; opportunity-to-observe; absence/exclusion; corroboration/conflict; conclusion-specific sufficiency | **Accepted** |
| 02 | Event/Effective Time, Knowledge Cut & Correction | exact `as-known` semantics; late evidence; correction/supersession; `not known by cutoff`; dependent reassessment/reopen | **Next** |
| 03 | Causal Epistemics, Confirmation & Multiple Contributors | claim-status vocabulary; support/contradiction; confirmation standard; review authority boundary; challenge after confirmation | Planned |
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

## Phase boundaries

Phase 004 may refine evidence standards used by Observation, Assessment, Causal Claim, Impact, Execution Gate, Propagation Safeguard, historical replay, and Explanation. It must not:

- invent source-authority rules that belong in Phase 005;
- invent statistical/anomaly models that belong in Phase 006;
- select Lineage/control implementations that belong in Phase 007/010;
- decide Explanation UX/LLM behavior that belongs in Phase 008/010;
- silently require production-repository changes or make passive monitoring blocking.

## Phase exit direction

Phase 004 exits when the project has explicit, internally consistent standards for evidence applicability/coverage/sufficiency, historical knowledge cuts and corrections, causal epistemic transitions/confirmation, exposure/readiness/control proof, and retained-versus-reconstructed historical conclusions—without collapsing source authority, authorization, health, causality, or architecture.

**Group 02 — Event/Effective Time, Knowledge Cut & Correction is next and has not started.**
