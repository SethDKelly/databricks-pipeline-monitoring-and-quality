# CKR-G Execution Review — Questioning, Explanation & Experience Contracts

**Status:** IN EXECUTION — ATOMIC CUTOVER COMPLETE / CUTOVER VALIDATION PENDING

**Reviewed:** 2026-09-04

## Objective

Canonicalize EXPL-001–EXPL-160 without turning question/answer composition into an independent truth model, weakening source-domain epistemic states, conflating current disclosure with truth, rewriting prior communication, or importing INTG/ARCH ownership.

## Accepted topology

CKR-G maps the accepted Phase 008 range into eight bounded experience resources:

- EXPL-001–012 — question identity, scope and temporal perspective;
- EXPL-013–028 — answer structure and basis traceability;
- EXPL-029–049 — health/change/execution question semantics;
- EXPL-050–080 — Investigation/causality/Impact/control/governance question semantics;
- EXPL-081–100 — uncertainty/conflict/negative-claim epistemic language;
- EXPL-101–120 — audience authorization, safe abstraction and basis inspection;
- EXPL-121–140 — progressive maturity, refresh and retention;
- EXPL-141–160 — historical/comparative Explanation and exit.

The atomic cutover promotes these eight resources to current authority, moves EXPL to `canonicalized`, and reclassifies Phase 008 as design history/provenance. No EXPL-161, new concept, new stable family or architecture decision is introduced.

## Semantic conservation

The accepted [`ckr_g_semantic_conservation_matrix.md`](ckr_g_semantic_conservation_matrix.md) preserves question ≠ truth/authorization, answer statement ≠ independent truth, source-owner/epistemic preservation, explicit cross-concept join logic, sibling independence, exact negative-evidence burdens, safe abstraction that cannot strengthen truth, retained communication versus reconstruction, and historical source/as-known/retained/current-retrospective separation.

No A4 semantic change was required.

## Deterministic protection

`scripts/agentic/validate_ckr_g_experience.py` requires exact EXPL-001–EXPL-160 heading coverage, the eight-document topology, matching authority markers, Phase 008 provenance, prior canonical cutovers, later-family isolation and core semantic-conservation boundaries.

`fixtures/ckr_g_experience_scenarios.yaml` adds **CKRG-01–CKRG-48**. The conformance guard suite contains **43 negative controls**, including omission, partial topology, question/truth/authorization collapse, sibling-state propagation, disclosure overstatement, historical-view collapse and premature INTG ownership.

## Validation history

### Initial candidate diagnostics

Candidate head `56a705898297add798300f508ab6a95bf0a53653` passed Documentation consistency #258 but exposed a heading-guard false positive in Agentic conformance #140. The validator was corrected to distinguish textual `no EXPL-161` statements from an actual unaccepted heading.

Head `67da37b0085d62fa43d7f2d7ed4da6919799878a` passed Documentation consistency #259 and exposed one missing validator assertion through the sibling-state negative control in Agentic conformance #141. The required sibling-independence boundary was added to the validator.

These were conformance-guard defects only; Phase 008 remained authoritative throughout candidate review and no product semantic change was made.

### Candidate gate

Final candidate head `c7330738ec70f3b45afa90efbdafb695be418c1c` passed:

- Agentic conformance **#142 — SUCCESS** (run ID `33874091270`);
- Documentation consistency **#260 — SUCCESS** (run ID `33874091336`).

This authorized atomic EXPL cutover.

## Scope isolation

INTG-001–INTG-270 and ARCH-001–ARCH-500 remain legacy-authoritative until CKR-H/I. CKR-G references integration/architecture requirements but selects no source mapping, retrieval/persistence architecture, LLM implementation, UI, IAM product or technical placement.

## Implementation gate

Implementation 001-A remains blocked until CKR-K. CKR-G remains IN EXECUTION until cutover and closure heads pass the normal repository gates.
