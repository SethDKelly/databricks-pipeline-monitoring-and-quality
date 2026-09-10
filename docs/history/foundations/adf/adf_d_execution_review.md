# ADF-D — Execution Review

**Status:** ACCEPTED — ADF-D COMPLETE

## Review question

Has ADF-D implemented one portable, human-directed workflow source that Cursor, Claude Code and Codex can consume with materially equivalent semantics without creating separate tool-specific DMTZ workflow rulebooks?

**Conclusion: yes, at the repository workflow/configuration layer.**

ADF-D establishes the canonical workflow source and documented invocation/adaptation paths. It does not claim that installed Cursor/Claude Code/Codex binaries have successfully invoked every workflow; ADF-G owns tool-in-the-loop runtime verification. ADF-F owns CI enforcement and automated scenario execution.

## Delivered artifacts

- `.agents/skills/resolve-context/SKILL.md`;
- `.agents/skills/implement-group/SKILL.md`;
- `.agents/skills/resolve-contract/SKILL.md`;
- `.agents/skills/run-conformance/SKILL.md`;
- `.agents/skills/review-change/SKILL.md`;
- `.agents/skills/update-traceability/SKILL.md`;
- `.agents/skills/exit-review/SKILL.md`;
- `.claude/commands/<name>.md` thin bridges for all seven workflows;
- `portable_workflow_profile.md`;
- `workflow_invocation.md`;
- `fixtures/adf_d_workflow_scenarios.yaml`;
- `scripts/agentic/validate_agent_skills.py`;
- seven stable `knowledge/workflows/*.md` routing concepts plus the workflow index;
- updated `tool_compatibility.json` and `external_standards_baseline.md`;
- synchronized root/implementation/Cursor status-routing surfaces.

## Findings

### 1. Canonical portable workflow source — PASS

ADF-D uses:

`.agents/skills/<skill-name>/SKILL.md`

as the single canonical DMTZ workflow source.

The original design sketch proposed `agent-skills/`, but current Cursor and Codex documentation both support repository Agent Skills under `.agents/skills/`. Selecting the native shared location improves portability and removes an unnecessary custom directory convention.

Canonical skills use only the common portable `name` and `description` frontmatter plus provider-neutral Markdown workflow instructions.

No provider-specific model, permission, subagent, dynamic-shell or UI metadata is embedded in the shared source.

### 2. Seven initial workflows — PASS

All planned workflows are implemented:

1. `resolve-context` — A1, read-only minimal-context resolution;
2. `implement-group` — A2, one human-selected group/task, necessary support changes and safe validation, then stop;
3. `resolve-contract` — A1, exact stable-ID/canonical semantic lookup;
4. `run-conformance` — A1 by default, safe checks/reporting without rewriting requirements or self-authorized fixes;
5. `review-change` — A1 substantive review, no edits merely because a defect is found;
6. `update-traceability` — A2 supporting workflow, evidence required before advancing status/traceability;
7. `exit-review` — A1 evaluation, with A2 only when the human explicitly requests recording the bounded review/status artifact.

Each workflow includes explicit human-directed boundary, ordered procedure, output expectations and stop conditions.

### 3. Human-directed skill selection — PASS

ADF-D distinguishes **skill selection** from **work selection**.

A tool may explicitly invoke or implicitly match a relevant skill inside a task already selected by a human. That convenience does not:

- create a new task;
- expand scope;
- authorize A3 external/destructive action;
- authorize A4 semantic/architecture change;
- delegate repository implementation to another agent;
- continue automatically into the next group.

This preserves ADF-A while allowing native skill matching behavior.

### 4. Cursor workflow path — PASS at documented/configuration layer

Cursor consumes the canonical `.agents/skills/` location directly.

No duplicate Cursor-specific workflow corpus was created. Existing `.cursor/rules/` remain scoped routing/guardrail mechanics rather than workflow copies.

Actual Cursor invocation/discovery remains ADF-G runtime evidence.

### 5. Claude Code workflow path — PASS at documented/configuration layer

Claude Code follows the open Agent Skills model but normally discovers project skills from `.claude/skills/`.

DMTZ intentionally does not duplicate the canonical workflow set there because Cursor also discovers compatible Claude skill locations; duplicate names would introduce avoidable ambiguity and drift risk.

