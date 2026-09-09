# DMTZ Knowledge Routing Maintenance Workflow

**Status:** ACCEPTED — ADF-E / REFINED CKR-J + DPTN-E

## Purpose

Keep the authored discovery root and generated OKF compatibility projection aligned with current repository authority without creating semantic backflow or a second hand-maintained routing plane.

## Trigger

Use this workflow when a change moves/renames a routed current resource, changes domain/project routing identity, adds/removes a repository-owned workflow or implementation package, or changes a critical discovery boundary.

Routine canonical prose changes that leave routing accurate require no OKF rewrite.

## Procedure

1. Make/review the canonical or current operational change first.
2. If the human/tool-neutral discovery structure changed, update `docs/index.md` minimally.
3. If a bounded domain/project compatibility route changed, update `docs/routing/okf_projection.json` minimally.
4. Do **not** hand-edit `knowledge/`.
5. Regenerate with `python3 scripts/agentic/generate_okf_projection.py --write`.
6. Run `python3 scripts/agentic/generate_okf_projection.py --check` and `scripts/agentic/validate_okf.py`.
7. Run stable-reference/current-owner validation when canonical route targets changed.
8. Run DPTN/current conformance checks as applicable.
9. If a route cannot be established from current authority, fail/report it; never invent a semantic owner to satisfy routing.

## Generated versus authored content

Authored current discovery:
- `docs/index.md`.

Authored bounded projection input:
- `docs/routing/okf_projection.json`.

Repository-owned catalogs used mechanically:
- `.agents/skills/*/SKILL.md`;
- `docs/implementation/NNN_*/README.md`.

Generated compatibility output:
- top-level `knowledge/`.

Historical authored routing:
- `docs/history/routing/okf-pre-dptn-e/`.

Generated output may be rebuilt freely from its current sources. Historical routing must not be rewritten to match current state.

## Exact stable-reference changes

When canonical target-document structure changes, deterministic stable-ID resolution must still produce exactly one `owner_path::ID`. Missing/duplicate current definitions fail conformance. Historical occurrences and generated OKF entries are never fallback current owners.

## Failure behavior

Generated drift, broken routes, missing source catalogs, unresolved moved resources, or ambiguous stable-ID ownership are explicit failures. They never mean the underlying DMTZ constraint disappeared.
