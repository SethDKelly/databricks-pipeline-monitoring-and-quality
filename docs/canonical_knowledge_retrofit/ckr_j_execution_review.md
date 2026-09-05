# CKR-J Execution Review — OKF, Stable References, Agent Routing & Drift Enforcement

**Status:** IN EXECUTION — ROUTING CUTOVER VALIDATION

**Reviewed:** 2026-09-04

## Objective

Finish the CKR routing layer after all semantic families are canonicalized: make current-truth OKF routes canonical-first, make every accepted stable ID deterministically resolve to its canonical owner, separate history discovery from default resolution, align shared agent workflows, and fail conformance when those routing guarantees drift.

CKR-J changes routing/discovery/drift enforcement only. It does not change DMTZ concepts, stable-ID meaning, architecture, evidence semantics, product behavior or implementation state.

## Accepted result under cutover validation

The activated routing design is:

`accepted stable range + CKR family target_documents + exactly one accepted canonical stable definition → owner_path::STABLE-ID`.

Canonical stable-definition coverage is **1,237/1,237** while preserving all prior CKR topology:

- **737** definition headings across SYN/REF/AUTH/HLTH/OPS/EXPL/INTG;
- **416** ARCH `Stable ID index` members across seven compact architecture segments;
- **84** ARCH named stable-contract list members in the runtime/health/Lineage/Impact segment.

No canonical semantic document was expanded merely to satisfy routing. In particular, CKR-J does not manufacture 500 ARCH headings or restore the Phase 010 one-file-per-ID structure.

## Live routing cutover

The atomic cutover activates:

- `ckr_j_routing_manifest.json` as the machine-checkable routing projection;
- `stable_id_registry.json` canonical resolution metadata while preserving all accepted ranges;
- `resolve_stable_id.py` default canonical-only resolution with explicit `--history` provenance mode;
- seven canonical-first semantic OKF domain routes;
- a compact stable-reference OKF project route;
- canonical BODY-LINK impact review in `knowledge_impact.py`;
- shared resolve-context / resolve-contract / update-traceability routing;
- canonical-owner validation for operational agent-facing stable-ID citations.

The registry, manifest, resolver and OKF bundle remain derived routing machinery and cannot own, strengthen, weaken or reinterpret DMTZ semantics.

## Candidate diagnostic history

### Initial candidate diagnostic

Head `ca2be7f33cf8cb68f9b51b34d2c3368b68af1108`:

- Documentation consistency **#282 — SUCCESS** (run `33936494780`);
- Agentic conformance **#164 — FAILURE** (run `33936494715`).

All non-J checks and all 12 CKR-J guards passed. CKR-J stable coverage was 737/1,237 because the first validator assumed every canonical definition was a Markdown heading. The 500 missing IDs were ARCH and no semantic document was changed.

### Second candidate diagnostic

Head `2ace9b9b4a580651d3febe0bf6fee9572ec67b7b`:

- Documentation consistency **#288 — SUCCESS** (run `33936668827`);
- Agentic conformance **#170 — FAILURE** (run `33936668820`).

Coverage became 1,153/1,237 = 737 headings + 416 ARCH index members. The remaining 84 were exactly ARCH-191–ARCH-274, represented by the accepted runtime segment's named stable-contract lists. All other conformance and all 12 CKR-J guards passed.

### Corrected candidate gate

Head `8ed987651307114f98af113675a898ec80a92493` recognized all three accepted canonical definition forms and changed no semantic owner/content. It passed:

- Agentic conformance **#174 — SUCCESS** (run `33936778055`);
- Documentation consistency **#292 — SUCCESS** (run `33936778058`).

This authorized the atomic routing cutover.

## Deterministic protection

`validate_ckr_j_routing.py` protects exact 1,237-ID resolution, definition-form counts, all families remaining canonicalized, canonical-first seven-domain OKF routing, project routes, agent routing surfaces, separate history mode and fixture identity.

`test_ckr_j_routing_guards.py` adds **12 state-aware negative controls** that fail on no-op mutations and remain meaningful both before and after activation.

The shared conformance suite continues to protect prior CKR semantic families, context budgets, OKF structure, secrets/security and earlier negative controls.

## Cutover gate

The activated routing tree must pass exact-head Agentic conformance and Documentation consistency before CKR-J can close. CKR-J remains `IN EXECUTION` during this validation.

## Exit boundary

CKR-K remains planned/unstarted. Implementation 001-A remains blocked until CKR-K accepts the complete retrofit.
