# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. ADF-A through ADF-H are complete, and the repository is executing a bounded **Databricks Agent Skills Integration Addendum** before the Agentic Development Foundation execution exit review.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live ADF/addendum execution authority.
2. [`docs/agentic_development_foundation/databricks_agent_skills_addendum.md`](docs/agentic_development_foundation/databricks_agent_skills_addendum.md) — reviewed Databricks vendor-skill composition and DMTZ overlay boundary.
3. [`docs/agentic_development_foundation/databricks_vendor_skills_profile.json`](docs/agentic_development_foundation/databricks_vendor_skills_profile.json) — exact reviewed vendor skill set/versions.
4. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
5. [`docs/agentic_development_foundation/execution_exit_criteria.md`](docs/agentic_development_foundation/execution_exit_criteria.md) — ADF-EX-01–ADF-EX-20 gates, evaluated after the addendum closes.
6. [`docs/agentic_development_foundation/adf_g_progression_exception.md`](docs/agentic_development_foundation/adf_g_progression_exception.md) — bounded ADF-EX-17 deferred-verification exception.
7. [`knowledge/index.md`](knowledge/index.md) — portable OKF discovery when the canonical path is not already known.
8. [`.agents/skills/`](.agents/skills/) — canonical DMTZ workflows and Databricks platform overlays.
9. [`docs/agentic_development_foundation/conformance_policy.md`](docs/agentic_development_foundation/conformance_policy.md) — unified agentic validation/failure semantics.
10. [`docs/agentic_development_foundation/security_trust_lifecycle_policy.md`](docs/agentic_development_foundation/security_trust_lifecycle_policy.md) — security/trust/lifecycle policy.
11. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
12. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path/platform bridge.
13. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Agentic foundation state

Completed / accepted for exit review:

- ADF-A — Authority, Scope & Human-Directed Operating Boundary;
- ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile;
- ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract;
- ADF-D — Portable Skills & Human-Directed Workflow Contract;
- ADF-E — Context Discovery, Stable References & Knowledge Maintenance;
- ADF-F — Conformance, Validation, Drift Detection & CI;
- ADF-G — Developer Tool Compatibility, Onboarding & Operating Model — accepted for progression with **ADF-EX-17 deferred verification**;
- ADF-H — Security, Trust, Lifecycle & Governance.

Current pre-exit work:

- **Databricks Agent Skills Integration Addendum — IN EXECUTION.** The reviewed initial set includes core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI implementation skills are deferred. Vendor skills remain lower-authority operational guidance and are materialized locally under `.databricks/agent-skills/`; DMTZ-owned overlays remain canonical under `.agents/skills/`.

Cursor, Claude Code and Codex remain runtime-`unverified` until actual `ADF-G-XT01` evidence is recorded. The Databricks addendum does not promote those states.

Next required work after addendum closure:

- **Agentic Development Foundation execution exit review** — evaluate ADF-EX-01–ADF-EX-20 and explicitly decide the bounded ADF-EX-17 waiver;
- **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards** becomes eligible only if the foundation exit passes.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This command reports agentic **configuration conformance only**. It is not DMTZ domain health, data quality, target Databricks capability, coding-agent runtime proof, or production readiness.

## Databricks skills boundary

- Reviewed vendor profile: `docs/agentic_development_foundation/databricks_vendor_skills_profile.json`.
- DMTZ overlays: `dmtz-databricks-environment-discovery`, `dmtz-databricks-acquisition`, `dmtz-databricks-persistence`, `dmtz-databricks-lineage`, `dmtz-databricks-runtime-provenance`, and `dmtz-databricks-governance`.
- Local materialization helper: `python3 scripts/agentic/materialize_databricks_skills.py`; actual materialization/version proof is an Implementation 001-A environment check.
- Vendor instructions cannot authorize workspace access, deployment, governance changes, credentials, or A3/A4 actions.
- Automatic adoption of newly published Databricks skills is prohibited.
- Model/AI skills and managed Databricks MCP servers are outside the initial addendum.

## Coding-agent boundaries

- ADF-A defines A1–A4 human-directed scope.
- ADF-B defines `knowledge/` as routing, not truth.
- ADF-C keeps provider adapters thin over shared authority.
- ADF-D keeps DMTZ workflow meaning under `.agents/skills/`.
- ADF-E requires shortest-path discovery, exact stable-ID lookup and context budgets.
- ADF-F makes agentic invariants mechanically checkable and CI-gated.
- ADF-G preserves tool-neutral onboarding while keeping missing runtime evidence explicit.
- ADF-H governs least privilege, sensitive-data, trust, lifecycle, retention and memory boundaries.
- The Databricks addendum composes reviewed vendor operational knowledge beneath those controls; it does not create a new semantic authority.
- Autonomous task selection, multi-agent implementation delegation, unattended merge/deploy, and agent-created backlog work remain out of scope.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout. Agent tooling, OKF routing, DMTZ/vendor skills, security configuration and CI may not silently supersede them.
