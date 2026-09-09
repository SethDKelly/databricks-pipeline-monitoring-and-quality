# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-K COMPLETE / ACCEPTED — CKR EXIT ACCEPTED

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: COMPLETE / ACCEPTED.**
- **CKR-D — Evidence, Time, Authority & Governance: COMPLETE / ACCEPTED.**
- **CKR-E — Health, Quality, Metrics & Timing: COMPLETE / ACCEPTED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: COMPLETE / ACCEPTED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: COMPLETE / ACCEPTED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: COMPLETE / ACCEPTED.**
- **CKR-I — Technical Architecture: COMPLETE / ACCEPTED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: COMPLETE / ACCEPTED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: COMPLETE / ACCEPTED.**

## Accepted canonical semantic scope

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160, INTG-001–INTG-270 and ARCH-001–ARCH-500 resolve to canonical owners. The historical Phase 001–010 corpus remains design provenance under `docs/history/` after DPTN-B.

## Accepted routing and reference layer

- exact accepted stable IDs resolve deterministically through `scripts/agentic/resolve_stable_id.py <ID>`;
- stable locator is `owner_path::STABLE-ID`;
- stable-definition coverage is **1,237/1,237**: 737 definition headings, 416 ARCH stable-ID index members and 84 ARCH stable-contract list members;
- `--history` performs separate provenance occurrence discovery and never competes with current ownership;
- routing manifests, registries, resolvers and OKF remain derived routing machinery rather than semantic authority.

## CKR-K exit result

CKR-K validated **34/34** record-level entries, **24/24** concepts, all **8** stable families, all **1,237** stable IDs, **9/9** architecture inventory records, seven canonical-first domain routes, accepted CKR-A–J review evidence, bounded provenance/history preservation and representative current-truth locality. No unreviewed dual-authority condition remained at CKR exit.

The ownership inventory lifecycle remains `ckr_complete`. This is retrofit lifecycle metadata only; DPTN path normalization does not reopen CKR semantics.

See [`ckr_k_consolidation_provenance_matrix.md`](ckr_k_consolidation_provenance_matrix.md) and [`ckr_k_execution_review.md`](ckr_k_execution_review.md).

## Post-CKR topology handoff

DPTN is active. The CKR ownership inventory remains the semantic-owner ledger while DPTN changes physical paths only.

- **DPTN-A–C — COMPLETE / ACCEPTED**;
- **DPTN-D — NEXT / READY / NOT STARTED**;
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-B established `docs/history/` as provenance-only and relocated history. DPTN-C then executed MOVE-007 through MOVE-014: the eight substantive semantic roots moved from `docs/canonical/<family>/` to first-class `docs/<family>/` paths through an atomic physical-tree + ownership-inventory rebind. Accepted meaning and stable IDs did not change.

The ownership inventory now selects those normalized first-class paths. Any legacy `docs/canonical/<family>` redirect is compatibility only and cannot become a second current owner. `docs/canonical/README.md` remains an orientation surface pending DPTN-E.

Current DPTN authority: [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md). Current history role: [`../history/README.md`](../history/README.md).
