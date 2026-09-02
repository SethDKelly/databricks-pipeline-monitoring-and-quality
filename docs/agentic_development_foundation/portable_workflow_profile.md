# DMTZ Portable Workflow / Agent Skills Profile

**Status:** ACCEPTED — ADF-D

## Purpose

DMTZ defines recurring development procedures once as repository-owned Agent Skills while preserving the ADF-A human-directed authority model and the ADF-B/C knowledge/instruction topology.

The workflow layer describes **how to perform a bounded developer task**. It does not own product semantics, live program status, authorization, or work selection.

## Canonical source location

The canonical repository workflow source is:

`/.agents/skills/<skill-name>/SKILL.md`

This location was selected because current Cursor and Codex documentation both support repository Agent Skills under `.agents/skills/`, and both use the open Agent Skills `SKILL.md` model.

Claude Code supports the same Agent Skills standard but natively discovers project skills under `.claude/skills/`. DMTZ does not duplicate the canonical workflows there because Cursor also discovers Claude skill directories and duplicate skill names would create avoidable ambiguity. Instead, `.claude/commands/<skill-name>.md` contains a tiny bridge that directs Claude Code to the canonical `.agents/skills/` workflow.

Do not use symlinks as the sole distribution mechanism.

## Common portable subset

Canonical DMTZ skills use only this required frontmatter:

```yaml
---
name: lower-case-hyphen-name
description: concise trigger and boundary description
---
```

The canonical source does not use provider-specific frontmatter for:

- model/effort selection;
- allowed tools or permission bypass;
- implicit-invocation policy;
- subagent routing;
- dynamic shell interpolation;
- UI appearance.

Provider-specific metadata may be added only as a lower-precedence adapter after a concrete need is demonstrated and must not change workflow semantics.

## Human-directed invocation rule

Human-directed means the human selected the task/scope. It does **not** require that every host select the matching skill manually.

A supported tool may surface or implicitly select a skill when the current human request matches its description, but skill selection:

- cannot create a new task;
- cannot expand the current task envelope;
- cannot authorize A3/A4 actions;
- cannot continue to a new group after the requested task completes.

Explicit invocation is always acceptable when the host supports it.

## Initial canonical workflows

1. `resolve-context` — A1; find minimal current authority/context; no edits.
2. `implement-group` — A2; realize one human-selected group/task, validate, update directly impacted support artifacts, then stop.
3. `resolve-contract` — A1; locate exact canonical contract/scenario authority.
4. `run-conformance` — A1 by default; run safe checks and report faithfully; failures do not authorize fixes by themselves.
5. `review-change` — A1; substantive contract/security/test review; no edits by discovery alone.
6. `update-traceability` — A2 supporting workflow; advance traceability only with appropriate evidence.
7. `exit-review` — A1 evaluation; A2 only when the human explicitly asks to record the bounded exit/status artifact.

## Common workflow structure

Each skill should contain:

- a clear human-directed/action-class boundary;
- ordered workflow steps;
- output expectations;
- escalation/failure behavior where needed;
- explicit stop conditions.

Skills should route to `AGENTS.md`, `knowledge/index.md`, canonical docs, tests, and stable IDs rather than copying domain specifications.

## Tool invocation mapping

### Cursor

Native source: `.agents/skills/<name>/SKILL.md`.

Current documented explicit UX: `/skill-name` in Agent chat; Cursor may also select a skill when its description matches. Actual repository runtime smoke remains ADF-G.

### Claude Code

Native DMTZ bridge: `.claude/commands/<name>.md`.

Invoke as `/<name>`. The command instructs Claude to read and follow `.agents/skills/<name>/SKILL.md`. Claude Code continues to support command files while recommending skills for richer native packaging; DMTZ uses commands only as a thin compatibility bridge to avoid a second semantic copy.

### Codex

Native source: `.agents/skills/<name>/SKILL.md`.

Current documented explicit UX: type `$` to mention/select a skill in Codex CLI/IDE, or use `/skills` to inspect available skills. Actual repository runtime smoke remains ADF-G.

## Degraded behavior

If a tool does not discover the native skill/bridge:

1. the developer may directly ask the tool to read `.agents/skills/<name>/SKILL.md` and perform that workflow;
2. repository authority/tests remain unchanged;
3. record the native-discovery problem as a compatibility degradation for ADF-G/H;
4. do not create a new provider-specific semantic workflow as a workaround.

## Security and autonomy boundary

The initial workflows are instruction-only. They introduce no credentials, external service configuration, deployment capability, subagents, automatic queues, or unattended continuation.

A skill can use only tools/actions already authorized by the human task and repository environment. Tool availability is not permission.

## Change rule

Material workflow changes should update:

- the canonical `.agents/skills/` source;
- affected OKF workflow routing;
- relevant fixtures/validation;
- tool bridges only when mechanics change.

Do not edit provider bridges to change shared workflow meaning.