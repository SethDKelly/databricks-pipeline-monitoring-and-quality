# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. The implementation program is defined. Before executable product work begins, the repository is establishing the **Agentic Development Foundation** so developers can use Cursor, Claude Code, Codex, or ordinary tooling against one shared authority/knowledge/workflow model.

## Start here

1. [`knowledge/index.md`](knowledge/index.md) — portable OKF v0.2 discovery entry for project, domain, implementation and workflow routing.
2. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live pre-implementation enabling foundation and ADF execution status.
3. [`docs/agentic_development_foundation/authority_scope_policy.md`](docs/agentic_development_foundation/authority_scope_policy.md) — accepted human-directed authority/action policy from completed ADF-A.
4. [`docs/agentic_development_foundation/tool_compatibility.json`](docs/agentic_development_foundation/tool_compatibility.json) — current Cursor/Claude Code/Codex adapter compatibility manifest from completed ADF-C.
5. [`docs/agentic_development_foundation/adf_c_execution_review.md`](docs/agentic_development_foundation/adf_c_execution_review.md) — ADF-C repository-adapter execution evidence and closure.
6. [`docs/agentic_development_foundation/okf_profile.md`](docs/agentic_development_foundation/okf_profile.md) — accepted DMTZ OKF v0.2 producer profile from completed ADF-B.
7. [`docs/implementation/enterprise_team_handoff.md`](docs/implementation/enterprise_team_handoff.md) — team prerequisites, roles, pilot topology and onboarding.
8. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
9. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — first executable product implementation package after the Agentic Development Foundation exits.
10. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — secondary stable-ID/canonical-document bridge complementing the OKF routing bundle.
11. [`docs/implementation/technology_baseline.md`](docs/implementation/technology_baseline.md) — reference stack and version-pinning expectations.
12. [`docs/implementation/validation_strategy.md`](docs/implementation/validation_strategy.md) — design-scenario to executable-test strategy.
13. [`docs/implementation/traceability_and_change_control.md`](docs/implementation/traceability_and_change_control.md) — frozen-contract change control.
14. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — immediate frozen architecture handoff.

## Coding-agent guidance

- Root [`AGENTS.md`](AGENTS.md) remains the shared repository constitution.
- Completed ADF-A establishes common A1–A4 action classes and human-directed scope.
- Completed ADF-B establishes `knowledge/` as a portable routing projection over canonical authority.
- Completed ADF-C establishes thin adapters: Cursor uses root `AGENTS.md` + scoped `.cursor/rules`; Claude Code uses `.claude/CLAUDE.md` importing shared authority; Codex uses root `AGENTS.md` natively.
- Tool compatibility facts live in `tool_compatibility.json`; documentation verification is distinct from ADF-G runtime smoke verification.
- Autonomous task execution, multi-agent delegation/orchestration, unattended merge/deploy and agent-created work allocation are **not** part of the accepted foundation.

## Immediate next work

**ADF-A, ADF-B and ADF-C are COMPLETE / ACCEPTED.**

The next eligible groups are:

- **ADF-D — Portable Skills & Human-Directed Workflow Contract**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance**

They may proceed in either order or overlap according to the accepted dependency model.

Remaining foundation sequence:

- ADF-F — Conformance, Validation, Drift Detection & CI
- ADF-G — Developer Tool Compatibility, Onboarding & Operating Model
- ADF-H — Security, Trust, Lifecycle & Governance

After the implemented Agentic Development Foundation passes its execution exit review, proceed to **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards**.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout; neither OKF routing, agent tooling nor implementation convenience supersedes them.
