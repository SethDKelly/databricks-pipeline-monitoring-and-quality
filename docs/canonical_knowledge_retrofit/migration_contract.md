# CKR Migration Contract

**Status:** ACCEPTED — CKR-A MIGRATION CONTRACT / PHYSICAL ROUTING REBOUND DPTN-F

## Purpose

This contract defines how a DMTZ semantic record moves from legacy chronological ownership to current semantic knowledge without losing provenance, manufacturing new semantics or creating two simultaneous current owners.

CKR migration is complete. DPTN later changed physical paths only. References below to a canonical target therefore mean the **current target selected by `canonical_ownership_inventory.json`**, now under the first-class `docs/<family>/` topology.

## Migration states

### `legacy_authoritative`

The existing inventoried owner remains the current semantic authority.

Requirements:

- `current_owner` or `current_owner_root` exists;
- a target owner/root is declared in the ownership inventory;
- target structural indexes may exist, but no candidate is treated as current truth;
- routing may still point to the legacy owner until the record is migrated.

### `candidate_ready`

A candidate current resource exists for review, but cutover has not occurred.

Requirements:

- legacy current owner remains authoritative;
- candidate is explicitly marked `CANDIDATE / NOT CURRENT AUTHORITY`;
- candidate contains provenance and coverage sufficient for review;
- semantic comparison/conformance is complete enough to decide cutover;
- routine current-truth routing must not be switched to the candidate yet.

### `canonicalized`

The inventory-selected target is the sole current semantic owner.

Requirements:

- target exists at its current first-class path under `docs/<family>/`;
- target explicitly declares current canonical authority;
- provenance identifies the relevant legacy sources;
- all required accepted meaning/stable-ID coverage is preserved;
- normal agent/stable-ID routing points to the current owner;
- legacy source is treated as design history/provenance for that record;
- no living index or implementation guidance presents the legacy source or a compatibility redirect as the current owner.

### `history_only`

The resource is provenance/rationale and does not own current semantics.

Typical examples include scenario reviews, superseded wording, chronological exit records and decision rationale after their current semantic outcome has been promoted into current knowledge.

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

1. target is marked current authority;
2. ownership inventory changes the record to `canonicalized`;
3. required current-truth routes switch to the target;
4. stable-ID ownership routing is updated where applicable;
5. living indexes/agent guidance stop naming the legacy source as current owner;
6. provenance links are present;
7. semantic-conservation and documentation conformance pass.

A partial cutover is a migration defect.

DPTN-C later performed a separate atomic **path-only** promotion from the CKR-era `docs/canonical/<family>/` namespace to first-class `docs/<family>/` owners and rebound the ownership inventory at the same time. That path promotion did not reopen semantic cutover.

## No dual-authority rule

The following states are prohibited:

- legacy owner and current target both claim current authority;
- inventory says `canonicalized` but the current target is missing;
- inventory says `legacy_authoritative` while a target semantic document claims current authority;
- current routing sends current questions to history after canonicalization;
- a compatibility redirect is treated as an alternate semantic owner;
- a current target delegates essential meaning back to multiple historical phase files.

Current resources may cite history for rationale; they must not require design-history reconstruction to answer the current semantic question they own.

## Semantic-conservation gate

Before cutover, the migration group verifies that the candidate preserves applicable accepted meaning from original owners, later accepted refinements, stable-ID contracts, cross-cutting authority/evidence/time rules, material accepted decisions, architecture constraints, and relevant scenario/exit conclusions.

The goal is not textual equivalence. The goal is semantic equivalence and improved current-truth locality.

## Contradiction handling

When sources appear inconsistent:

1. do not silently choose the newest file;
2. do not choose the first search result;
3. identify the source's accepted scope, later supersession and applicable stable IDs;
4. record whether the issue is wording drift, explicit supersession or genuine unresolved semantic conflict;
5. use A4 change control for genuine meaning changes;
6. do not change current ownership until the conflict is resolved through accepted authority.

## Provenance requirements

A current semantic resource retains bounded provenance sufficient for audit: original owner/source, material later refinement sources, relevant stable-ID families/ranges, and material decision/exit references when needed to explain accepted meaning.

Provenance should not turn a current resource into a full chronology.

## Historical preservation

Historical records live under `docs/history/` after DPTN. They preserve accepted-at-the-time evolution and are not rewritten to look current. Historical text, links and status statements must be interpreted in historical context.

## Canonical document metadata contract

Substantive current semantic documents retain compact authority metadata sufficient to state canonical key/kind, authority status, current scope/question, accepted stable IDs/ranges where applicable, provenance, and related current resources.

Do not duplicate OKF lifecycle/trust metadata into semantic authority headers.

## Domain migration independence

CKR migrated by semantic domain, not phase number. The accepted ownership inventory remains the durable current-owner ledger after CKR and DPTN.

Normal lookup follows the inventory record for the requested semantic domain. Directory presence, `docs/canonical/` redirects, generated OKF, history and search order do not imply ownership.

## Implementation gate

CKR-K accepted the CKR exit after all required current semantic domains had owners, canonical-first routing was established, stable-ID ownership was deterministic, current-truth questions no longer required chronological reconstruction, history remained accessible, and no unreviewed dual-authority condition remained.

DPTN was subsequently interposed as a separate topology gate. **Implementation 001-A remains BLOCKED / NOT STARTED until DPTN-G exit acceptance.** DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself begin implementation.
