# Databricks Agent Skills Integration Addendum — Execution Review

**Status:** ACCEPTED — DATABRICKS AGENT SKILLS PRE-EXIT ADDENDUM COMPLETE

## Review question

Can DMTZ use a curated first-party Databricks Agent Skills set, including Unity Catalog and Lakeflow Connect, without allowing vendor guidance to supersede DMTZ semantics, security, human-directed scope or tool-neutral portability?

**Conclusion: yes, with local vendor-skill materialization retained as an Implementation 001-A environment verification.**

## Authority decision

The addendum is accepted as a bounded cross-cutting extension of ADF-D through ADF-H. It is not ADF-I and does not reopen completed ADF groups.

Databricks Agent Skills remain **reviewed vendor operational guidance**. Canonical DMTZ contracts, root `AGENTS.md`, A1–A4 scope, active implementation authority and DMTZ-owned overlays remain higher authority.

A vendor skill recommendation cannot create A3/A4 permission, DMTZ Assertion Authority, Capability Authorization, evidence sufficiency, causal confirmation, Impact, health or control truth.

## Reviewed upstream baseline

- upstream: `databricks/databricks-agent-skills`;
- release: `v0.2.14`;
- reviewed commit: `ce0599506bad5dd63dead9ab88c440ebd2d8336c`;
- reviewed on: 2026-09-02;
- review horizon: 30 days.

The initial reviewed vendor set is exactly:

1. `databricks-core` 0.1.0;
2. `databricks-dabs` 0.0.1;
3. `databricks-jobs` 0.2.0;
4. `databricks-pipelines` 0.3.0;
5. `databricks-data-discovery` 0.1.0;
6. `databricks-dbsql` 0.1.0;
7. `databricks-unity-catalog` 0.3.0;
8. `databricks-lakeflow-connect` 0.1.0.

Unity Catalog and Lakeflow Connect are therefore first-class parts of the initial developer dependency profile.

## Explicitly deferred

The initial profile does not select model/AI implementation skills, including Model Serving, ML training/evaluation, Agent Bricks, AI Functions, AI Runtime and Vector Search. Adding any of those requires a later explicit review/profile/conformance change.

Automatic adoption of newly published upstream skills is prohibited.

Managed Databricks MCP servers are not configured by this addendum. They expose live tools rather than reviewed instruction/knowledge and require separate G3/G4 permission, data, network, retention and security review.

## DMTZ-owned overlays — PASS

Six canonical overlays are registered under `.agents/skills/`:

- `dmtz-databricks-environment-discovery`;
- `dmtz-databricks-acquisition`;
- `dmtz-databricks-persistence`;
- `dmtz-databricks-lineage`;
- `dmtz-databricks-runtime-provenance`;
- `dmtz-databricks-governance`.

Each has a thin Claude command bridge and stable OKF workflow route. Cursor/Codex consume the canonical `.agents/skills/` location. No vendor `databricks-*` skill is copied into canonical DMTZ skill storage.

The composition rule is accepted:

> **Databricks skills know how Databricks works. DMTZ overlays constrain how that capability may realize DMTZ.**

## Semantic protection — PASS

The overlays preserve at minimum:

- Lakeflow Connect/Pipeline/Job success ≠ completeness, freshness, quality or health;
- source/connector denial, timeout, retention gap, schema failure or partial coverage ≠ negative domain fact;
- Delta time travel ≠ the sole historical/as-known model;
- Unity Catalog Lineage ≠ encounter/exposure/Impact/cause;
- names/timestamp proximity ≠ canonical run/deployment identity or causality;
- Unity Catalog privileges/ownership ≠ DMTZ Assertion Authority;
- authentication ≠ Capability Authorization ≠ Assertion Authority;
- target workspace capability remains deployment-specific verification.

## Permissions/security — PASS

Local vendor-skill materialization does not authorize Databricks workspace access. Workspace reads/writes, deployment, pipeline/job runs, connection creation, governance mutation and other external actions remain governed by ADF-A A3 plus normal environment gates.

Vendor skills cannot override ADF-H least privilege, secret/sensitive-data, prompt/content-trust, provider-memory or external-integration governance.

