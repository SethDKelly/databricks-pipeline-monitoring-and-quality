# CKR Migration Contract

**Status:** ACCEPTED FOR CKR-A EXECUTION

## Purpose

This contract defines how a DMTZ semantic record moves from legacy chronological ownership to canonical knowledge without losing provenance, manufacturing new semantics or creating two simultaneous current owners.

## Migration states

### `legacy_authoritative`

The existing inventoried owner remains the current semantic authority.

Requirements:

- `current_owner` or `current_owner_root` exists;
- a `target_owner` or `target_owner_root` under `docs/canonical/` is declared;
- target structural indexes may exist, but no semantic candidate is treated as current truth;
- OKF and agent routing may still point to the legacy owner until that record is migrated.

### `candidate_ready`

A candidate canonical resource exists for review, but cutover has not occurred.

Requirements:

- legacy current owner remains authoritative;
- candidate is explicitly marked `CANDIDATE / NOT CURRENT AUTHORITY`;
- candidate contains provenance and coverage sufficient for review;
- semantic comparison/conformance is complete enough to decide cutover;
- routine current-truth routing must not be switched to the candidate yet.

### `canonicalized`

The canonical target is the sole current semantic owner.

Requirements:

- target exists under `docs/canonical/`;
- target explicitly declares canonical authority;
- provenance identifies the relevant legacy sources;
- all required accepted meaning/stable-ID coverage is preserved;
- normal OKF/agent/stable-ID routing points to canonical authority;
- legacy source is treated as design history/provenance for that record;
- no living index or implementation guidance continues to present the legacy source as the current owner.

### `history_only`

The resource is provenance/rationale and does not own current semantics.

Typical examples include scenario reviews, superseded wording, chronological exit records and decision rationale after their current semantic outcome has been promoted into canonical knowledge.

## Allowed state transitions

```text
legacy_authoritative
        │
        ▼
candidate_ready
        │
        ▼
canonicalized
```

A record may move from `candidate_ready` back to `legacy_authoritative` when review rejects or defers the candidate.

`history_only` is a resource classification rather than an alternative current-owner state. A legacy owner becomes history/provenance for its migrated semantic record only after canonical cutover.

## Atomic cutover

Cutover is one accepted repository change in which all of the following become true together:

1. canonical target is marked current authority;
2. ownership inventory changes the record to `canonicalized`;
3. required OKF/current-truth routes switch to the canonical target;
4. stable-ID ownership routing is updated where CKR-J has made it applicable;
5. living indexes/agent guidance stop naming the legacy source as current owner;
6. provenance links are present;
7. semantic-conservation and documentation conformance pass.

A partial cutover is a migration defect.

## No dual-authority rule

The following states are prohibited:

- legacy owner and canonical target both claim current authority;
- inventory says `canonicalized` but target is missing;
- inventory says `legacy_authoritative` while a target semantic document claims current authority;
- OKF routes current questions to history after canonicalization;
- a canonical target delegates essential current meaning back to multiple historical phase files.

Canonical resources may cite history for rationale; they must not require design-history reconstruction to answer the current semantic question they own.

## Semantic-conservation gate

Before cutover, the migration group must verify that the candidate preserves applicable accepted meaning from:

- original concept/current owner;
- later accepted refinements;
- stable-ID contracts;
- cross-cutting authority/evidence/time rules;
- accepted decision records where they materially constrain meaning;
- architecture constraints when the target is architectural;
- relevant scenario/exit conclusions that reveal mandatory edge cases.

The goal is not textual equivalence. The goal is semantic equivalence and improved current-truth locality.

## Contradiction handling

When legacy sources appear inconsistent:

1. do not silently choose the newest file;
2. do not choose the first search result;
3. identify the source's accepted scope, later supersession and applicable stable IDs;
4. record whether the issue is wording drift, explicit supersession or genuine unresolved semantic conflict;
5. use A4 change control for genuine meaning changes;
6. keep the record `legacy_authoritative` or `candidate_ready` until the conflict is resolved.

## Provenance requirements

A canonical semantic resource must retain bounded provenance. At minimum, record:

- original owner/source;
- material later refinement source(s);
- stable-ID families/ranges or exact IDs owned/relevant;
- material decision/exit references where needed to explain accepted meaning.

Provenance should be sufficient for audit without turning the canonical resource into a full chronology.

## Historical preservation

CKR does not require rewriting old phase documents to make them read as current documentation.

After cutover, historical records may receive a small non-semantic banner or index classification saying current meaning is elsewhere, but their original accepted-at-the-time narrative should otherwise remain intact.

Historical files are valuable precisely because they preserve design evolution.

## Canonical document metadata contract

Substantive canonical documents created in CKR-B onward should include a compact authority header using the template in `canonical_document_template.md`.

Required fields/sections are intentionally small:

- canonical key;
- kind;
- authority status (`CANDIDATE` or `CANONICAL`);
- current scope/question owned;
- accepted stable IDs/ranges where applicable;
- provenance links;
- related canonical resources.

Do not duplicate OKF lifecycle/trust metadata into semantic authority headers unless a future CKR group explicitly needs it.

## Domain migration independence

CKR migrates by semantic domain, not phase number. One domain may be canonicalized while another remains legacy-authoritative.

Normal lookup follows the inventory record for the requested semantic domain. The mere existence of `docs/canonical/` does not imply the whole repository has completed migration.

## Implementation gate

No product implementation begins until CKR-K confirms:

- all required current semantic domains have canonical owners;
- canonical-first routing is enforced;
- stable-ID ownership is deterministic for implementation traceability;
- representative current-truth questions no longer require chronological reconstruction;
- design history remains accessible for provenance;
- no unreviewed dual-authority conditions remain.
