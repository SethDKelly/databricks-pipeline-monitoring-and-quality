# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. The implementation program is defined. Before executable product work begins, the repository is establishing the **Agentic Development Foundation** so developers can use Cursor, Claude Code, Codex, or ordinary tooling against one shared authority/knowledge/workflow model.

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live pre-implementation enabling foundation and ADF execution status.
2. [`docs/agentic_development_foundation/authority_scope_policy.md`](docs/agentic_development_foundation/authority_scope_policy.md) — accepted human-directed authority/action policy from completed ADF-A.
3. [`docs/agentic_development_foundation/adf_a_execution_review.md`](docs/agentic_development_foundation/adf_a_execution_review.md) — ADF-A execution evidence and closure.
4. [`docs/agentic_development_foundation/design_exit_review.md`](docs/agentic_development_foundation/design_exit_review.md) — accepted overall foundation design exit review.
5. [`docs/implementation/enterprise_team_handoff.md`](docs/implementation/enterprise_team_handoff.md) — team prerequisites, roles, pilot topology and onboarding.
6. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
7. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — first executable product implementation package after the Agentic Development Foundation exits.
8. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact task-to-contract routing; it will be integrated with the OKF knowledge plane during ADF-B/E execution.
9. [`docs/implementation/technology_baseline.md`](docs/implementation/technology_baseline.md) — reference stack and version-pinning expectations.
10. [`docs/implementation/validation_strategy.md`](docs/implementation/validation_strategy.md) — design-scenario to executable-test strategy.
11. [`docs/implementation/traceability_and_change_control.md`](docs/implementation/traceability_and_change_control.md) — frozen-contract change control.
12. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — immediate frozen architecture handoff.

## Coding-agent guidance

- Root [`AGENTS.md`](AGENTS.md) remains the shared repository constitution.
- Completed ADF-A establishes common A1–A4 action classes and human-directed scope in [`authority_scope_policy.md`](docs/agentic_development_foundation/authority_scope_policy.md).
- `.cursor/rules/*.mdc` remains a scoped Cursor adapter layer rather than a second source of truth.
- ADF-B will implement the portable OKF v0.2 knowledge plane; ADF-C will implement thin Cursor/Claude/Codex adapter mechanics against the ADF-A policy.
- Autonomous task execution, multi-agent delegation/orchestration, unattended merge/deploy and agent-created work allocation are **not** part of the accepted foundation; see the deferred autonomous backlog only if that work is explicitly reopened later.

## Immediate next work

**ADF-A is COMPLETE / ACCEPTED.**

The next eligible groups are:

- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract**

They may proceed in either order or overlap according to the accepted ADF dependency model.

Remaining foundation sequence:

- ADF-D — Portable Skills & Human-Directed Workflow Contract
- ADF-E — Context Discovery, Stable References & Knowledge Maintenance
- ADF-F — Conformance, Validation, Drift Detection & CI
- ADF-G — Developer Tool Compatibility, Onboarding & Operating Model
- ADF-H — Security, Trust, Lifecycle & Governance

After the implemented Agentic Development Foundation passes its execution exit review, proceed to **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards**.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout; neither agentic tooling nor implementation convenience supersedes them.