## Materialization model — PASS at repository contract level

Reviewed vendor skills are materialized locally beneath ignored `.databricks/agent-skills/` using the Databricks CLI `aitools --path` path rather than allowing vendor install mechanics to silently modify each coding-agent configuration.

`scripts/agentic/materialize_databricks_skills.py` constructs the exact reviewed eight-skill install command, verifies a compatible CLI before execution, validates every materialized name/version against the reviewed profile, rejects extra/unreviewed vendor skills, and only replaces the configured ignored materialization directory when explicitly requested.

## Environment residual — EXPLICIT / ACCEPTED FOR HANDOFF

**`DBX-SKILL-RUN-01` remains pending for Implementation 001-A.**

The current execution environment did not perform actual `databricks aitools --path` materialization. This is not represented as PASS.

001-A must establish the Databricks CLI development environment and execute/record local exact name/version validation. If materialization fails, vendor-skill convenience is degraded and developers fall back to official Databricks documentation/manual procedures while DMTZ semantics remain unchanged.

This residual requires no waiver of a DMTZ semantic/security gate and does not authorize workspace access.

## First repository CI evidence — PASS

PR #4 (`Integrate reviewed Databricks Agent Skills before ADF exit`) validated branch head `d76fcab6c92211e448d7f69bea1923118fa31a6c`.

- **Agentic conformance #36** — run ID `33710142266`, job `100507650330`: SUCCESS.
- **Documentation consistency #154** — run ID `33710142286`: SUCCESS.

Agentic conformance #36 reported:

- documentation consistency — PASS;
- OKF structure/resources — PASS, 0 errors / 0 warnings;
- tool adapters — PASS, expected provider-runtime warnings only;
- portable skills — PASS, **13 registered DMTZ skills**;
- agentic references — PASS, **30 unique accepted stable IDs**;
- ADF status drift — PASS;
- fixture/addendum catalog — PASS, **122 scenarios**;
- context budgets — PASS;
- ADF-G compatibility evidence — PASS with three expected provider-runtime-unverified warnings;
- Databricks Agent Skills addendum — PASS, **0 errors / 1 expected local-materialization-pending warning**;
- agentic secret scan — PASS, **0 errors / 143 governed text files scanned**;
- ADF-H security/lifecycle governance — PASS;
- negative controls — PASS, **12 / 12 seeded defects detected**;
- deprecated knowledge entries — 0;
- stale knowledge entries — 0.

The two Databricks-specific negative controls prove that automatic vendor-skill expansion is rejected and inserting deferred `databricks-model-serving` into the initial selected set is rejected.

## Context efficiency — PASS

Run #36 measured:

- root `AGENTS.md`: **12,243 / 16,384 bytes**;
- `.claude/CLAUDE.md`: **1,054 / 2,048 bytes**;
- Cursor rules aggregate: **20,034 / 32,768 bytes**;
- Cursor routing rule: **4,523 / 6,144 bytes**;
- Cursor root baseline: **12,243 / 20,480 bytes**;
- Claude root baseline: **13,297 / 18,432 bytes**;
- Codex root baseline: **12,243 / 16,384 bytes**;
- all six DMTZ Databricks overlays are below 2 KB and all bridges/routes remain within configured budgets.

The addendum therefore does not require a monolithic Databricks prompt or loading all vendor skills for every task.

## Relationship to ADF exit

The addendum strengthens the implementation basis for ADF-EX-03, ADF-EX-05, ADF-EX-11–16 and ADF-EX-18–20 without altering their accepted meaning.

**ADF-EX-17 remains deferred verification exactly as before.** This addendum neither closes nor broadens that waiver.

The execution exit review must consider this accepted addendum and retain `DBX-SKILL-RUN-01` as an Implementation 001-A environment obligation.

## Exit decision

**Databricks Agent Skills Integration Addendum: COMPLETE / ACCEPTED.**

Next required work after final synchronized closure CI is the **Agentic Development Foundation execution exit review**. Do not begin Implementation 001-A until that review passes under the documented gate/waiver rule.
