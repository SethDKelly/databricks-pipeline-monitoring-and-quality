---
name: resolve-contract
description: Resolve an exact DMTZ stable contract/scenario ID or bounded semantic question to its canonical source and minimal surrounding context. Use for precise contract lookup; summaries remain advisory and this workflow never edits repository files.
---
# Resolve contract

## Human-directed boundary

This workflow is **A1 — read/review/plan**. It locates authority; it does not create or modify authority.

## Workflow

1. Normalize the requested stable ID or bounded semantic question without broadening it.
2. If an exact ID is supplied, search that exact token in canonical `docs/` first. Use `docs/implementation/agent_reference_index.md` only as a secondary range/path bridge when useful.
3. If no exact ID is known, use `knowledge/index.md` to find the smallest relevant domain/architecture resource, then search within canonical docs for the governing IDs.
4. Read only enough surrounding text to understand the contract's definition, conditions, exceptions, and relationships required for the task.
5. Distinguish the exact accepted contract from examples, scenarios, OKF summaries, implementation notes, model memory, and derived explanations.
6. If multiple accepted contracts interact, list each one and the specific relationship needed; do not collapse their identities.
7. Surface conflicting, missing, superseded, or unresolved authority explicitly.

## Output

Return:

- exact stable ID(s) or explicitly bounded semantic result;
- canonical file path(s) and section/context needed;
- concise application note for the current task;
- related IDs only when materially required;
- unresolved ambiguity or change-control concern.

## Stop conditions

Do not invent a stable ID, infer accepted semantics from an OKF summary, or treat historical/deprecated text as current when live authority is unresolved.

Do not edit repository files.