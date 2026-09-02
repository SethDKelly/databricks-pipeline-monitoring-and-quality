# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. The implementation program is defined. Before executable product work begins, the repository will establish the **Agentic Development Foundation** so developers can use Cursor, Claude Code, Codex, or ordinary tooling against one shared authority/knowledge/workflow model.

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — immediate pre-implementation enabling foundation and ADF-A–ADF-H execution plan.
2. [`docs/agentic_development_foundation/design_exit_review.md`](docs/agentic_development_foundation/design_exit_review.md) — accepted foundation design exit review.
3. [`docs/implementation/enterprise_team_handoff.md`](docs/implementation/enterprise_team_handoff.md) — team prerequisites, roles, pilot topology and onboarding.
4. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
5. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — first executable product implementation package after the Agentic Development Foundation exits.
6. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact task-to-contract routing; it will be integrated with the OKF knowledge plane during ADF execution.
7. [`docs/implementation/technology_baseline.md`](docs/implementation/technology_baseline.md) — reference stack and version-pinning expectations.
8. [`docs/implementation/validation_strategy.md`](docs/implementation/validation_strategy.md) — design-scenario to executable-test strategy.
9. [`docs/implementation/traceability_and_change_control.md`](docs/implementation/traceability_and_change_control.md) — frozen-contract change control.
10. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — immediate frozen architecture handoff.

## Coding-agent guidance

- Root [`AGENTS.md`](AGENTS.md) remains the shared repository constitution.
- `.cursor/rules/*.mdc` remains a scoped Cursor adapter layer rather than a second source of truth.
- The Agentic Development Foundation designs a portable OKF v0.2 knowledge plane plus human-directed workflow/skill layer and thin Cursor/Claude/Codex adapters.
- Autonomous task execution, multi-agent delegation/orchestration, unattended merge/deploy and agent-created work allocation are **not** part of the accepted foundation; see the deferred autonomous backlog only if that work is explicitly reopened later.

## Immediate next work

**ADF-A — Authority, Scope & Human-Directed Operating Boundary**

The full enabling sequence is:

- ADF-A — Authority, Scope & Human-Directed Operating Boundary
- ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile
- ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract
- ADF-D — Portable Skills & Human-Directed Workflow Contract
- ADF-E — Context Discovery, Stable References & Knowledge Maintenance
- ADF-F — Conformance, Validation, Drift Detection & CI
- ADF-G — Developer Tool Compatibility, Onboarding & Operating Model
- ADF-H — Security, Trust, Lifecycle & Governance

After the implemented Agentic Development Foundation passes its execution exit review, proceed to **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards**.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout; neither agentic tooling nor implementation convenience supersedes them.
