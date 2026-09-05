---
name: resolve-contract
description: Resolve an exact DMTZ stable contract/scenario ID or bounded semantic question to its canonical source and minimal surrounding context. Use for precise contract lookup; summaries remain advisory and this workflow never edits repository files.
---
# Resolve contract

## Human-directed boundary

This workflow is **A1 — read/review/plan**. It locates authority; it does not create or modify authority.

## Workflow

1. Normalize the requested stable ID or bounded semantic question without broadening it.
2. Apply `docs/agentic_development_foundation/stable_reference_policy.md`.
3. If an exact accepted ID is supplied, run `python3 scripts/agentic/resolve_stable_id.py <ID>` when a local checkout is available. Default resolution returns exactly one current canonical locator `owner_path::ID` derived from the accepted range registry and CKR ownership inventory.
4. Read only the smallest surrounding canonical owner context needed for definition, conditions, exceptions and material relationships.
5. Use `--history` only when the task explicitly needs provenance, rationale, supersession or historical occurrence inspection. History never competes with current canonical ownership.
6. If no exact ID is known, use one bounded `knowledge/index.md` domain route, follow its canonical resource, identify governing IDs, then resolve those IDs exactly.
7. Distinguish accepted contracts from OKF summaries, examples, implementation notes, historical text, model memory and derived explanations.
8. If multiple accepted contracts interact, keep each identity separate and name the required relationship.
9. Surface missing, duplicate, range-invalid or unresolved canonical stable definitions explicitly.

## Output

Return exact stable ID(s), accepted-range result, canonical locator/path and minimum section context, concise application note, materially related IDs, and unresolved authority/change-control concerns.

## Stop conditions

Do not invent a stable ID, infer accepted semantics from OKF, use repository first-match order as authority, or treat historical text as current. Do not edit repository files.
