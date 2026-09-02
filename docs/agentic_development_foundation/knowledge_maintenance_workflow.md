# DMTZ Knowledge Routing Maintenance Workflow

**Status:** ACCEPTED — ADF-E

## Purpose

Keep the OKF routing projection current when canonical repository material changes without turning every canonical edit into a knowledge rewrite.

## Trigger

Use this workflow when a change:

- moves/renames a canonical resource referenced by `knowledge/`;
- changes a title/role/lifecycle or critical boundary used by a routing concept;
- materially changes project/domain/implementation/workflow routing;
- deprecates/replaces a route;
- changes an external/tool compatibility fact represented in knowledge metadata.

Routine prose/code changes that leave routing accurate do not require ceremonial OKF edits.

## Procedure

1. Make or review the canonical change first. `knowledge/` never drives semantic changes back into `docs/`.
2. Run `scripts/agentic/knowledge_impact.py --changed <path>` for changed canonical paths when a local checkout is available.
3. Treat returned concepts as **review candidates**, not automatically stale artifacts.
4. For each candidate, ask only whether its resource path, concise description, lifecycle, provenance/compatibility metadata, or critical boundary reminder became inaccurate.
5. If still accurate, make no OKF change.
6. If inaccurate, update the smallest routing metadata/body necessary. Do not copy new contract prose into the knowledge layer.
7. If a route is replaced but must remain discoverable during transition, mark it `deprecated` and link the replacement.
8. Record material routing changes in `knowledge/log.md`.
9. Run `scripts/agentic/validate_okf.py` and the applicable context/reference checks.
10. If a referenced canonical resource is missing and the correct replacement cannot be established, fail/report the knowledge layer; do not invent a path or alter canonical docs to satisfy routing.

## Changed-source semantics

A canonical file change means **review may be required**, not that every referencing knowledge concept is automatically wrong. Hash equality is therefore not used as a universal freshness rule.

## Generated versus authored content

Mechanical reverse-reference/impact reports may be generated and discarded/rebuilt. Interpretive routing descriptions remain short, reviewable repository content.

## Failure behavior

Broken links, deprecated routes without a usable current route, and unresolved moved resources are explicit maintenance failures. They never mean the underlying DMTZ constraint disappeared.
