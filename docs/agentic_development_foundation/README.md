# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — CKR COMPLETE / DPTN-A COMPLETE

**Current handoff:** CKR COMPLETE / EXIT ACCEPTED — DPTN-A COMPLETE / ACCEPTED — DPTN-B NEXT / READY / NOT STARTED — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

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

The formal ADF exit decision remains [`execution_exit_review.md`](execution_exit_review.md): ADF-EX-01–16 and 18–20 PASS; ADF-EX-17 remains **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**.

## Relationship to completed CKR and DPTN

ADF exit was accepted before CKR and DPTN were inserted ahead of product implementation. CKR has completed and exited successfully. DPTN-A has now completed/accepted its physical-topology inventory and move plan. Neither later program reopens or rewrites the historical ADF exit.

Current progression is owned by `docs/documentation_topology_normalization/README.md` and `docs/implementation/README.md`:

- CKR-A–K — COMPLETE / ACCEPTED;
- CKR EXIT — ACCEPTED;
- DPTN-A — COMPLETE / ACCEPTED;
- DPTN-B — NEXT / READY / NOT STARTED;
- DPTN-C–G — PLANNED;
- **Implementation 001-A — BLOCKED ON DPTN EXIT.**

CKR established current canonical semantic ownership under `docs/canonical/`, deterministic stable-ID resolution, canonical-first OKF routing, preserved design history/provenance and drift enforcement. Those current paths remain unchanged after DPTN-A. `knowledge/` remains routing rather than truth. Phase 001–010 remains provenance for migrated meanings.

DPTN-A acceptance authorizes no physical relocation. DPTN-B must be explicitly human-selected before any history move begins. DPTN exit will return Implementation 001-A to NEXT / READY / NOT STARTED, after which a subsequent explicit human-selected implementation task is still required.

Primary current routes: [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md), [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md), and [`../implementation/README.md`](../implementation/README.md).

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until the common `ADF-G-XT01` bounded exercise is actually run in each provider runtime and recorded in `runtime_compatibility_evidence.json`. The waiver does not convert missing runtime evidence to PASS.

## Databricks Agent Skills addendum

The accepted vendor set remains `databricks-core`, `databricks-dabs`, `databricks-jobs`, `databricks-pipelines`, `databricks-data-discovery`, `databricks-dbsql`, `databricks-unity-catalog`, and `databricks-lakeflow-connect`.

Vendor skills are reviewed operational guidance, never DMTZ semantic/authorization authority. DMTZ overlays remain canonical development workflows under `.agents/skills/`. Model/AI implementation skills and managed Databricks MCP servers remain deferred. `DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation.

## Durable foundation model

A1–A4 remains the human-directed action model. Accepted DMTZ semantics outrank agent tooling, vendor guidance and memory. OKF remains routing. Canonical workflows live under `.agents/skills/`; Claude uses thin bridges. Progressive disclosure, stable references and context budgets remain mandatory.

The completed CKR ownership inventory still selects current canonical owners. DPTN future targets, search order, path presence, model/tool memory, vendor guidance and historical occurrences cannot override that ownership until a later validated DPTN cutover updates the current route.

Canonical conformance command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Its PASS result is repository configuration/documentation conformance, not DMTZ domain health or provider/Databricks runtime proof.

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
- [`stable_reference_policy.md`](stable_reference_policy.md) / [`stable_id_registry.json`](stable_id_registry.json) — stable reference discipline;
- [`context_discovery_policy.md`](context_discovery_policy.md) — bounded context discovery;
- [`conformance_policy.md`](conformance_policy.md) — conformance model;
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md) / [`agentic_change_governance.md`](agentic_change_governance.md) — security/change governance;
- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md) — reviewed Databricks skills boundary;
- [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md) — completed CKR authority/exit state;
- [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md) — current DPTN progression;
- [`../implementation/README.md`](../implementation/README.md) — current implementation progression.

## Current next dependency

**DPTN-B — NEXT / READY / NOT STARTED. Implementation 001-A — BLOCKED ON DPTN EXIT.**

DPTN-B requires a subsequent explicit human-selected task; DPTN-A acceptance does not authorize automatic continuation.
