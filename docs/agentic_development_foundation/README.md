# DMTZ Agentic Development Foundation

**Status:** IN EXECUTION — ADF-A / ADF-B / ADF-C / ADF-D / ADF-E COMPLETE; ADF-F NEXT

## Purpose

The Agentic Development Foundation establishes a tool-neutral, human-directed development model for using coding agents with DMTZ before Implementation 001 begins. It is an enabling foundation, not a new product/concept/architecture phase and not a replacement for the frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract stack.

The target outcome is that a developer may choose Cursor, Claude Code, Codex, or another compatible coding agent and receive the same project authority, knowledge-routing, workflow, validation and safety model without maintaining separate semantic copies for each tool.

## Current execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.** See [`adf_a_execution_review.md`](adf_a_execution_review.md).
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.** See [`adf_b_execution_review.md`](adf_b_execution_review.md) and [`../../knowledge/index.md`](../../knowledge/index.md).
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.** See [`adf_c_execution_review.md`](adf_c_execution_review.md) and [`tool_compatibility.json`](tool_compatibility.json).
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.** See [`adf_d_execution_review.md`](adf_d_execution_review.md), [`portable_workflow_profile.md`](portable_workflow_profile.md), and `.agents/skills/`.
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.** See [`adf_e_execution_review.md`](adf_e_execution_review.md), [`context_discovery_policy.md`](context_discovery_policy.md), and [`stable_reference_policy.md`](stable_reference_policy.md).
- **ADF-F — Conformance, Validation, Drift Detection & CI: NEXT / READY.**
- ADF-G–ADF-H remain planned behind their dependency gates.
- Implementation 001 remains planned and follows the implemented Agentic Development Foundation exit.

ADF-A established shared authority, ADF-B portable knowledge routing, ADF-C thin tool adapters, ADF-D one portable human-directed workflow source, and ADF-E deterministic context/reference/maintenance discipline. ADF-F now integrates those artifacts into a single conformance/CI path.

## Boundary

This foundation includes:

- portable knowledge discovery and progressive disclosure using an OKF v0.2-compatible knowledge bundle;
- shared project instruction authority rooted in `AGENTS.md`;
- thin tool-specific adapters for Cursor, Claude Code and Codex;
- portable, human-directed Agent Skills/workflows;
- stable-ID and canonical-document retrieval discipline;
- context-budget and context-bloat controls;
- validation, drift detection and CI checks for agent configuration/knowledge/workflow artifacts;
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

Those topics remain only in [`autonomous_backlog.md`](autonomous_backlog.md).

## Authority, knowledge, adapter, workflow and retrieval model

The shared ADF-A policy is [`authority_scope_policy.md`](authority_scope_policy.md).

Authority order:

1. accepted DMTZ functional/integration/technical contracts and canonical `docs/`;
2. root `AGENTS.md`;
3. live implementation status/package or active ADF status;
4. accepted Agentic Development Foundation mechanics;
5. tool-specific adapters only for native mechanics;
6. personal/user-level tool preferences and tool memory.

The ADF-B OKF bundle begins at [`../../knowledge/index.md`](../../knowledge/index.md). It is a routing projection, never semantic authority.

ADF-C tool access:

- Cursor: root `AGENTS.md` + scoped `.cursor/rules/*.mdc`;
- Claude Code: `.claude/CLAUDE.md` importing `../AGENTS.md`;
- Codex: root `AGENTS.md` natively;
- all tools: `knowledge/index.md` for portable discovery.

ADF-D workflow access:

- canonical workflows: `.agents/skills/<name>/SKILL.md`;
- Cursor: native `.agents/skills/` discovery;
- Claude Code: thin `.claude/commands/<name>.md` bridges to the canonical skills;
- Codex: native `.agents/skills/` discovery.

ADF-E retrieval/maintenance controls:

