# DMTZ Agent Reference Index

**Purpose:** compact secondary bridge from a task to accepted contract families, canonical document sets, and reviewed platform-development dependencies. Portable first-hop discovery begins at `knowledge/index.md`; DMTZ procedures live under `.agents/skills/`; exact stable-ID occurrence discovery follows ADF-E.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

The Databricks Agent Skills Integration Addendum is **COMPLETE / ACCEPTED**. The foundation execution exit review is the sole next pre-implementation gate.

Use the shortest path: explicit group/path/ID directly when known; otherwise `knowledge/index.md` → one route → canonical resource → exact IDs/tests as required. Do not load entire historical phases or all vendor skills for routine work.

## Universal start

| Need | Read first |
|---|---|
| Live Agentic Development Foundation status | `docs/agentic_development_foundation/README.md` |
| Foundation execution exit gates | `docs/agentic_development_foundation/execution_exit_criteria.md` |
| Databricks Agent Skills addendum/evidence | `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_agent_skills_addendum_execution_review.md` |
| Reviewed Databricks vendor skill set | `docs/agentic_development_foundation/databricks_vendor_skills_profile.json` |
| Local Databricks skill materialization | `scripts/agentic/materialize_databricks_skills.py` |
| Shared agent/developer constitution | root `AGENTS.md` |
| Portable knowledge discovery | `knowledge/index.md` |
| Canonical DMTZ workflow/overlay | `.agents/skills/<workflow>/SKILL.md` |
| Human-directed action policy | `docs/agentic_development_foundation/authority_scope_policy.md` |
| Context / stable-reference policy | `context_discovery_policy.md` / `stable_reference_policy.md` / `stable_id_registry.json` |
| Agentic conformance | `docs/agentic_development_foundation/conformance_policy.md` / `scripts/agentic/run_conformance.py` |
| Tool compatibility/runtime evidence | `tool_compatibility.json` / `runtime_compatibility_evidence.json` |
| ADF-G deferred-verification decision | `adf_g_progression_exception.md` |
| Agentic security/change governance | `security_trust_lifecycle_policy.md` / `agentic_change_governance.md` |
| Implementation-program status | `docs/implementation/README.md` |
| First implementation after ADF exit | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` |
| Frozen architecture handoff | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md` |
| Validation strategy / traceability | `docs/implementation/validation_strategy.md` / `traceability_and_change_control.md` |

## Agentic foundation routing

| Area | State | Primary source |
|---|---|---|
| Authority / human-directed scope | ADF-A — COMPLETE | `authority_scope_policy.md`; `adf_a_execution_review.md` |
| Portable OKF knowledge | ADF-B — COMPLETE | `knowledge/index.md`; `okf_profile.md`; `adf_b_execution_review.md` |
| Tool instruction adapters | ADF-C — COMPLETE | `tool_compatibility.json`; `adf_c_execution_review.md` |
| Portable DMTZ workflows | ADF-D — COMPLETE | `.agents/skills/`; `portable_workflow_profile.md`; `adf_d_execution_review.md` |
| Context / stable IDs / budgets | ADF-E — COMPLETE | `context_discovery_policy.md`; `stable_reference_policy.md`; `adf_e_execution_review.md` |
| Conformance / drift / CI | ADF-F — COMPLETE | `conformance_policy.md`; `run_conformance.py`; `adf_f_execution_review.md` |
| Cross-tool compatibility / onboarding | ADF-G — EX-17 DEFERRED | `runtime_compatibility_evidence.json`; `adf_g_progression_exception.md`; `adf_g_execution_review.md` |
| Security / trust / lifecycle | ADF-H — COMPLETE | `security_trust_lifecycle_policy.md`; `agentic_change_governance.md`; `adf_h_execution_review.md` |
| Databricks vendor skills / DMTZ overlays | ADDENDUM — COMPLETE | `databricks_agent_skills_addendum.md`; `databricks_vendor_skills_profile.json`; `databricks_agent_skills_addendum_execution_review.md` |
| Foundation execution exit | **NEXT** | `execution_exit_criteria.md`; ADF/addendum execution reviews; `adf_g_progression_exception.md` |

Autonomy remains out of scope; see `autonomous_backlog.md` only when explicitly reviewing deferred future work.

## Workflow map

Core DMTZ workflows:

- `resolve-context`;
- `implement-group`;
- `resolve-contract`;
- `run-conformance`;
- `review-change`;
- `update-traceability`;
- `exit-review`.

DMTZ Databricks overlays:

- `dmtz-databricks-environment-discovery`;
- `dmtz-databricks-acquisition`;
- `dmtz-databricks-persistence`;
- `dmtz-databricks-lineage`;
- `dmtz-databricks-runtime-provenance`;
- `dmtz-databricks-governance`.

Cursor and Codex consume `.agents/skills/` directly. Claude Code uses thin `.claude/commands/` bridges. Reviewed Databricks vendor skills, when materialized, live under ignored `.databricks/agent-skills/` and are supporting operational context only.

## Databricks vendor profile

Accepted initial set: `databricks-core`, `databricks-dabs`, `databricks-jobs`, `databricks-pipelines`, `databricks-data-discovery`, `databricks-dbsql`, `databricks-unity-catalog`, `databricks-lakeflow-connect`.

Model/AI implementation skills are deferred. Automatic upstream expansion is prohibited. Managed Databricks MCP servers require separate G3/G4 review.

`DBX-SKILL-RUN-01` — actual local `aitools --path` materialization and exact reviewed version verification — is an Implementation 001-A environment obligation.

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

Use `scripts/agentic/resolve_stable_id.py <ID>` when exact occurrence discovery helps. Search hits are candidates; owning canonical documents determine meaning.

## DMTZ domain routing

| Working area | Implementation | Phase 010 | Primary contracts | Key boundary |
|---|---|---|---|---|
| IDs, evidence, time, persistence | 001 B/D | ARCH-033–080 | REF, SYN | bitemporal/non-rewriting truth |
| Identity, scope, authority, disclosure | 002 | ARCH-081–132 | AUTH, REF | identity / authority / permission separation |
| Databricks/GitHub acquisition | 003; 001-E slice | ARCH-133–190 | INTG, REF | partial/error ≠ negative fact |
| Runtime, health, quality, Lineage, Impact | 004 | ARCH-191–274 | HLTH, OPS, INTG | execution/health/Lineage/exposure distinctions |
| Investigation / causal claims / replay | 005 | ARCH-275–350 | REF, OPS, EXPL | hypothesis ≠ confirmation |
| Statement/Answer IR, API/UI | 006; 001-F slice | ARCH-275–350 / 421–500 | EXPL, AUTH | deterministic, traceable projection |
| Security/deployment/SLO/cost/DR | 007 | ARCH-421–500 | AUTH, INTG | operational health ≠ domain health |
| MVP pilot | 008 | Group 09 | all applicable | executable bounded proof |
| Enterprise scale / integrations | 009 | Groups 01/04/08/09 | INTG, AUTH, EXPL | optional dependencies do not own truth |
| Gate / Safeguard | 010 | ARCH-351–420 | OPS, REF, AUTH | decision ≠ enforcement ≠ execution/prevention |
| Production graduation | 011 | Groups 08/09 | all supported | actual production evidence/ownership |

## Context-minimization rule

Expected routine context:

**root `AGENTS.md` → matching DMTZ workflow/overlay when useful → explicit path/ID directly when known; otherwise `knowledge/index.md` → one route → active group → canonical source → reviewed vendor skill only when its operational mechanic is needed → exact contracts/tests.**

Do not preload all DMTZ skills, vendor skills, OKF concepts or contract families.
