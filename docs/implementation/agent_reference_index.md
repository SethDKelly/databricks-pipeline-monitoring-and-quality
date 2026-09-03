# DMTZ Agent Reference Index

**Purpose:** compact secondary bridge from a task to accepted contract families, canonical document sets, and reviewed platform-development dependencies. Portable first-hop discovery begins at `knowledge/index.md`; DMTZ procedures live under `.agents/skills/`; exact stable-ID occurrence discovery follows ADF-E.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

**Pre-exit condition:** Databricks Agent Skills Integration Addendum is IN EXECUTION; the foundation execution exit review follows its closure.

Use the shortest path: explicit group/path/ID directly when known; otherwise `knowledge/index.md` → one route → canonical resource → exact IDs/tests as required. Do not load entire historical phases or all vendor skills for routine work.

## Universal start

| Need | Read first |
|---|---|
| Live Agentic Development Foundation/addendum status | `docs/agentic_development_foundation/README.md` |
| Databricks Agent Skills addendum | `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` |
| Reviewed Databricks vendor skill set | `docs/agentic_development_foundation/databricks_vendor_skills_profile.json` |
| Local Databricks skill materialization | `scripts/agentic/materialize_databricks_skills.py` |
| Foundation execution exit gates | `docs/agentic_development_foundation/execution_exit_criteria.md` |
| Shared agent/developer constitution | root `AGENTS.md` |
| Portable knowledge discovery | `knowledge/index.md` |
| Canonical DMTZ workflow/overlay | `.agents/skills/<workflow>/SKILL.md` |
| Human-directed action policy | `docs/agentic_development_foundation/authority_scope_policy.md` |
| Context discovery policy | `docs/agentic_development_foundation/context_discovery_policy.md` |
| Stable-ID policy / accepted ranges | `docs/agentic_development_foundation/stable_reference_policy.md` / `stable_id_registry.json` |
| Context budgets | `docs/agentic_development_foundation/context_budget_policy.md` |
| Agentic conformance | `docs/agentic_development_foundation/conformance_policy.md` / `scripts/agentic/run_conformance.py` |
| Tool compatibility/runtime evidence | `docs/agentic_development_foundation/tool_compatibility.json` / `runtime_compatibility_evidence.json` |
| ADF-G progression exception | `docs/agentic_development_foundation/adf_g_progression_exception.md` |
| Agentic security/change governance | `docs/agentic_development_foundation/security_trust_lifecycle_policy.md` / `agentic_change_governance.md` |
| Implementation-program status | `docs/implementation/README.md` |
| First implementation after ADF exit | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` |
| Frozen architecture handoff | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md` |
| Frozen target architecture | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md` |
| Validation strategy | `docs/implementation/validation_strategy.md` |
| Traceability/change control | `docs/implementation/traceability_and_change_control.md` |

## Agentic foundation routing

| Area | Group | Primary source |
|---|---|---|
| Authority / human-directed scope | ADF-A — COMPLETE | `authority_scope_policy.md`; `adf_a_execution_review.md` |
| Portable OKF knowledge | ADF-B — COMPLETE | `knowledge/index.md`; `okf_profile.md`; `adf_b_execution_review.md` |
| Cursor/Claude/Codex instruction adapters | ADF-C — COMPLETE | `tool_compatibility.json`; `adf_c_execution_review.md` |
| Portable DMTZ workflows / Agent Skills | ADF-D — COMPLETE | `.agents/skills/`; `portable_workflow_profile.md`; `adf_d_execution_review.md` |
| Context / stable IDs / maintenance / budgets | ADF-E — COMPLETE | `context_discovery_policy.md`; `stable_reference_policy.md`; `adf_e_execution_review.md` |
| Conformance / drift / CI | ADF-F — COMPLETE | `conformance_policy.md`; `scripts/agentic/run_conformance.py`; `adf_f_execution_review.md` |
| Cross-tool runtime compatibility / onboarding | ADF-G — ACCEPTED FOR PROGRESSION; EX-17 DEFERRED | `tool_compatibility_matrix.md`; `developer_onboarding.md`; `runtime_compatibility_evidence.json`; `adf_g_progression_exception.md` |
| Security / trust / lifecycle governance | ADF-H — COMPLETE | `security_trust_lifecycle_policy.md`; `agentic_change_governance.md`; `tool_lifecycle_review.json`; `adf_h_execution_review.md` |
| Databricks vendor skills / DMTZ overlays | PRE-EXIT ADDENDUM — IN EXECUTION | `databricks_agent_skills_addendum.md`; `databricks_vendor_skills_profile.json`; `databricks_agent_skills_addendum_execution_review.md` |
| Foundation execution exit | NEXT AFTER ADDENDUM | `execution_exit_criteria.md`; ADF-A–ADF-H/addendum execution reviews; `adf_g_progression_exception.md` |

Autonomy remains out of scope; see `autonomous_backlog.md` only when explicitly reviewing deferred future work.

## Workflow map

Core:

- `resolve-context` — A1 minimum authoritative context;
- `implement-group` — A2 one human-selected group/task, then stop;
- `resolve-contract` — A1 accepted stable-ID/semantic lookup;
- `run-conformance` — A1 safe deterministic validation by default;
- `review-change` — A1 substantive review;
- `update-traceability` — evidence-backed A2 supporting update;
- `exit-review` — A1 evaluation; bounded A2 only when recording the requested review/status artifact.

DMTZ Databricks overlays:

- `dmtz-databricks-environment-discovery` — target/CLI/workspace capability without universalizing one deployment;
- `dmtz-databricks-acquisition` — Lakeflow/Pipeline acquisition preserving partial/error/unknown semantics;
- `dmtz-databricks-persistence` — Delta realization preserving explicit knowledge-time/non-rewriting history;
- `dmtz-databricks-lineage` — UC/system Lineage without exposure/Impact/cause collapse;
- `dmtz-databricks-runtime-provenance` — Jobs/Pipelines exact identity/correlation without name/time proxies;
- `dmtz-databricks-governance` — UC privileges/access without authority/authorization collapse.

Cursor and Codex consume `.agents/skills/` directly. Claude Code uses thin `.claude/commands/` bridges. Reviewed Databricks vendor skills are locally materialized operational context under `.databricks/agent-skills/`; they are not canonical DMTZ skills.

## Databricks vendor profile

Initial reviewed set:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

Model/AI implementation skills are deferred. Automatic adoption of new upstream skills is prohibited. Managed Databricks MCP servers are a separate G3/G4 integration decision.

`DBX-SKILL-RUN-01` — actual local `aitools --path` materialization and exact reviewed version verification — is planned for Implementation 001-A once the development CLI environment exists.

## Stable-ID discipline

Accepted ranges:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

Use `scripts/agentic/resolve_stable_id.py <ID>` when exact occurrence discovery helps. Every hit is a candidate; neither first-hit order nor definition-like formatting establishes canonical ownership.

## DMTZ domain routing

| Working area | Implementation | Phase 010 architecture | Primary contract families | Key boundary |
|---|---|---|---|---|
| Canonical IDs, evidence, provenance, time, persistence | 001 B/D | Group 02 / ARCH-033–080 | REF, SYN | bitemporal/knowledge-cut non-rewriting truth |
| Identity, scope, authority, authorization, disclosure | 002 | Group 03 / ARCH-081–132 | AUTH, REF | identity / authority / permission separation |
| Databricks/GitHub acquisition, capability, coverage | 003; slice in 001-E | Group 04 / ARCH-133–190 | INTG, REF | partial/error ≠ negative fact |
| Runtime provenance, health, quality, change, Lineage, Impact | 004 | Group 05 / ARCH-191–274 | HLTH, OPS, INTG | execution/health/Lineage/exposure distinctions |
| Investigation, causal claims, historical replay | 005 | Group 06 / ARCH-275–350 | REF, OPS, EXPL | hypothesis/localization ≠ confirmation |
| Statement/Answer IR, Explanation, basis, API/UI | 006; first Statement IR in 001-F | Groups 06/08 | EXPL, AUTH | deterministic, traceable, authorization-aware projection |
| Security, deployment, observability, SLO, cost, DR | 007 | Group 08 / ARCH-421–500 | AUTH, INTG | operational health ≠ domain health |
| MVP pilot / release candidate | 008 | Group 09 | all applicable | executable proof of bounded MVP |
| Enterprise scale / optional integrations | 009 | Groups 01/04/08/09 | INTG, AUTH, EXPL | optional dependencies do not own truth |
| Execution Gate / Propagation Safeguard | 010 | Group 07 / ARCH-351–420 | OPS, REF, AUTH | decision/enforcement/execution/prevention distinctions |
| Production graduation | 011 | Groups 08/09 | all supported | actual production capability / ownership / SLO / DR evidence |

## Phase 010 group paths

1. `docs/concepts/phase_010/01_architecture_frame_environment_discovery_decision_criteria/`
2. `docs/concepts/phase_010/02_evidence_provenance_temporal_persistence_architecture/`
3. `docs/concepts/phase_010/03_identity_scope_authority_authorization_disclosure_architecture/`
4. `docs/concepts/phase_010/04_source_acquisition_adapter_synchronization_integration_health_architecture/`
5. `docs/concepts/phase_010/05_runtime_provenance_health_lineage_impact_evidence_architecture/`
6. `docs/concepts/phase_010/06_investigation_reasoning_historical_replay_explanation_architecture/`
7. `docs/concepts/phase_010/07_execution_gate_propagation_safeguard_active_control_architecture/`
8. `docs/concepts/phase_010/08_serving_security_deployment_observability_cost_architecture/`
9. `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/`

## Implementation package paths

`001_executable_foundations_walking_skeleton/` through `011_production_graduation_operational_acceptance/` live under `docs/implementation/`.

## Context-minimization rule

Expected routine context:

**root `AGENTS.md` → matching DMTZ workflow/overlay when useful → explicit path/ID directly when known; otherwise `knowledge/index.md` → one route → active group → canonical source → reviewed vendor skill only when its operational mechanic is needed → exact contracts/tests.**

Do not preload all DMTZ skills, vendor skills, OKF concepts or contract families.
