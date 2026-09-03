# DMTZ Agentic Development Foundation

**Status:** IN EXECUTION — ADF-A THROUGH ADF-G ACCEPTED FOR PROGRESSION; ADF-EX-17 DEFERRED VERIFICATION; ADF-H IN EXECUTION

## Purpose

The Agentic Development Foundation establishes a tool-neutral, human-directed development model for Cursor, Claude Code, Codex, and ordinary development before Implementation 001 begins. It is enabling infrastructure, not a new DMTZ product/concept/architecture phase and not a replacement for the frozen SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contract stack.

## Current execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**
- **ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: COMPLETE / ACCEPTED FOR PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION.**
- **ADF-H — Security, Trust, Lifecycle & Governance: IN EXECUTION — SECURITY/TRUST/LIFECYCLE GOVERNANCE.**

**ADF status mirror: COMPLETE ADF-A–ADF-G (ADF-EX-17 deferred); IN EXECUTION ADF-H.**

The ADF-G progression exception is narrow: Cursor, Claude Code and Codex remain runtime-`unverified` until `ADF-G-XT01` is actually exercised. The exception does not weaken shared authority, security, canonical-reference or human-directed boundaries.

Implementation 001 remains planned and blocked until ADF-H and the foundation execution exit review are complete. The exit review must treat ADF-EX-17 as an explicit bounded deferred-verification waiver rather than a PASS.

## Implemented foundation model

### Authority and human direction — ADF-A

Shared authority is rooted in canonical `docs/`, root `AGENTS.md`, live ADF/implementation status, accepted ADF mechanics, then thin tool adapters. A1–A4 action classes preserve human-selected task scope and prevent autonomous continuation, external/destructive action without explicit authorization, or silent semantic change.

### Portable knowledge — ADF-B

`knowledge/index.md` is an OKF v0.2 portable routing plane. It is never an independent source of DMTZ truth, authority, health, evidence sufficiency, or causality.

### Tool adapters — ADF-C

- Cursor: root `AGENTS.md` + scoped `.cursor/rules/*.mdc`;
- Claude Code: `.claude/CLAUDE.md` importing `../AGENTS.md`;
- Codex: root `AGENTS.md` natively.

`tool_compatibility.json` records documented compatibility state. Actual installed-tool behavior is recorded separately in the ADF-G runtime ledger.

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

It composes documentation consistency, OKF, adapter, skill, canonical-reference, ADF-status, fixture, context-budget, compatibility-evidence, security/lifecycle and negative-control checks. `.github/workflows/agentic-conformance.yml` runs the same path in CI.

The report describes **agentic configuration conformance only**. It is not DMTZ domain health, data quality, source health, application correctness, or production readiness.

### Compatibility and onboarding — ADF-G

Repository-level portability and the ordinary IDE/CLI path are accepted. `developer_onboarding.md`, `tool_compatibility_matrix.md`, `adf_g_runtime_probe.md`, and `runtime_compatibility_evidence.json` define one shared onboarding/runtime evidence model.

The human-authorized [`adf_g_progression_exception.md`](adf_g_progression_exception.md) permits sequencing to ADF-H while **ADF-EX-17 remains deferred verification**. Cursor, Claude Code and Codex are still runtime-unverified and cannot be called runtime-supported until actual provider evidence exists.

### Security, trust and lifecycle — ADF-H (in execution)

ADF-H consolidates least privilege, secret/sensitive-data boundaries, prompt-injection/content trust, tool-memory noncanonicality, provider lifecycle/reverification, agentic change governance, retention and human fallback.

Primary artifacts are:

- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md);
- [`agentic_change_governance.md`](agentic_change_governance.md);
- [`tool_lifecycle_review.json`](tool_lifecycle_review.json);
- `scripts/agentic/scan_agentic_secrets.py`;
- `scripts/agentic/validate_adf_h_governance.py`.

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
- [`adf_g_progression_exception.md`](adf_g_progression_exception.md)
- [`portable_workflow_profile.md`](portable_workflow_profile.md)
- [`context_discovery_policy.md`](context_discovery_policy.md)
- [`stable_reference_policy.md`](stable_reference_policy.md)
- [`context_budget_policy.md`](context_budget_policy.md)
- [`conformance_policy.md`](conformance_policy.md)
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md)
- [`agentic_change_governance.md`](agentic_change_governance.md)
- [`tool_lifecycle_review.json`](tool_lifecycle_review.json)
- [`execution_exit_criteria.md`](execution_exit_criteria.md)

Execution evidence is recorded in `adf_a_execution_review.md` onward. ADF-G's runtime limitation remains visible in `adf_g_execution_review.md` and the bounded progression exception.

## Remaining dependency sequence

1. **ADF-H — Security, Trust, Lifecycle & Governance:** complete and validate the current security/trust/lifecycle group.
2. **Foundation execution exit review:** evaluate ADF-EX-01–ADF-EX-20 using A–H evidence, explicitly treating ADF-EX-17 as deferred/waived rather than passed unless actual provider runtime evidence has appeared.
3. **Implementation 001-A** begins only after the foundation exit passes under the documented mandatory-gate/waiver rule.

Autonomy is not part of the foundation success condition.
