# DMTZ Agentic Development Foundation

**Status:** ADF-A THROUGH ADF-H + DATABRICKS AGENT SKILLS ADDENDUM COMPLETE / ACCEPTED FOR EXIT REVIEW — ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT

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
- **ADF-H — Security, Trust, Lifecycle & Governance: COMPLETE / ACCEPTED.**

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

ADF-EX-17 remains a narrow deferred-verification condition: Cursor, Claude Code and Codex remain runtime-`unverified` until `ADF-G-XT01` is actually exercised. It is not PASS and does not weaken shared authority, security, canonical-reference or human-directed boundaries.

## Pre-exit Databricks Agent Skills addendum — COMPLETE / ACCEPTED

The bounded **Databricks Agent Skills Integration Addendum** is complete. It is not ADF-I and does not reopen ADF-A–ADF-H.

The accepted initial vendor set is:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

Model/AI implementation skills are explicitly deferred. Managed Databricks MCP servers are not configured by this addendum and require separate security/integration review.

Vendor skills remain reviewed operational guidance and are materialized locally under ignored `.databricks/agent-skills/`; they are not copied into canonical DMTZ skill storage. DMTZ-owned overlays remain under `.agents/skills/` for environment discovery, acquisition, persistence, Lineage, runtime provenance and governance.

`DBX-SKILL-RUN-01` remains an Implementation 001-A environment obligation: establish a compatible Databricks CLI and record exact local reviewed-skill materialization/version evidence. That residual is not represented as completed environment proof and does not authorize workspace access.

Primary references:

- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md)
- [`databricks_vendor_skills_profile.json`](databricks_vendor_skills_profile.json)
- [`databricks_agent_skills_addendum_execution_review.md`](databricks_agent_skills_addendum_execution_review.md)
- `scripts/agentic/materialize_databricks_skills.py`
- `scripts/agentic/validate_databricks_agent_skills.py`

## Implemented foundation model

### Authority and human direction — ADF-A

Canonical DMTZ docs/contracts remain highest project authority. Root `AGENTS.md`, live program/group scope, accepted foundation mechanics and thin provider adapters follow. A1–A4 preserves human-selected scope and prevents tooling availability from becoming permission.

### Portable knowledge and workflows — ADF-B through ADF-E

`knowledge/` is an OKF routing plane, never product truth. Canonical DMTZ workflows live once under `.agents/skills/`; Claude uses thin command bridges. Progressive disclosure, exact stable-ID resolution and deterministic context budgets avoid monolithic prompts and first-search-hit authority.

The Databricks addendum follows the same rule: **Databricks skills know how Databricks works; DMTZ overlays constrain how that capability may realize DMTZ.**

### Conformance and CI — ADF-F

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

It validates documentation consistency, OKF, adapters, DMTZ skills, canonical references, ADF status, fixtures/addenda, context budgets, provider compatibility evidence, reviewed Databricks vendor-skill integration, secret scanning, security/lifecycle governance and negative controls.

Agentic configuration PASS is not DMTZ domain health, provider runtime proof, target Databricks capability or production readiness.

### Compatibility, security and lifecycle — ADF-G / ADF-H

Provider runtime evidence remains independent from documentation/configuration compatibility. Least privilege, secret/sensitive-data boundaries, prompt/content trust, noncanonical tool memory, provider/vendor lifecycle review, G1–G5 change governance, retention and human fallback remain mandatory.

Databricks vendor skills are a reviewed G2/G3 dependency. Any change to permissions, external integrations, data exposure or security boundaries becomes G4. Vendor instructions never create DMTZ semantic authority or A3/A4 permission.

## Foundation boundary

Included:

- shared repository authority and human-directed A1–A4 action;
- portable OKF discovery and DMTZ Agent Skills;
- thin Cursor/Claude/Codex adapters;
- reviewed Databricks vendor-skill dependency composition through DMTZ-owned overlays;
- exact references/context budgets;
- deterministic conformance/drift/CI;
- tool compatibility/onboarding;
- security/trust/lifecycle governance.

Explicitly excluded:

- unattended/autonomous implementation or work selection;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- agent/tool memory as canonical truth;
- automatic adoption of newly published Databricks skills;
- Databricks model/AI implementation skills in the initial addendum;
- managed Databricks MCP servers without separate review.

Deferred autonomy remains only in [`autonomous_backlog.md`](autonomous_backlog.md).

## Key references

- [`authority_scope_policy.md`](authority_scope_policy.md)
- [`okf_profile.md`](okf_profile.md)
- [`portable_workflow_profile.md`](portable_workflow_profile.md)
- [`context_discovery_policy.md`](context_discovery_policy.md)
- [`stable_reference_policy.md`](stable_reference_policy.md)
- [`conformance_policy.md`](conformance_policy.md)
- [`runtime_compatibility_evidence.json`](runtime_compatibility_evidence.json)
- [`adf_g_progression_exception.md`](adf_g_progression_exception.md)
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md)
- [`agentic_change_governance.md`](agentic_change_governance.md)
- [`tool_lifecycle_review.json`](tool_lifecycle_review.json)
- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md)
- [`databricks_vendor_skills_profile.json`](databricks_vendor_skills_profile.json)
- [`execution_exit_criteria.md`](execution_exit_criteria.md)

Execution evidence is recorded in `adf_a_execution_review.md` through `adf_h_execution_review.md` plus the accepted Databricks addendum execution review.

## Next dependency

1. **Agentic Development Foundation execution exit review:** evaluate ADF-EX-01–ADF-EX-20 plus the accepted Databricks addendum, explicitly deciding the bounded ADF-EX-17 deferred-verification waiver and carrying `DBX-SKILL-RUN-01` into Implementation 001-A.
2. **Implementation 001-A** becomes eligible only if that exit review passes under the documented gate/waiver rule.

Autonomy is not part of the foundation success condition.
