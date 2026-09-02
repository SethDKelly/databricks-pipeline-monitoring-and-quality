# DMTZ Agentic Development Foundation

**Status:** IN EXECUTION — ADF-A THROUGH ADF-F COMPLETE / ACCEPTED; ADF-G IN EXECUTION / PROVIDER RUNTIME EVIDENCE PENDING

## Purpose

The Agentic Development Foundation establishes a tool-neutral, human-directed development model for Cursor, Claude Code, Codex, and ordinary development before Implementation 001 begins. It is enabling infrastructure, not a new DMTZ product/concept/architecture phase and not a replacement for the frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract stack.

## Current execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**
- **ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: IN EXECUTION — REPOSITORY/ONBOARDING BASELINE IMPLEMENTED; PROVIDER RUNTIME SMOKES PENDING.**
- **ADF-H — Security, Trust, Lifecycle & Governance: PLANNED.**

**ADF status mirror: COMPLETE ADF-A–ADF-F; IN EXECUTION ADF-G.**

Implementation 001 remains planned and blocked until ADF-G, ADF-H, and the foundation execution exit review are complete.

## Implemented foundation model

### Authority and human direction — ADF-A

Shared authority is rooted in canonical `docs/`, root `AGENTS.md`, live ADF/implementation status, accepted ADF mechanics, then thin tool adapters. A1–A4 action classes preserve human-selected task scope and prevent autonomous continuation, external/destructive action without explicit authorization, or silent semantic change.

### Portable knowledge — ADF-B

`knowledge/index.md` is an OKF v0.2 portable routing plane. It is never an independent source of DMTZ truth, authority, health, evidence sufficiency, or causality.

### Tool adapters — ADF-C

- Cursor: root `AGENTS.md` + scoped `.cursor/rules/*.mdc`;
- Claude Code: `.claude/CLAUDE.md` importing `../AGENTS.md`;
- Codex: root `AGENTS.md` natively.

`tool_compatibility.json` records documented compatibility state. Actual installed-tool behavior remains ADF-G evidence.

### Human-directed workflows — ADF-D

Canonical workflows live once under `.agents/skills/`:

- `resolve-context`;
- `implement-group`;
- `resolve-contract`;
- `run-conformance`;
- `review-change`;
- `update-traceability`;
- `exit-review`.

Cursor and Codex consume the canonical location directly. Claude Code uses thin `.claude/commands/` bridges. Workflow or skill selection does not create new work scope.

### Context and stable references — ADF-E

Use the shortest authoritative path: explicit path/ID when known, otherwise one OKF route to the canonical resource, then exact stable IDs/tests as needed. `stable_id_registry.json`, `resolve_stable_id.py`, `context_budget.json`, `measure_context_budget.py`, and `knowledge_impact.py` make reference/budget/maintenance behavior deterministic without becoming semantic authority.

### Conformance and CI — ADF-F

`conformance_policy.md` defines the canonical conformance semantics. The repository-owned command is:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

It composes documentation consistency, OKF, adapter, skill, canonical-reference, ADF-status, fixture, context-budget, compatibility-evidence, and negative-control checks. `.github/workflows/agentic-conformance.yml` runs the same path in CI.

The report describes **agentic configuration conformance only**. It is not DMTZ domain health, data quality, source health, application correctness, or production readiness.

### Compatibility and onboarding — ADF-G (in execution)

Repository-level portability and the ordinary IDE/CLI path are implemented. `developer_onboarding.md`, `tool_compatibility_matrix.md`, `adf_g_runtime_probe.md`, and `runtime_compatibility_evidence.json` define one shared onboarding/runtime evidence model. Cursor, Claude Code and Codex remain runtime-unverified until the same bounded exercise is performed in actual provider runtimes.

## Foundation boundary

Included:

- shared repository agent authority;
- portable OKF discovery/progressive disclosure;
- thin Cursor/Claude/Codex adapters;
- portable human-directed skills/workflows;
- exact stable-ID/canonical-reference retrieval;
- context budgets;
- deterministic agentic conformance/drift/CI;
- developer tool compatibility/onboarding;
- security/trust/lifecycle governance.

Explicitly excluded:

- unattended/autonomous implementation;
- agent-created backlog/work allocation;
- multi-agent implementation delegation/orchestration;
- automatic spawning of repository implementation agents;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- agent memory as canonical project truth.

Deferred autonomy remains only in [`autonomous_backlog.md`](autonomous_backlog.md).

## Key references

- [`authority_scope_policy.md`](authority_scope_policy.md)
- [`okf_profile.md`](okf_profile.md)
- [`tool_compatibility.json`](tool_compatibility.json)
- [`tool_compatibility_matrix.md`](tool_compatibility_matrix.md)
- [`developer_onboarding.md`](developer_onboarding.md)
- [`adf_g_runtime_probe.md`](adf_g_runtime_probe.md)
- [`runtime_compatibility_evidence.json`](runtime_compatibility_evidence.json)
- [`portable_workflow_profile.md`](portable_workflow_profile.md)
- [`context_discovery_policy.md`](context_discovery_policy.md)
- [`stable_reference_policy.md`](stable_reference_policy.md)
- [`context_budget_policy.md`](context_budget_policy.md)
- [`conformance_policy.md`](conformance_policy.md)
- [`compatibility_smoke_checklist.md`](compatibility_smoke_checklist.md)
- [`execution_exit_criteria.md`](execution_exit_criteria.md)

Execution evidence for completed groups is in `adf_a_execution_review.md` through `adf_f_execution_review.md`; ADF-G's current partial evidence is in `adf_g_execution_review.md`.

## Remaining dependency sequence

1. **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model:** execute `ADF-G-XT01` in actual Cursor, Claude Code and Codex runtimes, update the runtime ledger, and rerun conformance.
2. **ADF-H — Security, Trust, Lifecycle & Governance:** consolidate least privilege, secrets/data boundaries, lifecycle/reverification horizons, and long-term governance after ADF-G acceptance.
3. **Foundation execution exit review:** evaluate ADF-EX-01–ADF-EX-20 using A–H evidence.
4. **Implementation 001-A** begins only after the foundation exit passes or a narrow explicit non-semantic/non-security waiver is accepted.

Autonomy is not part of the foundation success condition.
