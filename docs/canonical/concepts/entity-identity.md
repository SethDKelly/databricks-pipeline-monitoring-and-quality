# Entity Identity

**Canonical key:** `concept.entity_identity`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.entity_identity`

**Owns current question:** When do source-specific references denote the same logical ecosystem entity across systems and time?

**Stable IDs:** N/A

## Current semantics

Entity Identity preserves logical identities, entity kind, source/system/namespace/environment-qualified references, reference validity, equivalence/separation claims, provenance, assertion/effective time, corrections, and unresolved conflicts. Replacement, split, merge, derivation, migration, and succession remain relationships among identities rather than identity equivalence.

## Actions

- `establish` — create a logical identity where distinctness is sufficiently established.
- `recognize` — resolve a source reference as identified, ambiguous, unknown, conflicting, unauthorized, or unavailable.
- `associateReference` — record justified equivalence to an existing identity.
- `separate` — correct conflation or assert distinctness without deleting prior evidence.
- `endReference` — close a source reference validity interval without changing the logical entity.

## Invariants / boundaries

- Human-readable name alone never proves identity; no vendor identifier is universal across sources.
- Environment/context/time qualification is material.
- Rename may preserve identity with continuity evidence; delete/recreate under the same name does not automatically do so.
- Production/test/development instances remain distinct by default.
- Replacement/succession/split/merge/derivation are not identity.
- Corrections do not rewrite original source observations, deployments, or Lineage facts.
- Entity Identity does not own semantics, responsibility, scope, health, Lineage, or authorization.

## Ambiguity / evidence

Insufficient cross-source evidence remains ambiguous/unknown rather than convenient unification. Restricted referents may remain opaque.

## Synchronizations / related canonical resources

All subject-owning concepts use Entity Identity without taking over identity resolution. Change and Lineage own relationships among distinct identities.

## Non-goals

Discovery completeness, business meaning, monitoring scope, health, Lineage truth, authorization, or a universal identifier format.

## Provenance

- `docs/concepts/phase_002/01_scope_and_identity/entity_identity.md`
- `docs/concepts/phase_003/01_subject_scope_and_context/`
