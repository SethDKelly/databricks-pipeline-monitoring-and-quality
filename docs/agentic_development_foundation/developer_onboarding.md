# DMTZ Developer Onboarding — Agentic Foundation

**Status:** ACCEPTED — ADF-G onboarding baseline / REBOUND DPTN-F

## Goal

A developer should be able to work on DMTZ with Cursor, Claude Code, Codex, or no coding agent at all while using the same repository authority, workflows, validation and normal Git/PR process.

No tool-specific setup creates DMTZ truth. Personal preferences may improve ergonomics but may not change team acceptance criteria.

## 1. Start from repository authority

Read only what the task requires.

1. Root `AGENTS.md` — shared engineering/agent constitution.
2. `docs/index.md` — repository-native routing/discovery when the exact current owner is not already known.
3. `docs/documentation_topology_normalization/README.md` — live DPTN state while topology normalization is active.
4. `docs/implementation/README.md` — implementation-program state once implementation work is active.
5. One relevant `.agents/skills/<name>/SKILL.md` workflow when a reusable procedure is useful.
6. Generated `knowledge/index.md` only when an OKF v0.2 compatibility surface is explicitly useful.

Do not preload the full design corpus.

## 2. Understand task authority

ADF-A action classes remain the shared model:

- **A1:** read/review/plan; no edits merely because a defect is found;
- **A2:** bounded change/build/fix inside the human-selected task;
- **A3:** external/destructive/scope-expanding action requires explicit task-specific human authorization and normal gates;
- **A4:** architecture/semantic change follows DMTZ change control and may not silently weaken accepted contracts.

Finishing a task does not authorize the next task.

## 3. Resolve one stable contract

Example:

```bash
python3 scripts/agentic/resolve_stable_id.py AUTH-034
```

Default resolution validates the accepted range, follows the CKR ownership inventory, requires exactly one current stable definition, and returns the deterministic locator `owner_path::AUTH-034`. Read only the minimum surrounding current-owner context required by the task.

Use `--history` only for explicit provenance/rationale/history work. Historical occurrences, redirects, search order and first matches never compete with the current locator.

## 4. Run repository conformance

Agentic/configuration conformance is available to every developer:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

A PASS describes agentic repository configuration only. It is not DMTZ domain health or production readiness.

## 5. Tool choice

### Cursor

Expected shared surfaces:

- root `AGENTS.md`;
- `docs/index.md` for repository-native discovery;
- scoped `.cursor/rules/*.mdc`;
- `.agents/skills/`.

Use native rule/skill discovery when it works. If a native convenience is unavailable, read the shared repository artifact directly rather than copying DMTZ semantics into another rulebook.

### Claude Code

Expected shared surfaces:

- `.claude/CLAUDE.md`, which imports `../AGENTS.md`;
- `docs/index.md` for repository-native discovery;
- `.claude/commands/<workflow>.md` thin bridges;
- canonical workflows under `.agents/skills/`.

Use `/context` when available to confirm project memory loading. Claude auto-memory and user-level instructions are personal context, not repository authority.

### Codex

Expected shared surfaces:

- root `AGENTS.md` and any future legitimate nested `AGENTS.md` for scoped directories;
- `docs/index.md` for repository-native discovery;
- `.agents/skills/`;
- normal repository read/search/edit/test capabilities.

No model name/version is part of DMTZ semantic authority.

### Ordinary IDE / CLI

No AI tool is required. Read the same repository files, use the same scripts/tests, make ordinary code/documentation changes, review the diff, and use the normal Git/PR process.

## 6. Representative onboarding exercise

Before relying on a coding-agent runtime for DMTZ work, perform the ADF-G bounded runtime exercise in `adf_g_runtime_probe.md`.

The exercise is intentionally read-only and asks the tool to:

- determine current ADF/DPTN state from repository authority;
- use `docs/index.md` when discovery is needed;
- resolve `AUTH-034` to its deterministic current owner;
- locate the `run-conformance` workflow;
- report the canonical conformance command;
- stop without edits or automatic continuation.

Record the result in `runtime_compatibility_evidence.json`.

## 7. Personal settings

Personal settings may control tone, UI, local shortcuts, preferred shell, or similar convenience. They must not:

- supersede accepted DMTZ contracts;
- disable mandatory validation;
- turn A1 review into edits;
- authorize A3 actions;
- make tool memory canonical;
- create a different implementation status;
- create automatic next-task continuation.

When personal settings conflict with repository authority, repository authority wins.

## 8. Normal development lifecycle

The standard workflow is deliberately tool-neutral:

```text
developer selects task
  → resolve shared context
  → review/plan/implement inside task
  → run repository-defined validation
  → inspect diff and evidence
  → normal Git/PR/team process
```

There is no special "AI branch" acceptance model. Agent-authored changes are ordinary repository changes subject to ordinary review and gates.

## 9. Adding another coding agent

A new coding agent can be added without redesigning DMTZ if it can consume or bridge to:

- root/shared repository authority;
- `docs/index.md` repository-native progressive disclosure;
- generated `knowledge/index.md` when OKF compatibility is needed;
- canonical `.agents/skills/` workflows or a thin non-semantic bridge;
- repository validation and normal Git workflow;
- A1–A4 human-directed boundaries.

Add only the smallest native adapter necessary. Record documented behavior in `tool_compatibility.json`, add a runtime evidence entry, and run the same representative task before calling the tool supported.
