# DMTZ Implementation — Start Here

Phase 010 — Technical Architecture is complete. The implementation program is defined. Before executable product work begins, the repository is completing the **Agentic Development Foundation** so Cursor, Claude Code, Codex, and ordinary tooling operate against one shared authority/knowledge/workflow model.

## Start here

1. [`knowledge/index.md`](knowledge/index.md) — portable OKF discovery entry.
2. [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md) — live ADF status.
3. [`AGENTS.md`](AGENTS.md) — shared repository agent/developer constitution.
4. [`docs/agentic_development_foundation/authority_scope_policy.md`](docs/agentic_development_foundation/authority_scope_policy.md) — A1–A4 human-directed scope policy.
5. [`.agents/skills/`](.agents/skills/) — canonical portable DMTZ development workflows from completed ADF-D.
6. [`docs/agentic_development_foundation/portable_workflow_profile.md`](docs/agentic_development_foundation/portable_workflow_profile.md) — workflow portability/invocation contract.
7. [`docs/agentic_development_foundation/tool_compatibility.json`](docs/agentic_development_foundation/tool_compatibility.json) — Cursor/Claude Code/Codex compatibility manifest.
8. [`docs/implementation/README.md`](docs/implementation/README.md) — implementation-program status and 001–011 roadmap.
9. [`docs/implementation/001_executable_foundations_walking_skeleton/README.md`](docs/implementation/001_executable_foundations_walking_skeleton/README.md) — first product implementation package after ADF exit.
10. [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md) — secondary exact stable-ID/canonical-document bridge.
11. [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — frozen architecture handoff.

## Coding-agent guidance

- ADF-A defines common A1–A4 human-directed scope.
- ADF-B defines `knowledge/` as portable routing, not semantic authority.
- ADF-C defines thin tool adapters over shared `AGENTS.md`.
- ADF-D defines the seven canonical workflows under `.agents/skills/`.
- Cursor and Codex consume `.agents/skills/` natively; Claude Code uses thin `.claude/commands/` bridges to the same source.
- Skill selection does not create new work or expand the human-selected task.
- Tool compatibility documentation is not runtime certification; ADF-G owns live tool smoke evidence.
- Autonomous task selection, multi-agent delegation, unattended merge/deploy, and agent-created backlog work remain out of scope.

## Immediate next work

**ADF-A through ADF-D are COMPLETE / ACCEPTED.**

The next required group is:

- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance**

Remaining foundation sequence:

- ADF-F — Conformance, Validation, Drift Detection & CI
- ADF-G — Developer Tool Compatibility, Onboarding & Operating Model
- ADF-H — Security, Trust, Lifecycle & Governance
- Agentic Development Foundation execution exit review

Only after that exit, proceed to **Implementation 001-A — Developer Environment, Repository Structure & Engineering Standards**.

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts remain authoritative throughout; neither OKF routing, skills, agent tooling, nor implementation convenience supersedes them.
