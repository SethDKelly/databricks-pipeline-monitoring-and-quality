# DMTZ OKF Knowledge Maintenance Policy

**Status:** ACCEPTED — ADF-B

## Ownership

Canonical DMTZ documents/code/tests remain the source of truth. `knowledge/` is a maintained routing projection.

A change to canonical material should update an OKF entry only when the change affects routing, title/description, lifecycle, resource location, or a critical boundary reminder. Routine canonical edits do not require rewriting every knowledge concept.

## Maintenance rules

1. Prefer concise human-reviewed routing text.
2. Prefer deterministic generation only for mechanical indexes/metadata when generation is later introduced.
3. Never generate changes from `knowledge/` back into canonical `docs/` automatically.
4. Broken `resource` or local Markdown links are knowledge-layer defects and should fail validation.
5. `deprecated` and stale entries must be surfaced explicitly rather than silently treated as current.
6. Unknown producer-defined OKF types must remain consumable.
7. A knowledge entry conflict with canonical authority is resolved in favor of canonical authority.
8. Tool memory/search summaries may use OKF routing but cannot promote an OKF description into higher authority.

## Provenance and verification

Use OKF v0.2 provenance/verification fields selectively. A direct `resource` link to one canonical DMTZ source is normally sufficient for a simple hand-maintained routing concept.

Use `sources` when an entry genuinely synthesizes multiple sources. Use `verified` when a review event is meaningful and maintainable. Do not add ceremonial verification metadata that will immediately drift.

## Staleness

Use `stale_after` for compatibility or externally version-sensitive knowledge, not for timeless repository routing that is already protected by link/status checks.

A stale entry should be reported as stale. Staleness does not automatically invalidate the canonical resource it points to.

## Lifecycle transitions

When replacing an OKF concept:

- prefer updating the current concept in place when identity/purpose is unchanged;
- use `deprecated` when a historical route must remain discoverable during transition;
- link the replacement in the body;
- remove dead transitional entries only when no longer useful and normal Git history is sufficient.

## Progressive-disclosure maintenance

Keep root and nested indexes small. Add a new routing layer only when a directory becomes hard to scan or context measurements show value.

The expected traversal remains:

`knowledge/index.md` → one category index → one concept → canonical resource → exact stable IDs as needed.

## Validation

`scripts/agentic/validate_okf.py` provides the ADF-B deterministic structural/resource/link check. ADF-F owns later CI integration, richer fixture automation and context-budget enforcement.