Instead, `.claude/commands/<name>.md` provides a very small slash-command bridge directing Claude Code to the canonical `.agents/skills/<name>/SKILL.md` file.

The bridges contain no independent DMTZ workflow semantics, authority, permission or scope.

Actual Claude Code invocation remains ADF-G runtime evidence.

### 6. Codex workflow path — PASS at documented/configuration layer

Codex consumes repository `.agents/skills/` directly, so no Codex-specific workflow copy or semantic rulebook is required.

Actual Codex skill discovery/invocation remains ADF-G runtime evidence.

### 7. OKF workflow routing — PASS

`knowledge/workflows/` now contains stable routing concepts for all seven implemented workflows.

The routing entries point to `.agents/skills/<name>/SKILL.md`; they do not own workflow meaning themselves.

The prior ADF-B workflow placeholders have therefore been replaced by current routing without turning OKF into workflow authority.

### 8. Portable invocation/degraded behavior — PASS

`workflow_invocation.md` documents the current tool-specific invocation mapping while treating invocation syntax as a compatibility convenience.

If a native tool fails to discover a skill/bridge, the degraded fallback is to tell the tool to read the canonical `.agents/skills/<name>/SKILL.md` directly. This loses convenience, not repository semantics or acceptance criteria.

### 9. Deterministic static validation seam — PASS

`scripts/agentic/validate_agent_skills.py` checks:

- presence of all seven canonical skills;
- directory/frontmatter name consistency;
- common portable frontmatter only;
- required workflow section markers;
- focused workflow size budget;
- presence/thinness of each Claude command bridge;
- absence of duplicate `.claude/skills/<name>/SKILL.md` sources;
- stable OKF workflow routes to canonical skills;
- compatibility manifest no longer defers ADF-D realization.

During ADF-D readback, the initial validator contained a malformed quote-stripping expression. That defect was identified before group closure and corrected. This review does not claim CI enforcement; ADF-F owns execution/integration of this validator and the scenario fixtures.

### 10. Workflow scenario corpus — PASS

`fixtures/adf_d_workflow_scenarios.yaml` records reusable scenarios for:

- read-only context resolution;
- bounded implementation and stopping behavior;
- canonical contract authority;
- truthful conformance failures;
- review-only behavior;
- evidence-backed traceability;
- mandatory exit-gate handling;
- implicit/explicit skill selection without scope creation;
- A3/A4 escalation;
- thin Claude bridging;
- degraded native discovery;
- design PASS versus executable proof;
- no agent delegation.

These scenarios become automated-conformance candidates in ADF-F.

### 11. Context efficiency — PASS

Workflows are on-demand artifacts rather than additions to persistent `AGENTS.md`/tool rule context.

The shared constitution contains only the workflow map/boundaries; detailed procedures live in the skill selected for the current task.

This preserves progressive disclosure and avoids loading seven procedures into every agent session.

### 12. Autonomy boundary — PASS

ADF-D adds no task queue, subagent orchestration, automatic work allocation, unattended continuation, merge/deploy automation or autonomous backlog selection.

Native tool ability to select or execute a skill is not treated as authorization for autonomous development.

## Relationship to foundation exit gates

ADF-D establishes repository-configuration evidence for:

- **ADF-EX-11** — the portable workflow set is represented;
- **ADF-EX-12** — human task/scope remains controlling and workflows do not automatically continue to unrelated work;
- **ADF-EX-13** — tool-native workflow paths preserve the shared canonical procedure or provide an explicit degraded fallback.

These whole-foundation gates remain open until ADF-F/G provide deterministic execution and actual cross-tool runtime evidence.

## Residual obligations

- **ADF-E:** refine context discovery, exact stable-reference routing, knowledge maintenance and context budgets over the implemented workflows.
- **ADF-F:** execute/integrate OKF, adapter and workflow validators plus scenario fixtures into deterministic repository conformance/CI.
- **ADF-G:** exercise representative workflow invocation and bounded tasks in Cursor, Claude Code and Codex; record actual supported/degraded states.
- **ADF-H:** define long-term security/trust/lifecycle governance and compatibility review horizons.

## Exit decision

**ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**

The next required foundation group is **ADF-E — Context Discovery, Stable References & Knowledge Maintenance**.
