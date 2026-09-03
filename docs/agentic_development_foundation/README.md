# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — IMPLEMENTATION 001-A NEXT; ADF-EX-17 DEFERRED / WAIVED AS BOUNDED VERIFICATION DEBT

## Purpose

The Agentic Development Foundation establishes the tool-neutral, human-directed development operating model used by Cursor, Claude Code, Codex and ordinary development. It is enabling infrastructure, not a replacement for frozen DMTZ SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH semantics.

## Final execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**
- **ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: COMPLETE / ACCEPTED FOR PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION.**
- **ADF-H — Security, Trust, Lifecycle & Governance: COMPLETE / ACCEPTED.**
- **Databricks Agent Skills Integration Addendum: COMPLETE / ACCEPTED.**
- **Execution Exit Review / Consolidation: COMPLETE / ACCEPTED.**

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

The formal exit decision is [`execution_exit_review.md`](execution_exit_review.md). It adjudicates ADF-EX-01–ADF-EX-20 as:

- ADF-EX-01–ADF-EX-16 — **PASS**;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — **PASS**.

This is the only waived/deferred exit gate.

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until the common `ADF-G-XT01` bounded exercise is actually run in each provider runtime and recorded in `runtime_compatibility_evidence.json`.

The bounded waiver:

- does not convert missing runtime evidence to PASS;
- does not permit a provider to be called runtime-supported;
- does not weaken DMTZ semantic/change-control authority, A1–A4 human direction, canonical-reference discipline, security or deterministic conformance;
- requires a failed future smoke to reopen the affected provider adapter/support claim before that provider is relied on as supported.

Ordinary IDE/CLI development remains supported independently of coding-agent runtime availability.

## Databricks Agent Skills addendum

The accepted initial reviewed vendor set is:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

Vendor skills are reviewed operational guidance, never DMTZ semantic or authorization authority. DMTZ-owned overlays remain canonical under `.agents/skills/` for environment discovery, acquisition, persistence, Lineage, runtime provenance and governance.

Model/AI implementation skills remain deferred. Managed Databricks MCP servers remain outside the accepted addendum and require separate security/integration review.

`DBX-SKILL-RUN-01` is explicitly carried into **Implementation 001-A**: establish a compatible Databricks CLI and record exact local reviewed-skill `aitools --path` materialization/version evidence. This residual does not authorize workspace access and is not represented as target-runtime proof.

## Implemented foundation model

### Authority and human direction

Canonical DMTZ contracts/docs remain highest project authority. Root `AGENTS.md`, live implementation/group scope, accepted foundation mechanics, DMTZ-owned workflows/overlays, reviewed vendor guidance and thin provider adapters follow in that order.

A1–A4 remains the action model:

- A1 read/review/plan;
- A2 bounded repository change/build/fix;
- A3 external/destructive/scope-expanding action requires explicit task-specific human authorization plus normal gates;
- A4 semantic/architecture change follows DMTZ change control.

Foundation exit does not authorize automatic continuation into implementation work.

### Knowledge, workflows and context

`knowledge/` remains OKF routing rather than semantic truth. Canonical workflows live under `.agents/skills/`; Claude uses thin command bridges. Progressive disclosure, exact stable-ID resolution and deterministic context budgets prevent first-search-hit authority and monolithic persistent prompts.

### Conformance and CI

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The report covers repository agentic configuration only. It is not DMTZ domain health, data quality, source health, provider-runtime proof, target Databricks capability or production readiness.

### Security and lifecycle

Least privilege, secret/sensitive-data boundaries, prompt/content trust, noncanonical tool memory, provider/vendor lifecycle review, G1–G5 change governance and ordinary human fallback remain mandatory after foundation exit.

## Explicitly deferred / not authorized

- `ADF-G-XT01` provider-runtime verification remains open;
- autonomous task selection or unattended autonomous implementation;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- tool memory/personal state as canonical truth;
- automatic adoption of newly published Databricks skills;
- Databricks model/AI implementation skills until explicitly reviewed;
- managed Databricks MCP servers until separately reviewed.

Deferred autonomy remains only in [`autonomous_backlog.md`](autonomous_backlog.md).

## Key references

- [`execution_exit_review.md`](execution_exit_review.md) — final exit adjudication and residual debt;
- [`execution_exit_criteria.md`](execution_exit_criteria.md) — ADF-EX-01–ADF-EX-20 gate definitions;
- [`adf_g_progression_exception.md`](adf_g_progression_exception.md) — bounded ADF-EX-17 exception;
- [`runtime_compatibility_evidence.json`](runtime_compatibility_evidence.json) — provider runtime evidence ledger;
- [`authority_scope_policy.md`](authority_scope_policy.md);
- [`okf_profile.md`](okf_profile.md);
- [`portable_workflow_profile.md`](portable_workflow_profile.md);
- [`context_discovery_policy.md`](context_discovery_policy.md);
- [`stable_reference_policy.md`](stable_reference_policy.md);
- [`conformance_policy.md`](conformance_policy.md);
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md);
- [`agentic_change_governance.md`](agentic_change_governance.md);
- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md);
- [`databricks_agent_skills_addendum_execution_review.md`](databricks_agent_skills_addendum_execution_review.md);
- [`databricks_vendor_skills_profile.json`](databricks_vendor_skills_profile.json).

Execution evidence remains in `adf_a_execution_review.md` through `adf_h_execution_review.md`, the Databricks addendum execution review, and the final exit review.

## Next dependency

**Implementation 001-A — Development Environment, Repository Structure & Engineering Standards: NEXT / ELIGIBLE.**

001-A owns `DBX-SKILL-RUN-01` and the normal Implementation 001 entry obligations. `ADF-G-XT01` remains visible verification debt but does not block ordinary development or 001-A under the accepted bounded waiver.

Beginning 001-A still requires an explicit human-selected task. No foundation mechanism auto-starts it.
