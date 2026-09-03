# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. Before executable product work begins, the repository is completing the **Agentic Development Foundation** so Cursor, Claude Code, Codex, and ordinary tooling operate against one shared authority/knowledge/workflow/conformance model.

**ADF status mirror: COMPLETE ADF-A–ADF-G (ADF-EX-17 deferred); IN EXECUTION ADF-H.**

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live ADF execution authority.
2. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
3. [`knowledge/index.md`](knowledge/index.md) — portable OKF discovery when the canonical path is not already known.
4. [`.agents/skills/`](.agents/skills/) — canonical human-directed development workflows.
5. [`docs/agentic_development_foundation/conformance_policy.md`](docs/agentic_development_foundation/conformance_policy.md) — unified agentic validation/failure semantics.
6. [`docs/agentic_development_foundation/security_trust_lifecycle_policy.md`](docs/agentic_development_foundation/security_trust_lifecycle_policy.md) — agentic security/trust/lifecycle policy.
7. [`docs/agentic_development_foundation/tool_compatibility.json`](docs/agentic_development_foundation/tool_compatibility.json) — documented tool compatibility state.
8. [`docs/agentic_development_foundation/runtime_compatibility_evidence.json`](docs/agentic_development_foundation/runtime_compatibility_evidence.json) — provider runtime evidence ledger.
9. [`docs/agentic_development_foundation/adf_g_progression_exception.md`](docs/agentic_development_foundation/adf_g_progression_exception.md) — bounded ADF-EX-17 deferred-verification exception.
10. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
11. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path bridge.
12. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Agentic foundation state

Completed/accepted for progression:

- ADF-A — Authority, Scope & Human-Directed Operating Boundary;
- ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile;
- ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract;
- ADF-D — Portable Skills & Human-Directed Workflow Contract;
- ADF-E — Context Discovery, Stable References & Knowledge Maintenance;
- ADF-F — Conformance, Validation, Drift Detection & CI;
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model — accepted for progression with ADF-EX-17 deferred verification.** Cursor, Claude Code and Codex remain runtime-`unverified` until actual `ADF-G-XT01` evidence is recorded.

Current required group:

- **ADF-H — Security, Trust, Lifecycle & Governance: IN EXECUTION.**

Then:

- Agentic Development Foundation execution exit review, explicitly classifying ADF-EX-17 as deferred/waived rather than passed unless provider evidence has appeared;
- **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards** only after the foundation exit passes under the documented gate/waiver rule.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This command reports agentic **configuration conformance only**. It is not DMTZ domain health, data quality, source health, runtime correctness, or production readiness. Provider runtime verification remains independently recorded.

## Coding-agent boundaries

- ADF-A defines common A1–A4 human-directed scope.
- ADF-B defines `knowledge/` as routing, not truth.
- ADF-C keeps tool adapters thin over shared `AGENTS.md`.
- ADF-D keeps workflow meaning under `.agents/skills/`.
- ADF-E requires shortest-path discovery, exact accepted stable-ID lookup, and deterministic context budgets.
- ADF-F makes repository agentic invariants mechanically checkable and CI-gated.
- ADF-G establishes tool-neutral onboarding/repository compatibility while keeping missing provider runtime evidence explicit.
- ADF-H governs least privilege, secrets/sensitive data, trust, lifecycle, retention and tool-memory boundaries.
- Skill selection does not create new project scope.
- Autonomous task selection, multi-agent implementation delegation, unattended merge/deploy, and agent-created backlog work remain out of scope.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout. Agent tooling, OKF routing, workflows, test convenience, security configuration and CI may not silently supersede them.