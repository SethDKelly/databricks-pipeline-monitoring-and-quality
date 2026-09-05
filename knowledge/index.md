---
okf_version: "0.2"
---
# DMTZ Knowledge Bundle

Portable, tool-neutral routing into current DMTZ repository authority. This bundle is an index, not a source of product truth.

All accepted semantic families are canonicalized through CKR-I. The CKR ownership inventory and substantive `docs/canonical/` owners determine current meaning; OKF only helps locate them.

Start with the shortest relevant path:

- **Known stable ID:** use `python3 scripts/agentic/resolve_stable_id.py <ID>` directly; use `--history` only for explicit provenance/history work.
- **Unknown semantic location:** use one bounded [domain route](domains/index.md), then its canonical resource.
- [Project authority and current documentation ownership](project/index.md)
- [Implementation routing](implementation/index.md)
- [Development workflow routing](workflows/index.md)

For exact semantics, read the current canonical owner selected by repository authority. Do not treat an OKF summary, lifecycle value, verification marker, design-history occurrence, search rank or model memory as semantic authority.
