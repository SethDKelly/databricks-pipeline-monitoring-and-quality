# DMTZ OKF Knowledge Maintenance Policy

**Status:** ACCEPTED — ADF-B / REFINED ADF-E + CKR-J + DPTN-E

## Ownership

Canonical DMTZ documents/code/tests remain the source of truth. After DPTN-E, [`../index.md`](../index.md) is the single authored discovery root and top-level `knowledge/` is a **generated OKF v0.2 compatibility projection**. Neither surface creates semantic authority.

The bounded projection specification is `docs/routing/okf_projection.json`. It records route identity/targets only; it is not a semantic ownership ledger. Current semantic ownership remains selected by the CKR ownership inventory.

## Maintenance rules

1. Change canonical/current owning material first.
2. Do not hand-edit generated `knowledge/` files.
3. Update `docs/routing/okf_projection.json` only when the bounded domain/project routing map actually changes.
4. Workflow routing derives mechanically from `.agents/skills/*/SKILL.md`; implementation routing derives mechanically from `docs/implementation/NNN_*/README.md`.
5. Run `python3 scripts/agentic/generate_okf_projection.py --write` after a projection-input change and `--check` in validation/CI.
6. Never generate changes from `knowledge/` back into canonical `docs/`.
7. Broken generated `resource` or local Markdown links are routing defects.
8. A generated-route conflict with canonical authority is resolved in favor of canonical authority and the projection source must be corrected.
9. History remains separately discoverable but never competes with current routing or semantic ownership.
10. Do not add one generated concept per stable ID, workflow or implementation package merely for catalog symmetry; prefer bounded indexes where the authoritative catalog already exists.

## Provenance and compatibility

The complete pre-DPTN-E authored `knowledge/` tree is preserved under `docs/history/routing/okf-pre-dptn-e/`. It is historical provenance only. Completed CKR-J checks may rehydrate it ephemerally to reproduce accepted-era routing validation; current DPTN checks inspect the generated tree.

## Progressive disclosure

Normal discovery is:

`docs/index.md` → one current domain/operational route → current owner → exact stable IDs as needed.

Generic OKF consumers may use:

`knowledge/index.md` → generated domain/project/catalog route → current owner.

When an exact stable ID is already known, use `scripts/agentic/resolve_stable_id.py <ID>` directly.

## Validation

- `scripts/agentic/generate_okf_projection.py --check` enforces exact generated output;
- `scripts/agentic/validate_okf.py` validates OKF structure/resources/links;
- `scripts/agentic/validate_dptn_e_convergence.py` validates discovery/projection topology;
- completed CKR-J validation remains protected through accepted-era compatibility projection;
- context-budget and integrated conformance checks remain mandatory.
