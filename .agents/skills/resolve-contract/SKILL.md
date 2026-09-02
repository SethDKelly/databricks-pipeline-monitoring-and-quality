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
3. If an exact ID is supplied, validate it against `stable_id_registry.json` and search that exact token in canonical `docs/`. When a local checkout is available, `scripts/agentic/resolve_stable_id.py <ID>` provides deterministic occurrence discovery.
4. Treat every search hit as a retrieval candidate. A mechanically identified `definition_candidate` is not automatically canonical; indexes, matrices, handoffs, examples, and historical docs may quote the ID.
5. Use live repository authority and the accepted owning document to select the canonical meaning, then read only enough surrounding text to understand the definition, conditions, exceptions, and relationships required for the task.
6. If no exact ID is known, use `knowledge/index.md` to find the smallest relevant domain/architecture resource, identify the governing accepted IDs there, then resolve those IDs exactly.
7. Distinguish accepted contracts from examples, scenarios, OKF summaries, implementation notes, model memory, and derived explanations.
8. If multiple accepted contracts interact, list each one and the specific relationship needed; do not collapse their identities.
9. Surface conflicting, missing, superseded, range-invalid, or unresolved authority explicitly.

## Output

Return:

- exact stable ID(s) or explicitly bounded semantic result;
- accepted-range validation result;
- canonical file path(s) and section/context needed;
- concise application note for the current task;
- related IDs only when materially required;
- unresolved ambiguity or change-control concern.

## Stop conditions

Do not invent a stable ID, infer accepted semantics from an OKF summary, treat the first repository hit as canonical solely by search order, or treat historical/deprecated text as current when live authority is unresolved.

Do not edit repository files.