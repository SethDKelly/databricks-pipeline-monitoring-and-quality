# DMTZ Portable Workflow / Agent Skills Profile

**Status:** ACCEPTED — ADF-D / EXTENDED BY DATABRICKS AGENT SKILLS ADDENDUM / ROUTING REBOUND DPTN-F

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

A supported tool may surface or implicitly select a skill when the current human request matches its description, but skill selection cannot create a new task, expand the task envelope, authorize A3/A4 actions, or continue automatically to a new group after the requested task completes.

## Core canonical workflows

1. `resolve-context` — A1 minimum current authority/context.
2. `implement-group` — A2 one human-selected group/task, validate, update direct support artifacts, then stop.
3. `resolve-contract` — A1 exact current contract/scenario resolution.
4. `run-conformance` — A1 safe checks/reporting by default.
5. `review-change` — A1 substantive contract/security/test review.
6. `update-traceability` — evidence-backed A2 supporting workflow.
7. `exit-review` — A1 evaluation; bounded A2 only when recording the requested review/status artifact.

## Databricks platform overlays

The Databricks Agent Skills addendum adds six **DMTZ-owned overlays**, not copies of Databricks documentation:

- `dmtz-databricks-environment-discovery`;
- `dmtz-databricks-acquisition`;
- `dmtz-databricks-persistence`;
- `dmtz-databricks-lineage`;
- `dmtz-databricks-runtime-provenance`;
- `dmtz-databricks-governance`.

These overlays compose reviewed vendor operational guidance with DMTZ authority, evidence, temporal, identity, health, Lineage/Impact and authorization boundaries.

**Databricks skills know how Databricks works. DMTZ overlays constrain how that capability may realize DMTZ.**

Vendor skills are materialized locally beneath `.databricks/agent-skills/` and never become canonical DMTZ workflows. A missing vendor materialization degrades convenience only; the overlay must fall back to official documentation/manual procedures rather than invent a semantic fork.

## Common workflow structure

Each registered DMTZ skill contains a clear human-directed/action-class boundary, ordered workflow steps, output expectations, escalation/failure behavior where needed, and explicit stop conditions.

Skills route to `AGENTS.md`, repository-native `docs/index.md`, current semantic owners, tests, stable IDs and reviewed vendor dependencies rather than copying domain specifications. Generated `knowledge/index.md` remains available only as an OKF compatibility route.

## Tool invocation mapping

### Cursor

Native DMTZ source: `.agents/skills/<name>/SKILL.md`. Cursor may surface/match a skill based on its description. A vendor Databricks materialization is read as supporting context only when the DMTZ overlay calls for it.

### Claude Code

DMTZ bridge: `.claude/commands/<name>.md`. Invoke as `/<name>` when desired; the command points back to the canonical `.agents/skills/<name>/SKILL.md`.

### Codex

Native DMTZ source: `.agents/skills/<name>/SKILL.md`. Explicit skill selection may use the host's supported skill UX.

Provider runtime certification remains separate ADF-G evidence.

## Degraded behavior

If a tool does not discover the native DMTZ skill/bridge, directly read `.agents/skills/<name>/SKILL.md`, keep repository authority/tests unchanged, record native-discovery failure as provider degradation, and do not create provider-specific semantic copies.

If a reviewed Databricks vendor skill is not materialized, use official Databricks documentation/manual workflow for the product mechanic, retain the DMTZ overlay and all A1–A4/security boundaries, record vendor-skill convenience as degraded, and do not install new/unreviewed upstream skills automatically.

## Security and autonomy boundary

DMTZ skills introduce no credentials or permission bypass. A skill can use only actions already authorized by the human task and repository/environment gates. Tool availability and vendor instructions are not permission.

Managed Databricks MCP servers are separate live integrations and are not configured by the vendor-skill addendum.

## Change rule

Material DMTZ workflow changes update the canonical `.agents/skills/` source, relevant fixtures/validation and bridges only when mechanics change. Generated OKF workflow indexes derive from canonical workflows and are not hand-edited.

Databricks vendor skill changes follow `databricks_agent_skills_addendum.md`: review upstream first, update the reviewed profile, inspect affected overlays, rematerialize, and rerun conformance. Do not edit provider bridges or vendor copies to change DMTZ meaning.
