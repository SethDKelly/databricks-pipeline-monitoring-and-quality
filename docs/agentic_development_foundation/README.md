# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — CKR COMPLETE / DPTN-A IN EXECUTION

**Current handoff:** CKR COMPLETE / EXIT ACCEPTED — DPTN-A IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

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

The formal ADF exit decision remains [`execution_exit_review.md`](execution_exit_review.md):

- ADF-EX-01–ADF-EX-16 — PASS;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — PASS.

## Relationship to completed CKR and active DPTN

ADF exit was accepted before the later Canonical Knowledge & Documentation Authority Retrofit was inserted ahead of product implementation. CKR has subsequently completed and exited successfully; this does not reopen or rewrite the historical ADF exit.

A later bounded Documentation Physical Topology Normalization (DPTN) program is now active before product implementation. DPTN changes physical documentation organization/routing only and does not reopen ADF or CKR semantics.

Current progression is owned by `docs/documentation_topology_normalization/README.md` and `docs/implementation/README.md`:

- CKR-A–K — COMPLETE / ACCEPTED;
- CKR EXIT — ACCEPTED;
- DPTN-A — IN EXECUTION;
- DPTN-B–G — PLANNED;
- **Implementation 001-A — BLOCKED ON DPTN EXIT.**

CKR established current canonical semantic ownership under `docs/canonical/`, deterministic stable-ID resolution, canonical-first OKF routing, preserved design history/provenance and drift enforcement. Those current paths remain unchanged during DPTN-A. `knowledge/` remains routing rather than truth. Phase 001–010 remains provenance for migrated meanings.

DPTN-A authorizes inventory and move planning only; it does not authorize physical relocation or product implementation. DPTN exit will return Implementation 001-A to NEXT / READY / NOT STARTED, after which a subsequent explicit human-selected implementation task is still required.

Primary current routes: [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md), [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md), and [`../implementation/README.md`](../implementation/README.md).

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until the common `ADF-G-XT01` bounded exercise is actually run in each provider runtime and recorded in `runtime_compatibility_evidence.json`.

The waiver does not convert missing runtime evidence to PASS, permit unsupported provider claims, or weaken DMTZ semantic/change-control authority, A1–A4 human direction, current-owner discipline, security or deterministic conformance.

## Databricks Agent Skills addendum

The accepted vendor set remains:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

Vendor skills are reviewed operational guidance, never DMTZ semantic/authorization authority. DMTZ overlays remain canonical development workflows under `.agents/skills/`. Model/AI implementation skills and managed Databricks MCP servers remain deferred.

`DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation.

## Durable foundation model

### Authority and human direction

A1–A4 remains the action model. Accepted DMTZ semantics outrank agent tooling, vendor guidance and memory. Documentation-only synchronization/topology work remains A2 unless it discovers a genuine semantic/architecture contradiction, which requires A4 change control.

### Knowledge, workflows and context

OKF remains routing. Canonical workflows live under `.agents/skills/`; Claude uses thin bridges. Progressive disclosure, stable references and context budgets remain mandatory.

The completed CKR ownership inventory selects current canonical owners during DPTN-A. DPTN future targets, search order, path presence, model/tool memory, vendor guidance and historical occurrences cannot override that ownership.

### Conformance and CI

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The runner validates canonical-knowledge authority, CKR/ADF/DPTN status, routing, references, context budgets, guards and other accepted repository-configuration constraints. Its PASS result is repository configuration/documentation conformance, not DMTZ domain health or provider/Databricks runtime proof.

### Security and lifecycle

Least privilege, secret/sensitive-data boundaries, prompt/content trust, noncanonical tool memory, provider/vendor lifecycle review and G1–G5 change governance remain mandatory.

## Explicitly deferred / not authorized

- `ADF-G-XT01` provider-runtime verification remains open;
- autonomous task selection or unattended autonomous implementation;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- tool memory/personal state as canonical truth;
- automatic adoption of newly published Databricks skills;
- Databricks model/AI implementation skills until explicitly reviewed;
- managed Databricks MCP servers until separately reviewed;
- DPTN-B physical relocation unless separately human-selected;
- product implementation while DPTN is incomplete.

## Key references

- [`execution_exit_review.md`](execution_exit_review.md) — accepted ADF exit as of its decision time;
- [`authority_scope_policy.md`](authority_scope_policy.md) — human-directed authority;
- [`okf_profile.md`](okf_profile.md) — OKF profile;
- [`stable_reference_policy.md`](stable_reference_policy.md) / [`stable_id_registry.json`](stable_id_registry.json) — stable reference discipline refined by CKR-J;
- [`context_discovery_policy.md`](context_discovery_policy.md) — canonical-first bounded context discovery;
- [`conformance_policy.md`](conformance_policy.md) — conformance model;
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md) / [`agentic_change_governance.md`](agentic_change_governance.md) — security/change governance;
- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md) — reviewed Databricks skills boundary;
- [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md) — completed CKR authority/exit state;
- [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md) — current DPTN progression;
- [`../implementation/README.md`](../implementation/README.md) — current implementation progression.

## Current next dependency

**DPTN-A — IN EXECUTION. Implementation 001-A — BLOCKED ON DPTN EXIT.**

DPTN-A completion will not authorize DPTN-B automatically; a subsequent explicit human-selected DPTN-B task is required.
