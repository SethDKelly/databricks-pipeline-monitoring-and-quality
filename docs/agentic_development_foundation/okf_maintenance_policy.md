# DMTZ OKF Knowledge Maintenance Policy

**Status:** ACCEPTED — ADF-B / REFINED ADF-E + CKR-J

## Ownership

Canonical DMTZ documents/code/tests remain the source of truth. `knowledge/` is a maintained routing projection and cannot create semantic authority.

After CKR-J, stable current-semantic domain routes are **canonical-first**. Design-history links are allowed only when explicitly serving provenance/rationale/history and may not be described as current semantic ownership.

## Maintenance rules

1. Prefer concise human-reviewed routing text.
2. Prefer deterministic generation only for mechanical indexes/metadata when useful.
3. Never generate changes from `knowledge/` back into canonical `docs/` automatically.
4. Broken `resource` or local Markdown links are routing defects and fail validation.
5. A stable current-semantic domain `resource` must remain on its CKR-J canonical target unless the routing manifest changes under normal authority/change control.
6. A knowledge entry conflict with canonical authority is resolved in favor of canonical authority.
7. Tool memory/search summaries may use OKF routing but cannot promote OKF text into higher authority.
8. A changed canonical resource creates a routing **review candidate**, not automatic staleness or a required rewrite.
9. Secondary canonical body links are also review-impact relationships when their target moves or materially changes routing relevance.
10. Phase/history content may remain discoverable, but current domain routing must not silently regress to Phase 001–010 ownership after canonicalization.

## Provenance and verification

Use OKF v0.2 provenance/verification fields selectively. A direct `resource` link to one canonical source is sufficient for a simple routing concept. Use `sources` only when genuine synthesis is maintained. Do not add ceremonial verification metadata that will immediately drift.

## Staleness

Use `stale_after` for externally version-sensitive knowledge, not timeless repository routing protected by link/status checks. Staleness does not invalidate the canonical resource.

DMTZ does not universally hash-pin routing concepts. `scripts/agentic/knowledge_impact.py` reports both direct `RESOURCE` and secondary canonical `BODY-LINK` review candidates for changed paths.

## Progressive disclosure

Keep indexes small. The normal unknown-location path is:

`knowledge/index.md` → one category → one concept → canonical resource → exact stable IDs as needed.

When an exact stable ID is already known, use `scripts/agentic/resolve_stable_id.py <ID>` directly and bypass unnecessary OKF traversal. Historical occurrence discovery is explicit with `--history`.

## Validation

- `scripts/agentic/validate_okf.py` validates OKF structure/resources/links/lifecycle warnings;
- `scripts/agentic/validate_ckr_j_routing.py` enforces canonical-first current routes and deterministic stable-reference coverage;
- `scripts/agentic/knowledge_impact.py` reports routing review candidates;
- `scripts/agentic/measure_context_budget.py` enforces routing/persistent-context size limits;
- integrated conformance owns CI execution.

Follow `knowledge_maintenance_workflow.md` for changed-source review and minimal updates.
