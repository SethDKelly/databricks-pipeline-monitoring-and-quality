# CKR Documentation Authority Model

**Status:** ACCEPTED — CKR-A AUTHORITY / PHYSICAL ROUTING REBOUND DPTN-F

## 1. Purpose

DMTZ separates two legitimate documentation purposes:

1. **current semantic knowledge** — what DMTZ means now;
2. **design history** — how and why DMTZ arrived there.

Neither layer replaces the other. DPTN changes their physical topology without changing this authority model.

## 2. Authority layers

### Layer 1 — Current semantic knowledge

For every `canonicalized` record, the sole current semantic owner is the first-class path selected by `canonical_ownership_inventory.json`. Current semantic owner roots are `docs/concepts/`, `docs/architecture/`, `docs/authority/`, `docs/contracts/`, `docs/experience/`, `docs/invariants/`, `docs/policies/`, and `docs/reference/`.

Current semantic knowledge may own accepted concept definitions, policy and authority boundaries, invariants, stable-ID/domain contracts, user/experience contracts, technical architecture contracts, and canonical terminology/reference mappings.

Current resources must be independently usable for the question they own. They may cite history for provenance but may not require chronological reconstruction to obtain current meaning.

### Layer 2 — Design history and provenance

`docs/history/` preserves phase working records, original specifications, refinements, decisions, scenario/exit reviews, handoffs, gap registers, completed retrofit/foundation evidence and superseded formulations.

Design history explains origin, rationale, evolution, alternatives and historical state. It is not deleted merely because current meaning has a first-class owner, and it never competes with the current owner selected by the inventory.

### Layer 3 — Routing and operational guidance

`docs/index.md`, generated `knowledge/`, `AGENTS.md`, `.agents/skills/`, Cursor/Claude/Codex adapters and implementation routing help users and tools find the correct authority. They do not become semantic owners.

`knowledge/` is therefore an OKF v0.2 compatibility projection over the authority model—not the authority model itself.

## 3. Precedence

The accepted CKR migration states remain `legacy_authoritative`, `candidate_ready`, `canonicalized`, and `history_only`. CKR is complete, so current DMTZ semantic records are now resolved through their `canonicalized` inventory state.

For a `canonicalized` record:

1. inventory-selected first-class current owner under `docs/<family>/`;
2. accepted executable contracts/code/tests when implementation later exists and is explicitly subordinate to documentation semantics;
3. `docs/history/` provenance;
4. routing/generated-knowledge summaries.

Historical sources cease to be current semantic owners at cutover. Compatibility redirects under `docs/canonical/<family>/`, while they remain, are not an authority layer.

## 4. No dual-current-authority invariant

For every semantic record:

> **Exactly one authority state determines current ownership.**

The repository may contain many descriptions, citations, redirects and historical definitions, but only one accepted current owner is permitted after canonicalization. The presence of the same stable ID or concept name in multiple files does not imply multiple authority.

## 5. Current question routing

For normal current questions:

- `What is Lineage?` → the inventory-selected current Lineage concept under `docs/concepts/`;
- `What does OPS-005 require?` → `python3 scripts/agentic/resolve_stable_id.py OPS-005` → exactly one current `owner_path::OPS-005` locator;
- `What is the current evidence-sufficiency rule?` → current first-class contract owner;
- `What architecture owns historical evidence?` → current first-class architecture owner.

When the exact path/ID is unknown, use `docs/index.md`. Generated `knowledge/index.md` is available only for explicit OKF compatibility.

Open history only for provenance questions such as why a boundary was chosen, what a phase originally decided, which alternative was rejected, how an ID evolved, what an earlier exit review knew at the time, or whether a proposed change is consistent with prior rationale.

## 6. History cannot redefine current truth

After cutover, editing or discovering a historical file does not alter current meaning.

If history reveals a contradiction with current knowledge:

1. record the conflict;
2. identify the current owner and applicable stable IDs;
3. determine whether current documentation is incomplete/incorrect or the historical wording is superseded;
4. use A4 semantic/architecture change control when meaning must change;
5. update current knowledge only through accepted change, never by inference from chronology.

## 7. Current knowledge cannot erase history

Canonicalization retains provenance sufficient to explain where accepted meaning originated. A current resource should link to the smallest useful set of history sources when rationale is material, without duplicating every historical paragraph.

## 8. Stable IDs

SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH identifiers retain their accepted meanings throughout CKR and DPTN.

Current exact-ID resolution is deterministic through `scripts/agentic/resolve_stable_id.py <ID>` and returns `owner_path::STABLE-ID` against the inventory-selected current owner. `--history` performs separate provenance discovery. Search rank, first occurrence, redirect presence and history never determine the current owner.

## 9. Concept ownership

All 24 accepted concepts have one current first-class concept resource. A concept resource owns the concept's independent purpose, state/actions/invariants/non-goals and synchronization boundaries. Stable-ID contract documents may refine constraints without becoming a second concept definition.

This preserves Daniel Jackson-style concept independence while allowing cross-cutting contracts to constrain synchronization and evidence semantics.

## 10. Architecture ownership

Current architecture authority is under `docs/architecture/`, selected by the ownership inventory. Phase 010 is preserved under `docs/history/phases/phase_010/` as accepted design provenance. It does not compete with current architecture ownership.

## 11. Decision records

Historical phase decisions are preserved under `docs/history/decisions/` as rationale/provenance. A decision may explain current meaning, but the normal current-truth lookup surface is the inventory-selected first-class semantic owner.

## 12. Implementation relationship

CKR exit is accepted. DPTN is a later, separate documentation-topology normalization gate; while DPTN remains active, Implementation 001-A is blocked until DPTN-G exit acceptance. Neither CKR nor DPTN changes the accepted implementation roadmap by routing alone.
