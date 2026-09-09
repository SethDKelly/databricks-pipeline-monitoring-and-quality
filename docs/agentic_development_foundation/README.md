# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — CKR COMPLETE — DPTN ACTIVE

**Current handoff:** ADF EXIT ACCEPTED / CKR EXIT ACCEPTED — DPTN-A–C COMPLETE / ACCEPTED — DPTN-D NEXT / READY / NOT STARTED — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

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

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

The formal ADF exit decision remains [`execution_exit_review.md`](execution_exit_review.md): ADF-EX-01–16 and 18–20 PASS; ADF-EX-17 is **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**.

## Relationship to completed CKR and active DPTN

ADF exit was accepted before CKR. CKR subsequently completed and exited successfully; neither later program reopens or rewrites the historical ADF exit.

Current pre-implementation progression is owned by `docs/documentation_topology_normalization/README.md` and `docs/implementation/README.md`:

- CKR-A–K — COMPLETE / ACCEPTED;
- CKR EXIT — ACCEPTED;
- **DPTN-A–C — COMPLETE / ACCEPTED**;
- **DPTN-D — NEXT / READY / NOT STARTED**;
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

CKR established current semantic ownership, deterministic stable-ID resolution, canonical-first routing and drift enforcement. DPTN-B relocated historical/provenance material under `docs/history/`. DPTN-C promoted the eight substantive CKR owner roots to first-class `docs/<family>/` paths by path-only atomic cutover without changing accepted semantics.

Primary current routes: [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md), [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md), [`../history/README.md`](../history/README.md) and [`../implementation/README.md`](../implementation/README.md).

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until the common `ADF-G-XT01` bounded exercise is actually run in each provider runtime and recorded in `runtime_compatibility_evidence.json`. The waiver does not convert missing runtime evidence to PASS or weaken DMTZ authority/security/change control.

## Databricks Agent Skills addendum

The accepted vendor set remains `databricks-core`, `databricks-dabs`, `databricks-jobs`, `databricks-pipelines`, `databricks-data-discovery`, `databricks-dbsql`, `databricks-unity-catalog` and `databricks-lakeflow-connect`. Vendor skills are operational guidance, never DMTZ semantic/authorization authority. `DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation.

## Durable foundation model

### Authority and human direction

A1–A4 remains the action model. Accepted DMTZ semantics outrank agent tooling, vendor guidance and memory. Documentation-only synchronization work remains A2 unless it discovers a genuine semantic/architecture contradiction, which requires A4 change control.

### Knowledge, workflows and context

OKF remains routing. Canonical workflows live under `.agents/skills/`; Claude uses thin bridges. Progressive disclosure, stable references and context budgets remain mandatory.

The completed CKR ownership inventory selects current semantic owners at the DPTN-C first-class owner paths. `docs/history/` is provenance-only. Legacy redirects, cleared paths and move-map destinations do not establish authority. Search order, path presence, model/tool memory, vendor guidance and historical occurrences cannot override current ownership.

### Conformance and CI

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The runner validates canonical-knowledge authority, CKR/ADF/DPTN status, routing, references, context budgets, guards and accepted repository-configuration constraints. During DPTN, completed CKR checks may use a temporary accepted-era compatibility projection; DPTN topology validators run on the real tree. PASS is repository configuration/documentation conformance, not DMTZ domain health or runtime proof.

### Security and lifecycle

Least privilege, secret/sensitive-data boundaries, prompt/content trust, noncanonical tool memory, provider/vendor lifecycle review and G1–G5 change governance remain mandatory.

## Explicitly deferred / not authorized

- `ADF-G-XT01` provider-runtime verification;
- autonomous task selection or unattended autonomous implementation;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- tool memory/personal state as canonical truth;
- automatic adoption of newly published Databricks skills;
- Databricks model/AI implementation skills until explicitly reviewed;
- managed Databricks MCP servers until separately reviewed;
- product implementation while DPTN is active;
- DPTN-D/E/F/G continuation without explicit human selection.

## Key references

- [`execution_exit_review.md`](execution_exit_review.md) — accepted ADF exit;
- [`authority_scope_policy.md`](authority_scope_policy.md) — human-directed authority;
- [`stable_reference_policy.md`](stable_reference_policy.md) / [`stable_id_registry.json`](stable_id_registry.json) — stable references;
- [`context_discovery_policy.md`](context_discovery_policy.md) — bounded context discovery;
- [`conformance_policy.md`](conformance_policy.md) — conformance model;
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md) / [`agentic_change_governance.md`](agentic_change_governance.md) — security/change governance;
- [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md) — completed CKR authority;
- [`../documentation_topology_normalization/README.md`](../documentation_topology_normalization/README.md) — active DPTN;
- [`../history/README.md`](../history/README.md) — preserved history/provenance;
- [`../implementation/README.md`](../implementation/README.md) — implementation progression.

## Current next dependency

**DPTN-D — NEXT / READY / NOT STARTED.**

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN/ADF/CKR status does not authorize autonomous continuation beyond the explicitly selected phase.
