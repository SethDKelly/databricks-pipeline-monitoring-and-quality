# DMTZ Agent Reference Index

**Purpose:** provide a compact secondary bridge from a task to accepted contract families and canonical document sets. Portable first-hop discovery begins at `knowledge/index.md`; reusable task procedures live under `.agents/skills/`; exact stable-ID occurrence discovery follows ADF-E.

Do **not** load every historical phase for routine work. Prefer the shortest path: use an explicit group/path/ID directly when known; otherwise use `knowledge/index.md` → one category/concept → canonical resource, then exact stable IDs as required.

## Universal start

| Need | Read first |
|---|---|
| Portable knowledge discovery | `knowledge/index.md` |
| Portable development workflow | `.agents/skills/<workflow>/SKILL.md` |
| Repository implementation/agentic entry | `IMPLEMENTATION.md` |
| Current implementation status | `docs/implementation/README.md` |
| Current pre-implementation agentic work | `docs/agentic_development_foundation/README.md` |
| Shared engineering/agent constitution | root `AGENTS.md` |
| Human-directed authority/action policy | `docs/agentic_development_foundation/authority_scope_policy.md` |
| Context discovery policy | `docs/agentic_development_foundation/context_discovery_policy.md` |
| Stable-ID resolution policy | `docs/agentic_development_foundation/stable_reference_policy.md` |
| Accepted stable-ID ranges | `docs/agentic_development_foundation/stable_id_registry.json` |
| Context-size budgets | `docs/agentic_development_foundation/context_budget_policy.md` |
| Tool compatibility state | `docs/agentic_development_foundation/tool_compatibility.json` |
| Portable workflow profile | `docs/agentic_development_foundation/portable_workflow_profile.md` |
| DMTZ OKF producer profile | `docs/agentic_development_foundation/okf_profile.md` |
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
| Agent authority / human-directed action boundary | ADF-A — COMPLETE | `docs/agentic_development_foundation/authority_scope_policy.md`; `adf_a_execution_review.md` |
| OKF v0.2 portable knowledge plane | ADF-B — COMPLETE | `knowledge/index.md`; `okf_profile.md`; `adf_b_execution_review.md` |
| Cursor/Claude/Codex instruction adapters | ADF-C — COMPLETE | `tool_compatibility.json`; `adf_c_execution_review.md` |
| Portable human-directed workflows/skills | ADF-D — COMPLETE | `.agents/skills/`; `portable_workflow_profile.md`; `adf_d_execution_review.md` |
| Context/stable-ID discovery and routing maintenance | ADF-E — COMPLETE | `context_discovery_policy.md`; `stable_reference_policy.md`; `context_budget_policy.md`; `adf_e_execution_review.md` |
| Agentic validation/drift/CI | ADF-F — NEXT | `docs/agentic_development_foundation/06_adf_f_conformance_validation_ci.md` |
| Cross-tool onboarding/compatibility | ADF-G | `docs/agentic_development_foundation/07_adf_g_tool_compatibility_operating_model.md` |
| Security/trust/lifecycle governance | ADF-H | `docs/agentic_development_foundation/08_adf_h_security_trust_lifecycle_governance.md` |

Autonomy is out of scope. See `docs/agentic_development_foundation/autonomous_backlog.md` only when explicitly reviewing deferred future work.

## Workflow routing

- `resolve-context` — shortest-path minimum current authority/context; A1, no edits.
- `implement-group` — implement one human-selected task/group; A2, then stop.
- `resolve-contract` — validate accepted range, locate every exact occurrence, then identify canonical meaning through live authority; A1.
- `run-conformance` — safe deterministic checks/reporting; A1 by default.
- `review-change` — substantive read-only review; A1.
- `update-traceability` — evidence-backed A2 supporting update.
- `exit-review` — A1 evaluation; A2 only when explicitly recording the bounded review/status artifact.

Cursor and Codex consume `.agents/skills/` directly. Claude Code uses thin `.claude/commands/` bridges to the same source. Native runtime behavior remains ADF-G evidence.

## Tool adapter routing

- Cursor: root `AGENTS.md` + scoped `.cursor/rules/*.mdc` + `.agents/skills/`.
- Claude Code: `.claude/CLAUDE.md` imports `../AGENTS.md`; `.claude/commands/` bridges to `.agents/skills/`.
- Codex: root `AGENTS.md` + `.agents/skills/` natively; no parallel semantic rulebook.
- Portable discovery: `knowledge/index.md` for all supported tools when location is not already known.
- Repository/static validators/helpers: `scripts/agentic/validate_okf.py`, `validate_agent_adapters.py`, `validate_agent_skills.py`, `resolve_stable_id.py`, `measure_context_budget.py`, `knowledge_impact.py`.
- Runtime compatibility: ADF-G.

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
| Enterprise scale/optional Collibra/Immuta/search/model | 009 | Groups 01/04/08/09 | INTG/AUTH/EXPL | optional dependencies do not become hidden truth owners |
| Execution Gate / Propagation Safeguard | 010 | Group 07 / ARCH-351–420 | OPS/REF/AUTH | decision/enforcement/execution/prevention distinctions |
| Production graduation / operational acceptance | 011 | Group 09 + Group 08 | all supported profile | actual production capability, ownership, SLO, DR evidence |

The same domains are represented as portable OKF concepts under `knowledge/domains/`; this table remains useful for contract-family/range orientation.

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

Accepted ranges are defined machine-readably in `docs/agentic_development_foundation/stable_id_registry.json`.

When an exact ID is known:

1. validate family/range;
2. search the exact token under `docs/`;
3. return all exact occurrences rather than only the first match;
4. treat mechanical `definition_candidate` classification as a retrieval hint only;
5. identify canonical meaning from the accepted owning document/live repository authority;
6. read only the surrounding section required for the task.

`scripts/agentic/resolve_stable_id.py <ID>` performs deterministic range/occurrence discovery when a local checkout is available.

Examples:

- `REF-004` — accepted REF family lookup;
- `AUTH-034` — accepted AUTH family lookup;
- `HLTH-030` — accepted HLTH family lookup;
- `OPS-067` — accepted OPS family lookup;
- `EXPL-101` — accepted EXPL family lookup;
- `INTG-145` — accepted INTG family lookup;
- `ARCH-017` — accepted ARCH family lookup.

Do not infer the contract meaning from these labels, the OKF route, this index, or search order. The exact accepted source owns the semantics.

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

Expected routine context is the shortest sufficient subset of:

**root `AGENTS.md` → matching `.agents/skills/` workflow when useful → explicit path/ID directly when known; otherwise `knowledge/index.md` → one category/concept → active scoped tool adapter/group → canonical resource → exact stable contracts/tests.**

Do not preload all skills, OKF concepts, Cursor rules, or SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documentation. Deterministic byte budgets live in `docs/agentic_development_foundation/context_budget.json`.
