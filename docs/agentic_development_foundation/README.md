# DMTZ Agentic Development Foundation

**Status:** IN EXECUTION — ADF-A / ADF-B / ADF-C COMPLETE; ADF-D / ADF-E NEXT

## Purpose

The Agentic Development Foundation establishes a tool-neutral, human-directed development model for using coding agents with DMTZ before Implementation 001 begins. It is an enabling foundation, not a new product/concept/architecture phase and not a replacement for the frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract stack.

The target outcome is that a developer may choose Cursor, Claude Code, Codex, or another compatible coding agent and receive the same project authority, knowledge-routing, workflow, validation and safety model without maintaining separate semantic copies for each tool.

## Current execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.** See [`adf_a_execution_review.md`](adf_a_execution_review.md).
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.** See [`adf_b_execution_review.md`](adf_b_execution_review.md) and the portable [`../../knowledge/index.md`](../../knowledge/index.md) bundle.
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.** See [`adf_c_execution_review.md`](adf_c_execution_review.md) and [`tool_compatibility.json`](tool_compatibility.json).
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: NEXT / READY.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: NEXT / READY.**
- ADF-F–ADF-H remain planned behind their dependency gates.
- Implementation 001 remains planned and follows the implemented Agentic Development Foundation exit.

ADF-A established shared authority, ADF-B established portable knowledge routing, and ADF-C established thin tool adapters. ADF-D and ADF-E may now realize portable workflows and refine discovery/maintenance over those shared foundations.

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

## Authority, knowledge and adapter model

The shared ADF-A policy is [`authority_scope_policy.md`](authority_scope_policy.md).

The authority order is:

1. accepted DMTZ functional/integration/technical contracts and canonical `docs/`;
2. root `AGENTS.md` for repository-wide agent/developer behavior;
3. live implementation status/package or active ADF status;
4. accepted Agentic Development Foundation mechanics;
5. tool-specific adapters only for mechanics unique to that tool;
6. personal/user-level tool preferences and tool memory.

The ADF-B OKF bundle begins at [`../../knowledge/index.md`](../../knowledge/index.md). It is a routing projection over higher authority, never a new semantic authority.

ADF-C realizes tool access as follows:

- Cursor: root `AGENTS.md` + scoped `.cursor/rules/*.mdc`;
- Claude Code: `.claude/CLAUDE.md` importing `../AGENTS.md`;
- Codex: root `AGENTS.md` natively;
- all tools: `knowledge/index.md` for portable first-hop discovery when needed.

No OKF entry, skill, Cursor rule, Claude rule, generated index or tool memory may become an independent source of DMTZ semantic truth.

ADF-A established four common action classes:

- A1 read/review/plan;
- A2 change/build/fix;
- A3 external/destructive/scope-expanding;
- A4 architecture/semantic change.

See [`tool_adapter_authority_checklist.md`](tool_adapter_authority_checklist.md), [`okf_profile.md`](okf_profile.md), [`tool_compatibility.json`](tool_compatibility.json), and the ADF-A/B/C fixtures for downstream workflow/conformance inputs.

## External standards baseline

The foundation currently targets:

- **Open Knowledge Format v0.2** from the upstream GoogleCloudPlatform `knowledge-catalog` specification, reverified during ADF-B;
- current Cursor `AGENTS.md` / scoped project-rule behavior, reverified during ADF-C;
- current Claude Code `.claude/CLAUDE.md`, imports, rules and skills behavior, reverified during ADF-C;
- current Codex `AGENTS.md` repository guidance behavior, reverified during ADF-C.

Vendor/tool behavior is version-sensitive. [`external_standards_baseline.md`](external_standards_baseline.md) records the compatibility facts and the separation between documentation verification and later runtime smoke verification.

## Execution groups

1. **ADF-A — Authority, Scope & Human-Directed Operating Boundary — COMPLETE**
2. **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile — COMPLETE**
3. **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract — COMPLETE**
4. **ADF-D — Portable Skills & Human-Directed Workflow Contract — NEXT**
5. **ADF-E — Context Discovery, Stable References & Knowledge Maintenance — NEXT**
6. **ADF-F — Conformance, Validation, Drift Detection & CI**
7. **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model**
8. **ADF-H — Security, Trust, Lifecycle & Governance**

Detailed plans are in the corresponding files in this directory.

## Dependency sequence

ADF-A authority, ADF-B knowledge representation, and ADF-C tool-adapter realization are complete.

ADF-D and ADF-E may now proceed in either order or overlap where useful: workflows need the shared adapters/knowledge plane, while refined retrieval/maintenance can be developed independently over the same completed A–C foundation.

ADF-F validates the resulting artifacts and prevents drift.

ADF-G proves that a human developer can use Cursor, Claude Code or Codex without semantic divergence.

ADF-H consolidates security/trust/lifecycle rules across the whole foundation.

The design exit review is [`design_exit_review.md`](design_exit_review.md). The later implementation exit gate is [`execution_exit_criteria.md`](execution_exit_criteria.md).

## Implemented/planned repository shape

```text
/
├── AGENTS.md                     # shared repository constitution
├── IMPLEMENTATION.md
├── knowledge/                    # IMPLEMENTED in ADF-B
│   ├── index.md
│   ├── project/
│   ├── domains/
│   ├── implementation/
│   └── workflows/
├── agent-skills/                 # ADF-D planned canonical workflows
├── .cursor/
│   ├── rules/                    # scoped Cursor adapters
│   └── BUGBOT.md
├── .claude/
│   └── CLAUDE.md                 # IMPLEMENTED in ADF-C; imports ../AGENTS.md
├── docs/                         # canonical DMTZ source of truth
└── scripts/agentic/              # OKF + adapter validators; later ADF-F expansion
```

No root `CLAUDE.md` is used: current Cursor also reads a root `CLAUDE.md`, so `.claude/CLAUDE.md` avoids duplicate persistent Cursor context while remaining a supported Claude Code project-instruction location.

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
