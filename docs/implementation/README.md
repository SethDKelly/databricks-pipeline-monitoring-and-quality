# DMTZ Implementation Program

**Current status: Implementation 001-A — NEXT / READY / NOT STARTED.**

The implementation program turns the accepted DMTZ semantic and architecture contracts into executable product behavior. Implementation begins only from an explicitly human-selected package/group/task and must remain subordinate to the current documentation owners reached through [`../index.md`](../index.md).

## Program sequence

| Package | Scope |
|---|---|
| [001](001_executable_foundations_walking_skeleton/README.md) | Executable foundations and walking skeleton |
| [002](002_identity_scope_authority_authorization_runtime/README.md) | Identity, scope, authority, authorization runtime |
| [003](003_source_acquisition_capability_evidence_reliability/README.md) | Source acquisition, capability evidence, reliability |
| [004](004_runtime_provenance_health_quality_change_lineage/README.md) | Runtime provenance, health, quality, change, Lineage |
| [005](005_investigation_impact_reasoning_historical_replay/README.md) | Investigation, Impact, reasoning, historical replay |
| [006](006_serving_explanation_basis_user_experience/README.md) | Serving, Explanation, basis inspection, user experience |
| [007](007_operationalization_security_resilience_slo_cost/README.md) | Operationalization, security, resilience, SLO, cost |
| [008](008_mvp_pilot_validation_release_candidate/README.md) | MVP pilot validation and release candidate |
| [009](009_enterprise_expansion_scale_optional_integrations/README.md) | Enterprise expansion, scale, optional integrations |
| [010](010_active_control_enterprise_control_plane/README.md) | Optional active-control enterprise control plane |
| [011](011_production_graduation_operational_acceptance/README.md) | Production graduation and operational acceptance |

Package sequencing expresses dependency and acceptance order; it is not permission for an agent to continue automatically from one package to the next.

## Starting implementation

Implementation 001 establishes the smallest executable spine. **001-A is the next eligible group**, but it remains not started until explicitly selected.

Before implementation work:

1. read root [`AGENTS.md`](../../AGENTS.md) and local [`AGENTS.md`](AGENTS.md);
2. read the selected package/group acceptance boundary;
3. resolve current semantic context through [`../index.md`](../index.md) and the ownership inventory;
4. resolve exact accepted IDs with `python3 scripts/agentic/resolve_stable_id.py <ID>`;
5. identify the executable evidence required to claim completion.

Use `--history` only when provenance or prior rationale is actually needed. Generated `knowledge/` content is compatibility routing only.

## Implementation rules

- Preserve accepted semantic and architecture contracts unless a governed change explicitly reopens them.
- Prefer the smallest compliant implementation over speculative framework construction.
- Add executable proof at the lowest level appropriate to the behavior being introduced.
- Keep unknown, unavailable, partial, conflicting, unauthorized, and unsupported states explicit.
- Treat vendor/platform capability as something to verify against the target environment, not something documentation alone proves.
- Update directly impacted ADRs, traceability, tests, and current documentation as implementation makes choices concrete.
- Stop at the selected package/group/task boundary and report residual obligations rather than silently rolling them forward.

Historical design, completed reviews, and documentation-normalization evidence are preserved under [`../history/`](../history/README.md); they are not routine implementation contract surfaces.
