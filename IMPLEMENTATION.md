# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture, ADF-A through ADF-H, the Databricks Agent Skills Integration Addendum, and the **Agentic Development Foundation Execution Exit Review** are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

## Start here

1. [`docs/implementation/README.md`](docs/implementation/README.md) — live implementation-program authority.
2. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — Implementation 001 package authority.
3. [`docs/agentic_development_foundation/execution_exit_review.md`](docs/agentic_development_foundation/execution_exit_review.md) — accepted foundation exit and residual debt.
4. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — completed ADF/addendum authority.
5. [`docs/agentic_development_foundation/adf_g_progression_exception.md`](docs/agentic_development_foundation/adf_g_progression_exception.md) — ADF-EX-17 bounded waiver.
6. [`docs/agentic_development_foundation/databricks_agent_skills_addendum_execution_review.md`](docs/agentic_development_foundation/databricks_agent_skills_addendum_execution_review.md) — Databricks skill integration evidence and `DBX-SKILL-RUN-01` handoff.
7. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
8. [`knowledge/index.md`](knowledge/index.md) — portable discovery when needed.
9. [`.agents/skills/`](.agents/skills/) — canonical DMTZ workflows and Databricks overlays.
10. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path/platform bridge.
11. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Foundation exit disposition

The accepted `execution_exit_review.md` records:

- ADF-EX-01–ADF-EX-16 — **PASS**;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — **PASS**;
- Databricks Agent Skills Integration Addendum — **ACCEPTED**;
- `ADF-G-XT01` — **OPEN / CARRIED FORWARD**;
- `DBX-SKILL-RUN-01` — **OPEN / IMPLEMENTATION 001-A**;
- autonomous development — **DEFERRED / NOT AUTHORIZED**.

Cursor, Claude Code and Codex remain runtime-`unverified`; the waiver is not provider runtime support. Ordinary IDE/CLI development remains supported.

## Next eligible work

**Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards: NEXT / ELIGIBLE.**

001-A owns the first actual Databricks CLI/vendor-skill environment verification (`DBX-SKILL-RUN-01`). Beginning 001-A still requires an explicit human-selected task; foundation exit does not auto-start it.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This reports agentic **configuration conformance only**. It is not DMTZ domain health, data quality, target Databricks capability, provider-runtime certification or production readiness.

## Databricks skill composition

- vendor dependency authority: `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_vendor_skills_profile.json`;
- canonical DMTZ overlays: `.agents/skills/dmtz-databricks-*`;
- local vendor materialization: ignored `.databricks/agent-skills/` through `scripts/agentic/materialize_databricks_skills.py`;
- reviewed vendor skills: core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect;
- model/AI implementation skills remain deferred;
- automatic vendor-skill expansion is prohibited;
- managed Databricks MCP servers require later explicit security/integration review;
- vendor instructions cannot create workspace permission, semantic authority or A3/A4 authorization.

## Coding-agent boundaries

- skill selection does not create new project scope;
- `ADF-G-XT01` remains future provider-runtime verification debt;
- autonomous task selection, multi-agent implementation delegation, unattended merge/deploy and agent-created backlog work remain out of scope;
- accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative over code, tooling and vendor guidance;
- design-scenario PASS, agentic conformance PASS and vendor documentation are not substitutes for executable product/target evidence.
