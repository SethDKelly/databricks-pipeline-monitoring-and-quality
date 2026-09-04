# CKR-H Execution Review — Integration, Source Authority & Evidence Availability

**Status:** IN EXECUTION — CANDIDATE REVIEW

**Reviewed:** 2026-09-04

## Objective

Canonicalize INTG-001–INTG-270 without turning source availability into authority, vendor capability into product truth, timestamp proximity into identity/association, partial coverage into strong negatives, lineage into exposure/Impact, source replay into actual retained communication, or Phase 009 integration findings into Phase 010 architecture decisions.

## Exact scope

CKR-H owns only the accepted Phase 009 INTG family:

- INTG-001–022 — integration contract vocabulary/source roles/capability matrix;
- INTG-023–050 — identity/scope/governance/authority/authorization sources;
- INTG-051–083 — change/deployment/execution/version/runtime evidence;
- INTG-084–119 — health/schema/metrics/expectations/Baselines/reconciliation evidence;
- INTG-120–153 — Lineage/consumer use/exposure/effect/Impact evidence;
- INTG-154–200 — Investigation/causality/Safeguard/Gate/control evidence;
- INTG-201–238 — Explanation/historical replay/basis inspection/disclosure sources;
- INTG-239–270 — cross-source coverage/latency/retention/cost/consolidated feasibility.

No INTG-271, new concept, new stable family or architecture contract is accepted by this migration.

## Candidate topology

The eight bounded canonical candidates are under `docs/canonical/contracts/integration/`:

1. `integration-contract-vocabulary.md`
2. `identity-governance-authority-sources.md`
3. `change-deployment-runtime-evidence.md`
4. `health-quality-measurement-sources.md`
5. `lineage-exposure-impact-sources.md`
6. `investigation-causality-control-sources.md`
7. `explanation-replay-disclosure-sources.md`
8. `cross-source-feasibility-retention-cost.md`

During candidate review they are explicitly `CANDIDATE / NOT CURRENT AUTHORITY`; Phase 009 remains the current INTG owner.

## Semantic conservation

[`ckr_h_semantic_conservation_matrix.md`](ckr_h_semantic_conservation_matrix.md) preserves the accepted boundaries, especially:

- available ≠ relevant ≠ eligible ≠ authoritative ≠ sufficient ≠ authorized;
- source-local identity ≠ ecosystem Entity Identity;
- timestamp proximity ≠ exact cross-system association;
- positive support ≠ negative-evidence capability;
- no returned record ≠ absence;
- current availability ≠ historical replay;
- late/backfilled evidence now ≠ evidence available at an earlier K;
- common-derived endpoints ≠ independent corroboration;
- fallback availability ≠ inherited authority;
- integration failure ≠ monitored-product negative;
- GitHub Actions success ≠ Databricks activation;
- configured dependency ≠ actual precedence ≠ waiting ≠ version consumption;
- execution success ≠ output existence ≠ freshness/currentness ≠ health;
- captured lineage event ≠ encounter ≠ exposure;
- exposure ≠ effect ≠ consequence ≠ causal attribution;
- localization ≠ Causal Claim;
- Safeguard enforcement ≠ prevented exposure;
- HOLD/ADMIT ≠ execution outcome;
- historical source state ≠ as-known-at-cut Explanation ≠ retained actual communication ≠ current retrospective Explanation;
- support classification/latency/quota/cost ≠ truth or authority.

No A4 semantic change is intended. Phase 009 residual gaps remain architecture inputs, not reopened semantic questions.

## Deterministic protection

CKR-H adds:

- `scripts/agentic/validate_ckr_h_integration.py` for exact stable-ID/topology/authority/provenance/conservation checks;
- `fixtures/ckr_h_integration_scenarios.yaml` for migration-focused source-capability scenarios;
- conformance runner and fixture-catalog registration;
- negative controls for omitted IDs, partial topology, authority/availability collapse, timestamp-join inference, negative-evidence dilution, Lineage→exposure collapse, historical-view collapse and premature ARCH ownership.

## Candidate gate

Candidate review may advance to atomic cutover only after the exact branch head passes both:

- Agentic conformance;
- Documentation consistency.

Until then:

- `stable_family.INTG` remains `candidate_ready` once candidate wiring is committed;
- Phase 009 remains authoritative;
- canonical candidate files remain non-authoritative;
- ARCH remains legacy-authoritative under CKR-I;
- Implementation 001-A remains blocked until CKR-K.

## Atomic-cutover rule

After a green candidate head, one atomic cutover must:

1. move `stable_family.INTG` from `candidate_ready` to `canonicalized`;
2. promote all eight target resources together to `CANONICAL CURRENT AUTHORITY`;
3. reclassify Phase 009 as design history/provenance for INTG;
4. update current routing to the canonical integration root;
5. leave ARCH untouched and CKR-H `IN EXECUTION` until the cutover head itself is green.

Partial cutover or dual current authority is invalid.

## Closure rule

After a green cutover head, closure synchronization may mark CKR-H complete/accepted and CKR-I next/ready. CKR-I must remain unstarted until explicitly selected by the human. Closure and final evidence-only heads must also pass the normal exact-head gates before merge.

## Current decision

**CKR-H is in candidate review. No authority cutover has occurred yet.**
