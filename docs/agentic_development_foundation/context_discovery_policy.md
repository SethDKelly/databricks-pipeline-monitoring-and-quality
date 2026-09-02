# DMTZ Context Discovery Policy

**Status:** ACCEPTED — ADF-E

## Purpose

Resolve the smallest authoritative repository context needed for a human-selected task without preloading the DMTZ design corpus or substituting model/tool memory for repository authority.

## Default discovery path

Use the shortest path that reaches exact authority:

```text
human-selected task
  → root AGENTS.md / live status authority
  → knowledge/index.md only when location is not already known
  → one category/concept or active package/group
  → canonical resource
  → exact stable IDs/tests only as needed
```

Do not traverse every layer merely because it exists. If the active group or canonical file is already known, start there.

## Search order

Prefer:

1. explicit path/group/ID named by the human task;
2. live ADF or implementation status;
3. one OKF implementation/domain/workflow route;
4. exact stable-ID lookup;
5. targeted read of the canonical source;
6. broader repository semantic search only when no exact route/ID is known.

Public web search is not a substitute for DMTZ repository semantics. External sources are appropriate only for current vendor/platform facts or other external reality that canonical DMTZ documents intentionally do not own.

## Context-set rule

A resolved context set should normally contain only:

- the human task/action class;
- the current status/group authority relevant to the task;
- one active plan/package when applicable;
- one relevant OKF/domain route when discovery was needed;
- one or two canonical architecture/reference documents;
- exact stable contracts/scenarios/tests required to make the decision;
- unresolved external capability facts.

Loading another file requires a concrete question it answers.

## Progressive-disclosure rule

`knowledge/` is a routing projection, not a context bundle to preload. Traverse one route at a time and follow `resource` to canonical authority.

The secondary `docs/implementation/agent_reference_index.md` is useful for compact family/range/path orientation but is not required in every session.

## Memory and summary rule

Tool memory, chat history, generated summaries, OKF descriptions, and prior agent output may suggest where to look. They cannot supply missing accepted contract text or override live repository status.

A correctness-critical fact that must persist must exist in an appropriate repository artifact.

## Retrieval failure

When a required path/ID cannot be resolved:

1. report the missing or ambiguous reference;
2. list the search performed and candidate sources found;
3. do not infer the missing contract from memory;
4. do not use a similarly named historical contract as a silent substitute;
5. do not treat retrieval failure as evidence that no constraint exists;
6. stop or escalate when the unresolved authority is material to the requested action.

## Context expansion

Expand context only when one of these is true:

- a governing ID explicitly links another contract required to apply it;
- a canonical source names an exception/dependency whose semantics are material;
- executable behavior cannot be understood from the current bounded sources;
- target-environment reality requires current external verification;
- an apparent conflict requires change-control analysis.

Do not expand context simply to be comprehensive.

## Output discipline

`resolve-context` should report the context chosen and why, including unresolved items. It should not reproduce long contract prose when a precise path/ID is sufficient.
