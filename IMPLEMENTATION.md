# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. Before executable product work begins, the repository is completing the **Agentic Development Foundation** so Cursor, Claude Code, Codex, and ordinary tooling operate against one shared authority/knowledge/workflow/conformance model.

**ADF status mirror: COMPLETE ADF-A–ADF-F; IN EXECUTION ADF-G.**

## Start here

1. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live ADF execution authority.
2. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
3. [`knowledge/index.md`](knowledge/index.md) — portable OKF discovery when the canonical path is not already known.
4. [`.agents/skills/`](.agents/skills/) — canonical human-directed development workflows.
5. [`docs/agentic_development_foundation/conformance_policy.md`](docs/agentic_development_foundation/conformance_policy.md) — unified agentic validation/failure semantics.
6. [`docs/agentic_development_foundation/tool_compatibility.json`](docs/agentic_development_foundation/tool_compatibility.json) — Cursor/Claude Code/Codex compatibility state.
7. [`docs/agentic_development_foundation/runtime_compatibility_evidence.json`](docs/agentic_development_foundation/runtime_compatibility_evidence.json) — ADF-G provider runtime evidence ledger.
8. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
9. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — compact stable-ID/path bridge.
10. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Agentic foundation state

Completed and accepted:

- ADF-A — Authority, Scope & Human-Directed Operating Boundary;
- ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile;
- ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract;
- ADF-D — Portable Skills & Human-Directed Workflow Contract;
- ADF-E — Context Discovery, Stable References & Knowledge Maintenance;
- ADF-F — Conformance, Validation, Drift Detection & CI.

Current required group:

- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: IN EXECUTION.** Repository/onboarding compatibility and ordinary IDE/CLI viability are implemented; actual Cursor, Claude Code and Codex runtime smokes remain unverified until `ADF-G-XT01` is executed in those provider runtimes.

Then, after ADF-G acceptance:

- ADF-H — Security, Trust, Lifecycle & Governance;
- Agentic Development Foundation execution exit review;
- **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards** only after the foundation exit passes.

## Common conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This command reports agentic **configuration conformance only**. It is not DMTZ domain health, data quality, source health, runtime correctness, or production readiness. Provider runtime verification remains independent ADF-G evidence.

## Coding-agent boundaries

- ADF-A defines common A1–A4 human-directed scope.
- ADF-B defines `knowledge/` as routing, not truth.
- ADF-C keeps tool adapters thin over shared `AGENTS.md`.
- ADF-D keeps workflow meaning under `.agents/skills/`.
- ADF-E requires shortest-path discovery, exact accepted stable-ID lookup, and deterministic context budgets.
- ADF-F makes those repository configuration invariants mechanically checkable and CI-gated.
- ADF-G proves tool-neutral onboarding/repository compatibility and requires actual provider runtime evidence before acceptance.
- Skill selection does not create new project scope.
- Autonomous task selection, multi-agent implementation delegation, unattended merge/deploy, and agent-created backlog work remain out of scope.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout. Agent tooling, OKF routing, workflows, test convenience, and CI configuration may not silently supersede them.