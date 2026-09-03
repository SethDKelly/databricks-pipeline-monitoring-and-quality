# Databricks Agent Skills Integration Addendum

**Status:** IN EXECUTION — PRE-EXIT ADDENDUM

## Purpose

Integrate first-party Databricks Agent Skills into the DMTZ developer workflow without creating a new ADF phase, a second DMTZ authority surface, or provider-specific semantic forks.

This addendum cross-cuts ADF-D through ADF-H. It must be closed before the Agentic Development Foundation execution exit review.

## Authority model

Databricks Agent Skills are **vendor operational guidance**. They can explain current Databricks CLI/product workflows, but they do not own DMTZ semantics, project scope, authorization, evidence sufficiency, Assertion Authority, Capability Authorization, causal confirmation, Impact, or control decisions.

Precedence remains:

1. accepted DMTZ contracts/canonical `docs/`;
2. root `AGENTS.md` and A1–A4 human-directed authority;
3. live implementation/group scope;
4. accepted DMTZ portable workflows and platform overlays;
5. reviewed Databricks vendor skills;
6. tool memory/personal configuration.

A vendor skill recommendation never grants A3/A4 permission.

## Reviewed upstream baseline

Upstream repository: `databricks/databricks-agent-skills`.

Reviewed snapshot: release `v0.2.14`, commit `ce0599506bad5dd63dead9ab88c440ebd2d8336c`, reviewed 2026-09-02.

The initial DMTZ vendor set is intentionally curated:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

The machine-readable review snapshot is `databricks_vendor_skills_profile.json`.

## Explicit deferral

Model/AI implementation skills are not part of the initial set. Model Serving, ML training/evaluation, Agent Bricks, AI Functions, AI runtime and Vector Search can be considered later through the same review/change process.

No automatic addition of newly published upstream skills is permitted.

Managed MCP servers are also **not configured by this addendum**. Databricks documentation treats skills (knowledge/instructions) and managed MCP servers (live callable tools) as separate capabilities. MCP adoption remains a separate G3/G4 security/integration decision.

## Materialization model

DMTZ does not vendor-copy Databricks skills into canonical `.agents/skills/` and does not use `aitools` to silently modify each coding-agent configuration.

Reviewed vendor skills are materialized locally with the Databricks CLI `aitools --path` mode into:

`.databricks/agent-skills/`

That tree is already ignored by Git. `--path` writes resolved skill files without modifying coding agents or writing Databricks AI-tools install state.

Use:

```bash
python3 scripts/agentic/materialize_databricks_skills.py
python3 scripts/agentic/materialize_databricks_skills.py --execute
```

The helper builds the exact reviewed `databricks aitools install --path ... --skills ...` command and, after materialization, verifies that all selected skill names and reviewed versions match the repository profile and that no extra vendor skill appeared.

If upstream versions differ, stop and review the new upstream release before changing the profile. Do not silently accept drift.

## DMTZ platform overlays

DMTZ-specific overlays remain canonical repository skills:

- `dmtz-databricks-environment-discovery`;
- `dmtz-databricks-acquisition`;
- `dmtz-databricks-persistence`;
- `dmtz-databricks-lineage`;
- `dmtz-databricks-runtime-provenance`;
- `dmtz-databricks-governance`.

The overlays do **not** duplicate Databricks product documentation. They state DMTZ boundaries and route to the relevant reviewed vendor skills when local materialization is present.

### Core composition rule

**Databricks skills know how Databricks works. DMTZ overlays constrain how Databricks capability may be used to realize DMTZ.**

Examples:

- Unity Catalog privileges/access do not create DMTZ Assertion Authority.
- Lineage system tables do not establish encounter, exposure, Impact or cause.
- Lakeflow Connect success does not establish source completeness or monitored-data health.
- A missing source page, permission denial or connector failure cannot become a negative domain fact.
- Delta time travel is useful operational capability but is not the sole DMTZ definition of historical/as-known state.
- Job/pipeline names or timestamp proximity cannot establish canonical identity/correlation.

## Permissions and workspace interaction

Local inspection such as reading the reviewed profile or checking an installed CLI is not workspace authorization.

Any Databricks workspace read/write, deployment, pipeline/job run, GRANT/REVOKE, connection creation, credential-bearing operation, or other external action follows ADF-A A3 requirements unless the human-selected task explicitly authorizes that concrete external interaction.

Never expose or copy Databricks tokens/credentials into prompts, skills, knowledge, logs or repository artifacts.

## Update lifecycle

Upstream review horizon: 30 days, with immediate review when:

- selected skill metadata/version changes;
- `aitools` install/materialization semantics change;
- a selected skill materially changes permissions/auth/network behavior;
- a selected skill begins loading a new dependency automatically;
- a DMTZ overlay no longer preserves the relevant semantic boundary.

Update sequence:

1. inspect official Databricks docs and upstream manifest/diff;
2. update the reviewed upstream commit/release and selected versions;
3. review affected DMTZ overlays;
4. rematerialize locally and validate exact names/versions;
5. run agentic conformance;
6. record the review in the knowledge log.

Do not use an unrestricted update path that auto-installs newly added upstream skills.

## Implementation entry

Implementation 001-A should install/verify a compatible Databricks CLI and perform the first local materialization check. The inability to materialize vendor skills does not change DMTZ semantics; use official documentation/manual workflow and record the integration as degraded until repaired.

## Exit conditions for this addendum

- reviewed eight-skill profile is explicit and machine-valid;
- Unity Catalog and Lakeflow Connect are included;
- model/AI skills remain deferred;
- six DMTZ overlays exist and remain under shared A1–A4 authority;
- Claude bridges and OKF routes preserve one canonical overlay source;
- vendor skills are not checked into canonical DMTZ skill directories;
- local materialization/version validation has a deterministic helper;
- conformance rejects automatic vendor-skill expansion and deferred-model inclusion;
- Implementation 001-A is routed to perform environment materialization verification;
- unified repository conformance passes on the finalized addendum state.
