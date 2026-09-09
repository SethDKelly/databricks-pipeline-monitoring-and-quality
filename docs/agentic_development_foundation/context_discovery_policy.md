# DMTZ Context Discovery Policy

**Status:** ACCEPTED — ADF-E / REFINED CKR-J + DPTN-E

## Purpose

Resolve the smallest authoritative repository context needed for a human-selected task without preloading the DMTZ corpus or substituting routing/search/model memory for repository authority.

## Default discovery path

Use the shortest path that reaches exact authority:

```text
human-selected task
  → root AGENTS.md / live status authority
  → exact stable-ID resolver directly when an ID is known
  → otherwise docs/index.md when location is not already known
  → one current category/resource
  → exact current owner
  → exact stable IDs/tests only as needed
```

Generic OKF consumers may traverse generated `knowledge/index.md`, but repository-native discovery uses `docs/index.md`. Do not traverse every layer merely because it exists.

## Exact-ID fast path

When a stable ID is known, use:

```bash
python3 scripts/agentic/resolve_stable_id.py <ID>
```

The default result is the deterministic current canonical locator `owner_path::ID`. Use `--history` only for a concrete provenance/rationale/change question. Historical occurrences and generated OKF entries never participate in current owner selection.

## Search order

Prefer:

1. explicit path/group/ID named by the human task;
2. root/live DPTN/implementation authority;
3. deterministic exact stable-ID resolution when an ID is known;
4. `docs/index.md` when semantic/operational location is unknown;
5. one generated OKF route only when a consumer specifically uses OKF compatibility;
6. targeted read of the current owning source;
7. broader repository semantic search only when no exact route/ID is known.

Search order itself never establishes semantic authority.

## Context-set rule

A resolved context set should normally contain only the human task/action class, relevant live status, one active plan/package if applicable, one discovery route at most, one or two current owning resources, exact stable contracts/tests needed, and unresolved external capability facts.

Loading another file requires a concrete question it answers.

## Progressive-disclosure rule

`docs/index.md` is the authored discovery root. Top-level `knowledge/` is generated routing compatibility, not a context bundle to preload. A known stable ID may bypass both. `docs/implementation/agent_reference_index.md` is a compact optional orientation surface rather than required session context.

## Memory and summary rule

Tool memory, chat history, generated summaries, generated OKF descriptions and prior agent output may suggest where to look. They cannot supply missing accepted contract text or override live repository authority.

## Retrieval failure

When a required path/ID cannot be resolved: report the failure, identify the bounded search performed, do not infer from memory, do not substitute similarly named history, and stop/escalate when unresolved authority is material.

## Context expansion

Expand only when a governing ID names another material contract, a current owner names a material exception/dependency, behavior cannot be understood from bounded sources, external deployment reality needs verification, or an apparent conflict needs change-control analysis.

## Output discipline

`resolve-context` should report the context chosen and why, including current locators and unresolved items, without reproducing long contract prose when a precise path/ID is sufficient.
