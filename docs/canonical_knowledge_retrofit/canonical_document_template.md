# Canonical Knowledge Document Template

Use this template for substantive resources created under `docs/canonical/` in CKR-B onward. Structural README/index files are exempt.

```markdown
# <Title>

**Canonical key:** `<stable machine-readable key>`

**Kind:** CONCEPT | CONTRACT | POLICY | INVARIANT | AUTHORITY | EXPERIENCE | ARCHITECTURE | REFERENCE

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `<record id from canonical_ownership_inventory.json>`

**Owns current question:** <bounded statement of what this resource answers>

**Stable IDs:** <exact IDs/ranges where applicable, otherwise N/A>

## Current semantics

<independently usable accepted current meaning>

## Invariants / boundaries

<durable non-collapse rules>

## Synchronizations / related canonical resources

<references, not duplicate definitions>

## Provenance

- <original owner>
- <material refinement(s)>
- <material decision/exit source(s)>
```

At atomic cutover, `**Authority:** CANDIDATE / NOT CURRENT AUTHORITY` changes to `**Authority:** CANONICAL CURRENT AUTHORITY` in the same accepted change that updates the ownership inventory and required routing.

## Template rules

- A canonical resource must answer the bounded current question without requiring phase chronology reconstruction.
- Provenance links explain origin; they are not delegated semantic ownership.
- Stable IDs retain accepted meaning; owner-path migration does not renumber them.
- Avoid full restatement of other canonical resources. Link across concept/policy/contract boundaries.
- Do not place OKF trust/lifecycle metadata here merely because the resource is discoverable through OKF.
- A candidate is review material only until the inventory cutover is accepted.
