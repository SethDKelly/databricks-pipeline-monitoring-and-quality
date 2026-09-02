# DMTZ Agentic Development Foundation

**Status:** IN EXECUTION — ADF-A / ADF-B COMPLETE; ADF-C NEXT

## Purpose

The Agentic Development Foundation establishes a tool-neutral, human-directed development model for using coding agents with DMTZ before Implementation 001 begins. It is an enabling foundation, not a new product/concept/architecture phase and not a replacement for the frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract stack.

The target outcome is that a developer may choose Cursor, Claude Code, Codex, or another compatible coding agent and receive the same project authority, knowledge-routing, workflow, validation and safety model without maintaining separate semantic copies for each tool.

## Current execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.** See [`adf_a_execution_review.md`](adf_a_execution_review.md).
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.** See [`adf_b_execution_review.md`](adf_b_execution_review.md) and the portable [`../../knowledge/index.md`](../../knowledge/index.md) bundle.
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: NEXT / READY.**
- ADF-D–ADF-H remain planned behind their dependency gates.
- Implementation 001 remains planned and follows the implemented Agentic Development Foundation exit.

ADF-B established the portable knowledge plane. ADF-C must now make Cursor, Claude Code and Codex consume the same shared authority and knowledge entry points without creating semantic copies.

## Boundary

This foundation includes:

- portable knowledge discovery and progressive disclosure using an OKF v0.2-compatible knowledge bundle;
- shared project instruction authority rooted in `AGENTS.md`;
- thin tool-specific adapters for Cursor, Claude Code and Codex;
- portable, human-invoked development skills/workflows;
- stable-ID and canonical-document retrieval discipline;
- context-budget and context-bloat controls;
- validation, drift detection and CI checks for agent configuration/knowledge artifacts;
- developer onboarding and tool-choice compatibility;
- security, provenance, trust and lifecycle rules for agent-facing knowledge.

This foundation explicitly excludes:

- unattended/autonomous implementation;
- agent-created work allocation or backlog prioritization;
- multi-agent delegation/orchestration;
- automatic spawning of agents/subagents for repository work;
- unattended merging, deployment or external writes;
- autonomous architecture reopening;
- agent-to-agent coordination protocols;
- agent memory as canonical project truth.

Those topics are retained only in [`autonomous_backlog.md`](autonomous_backlog.md).

## Authority and knowledge model

The shared ADF-A policy is [`authority_scope_policy.md`](authority_scope_policy.md).

The authority order is:

1. accepted DMTZ functional/integration/technical contracts and canonical `docs/`;
2. root `AGENTS.md` for repository-wide agent/developer behavior;
3. live implementation status/package or active ADF status;
4. accepted Agentic Development Foundation mechanics;
5. tool-specific adapters only for mechanics unique to that tool;
6. personal/user-level tool preferences and tool memory.

The ADF-B OKF bundle begins at [`../../knowledge/index.md`](../../knowledge/index.md). It is a routing projection over higher authority, never a new semantic authority.

No OKF entry, skill, Cursor rule, Claude rule, generated index or tool memory may become an independent source of DMTZ semantic truth.

ADF-A established four common action classes:

- A1 read/review/plan;
- A2 change/build/fix;
- A3 external/destructive/scope-expanding;
- A4 architecture/semantic change.

See [`tool_adapter_authority_checklist.md`](tool_adapter_authority_checklist.md), [`okf_profile.md`](okf_profile.md), and the ADF-A/B fixtures for downstream adapter/conformance inputs.

## External standards baseline

The foundation targets:

- **Open Knowledge Format v0.2** from the upstream GoogleCloudPlatform `knowledge-catalog` specification, reverified during ADF-B;
- Cursor project rules and `AGENTS.md` support;
- Claude Code `CLAUDE.md`, `.claude/rules/` and `SKILL.md` support;
- Codex `AGENTS.md`-based repository guidance and portable skill compatibility where supported.

Vendor/tool behavior is version-sensitive. [`external_standards_baseline.md`](external_standards_baseline.md) records what is assumed and what must be reverified during execution.

## Execution groups

1. **ADF-A — Authority, Scope & Human-Directed Operating Boundary — COMPLETE**
2. **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile — COMPLETE**
3. **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract — NEXT**
4. **ADF-D — Portable Skills & Human-Directed Workflow Contract**
5. **ADF-E — Context Discovery, Stable References & Knowledge Maintenance**
6. **ADF-F — Conformance, Validation, Drift Detection & CI**
7. **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model**
8. **ADF-H — Security, Trust, Lifecycle & Governance**

Detailed plans are in the corresponding files in this directory.

## Dependency sequence

ADF-A authority and ADF-B knowledge representation are complete.

ADF-C is now the next required group. ADF-D and ADF-E consume A–C: workflows and refined discovery must know both where authority lives and how each supported tool reaches it.

ADF-F validates the resulting artifacts and prevents drift.

ADF-G proves that a human developer can use Cursor, Claude Code or Codex without semantic divergence.

ADF-H consolidates security/trust/lifecycle rules across the whole foundation.

The design exit review is [`design_exit_review.md`](design_exit_review.md). The later implementation exit gate is [`execution_exit_criteria.md`](execution_exit_criteria.md).

## Implemented/planned repository shape

```text
/
├── AGENTS.md                     # shared repository constitution
├── CLAUDE.md                     # ADF-C planned thin Claude adapter
├── IMPLEMENTATION.md
├── knowledge/                    # IMPLEMENTED in ADF-B
│   ├── index.md
│   ├── project/
│   ├── domains/
│   ├── implementation/
│   └── workflows/
├── agent-skills/                 # ADF-D planned canonical workflows
├── .cursor/
│   ├── rules/                    # existing scoped Cursor adapters
│   └── BUGBOT.md
├── .claude/                      # ADF-C/D only where native mechanics require it
├── docs/                         # canonical DMTZ source of truth
└── scripts/agentic/              # ADF-B validator; later ADF-F expansion
```

## Foundation success condition

The foundation is implemented successfully when the same bounded development task can be opened in Cursor, Claude Code and Codex and each tool can, with minimal tool-specific configuration:

1. identify current project/implementation authority;
2. find the smallest relevant DMTZ contract/document set;
3. invoke the same human-directed workflow semantics;
4. respect the same non-negotiable boundaries;
5. produce changes that are validated by the same repository tests/conformance checks;
6. avoid loading the entire design corpus by default;
7. avoid creating a competing tool-specific source of truth.

Autonomy is not part of this success condition.
