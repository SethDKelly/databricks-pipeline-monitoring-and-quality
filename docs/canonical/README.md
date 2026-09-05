# DMTZ Canonical Knowledge

**Authority state:** CANONICALIZATION COMPLETE — CKR EXIT ACCEPTED

This directory contains DMTZ **current accepted meaning** for all ownership-inventory records/families that CKR promoted to `canonicalized`. The ownership inventory lifecycle is `ckr_complete`; substantive canonical resources declare `CANONICAL CURRENT AUTHORITY`.

Semantic authority changes only through:

- [`../canonical_knowledge_retrofit/authority_model.md`](../canonical_knowledge_retrofit/authority_model.md)
- [`../canonical_knowledge_retrofit/migration_contract.md`](../canonical_knowledge_retrofit/migration_contract.md)
- [`../canonical_knowledge_retrofit/canonical_ownership_inventory.json`](../canonical_knowledge_retrofit/canonical_ownership_inventory.json)

## Current canonical scope

Canonical owners cover foundation/glossary, all 24 accepted concepts, SYN-001–035, shared authority vocabulary, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and **ARCH-001–500 plus the frozen reference architecture**.

Phase 001–010 material is design history/provenance for migrated meanings. Phase 010 remains the detailed design/review/atomic-contract provenance corpus for architecture, not an alternate current owner.

## Knowledge families

- [`concepts/`](concepts/) — independently understandable accepted concepts;
- [`contracts/`](contracts/) — cross-cutting/domain/stable-ID contracts;
- [`policies/`](policies/) — normative policy rules;
- [`invariants/`](invariants/) — durable semantic separations/non-collapse rules;
- [`authority/`](authority/) — authority, authorization, governance and disclosure boundaries;
- [`experience/`](experience/) — questioning, Explanation and user-facing contracts;
- [`architecture/`](architecture/) — current accepted technical architecture owners;
- [`reference/`](reference/) — terminology and compact reference surfaces.

## Lookup rule

Answer current semantic questions from the substantive canonical owner selected by the completed ownership inventory. Directory indexes are routing surfaces rather than additional truth owners.

For a known stable ID, use `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain the deterministic canonical locator `owner_path::STABLE-ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

Consult design history when provenance, rationale, historical reconstruction or change analysis is actually requested. Search order, recency, OKF summaries, vendor guidance and model/tool memory do not establish semantic authority.
