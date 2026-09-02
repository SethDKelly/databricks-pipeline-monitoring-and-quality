# ADF-D — Portable Skills & Human-Directed Workflow Contract

**Status:** COMPLETE / ACCEPTED

## Objective

Define reusable development procedures once, in a portable form, so Cursor/Claude/Codex users can invoke materially equivalent workflows without repeating long prompt recipes.

## Execution outcome

ADF-D uses `.agents/skills/<name>/SKILL.md` as the single canonical workflow source. This differs from the original proposed `agent-skills/` path because current Cursor and Codex documentation both natively discover repository skills under `.agents/skills/`.

Claude Code follows the same open Agent Skills standard but natively discovers project skills under `.claude/skills/`. DMTZ intentionally does **not** copy the seven canonical skills there because Cursor also discovers Claude skill directories. Instead `.claude/commands/<name>.md` provides a thin Claude-native invocation bridge that tells Claude to read the canonical `.agents/skills/` workflow.

See [`portable_workflow_profile.md`](portable_workflow_profile.md), [`workflow_invocation.md`](workflow_invocation.md), and [`adf_d_execution_review.md`](adf_d_execution_review.md).

## Scope

Skills are **human-directed workflow aids**, not autonomous workers. A human chooses the task. A host may explicitly or implicitly select the matching workflow inside that task, but skill selection cannot create a new task, expand scope, authorize A3/A4 action, or start unrelated follow-on work.

## Canonical skill source

```text
.agents/skills/
├── resolve-context/SKILL.md
├── implement-group/SKILL.md
├── resolve-contract/SKILL.md
├── run-conformance/SKILL.md
├── review-change/SKILL.md
├── update-traceability/SKILL.md
└── exit-review/SKILL.md
```

Canonical skills use only the common portable `name` and `description` frontmatter plus Markdown instructions. Provider-specific metadata, model selection, permission syntax, subagent routing, dynamic shell interpolation, and UI metadata are excluded from the shared workflow source.

## Implemented workflow semantics

### `resolve-context`

Read-only A1 workflow that resolves live authority, the smallest relevant OKF route/canonical files, exact stable IDs when needed, and unresolved assumptions. No repository edits.

### `implement-group`

A2 workflow for one human-selected group/task: resolve context, inspect state, state affected gates, implement the smallest compliant change, add appropriate proof, run safe validation, update directly impacted support artifacts, report residuals, and stop. It cannot start the next group.

### `resolve-contract`

Read-only A1 lookup of an exact stable ID or bounded semantic question to canonical source and minimal surrounding context. Summaries remain advisory.

### `run-conformance`

Normally A1: run safe deterministic checks appropriate to the current scope and report pass/fail/skipped/unavailable evidence faithfully. A failure does not itself authorize fixes or requirement weakening.

### `review-change`

Read-only A1 substantive review against affected contracts, security, historical semantics, and test obligations. Finding a defect does not authorize editing it.

### `update-traceability`

A2 supporting workflow that updates existing implementation traceability/status only when the material behavior and required supporting evidence actually exist.

### `exit-review`

A1 evaluation workflow; when a human explicitly asks to execute/record the repository exit review, writing the bounded review/status artifact is an A2 supporting action. Mandatory unresolved criteria cannot be self-waived.

## Skill design rules

- workflow steps, not duplicated domain specification;
- route through `AGENTS.md`, OKF, canonical docs/tests and exact stable IDs;
- safe failure: unresolved authority remains unresolved;
- no hidden provider-specific assumptions in canonical source;
- no external/destructive actions without A3 authorization;
- architecture/semantic conflicts remain A4 and follow DMTZ change control;
- no agent delegation or autonomous backlog selection;
- no automatic continuation to a new group;
- progressive/on-demand skill loading rather than persistent prompt bloat.

## Tool adapters

### Cursor

Consumes `.agents/skills/` natively. Current documented explicit invocation is `/skill-name`; description matching may also surface skills automatically within the current human task.

### Claude Code

Uses `.claude/commands/<name>.md` thin bridges, invoked as `/<name>`, which route to `.agents/skills/<name>/SKILL.md`. These bridges contain no independent DMTZ workflow semantics.

### Codex

Consumes `.agents/skills/` natively. Current documented explicit selection is `$<skill-name>` (or `/skills` to inspect skills); description matching may also select skills inside the current human task.

Native runtime discovery remains subject to ADF-G tool-in-the-loop verification.

## Deliverables

- canonical `.agents/skills/` portable workflow tree;
- all seven planned workflows;
- `portable_workflow_profile.md`;
- `workflow_invocation.md`;
- thin Claude command bridges;
- updated tool compatibility manifest;
- `fixtures/adf_d_workflow_scenarios.yaml`;
- `scripts/agentic/validate_agent_skills.py` deterministic structural validator;
- stable OKF workflow routes for all seven workflows;
- ADF-D execution review.

## Acceptance status

Repository-configuration acceptance is recorded in [`adf_d_execution_review.md`](adf_d_execution_review.md).

Cross-tool runtime invocation remains deliberately unclaimed until ADF-G. CI enforcement/automated fixture execution remains ADF-F.
