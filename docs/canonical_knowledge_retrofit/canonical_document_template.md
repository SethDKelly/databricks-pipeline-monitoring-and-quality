# Canonical Knowledge Document Template

**Routing note:** CKR originally created candidates in a temporary compatibility namespace; DPTN promoted accepted current owners to first-class `docs/<family>/` paths and later retired that compatibility namespace. The historical routing state is preserved under `docs/history/`.

Use this template for substantive current semantic resources governed by the CKR ownership model. Structural README/index files are exempt.

```markdown
# <Title>

**Canonical key:** `<stable machine-readable key>`

**Kind:** CONCEPT | CONTRACT | POLICY | INVARIANT | AUTHORITY | EXPERIENCE | ARCHITECTURE | REFERENCE

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration/change record:** `<governed record or change identifier>`

**Owns current question:** <bounded statement of what this resource answers>

**Stable IDs:** <exact IDs/ranges where applicable, otherwise N/A>

## Current semantics

<independently usable accepted current meaning>

## Invariants / boundaries

<durable non-collapse rules>

## Synchronizations / related current resources

<references, not duplicate definitions>

## Provenance

- <original owner>
- <material refinement(s)>
- <material decision/exit source(s)>
```

At accepted cutover, `**Authority:** CANDIDATE / NOT CURRENT AUTHORITY` changes to `**Authority:** CANONICAL CURRENT AUTHORITY` in the same governed change that updates required ownership/routing.

## Template rules

- A current semantic resource must answer the bounded current question without requiring phase chronology reconstruction.
- Provenance links explain origin; they are not delegated semantic ownership.
- Stable IDs retain accepted meaning; owner-path migration does not renumber them.
- Current semantic owners live in first-class `docs/<family>/` roots selected by `canonical_ownership_inventory.json`.
- Avoid full restatement of other current resources. Link across concept/policy/contract boundaries.
- Do not place OKF trust/lifecycle metadata here merely because the resource is discoverable through generated OKF.
- A candidate is review material only until its governed cutover is accepted.
