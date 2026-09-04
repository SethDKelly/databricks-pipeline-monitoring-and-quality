# CKR Documentation Authority Model

**Status:** ACCEPTED FOR CKR-A EXECUTION

## 1. Problem statement

DMTZ has a strong design record but its accepted current meaning is still partially distributed across chronological phase artifacts. A semantic question can require following an original concept specification, later refinements, stable-ID contracts, architecture consolidation and decision history before present meaning is clear.

That topology is valuable for provenance but expensive and error-prone for routine current-truth lookup.

CKR separates two legitimate documentation purposes:

1. **canonical knowledge** — what DMTZ means now;
2. **design history** — how and why DMTZ arrived there.

Neither layer replaces the other.

## 2. Authority layers

### Layer 1 — Canonical knowledge

After a record is `canonicalized`, current semantic authority for that record lives under `docs/canonical/`.

Canonical knowledge may own:

- accepted concept definitions;
- current policy and authority boundaries;
- invariants and semantic separations;
- domain/stable-ID contracts;
- user/experience contracts;
- technical architecture contracts;
- canonical terminology and reference mappings.

Canonical resources must be independently usable for the current question they own. They may cite history for provenance but may not require chronological reconstruction to obtain current meaning.

### Layer 2 — Design history and provenance

Design history includes:

- phase working records and group READMEs;
- original concept specifications after canonical cutover;
- refinement documents;
- decision records;
- scenario reviews;
- exit reviews;
- handoffs and gap registers;
- superseded terminology or earlier formulations preserved in context.

Design history explains origin, rationale, evolution, alternatives and historical state. It is never deleted merely because current meaning moved to canonical knowledge.

### Layer 3 — Routing and operational guidance

`knowledge/`, `AGENTS.md`, `.agents/skills/`, Cursor/Claude/Codex adapters and implementation routing help users and tools find the correct authority. They do not become semantic owners.

OKF is therefore a discovery/catalog plane over the authority model—not the authority model itself.

## 3. Precedence

For one semantic record, precedence is state-dependent.

### `legacy_authoritative`

1. inventoried legacy current owner;
2. accepted supporting stable-ID/refinement/decision material as required by that owner;
3. routing/knowledge summaries.

No target canonical candidate is current truth.

### `candidate_ready`

1. inventoried legacy current owner;
2. accepted supporting stable-ID/refinement/decision material;
3. canonical candidate for review only;
4. routing/knowledge summaries.

A candidate cannot silently override the legacy owner.

### `canonicalized`

1. canonical owner under `docs/canonical/`;
2. accepted executable contracts/code/tests when implementation later exists and is explicitly subordinate to documentation semantics;
3. design history/provenance;
4. routing/knowledge summaries.

Historical sources cease to be current semantic owners for that record at cutover.

### `history_only`

The resource is never a current semantic owner. It may support provenance/rationale only.

## 4. No dual-current-authority invariant

For every semantic record:

> **Exactly one authority state determines current ownership.**

The repository may contain many descriptions, citations and historical definitions, but only one accepted current owner is permitted after canonicalization.

The presence of the same stable ID or concept name in multiple files does not imply multiple authority.

## 5. Canonical question-routing rule

Once a record is canonicalized:

- `What is Lineage?` → canonical Lineage concept;
- `What does OPS-005 require?` → canonical OPS owner/anchor;
- `What is the current evidence-sufficiency rule?` → canonical policy/contract;
- `What architecture owns historical evidence?` → canonical architecture resource.

Design history should be opened only when the task asks questions such as:

- Why was this boundary chosen?
- What did Phase 004 originally decide?
- Which alternative was rejected?
- How did OPS-005 evolve?
- What did an earlier exit review know at the time?
- Is a proposed semantic change consistent with prior rationale?

## 6. History cannot redefine current truth

After cutover, editing or discovering a historical file does not alter current meaning.

If history reveals a contradiction with canonical knowledge:

1. record the conflict;
2. identify the accepted source and applicable stable IDs;
3. determine whether the canonical resource is incomplete/incorrect or the historical wording is superseded;
4. use existing A4 semantic/architecture change control when meaning must change;
5. update canonical knowledge only through accepted change, never by inference from chronology.

## 7. Canonical knowledge cannot erase history

Canonicalization must retain provenance sufficient to explain where accepted meaning originated.

A canonical resource should link to the smallest useful set of design-history sources, including original concept owner, material refinements, accepted decisions and relevant exit/architecture consolidation where appropriate.

Provenance is not an excuse to duplicate every historical paragraph in the canonical resource.

## 8. Stable IDs

SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH identifiers retain their accepted meanings throughout CKR.

During CKR-A–I:

- exact occurrence remains a retrieval aid;
- the ownership inventory records the migration state and target canonical domain;
- stable-ID meaning may not change simply because the owner path changes.

CKR-J will make canonicalized stable-ID ownership directly resolvable to canonical owner paths/anchors while preserving historical occurrence discovery separately.

## 9. Concept ownership

All 24 accepted concepts must eventually have one current canonical concept resource.

A concept resource owns the concept's independent purpose, state/actions/invariants/non-goals and synchronization boundaries. Stable-ID contract documents may refine constraints without becoming a second concept definition.

This preserves Daniel Jackson-style concept independence while allowing cross-cutting contracts to constrain synchronization and evidence semantics.

## 10. Architecture ownership

Phase 010 remains accepted design history and current legacy architecture authority until CKR-I cutover.

CKR-I will promote current architecture into `docs/canonical/architecture/` without rewriting Phase 010 as though the final architecture had been known at the beginning of the design process.

## 11. Decision records

`docs/decisions/` is primarily rationale/provenance. A decision may constrain current meaning while the corresponding semantic record remains legacy-authoritative, but after canonicalization the decision record is not the normal current-truth lookup surface.

Canonical resources cite the durable decision rather than requiring agents to infer current meaning from the decision chronology.

## 12. Implementation relationship

Implementation 001-A remains blocked during CKR because code/test/schema references should be created against the long-lived canonical authority topology rather than phase-era paths we already intend to demote to provenance.

CKR does not invalidate the accepted implementation roadmap or ADF exit. It changes the documentation dependency surface that implementation will consume.
