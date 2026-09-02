# ADF-A — Execution Review

**Status:** ACCEPTED — ADF-A COMPLETE

## Review question

Has ADF-A established one shared authority, scope and human-directed action model that later Cursor/Claude/Codex adapters and workflows can consume without inventing independent permission or semantic rules?

**Conclusion: yes.**

ADF-A closes at the shared-policy layer. Native Claude/Codex adapter realization is intentionally owned by ADF-C, and cross-tool in-tool smoke validation is owned by ADF-G. Those downstream obligations are not represented here as already executed.

## Delivered artifacts

- `docs/agentic_development_foundation/authority_scope_policy.md` — accepted shared tool-neutral authority/scope/action policy.
- `docs/agentic_development_foundation/tool_adapter_authority_checklist.md` — adapter review checklist and initial surface audit.
- `docs/agentic_development_foundation/fixtures/adf_a_boundary_scenarios.yaml` — reusable behavioral scenarios for later automated ADF-F validation.
- root `AGENTS.md` — synchronized with shared authority precedence and A1–A4 action classes.
- `.cursor/rules/00-implementation-routing.mdc` — synchronized to route Cursor through the shared policy and current ADF status.
- this execution review.

## Acceptance findings

### 1. Shared authority hierarchy — PASS

The accepted precedence is now explicit:

1. canonical DMTZ contracts/docs;
2. root `AGENTS.md`;
3. live program/active-package or active-ADF authority;
4. Agentic Development Foundation mechanics;
5. tool-specific repository adapters;
6. personal/user-level tool preferences and tool memory.

Human task intent establishes the current task/action envelope but does not silently rewrite higher repository/contract authority.

### 2. Human-directed execution contract — PASS

The policy distinguishes four action classes:

- A1 read/review/plan;
- A2 change/build/fix;
- A3 external/destructive/scope-expanding;
- A4 architecture/semantic change.

A2 work permits ordinary in-scope edits, directly necessary tests/fixtures/status/traceability updates and safe validation without repetitive approval prompts.

A1 does not become A2 merely because a defect is discovered.

A3 requires explicit task-specific human authorization plus applicable repository/team gates.

A4 routes through existing DMTZ change control.

### 3. Supporting-change envelope — PASS

The policy makes directly necessary supporting changes part of an explicitly requested implementation/fix task while excluding unrelated cleanup, speculative features, broad unneeded refactors and automatic continuation to the next group.

This provides useful developer-agent freedom without turning task interpretation into backlog autonomy.

### 4. Tool neutrality — PASS at shared-policy layer

No agent/tool is granted semantic privilege. Repository artifacts/tests/traceability/review remain the acceptance basis.

Current shared/root and Cursor surfaces are aligned with this rule.

Claude Code and Codex native adapter realization is not part of ADF-A and remains an explicit ADF-C deliverable. ADF-G must later demonstrate the same bounded task against all supported tools.

### 5. No hidden memory authority — PASS

Root and shared policy now state that tool memory, auto-memory, chat history and generated summaries are advisory only. Correctness-critical persistent facts must be promoted into repository artifacts.

### 6. Architecture constraint behavior — PASS

The A4 policy uses the already accepted implementation escalation order. An impossible target capability cannot be replaced silently with weaker semantics.

### 7. Human-directed/autonomous distinction — PASS

The policy explicitly excludes:

- agent-created/reprioritized backlog work;
- automatic continuation into follow-on groups;
- agent-to-agent implementation delegation;
- unattended merge/deploy;
- autonomous architecture reopening.

The deferred autonomous backlog remains the only holding area for those topics.

## Boundary scenario set

`fixtures/adf_a_boundary_scenarios.yaml` records reusable scenarios including:

- review remains review;
- implementation permits in-scope edits/tests;
- no repetitive approval for ordinary supporting changes;
- completion does not authorize the next group;
- generic implementation does not authorize deployment;
- explicit external actions still respect mandatory gates;
- architecture difficulty routes to change control;
- lower-precedence tool rules cannot override repository authority;
- memory is advisory;
- user-level preferences cannot disable mandatory validation;
- directly impacted status updates are in scope;
- agent delegation remains deferred.

These fixtures are design/execution evidence now and become candidates for deterministic automation in ADF-F.

## Initial adapter-surface audit

### Root `AGENTS.md` — PASS

It now exposes shared authority precedence, the accepted policy reference, A1–A4 classes, non-autonomy, completion stopping behavior and memory non-authority.

### Cursor routing — PASS

`.cursor/rules/00-implementation-routing.mdc` is scoped (`alwaysApply: false`), points to the shared policy and current ADF authority, and does not grant broader actions.

### Cursor change-control rule — PASS

`.cursor/rules/10-design-change-control.mdc` preserves the accepted implementation/architecture escalation order and does not weaken ADF-A authority.

### Claude/Codex native adapters — DEFERRED BY DESIGN

ADF-A has established the shared contract they must inherit. ADF-C must implement/verify native adapter mechanics; ADF-G must exercise cross-tool compatibility.

This is a downstream realization dependency, not an ADF-A defect.

## Relationship to foundation exit gates

ADF-A establishes the policy basis for:

- **ADF-EX-01** shared authority consistency;
- **ADF-EX-02** explicit human-directed action boundaries;
- **ADF-EX-03** tool adapters cannot silently supersede semantic/change-control authority.

Those full foundation gates remain open until ADF-C/G/F provide actual adapter and conformance evidence.

## Validation performed

At ADF-A execution time:

- shared root authority was read back and synchronized;
- active Cursor routing/change-control surfaces were manually reviewed for contradictory permission/authority behavior;
- stale pre-implementation wording previously removed from the active Cursor rule set was not reintroduced;
- machine-readable behavioral fixtures were added for later automation.

No claim is made that ADF-F automated checks already exist.

## Residual obligations

- ADF-B: build the OKF v0.2 knowledge plane without changing this authority model.
- ADF-C: implement Claude/Codex/Cursor native adapter contract and compatibility manifest against this policy.
- ADF-D: portable skills must use these same action classes and may not self-authorize continuation.
- ADF-F: automate relevant boundary/drift checks using these fixtures/checklists.
- ADF-G: exercise representative tasks across supported tools.
- ADF-H: incorporate policy lifecycle/security governance and review horizon.

## Exit decision

**ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**

Next eligible groups are **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile** and **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract**. They may proceed independently/overlap according to the accepted foundation dependency model.
