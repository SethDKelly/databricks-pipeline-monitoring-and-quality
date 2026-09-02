# DMTZ Agent Reference Index

**Purpose:** give developers and coding agents a compact routing surface from a task to the smallest authoritative document/contract set needed to work safely.

Do **not** load every historical phase for routine work. Follow the live status, then the active Agentic Development Foundation or implementation group, then exact stable IDs when deeper semantics are required.

## Universal start

| Need | Read first |
|---|---|
| Repository implementation/agentic entry | `IMPLEMENTATION.md` |
| Current implementation status | `docs/implementation/README.md` |
| Current pre-implementation agentic work | `docs/agentic_development_foundation/README.md` |
| Shared engineering/agent constitution | root `AGENTS.md` |
| Human-directed authority/action policy | `docs/agentic_development_foundation/authority_scope_policy.md` |
| Agentic knowledge/tool/workflow design | `docs/agentic_development_foundation/` |
| Active first product implementation | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` after ADF exit |
| Frozen implementation handoff | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md` |
| Frozen target/reference architecture | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md` |
| Validation/test strategy | `docs/implementation/validation_strategy.md` |
| Technology defaults | `docs/implementation/technology_baseline.md` |
| Traceability/change control | `docs/implementation/traceability_and_change_control.md` |
| Completion profiles | `docs/implementation/completion_definition.md` |

## Agentic foundation routing

| Working area | ADF group | Primary source |
|---|---|---|
| Agent authority / human-directed action boundary | ADF-A — COMPLETE | `docs/agentic_development_foundation/authority_scope_policy.md`; execution evidence in `adf_a_execution_review.md` |
| OKF v0.2 portable knowledge plane | ADF-B — NEXT | `docs/agentic_development_foundation/02_adf_b_okf_knowledge_plane.md` |
| Cursor/Claude/Codex instruction adapters | ADF-C — NEXT | `docs/agentic_development_foundation/03_adf_c_instruction_tool_adapters.md` |
| Portable human-directed workflows/skills | ADF-D | `docs/agentic_development_foundation/04_adf_d_portable_skills_workflows.md` |
| Context/stable-ID discovery and routing maintenance | ADF-E | `docs/agentic_development_foundation/05_adf_e_context_reference_maintenance.md` |
| Agentic validation/drift/CI | ADF-F | `docs/agentic_development_foundation/06_adf_f_conformance_validation_ci.md` |
| Cross-tool onboarding/compatibility | ADF-G | `docs/agentic_development_foundation/07_adf_g_tool_compatibility_operating_model.md` |
| Security/trust/lifecycle governance | ADF-H | `docs/agentic_development_foundation/08_adf_h_security_trust_lifecycle_governance.md` |

During ADF execution, autonomy is out of scope. See `docs/agentic_development_foundation/autonomous_backlog.md` only when explicitly reviewing deferred future work.

## DMTZ domain routing

| Working area | Implementation package | Phase 010 architecture | Primary earlier contract families | Key concern |
|---|---|---|---|---|
| Canonical IDs, evidence, provenance, time, persistence | 001 B/D | Group 02 / ARCH-033–080 | REF-001–030, SYN | bitemporal/knowledge-cut non-rewriting truth |
| Identity, scope, authority, authorization, disclosure | 002 | Group 03 / ARCH-081–132 | AUTH-001–053, REF | identity and permission/authority separation |
| Databricks/GitHub acquisition, capability, coverage | 003 (walking slice in 001-E) | Group 04 / ARCH-133–190 | INTG-001–270, REF | partial/error ≠ negative domain fact |
| Runtime/deployment provenance, health, quality, change, Lineage, Impact | 004 | Group 05 / ARCH-191–274 | HLTH-001–066, OPS-001–123, INTG | execution/health/Lineage/exposure distinctions |
| Investigation, causal claims, historical replay | 005 | Group 06 / ARCH-275–350 | REF, OPS, EXPL | hypothesis/localization ≠ confirmation; as-known replay |
| Statement/Answer IR, Explanation, basis, API/UI | 006 (first Statement IR in 001-F) | Groups 06/08 / ARCH-275–350, 421–500 | EXPL-001–160, AUTH | deterministic, traceable, authorization-aware projection |
| Security, deployment, observability, SLO, cost, DR | 007 | Group 08 / ARCH-421–500 | AUTH, INTG | operational health ≠ domain health; explicit degradation |
| MVP pilot / release candidate validation | 008 | Group 09 consolidation | all applicable | executable proof of bounded MVP profile |
| Enterprise scale/optional Collibra/Immuta/search/model | 009 | Groups 01/04/08/09 as relevant | INTG/AUTH/EXPL | optional dependencies do not become hidden truth owners |
| Execution Gate / Propagation Safeguard | 010 | Group 07 / ARCH-351–420 | OPS/REF/AUTH | decision/enforcement/execution/prevention distinctions |
| Production graduation / operational acceptance | 011 | Group 09 + Group 08 | all supported profile | actual production capability, ownership, SLO, DR evidence |

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

## Stable-ID search discipline

When a task or test references an ID, search that exact ID in `docs/` rather than loading an entire phase.

Examples:

- `REF-004` — locate the exact bounded coverage / negative-evidence contract;
- `AUTH-034` — use the exact accepted authority contract when confirmation/authority is involved;
- `HLTH-030` — locate the exact normative Expectation/Assessment contract;
- `OPS-067` — locate the exact operational/Impact proposition;
- `EXPL-101` — locate the exact Explanation contract;
- `INTG-145` — locate the exact integration/source evidence contract;
- `ARCH-017` — locate the exact architecture contract.

Do not treat examples or OKF summaries as substitutes for the exact contract text.

## Implementation package paths

- `docs/implementation/001_executable_foundations_walking_skeleton/`
- `docs/implementation/002_identity_scope_authority_authorization_runtime/`
- `docs/implementation/003_source_acquisition_capability_evidence_reliability/`
- `docs/implementation/004_runtime_provenance_health_quality_change_lineage/`
- `docs/implementation/005_investigation_impact_reasoning_historical_replay/`
- `docs/implementation/006_serving_explanation_basis_user_experience/`
- `docs/implementation/007_operationalization_security_resilience_slo_cost/`
- `docs/implementation/008_mvp_pilot_validation_release_candidate/`
- `docs/implementation/009_enterprise_expansion_scale_optional_integrations/`
- `docs/implementation/010_active_control_enterprise_control_plane/`
- `docs/implementation/011_production_graduation_operational_acceptance/`

## Context-minimization rule

Until ADF-B/E replaces this index with or integrates it into the OKF knowledge plane, the expected routine context stack is:

**root `AGENTS.md` → `authority_scope_policy.md` when scope/action is material → active scoped tool rule/adapter → active ADF or implementation group → one domain routing source → one or two canonical architecture/reference documents → exact stable contracts/tests as needed.**

Do not proactively load all SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documentation.
