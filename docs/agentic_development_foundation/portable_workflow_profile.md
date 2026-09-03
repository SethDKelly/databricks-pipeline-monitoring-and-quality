# DMTZ Portable Workflow / Agent Skills Profile

**Status:** ACCEPTED — ADF-D / EXTENDED BY DATABRICKS AGENT SKILLS ADDENDUM

## Purpose

DMTZ defines recurring development procedures once as repository-owned Agent Skills while preserving the ADF-A human-directed authority model and the ADF-B/C knowledge/instruction topology.

The workflow layer describes **how to perform a bounded developer task**. It does not own product semantics, live program status, authorization, or work selection.

## Canonical source location

The canonical repository workflow source is:

`/.agents/skills/<skill-name>/SKILL.md`

This location is shared by Cursor and Codex and remains the single semantic source for DMTZ workflows. Claude Code uses thin `.claude/commands/<skill-name>.md` bridges to the same files rather than duplicate `.claude/skills/` copies.

Do not use symlinks as the sole distribution mechanism.

## Common portable subset

Canonical DMTZ skills use only this required frontmatter:

```yaml
---
name: lower-case-hyphen-name
description: concise trigger and boundary description
---
```

The canonical source does not use provider-specific frontmatter for model/effort, permissions, implicit invocation, subagent routing, shell interpolation, or UI appearance.

## Human-directed invocation rule

Human-directed means the human selected the task/scope. It does **not** require that every host select the matching skill manually.

A supported tool may surface or implicitly select a skill when the current human request matches its description, but skill selection:

- cannot create a new task;
- cannot expand the current task envelope;
- cannot authorize A3/A4 actions;
- cannot continue to a new group after the requested task completes.

Explicit invocation is always acceptable when the host supports it.

## Core canonical workflows

1. `resolve-context` — A1 minimum current authority/context.
2. `implement-group` — A2 one human-selected group/task, validate, update direct support artifacts, then stop.
3. `resolve-contract` — A1 exact canonical contract/scenario resolution.
4. `run-conformance` — A1 safe checks/reporting by default.
5. `review-change` — A1 substantive contract/security/test review.
6. `update-traceability` — evidence-backed A2 supporting workflow.
7. `exit-review` — A1 evaluation; bounded A2 only when recording the requested review/status artifact.

## Databricks platform overlays

The pre-exit Databricks Agent Skills addendum adds six **DMTZ-owned overlays**, not copies of Databricks documentation:

- `dmtz-databricks-environment-discovery`;
- `dmtz-databricks-acquisition`;
- `dmtz-databricks-persistence`;
- `dmtz-databricks-lineage`;
- `dmtz-databricks-runtime-provenance`;
- `dmtz-databricks-governance`.

These overlays compose reviewed vendor operational guidance from `databricks_vendor_skills_profile.json` with DMTZ authority, evidence, temporal, identity, health, Lineage/Impact and authorization boundaries.

**Databricks skills know how Databricks works. DMTZ overlays constrain how that capability may realize DMTZ.**

Vendor skills are materialized locally beneath `.databricks/agent-skills/` and never become canonical DMTZ workflows. A missing vendor materialization degrades convenience only; the overlay must fall back to official documentation/manual procedures rather than invent a semantic fork.

## Common workflow structure

Each registered DMTZ skill contains:

- a clear human-directed/action-class boundary;
- ordered workflow steps;
- output expectations;
- escalation/failure behavior where needed;
- explicit stop conditions.

Skills route to `AGENTS.md`, `knowledge/index.md`, canonical docs, tests, stable IDs and reviewed vendor dependencies rather than copying domain specifications.

## Tool invocation mapping

### Cursor

Native DMTZ source: `.agents/skills/<name>/SKILL.md`. Cursor may surface/match a skill based on its description. A vendor Databricks materialization is read as supporting context only when the DMTZ overlay calls for it.

### Claude Code

DMTZ bridge: `.claude/commands/<name>.md`. Invoke as `/<name>` when desired; the command points back to the canonical `.agents/skills/<name>/SKILL.md`.

### Codex

Native DMTZ source: `.agents/skills/<name>/SKILL.md`. Explicit skill selection may use the host's supported skill UX.

Provider runtime certification remains separate ADF-G evidence.

## Degraded behavior

If a tool does not discover the native DMTZ skill/bridge:

1. directly read `.agents/skills/<name>/SKILL.md`;
2. keep repository authority/tests unchanged;
3. record native-discovery failure as provider degradation;
4. do not create provider-specific semantic copies.

If a reviewed Databricks vendor skill is not materialized:

1. use official Databricks documentation/manual workflow for the product mechanic;
2. retain the DMTZ overlay and all A1–A4/security boundaries;
3. record vendor-skill convenience as degraded;
4. do not install new/unreviewed upstream skills automatically.

## Security and autonomy boundary

DMTZ skills introduce no credentials or permission bypass. A skill can use only actions already authorized by the human task and repository/environment gates. Tool availability and vendor instructions are not permission.

Managed Databricks MCP servers are separate live integrations and are not configured by the vendor-skill addendum.

## Change rule

Material DMTZ workflow changes update the canonical `.agents/skills/` source, affected OKF route, relevant fixtures/validation and bridges only when mechanics change.

Databricks vendor skill changes follow `databricks_agent_skills_addendum.md`: review upstream first, update the reviewed profile, inspect affected overlays, rematerialize, and rerun conformance. Do not edit provider bridges or vendor copies to change DMTZ meaning.