- shortest-path discovery: [`context_discovery_policy.md`](context_discovery_policy.md);
- accepted stable-ID ranges/exact lookup: [`stable_reference_policy.md`](stable_reference_policy.md) + [`stable_id_registry.json`](stable_id_registry.json);
- deterministic context budgets: [`context_budget_policy.md`](context_budget_policy.md) + [`context_budget.json`](context_budget.json);
- canonical-change routing review: [`knowledge_maintenance_workflow.md`](knowledge_maintenance_workflow.md).

Initial workflows remain:

- `resolve-context`;
- `implement-group`;
- `resolve-contract`;
- `run-conformance`;
- `review-change`;
- `update-traceability`;
- `exit-review`.

No OKF entry, skill, Cursor rule, Claude adapter, generated index, stable-ID registry, context budget, or tool memory may become an independent source of DMTZ semantic truth.

ADF-A action classes remain controlling:

- A1 read/review/plan;
- A2 change/build/fix;
- A3 external/destructive/scope-expanding;
- A4 architecture/semantic change.

A tool may implicitly select a matching skill inside a human-selected task; that does not create new scope, permission, or autonomy.

## External standards baseline

Current standards/tool assumptions are recorded in [`external_standards_baseline.md`](external_standards_baseline.md):

- OKF v0.2 reverified during ADF-B;
- Cursor instructions/adapters reverified during ADF-C and Agent Skills during ADF-D;
- Claude Code instructions/adapters reverified during ADF-C and skills/commands during ADF-D;
- Codex `AGENTS.md` behavior reverified during ADF-C and `.agents/skills` behavior during ADF-D.

Documentation verification remains distinct from ADF-G runtime smoke verification.

## Execution groups

1. **ADF-A — Authority, Scope & Human-Directed Operating Boundary — COMPLETE**
2. **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile — COMPLETE**
3. **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract — COMPLETE**
4. **ADF-D — Portable Skills & Human-Directed Workflow Contract — COMPLETE**
5. **ADF-E — Context Discovery, Stable References & Knowledge Maintenance — COMPLETE**
6. **ADF-F — Conformance, Validation, Drift Detection & CI — NEXT**
7. **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model**
8. **ADF-H — Security, Trust, Lifecycle & Governance**

## Dependency sequence

ADF-A–ADF-E are complete.

ADF-F is now the next required group. It integrates deterministic validation/drift controls and the ADF-A–E scenario corpus into repository conformance/CI, including the agentic configuration-health report required by ADF-EX-16.

ADF-G performs actual tool-in-the-loop Cursor/Claude Code/Codex compatibility exercises.

ADF-H consolidates long-term security/trust/lifecycle governance and review horizons.

The design exit review is [`design_exit_review.md`](design_exit_review.md). The later foundation implementation exit gate is [`execution_exit_criteria.md`](execution_exit_criteria.md).

## Implemented/planned repository shape

```text
/
├── AGENTS.md
├── IMPLEMENTATION.md
├── knowledge/
├── .agents/
│   └── skills/                   # ADF-D canonical portable workflows
├── .cursor/
│   ├── rules/                    # ADF-C scoped adapters
│   └── BUGBOT.md
├── .claude/
│   ├── CLAUDE.md                 # ADF-C shared-authority bridge
│   └── commands/                 # ADF-D thin workflow bridges
├── docs/agentic_development_foundation/
│   ├── stable_id_registry.json   # ADF-E accepted ID ranges
│   └── context_budget.json       # ADF-E byte budgets
├── docs/
└── scripts/agentic/              # ADF-B–E deterministic helper/validation seams
```

No root `CLAUDE.md` is used. No duplicated DMTZ workflow set is placed under `.claude/skills/`.

## Foundation success condition

The foundation is implemented successfully when the same bounded development task can be opened in Cursor, Claude Code and Codex and each tool can, with minimal tool-specific configuration:

1. identify current project/implementation authority;
2. find the smallest relevant DMTZ contract/document set;
3. invoke the same human-directed workflow semantics;
4. respect the same non-negotiable boundaries;
5. produce changes validated by the same repository checks;
6. avoid loading the entire design corpus by default;
7. avoid creating a competing tool-specific source of truth.

Autonomy is not part of this success condition.
