# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture, ADF-A through ADF-H, and the bounded **Databricks Agent Skills Integration Addendum** are complete. The next required work is the **Agentic Development Foundation execution exit review** before executable product work begins.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live ADF/addendum authority.
2. [`docs/agentic_development_foundation/execution_exit_criteria.md`](docs/agentic_development_foundation/execution_exit_criteria.md) — ADF-EX-01–ADF-EX-20 gates.
3. [`docs/agentic_development_foundation/adf_g_progression_exception.md`](docs/agentic_development_foundation/adf_g_progression_exception.md) — bounded ADF-EX-17 deferred-verification exception.
4. [`docs/agentic_development_foundation/databricks_agent_skills_addendum_execution_review.md`](docs/agentic_development_foundation/databricks_agent_skills_addendum_execution_review.md) — accepted Databricks skill integration evidence and `DBX-SKILL-RUN-01` handoff.
5. [`docs/agentic_development_foundation/databricks_vendor_skills_profile.json`](docs/agentic_development_foundation/databricks_vendor_skills_profile.json) — exact reviewed vendor set/versions.
6. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
7. [`knowledge/index.md`](knowledge/index.md) — portable OKF discovery when needed.
8. [`.agents/skills/`](.agents/skills/) — canonical DMTZ workflows and Databricks overlays.
9. [`docs/agentic_development_foundation/conformance_policy.md`](docs/agentic_development_foundation/conformance_policy.md) — unified agentic validation.
10. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and roadmap.
11. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path/platform bridge.
12. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Foundation state

Completed / accepted for exit review:

- ADF-A through ADF-F — authority, knowledge, adapters, workflows, context/reference discipline and conformance;
- ADF-G — compatibility/onboarding baseline, with **ADF-EX-17 deferred verification**;
- ADF-H — security, trust, lifecycle and governance;
- **Databricks Agent Skills Integration Addendum — COMPLETE / ACCEPTED.**

The accepted Databricks initial vendor set is core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI implementation skills remain deferred. Managed Databricks MCP servers remain outside the addendum.

Cursor, Claude Code and Codex are still runtime-`unverified` until actual `ADF-G-XT01` evidence is recorded. The Databricks addendum does not alter that condition.

`DBX-SKILL-RUN-01` is an explicit Implementation 001-A environment obligation: establish a compatible Databricks CLI and record exact local `aitools --path` materialization/version evidence. It is not required to pretend target Databricks runtime capability exists before 001-A.

## Next required work

- **Agentic Development Foundation execution exit review** — evaluate ADF-EX-01–ADF-EX-20, explicitly decide the bounded ADF-EX-17 waiver, include the accepted Databricks addendum in the evidence set, and carry `DBX-SKILL-RUN-01` into 001-A if the exit passes.
- **Implementation 001-A** becomes eligible only after that exit review accepts the foundation.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This reports agentic **configuration conformance only**. It is not DMTZ domain health, data quality, target Databricks capability, provider-runtime certification or production readiness.

## Databricks skill composition

- vendor dependency authority: `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_vendor_skills_profile.json`;
- canonical DMTZ overlays: `.agents/skills/dmtz-databricks-*`;
- local vendor materialization: ignored `.databricks/agent-skills/` through `scripts/agentic/materialize_databricks_skills.py`;
- vendor skills remain lower-authority operational guidance;
- automatic adoption of new upstream skills is prohibited;
- model/AI skills and managed Databricks MCP servers require later explicit review;
- vendor instructions cannot create workspace permission, semantic authority or A3/A4 authorization.

## Coding-agent boundaries

- skill selection does not create new project scope;
- autonomous task selection, multi-agent implementation delegation, unattended merge/deploy and agent-created backlog work remain out of scope;
- accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative over code, agent tooling and vendor guidance;
- design-scenario PASS, agentic conformance PASS and vendor documentation are not substitutes for executable product/target evidence.
