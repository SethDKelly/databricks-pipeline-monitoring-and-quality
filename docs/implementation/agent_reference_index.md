# DMTZ Agent Reference Index

**Purpose:** compact secondary bridge from a task to accepted contract families, canonical document sets, active implementation authority, and reviewed platform-development dependencies. First-hop discovery begins at `knowledge/index.md` only when an explicit path/ID is not already known; procedures live under `.agents/skills/`.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

The Agentic Development Foundation execution exit and Databricks Agent Skills Integration Addendum are complete/accepted. **Implementation 001-A is the next eligible group.**

Use the shortest path: explicit group/path/ID directly when known; otherwise `knowledge/index.md` → one route → canonical resource → exact IDs/tests as required. Do not load entire historical phases or all vendor skills for routine work.

## Universal start

| Need | Read first |
|---|---|
| Live implementation status | `docs/implementation/README.md` |
| Implementation 001 package | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` |
| Foundation exit decision | `docs/agentic_development_foundation/execution_exit_review.md` |
| Completed ADF/addendum authority | `docs/agentic_development_foundation/README.md` |
| ADF exit gate definitions | `docs/agentic_development_foundation/execution_exit_criteria.md` |
| ADF-EX-17 bounded waiver | `docs/agentic_development_foundation/adf_g_progression_exception.md` |
| Runtime compatibility evidence | `docs/agentic_development_foundation/runtime_compatibility_evidence.json` |
| Databricks Agent Skills addendum/evidence | `docs/agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_agent_skills_addendum_execution_review.md` |
| Reviewed Databricks vendor set | `docs/agentic_development_foundation/databricks_vendor_skills_profile.json` |
| Local Databricks skill materialization | `scripts/agentic/materialize_databricks_skills.py` |
| Shared agent/developer constitution | root `AGENTS.md` |
| Portable knowledge discovery | `knowledge/index.md` |
| Canonical workflow/overlay | `.agents/skills/<workflow>/SKILL.md` |
| Human-directed action policy | `docs/agentic_development_foundation/authority_scope_policy.md` |
| Context / stable-reference policy | `context_discovery_policy.md` / `stable_reference_policy.md` / `stable_id_registry.json` |
| Agentic conformance | `docs/agentic_development_foundation/conformance_policy.md` / `scripts/agentic/run_conformance.py` |
| Security/change governance | `security_trust_lifecycle_policy.md` / `agentic_change_governance.md` |
| Frozen architecture handoff | `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md` |
| Validation strategy / traceability | `docs/implementation/validation_strategy.md` / `traceability_and_change_control.md` |

## Agentic foundation disposition

| Area | State | Primary source |
|---|---|---|
| Authority / human-directed scope | ADF-A — COMPLETE | `authority_scope_policy.md`; `adf_a_execution_review.md` |
| Portable OKF knowledge | ADF-B — COMPLETE | `knowledge/index.md`; `okf_profile.md`; `adf_b_execution_review.md` |
| Tool instruction adapters | ADF-C — COMPLETE | `tool_compatibility.json`; `adf_c_execution_review.md` |
| Portable DMTZ workflows | ADF-D — COMPLETE | `.agents/skills/`; `portable_workflow_profile.md`; `adf_d_execution_review.md` |
| Context / stable IDs / budgets | ADF-E — COMPLETE | `context_discovery_policy.md`; `stable_reference_policy.md`; `adf_e_execution_review.md` |
| Conformance / drift / CI | ADF-F — COMPLETE | `conformance_policy.md`; `run_conformance.py`; `adf_f_execution_review.md` |
| Cross-tool compatibility / onboarding | ADF-G — COMPLETE; EX-17 DEFERRED | `runtime_compatibility_evidence.json`; `adf_g_progression_exception.md`; `adf_g_execution_review.md` |
| Security / trust / lifecycle | ADF-H — COMPLETE | `security_trust_lifecycle_policy.md`; `agentic_change_governance.md`; `adf_h_execution_review.md` |
| Databricks vendor skills / overlays | ADDENDUM — COMPLETE | `databricks_agent_skills_addendum.md`; `databricks_vendor_skills_profile.json`; addendum review |
| Foundation execution exit | **ACCEPTED** | `execution_exit_review.md` |
| Next implementation | **001-A — NEXT / ELIGIBLE** | `001_executable_foundations_walking_skeleton/README.md` |

`ADF-G-XT01` remains provider-runtime verification debt. Cursor, Claude Code and Codex remain runtime-`unverified` until actual evidence exists. This does not block ordinary IDE/CLI development under the accepted bounded waiver.

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

`DBX-SKILL-RUN-01` — actual local `aitools --path` materialization and exact reviewed-version verification — is an **Implementation 001-A** environment obligation.

## Accepted stable-ID families

Use `docs/agentic_development_foundation/stable_id_registry.json` and `scripts/agentic/resolve_stable_id.py` for exact occurrence discovery. Accepted ranges remain:

- SYN-001–035;
- REF-001–030;
- AUTH-001–053;
- HLTH-001–066;
- OPS-001–123;
- EXPL-001–160;
- INTG-001–270;
- ARCH-001–500.

Search results are candidates; canonical ownership comes from accepted repository authority, not first-match order.
