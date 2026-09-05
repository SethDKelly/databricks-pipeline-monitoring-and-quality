# DMTZ Knowledge Routing Maintenance Workflow

**Status:** ACCEPTED — ADF-E / REFINED CKR-J

## Purpose

Keep the OKF routing projection current when canonical repository material changes without turning every canonical edit into a knowledge rewrite or semantic backflow.

## Trigger

Use this workflow when a change moves/renames a canonical resource referenced by `knowledge/`, changes routing identity/lifecycle or a critical boundary reminder, changes project/domain/workflow routing, deprecates/replaces a route, or changes an external/tool fact represented in knowledge metadata.

Routine canonical prose/code changes that leave routing accurate do not require ceremonial OKF edits.

## Procedure

1. Make or review the canonical change first. `knowledge/` never drives semantic changes back into `docs/`.
2. Run `scripts/agentic/knowledge_impact.py --changed <path>` for changed canonical paths when a local checkout is available.
3. Review both `RESOURCE` and `BODY-LINK` candidates. A body-link candidate means a concept routes secondarily to that canonical resource; it does not automatically mean the concept is stale.
4. Ask only whether resource/body route, description, lifecycle, provenance/compatibility metadata, or critical boundary reminder became inaccurate.
5. If still accurate, make no OKF change.
6. If inaccurate, update the smallest routing metadata/body necessary. Do not copy contract prose into the knowledge layer.
7. Stable current-semantic domain resources must remain canonical-first under the CKR-J routing manifest; a regression to Phase 001–010 current ownership is a validation failure.
8. If a historical route remains useful, keep it explicitly historical/provenance; do not let it compete with the current canonical route.
9. Record material routing changes in `knowledge/log.md` when the log is being maintained for that change.
10. Run `scripts/agentic/validate_okf.py`, `scripts/agentic/validate_ckr_j_routing.py`, stable-reference checks and applicable context checks.
11. If a canonical route is missing and the replacement cannot be established, fail/report routing; do not invent a path or alter canonical semantics to satisfy the projection.

## Changed-source semantics

A canonical file change means **review may be required**, not that every referencing knowledge concept is automatically wrong. Hash equality is not a universal freshness rule.

## Exact stable-reference changes

When canonical target-document structure changes, deterministic stable-ID resolution must still produce exactly one `owner_path::ID`. Missing or duplicate canonical stable definitions fail conformance. Historical occurrences are not fallback current owners.

## Generated versus authored content

Mechanical reverse-reference/impact reports may be generated and rebuilt. Interpretive routing descriptions remain short, reviewable repository content.

## Failure behavior

Broken links, canonical-route regressions, unresolved moved resources and ambiguous exact-ID owner resolution are explicit routing failures. They never mean the underlying DMTZ constraint disappeared.
