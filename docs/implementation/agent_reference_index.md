# DMTZ Agent Reference Index

**Purpose:** give developers and coding agents a compact routing surface from an implementation task to the smallest authoritative document/contract set needed to work safely.

Do **not** load every historical phase for routine work. Start here, follow the active implementation package, then search stable IDs when a deeper rule is required.

## Universal start

| Need | Read first |
|---|---|
| Current implementation status | `docs/implementation/README.md` |
| Repository implementation entry | `IMPLEMENTATION.md` |
| Engineering/agent discipline | `docs/implementation/AGENTS.md` and root `AGENTS.md` |
| Active first package | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` |
| Frozen implementation handoff | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md` |
| Frozen target/reference architecture | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md` |
| Validation/test strategy | `docs/implementation/validation_strategy.md` |
| Technology defaults | `docs/implementation/technology_baseline.md` |
| Traceability/change control | `docs/implementation/traceability_and_change_control.md` |
| Completion profiles | `docs/implementation/completion_definition.md` |

## Domain routing

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

- `REF-004` — bounded coverage / negative evidence requirements;
- `AUTH-034` — use the exact accepted authority contract text where causal confirmation/authority is involved;
- `HLTH-030` — locate the normative Expectation/Assessment contract;
- `OPS-067` — locate the exact operational/Impact proposition;
- `EXPL-101` — locate the exact audience/authorization Explanation contract;
- `INTG-145` — locate the exact integration/source evidence contract;
- `ARCH-017` — locate the exact architecture decision/contract.

Do not treat the examples above as summaries of those contracts; the exact document is authoritative.

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

For routine implementation, the expected context stack is:

**root `AGENTS.md` → active scoped Cursor rule → active implementation group → one or two domain architecture/reference documents → exact stable contracts/tests as needed.**

Do not proactively load all SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documentation.
