# DMTZ Implementation Program

**Status:** PLANNED / BLOCKED ON AGENTIC FOUNDATION EXIT — ADF-A THROUGH ADF-H + DATABRICKS AGENT SKILLS ADDENDUM COMPLETE; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

## Purpose and authority

This directory is the system of record for realization of the frozen DMTZ product, integration and technical architecture. It translates the accepted design stack through Phase 010 into executable software, infrastructure, automated validation and production-readiness work; it does not create a new truth model.

Accepted incoming ranges remain authoritative:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

Status authority:

- `docs/README.md` — design progression;
- **this file** — implementation-program progression;
- `../agentic_development_foundation/README.md` — ADF/addendum/exit status;
- active implementation package README/group plan — package-local progression.

Code, tests, knowledge, DMTZ/vendor skills, adapters, security policy or CI may not silently supersede accepted design/architecture contracts.

## Pre-implementation Agentic Development Foundation

Completed / accepted for exit review:

- ADF-A — shared authority and human-directed A1–A4 scope;
- ADF-B — OKF v0.2 portable knowledge routing;
- ADF-C — thin Cursor/Claude/Codex instruction adapters;
- ADF-D — canonical portable workflows under `.agents/skills/`;
- ADF-E — shortest-path context, exact stable references, maintenance and context budgets;
- ADF-F — unified conformance, drift detection, negative controls and CI;
- ADF-G — compatibility/onboarding baseline accepted for progression with **ADF-EX-17 deferred verification**;
- ADF-H — security, trust, lifecycle and governance;
- **Databricks Agent Skills Integration Addendum — COMPLETE / ACCEPTED.**

The accepted Databricks vendor set is core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI implementation skills remain deferred. Managed Databricks MCP servers remain outside the addendum.

Cursor, Claude Code and Codex remain runtime-`unverified` until actual `ADF-G-XT01` evidence is recorded. That is a bounded deferred-verification condition, not PASS.

`DBX-SKILL-RUN-01` remains an Implementation 001-A environment obligation: exact local Databricks Agent Skills materialization/version verification after a compatible CLI development environment is established.

Current required work:

- **Agentic Development Foundation execution exit review** — evaluate ADF-EX-01–ADF-EX-20, explicitly accept/reject the ADF-EX-17 waiver, include the accepted Databricks addendum, and carry `DBX-SKILL-RUN-01` forward if accepted.

Implementation 001-A begins only after that exit passes.

Canonical conformance command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Agentic configuration PASS/FAIL is distinct from DMTZ domain/runtime health, coding-agent runtime certification, and target Databricks capability.

## Databricks developer dependency profile

- accepted addendum: `../agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_agent_skills_addendum_execution_review.md`;
- reviewed vendor profile: `../agentic_development_foundation/databricks_vendor_skills_profile.json`;
- canonical DMTZ overlays: `../../.agents/skills/dmtz-databricks-*/SKILL.md`;
- local vendor materialization helper: `scripts/agentic/materialize_databricks_skills.py`;
- local vendor files: ignored `.databricks/agent-skills/`, never canonical DMTZ truth;
- automatic new vendor skills, initial model/AI skills, and managed Databricks MCP servers are not authorized by the accepted addendum.

## Implementation sequence

| Implementation | Outcome | Core MVP? |
|---|---|---:|
| **001 — Executable Foundations & Walking Skeleton** | Buildable repo, executable contracts/invariants, minimal Delta history, first Databricks slice, first evidence-to-Statement-IR question | Yes |
| **002 — Identity, Scope, Authority & Authorization Runtime** | Enterprise identity/governance/policy runtime and disclosure boundary | Yes |
| **003 — Source Acquisition, Capability & Evidence Reliability** | Production-shaped Databricks/GitHub acquisition, reconciliation, coverage and integration health | Yes |
| **004 — Runtime Provenance, Health, Quality, Change & Lineage** | Passive monitoring evidence spine and representative Impact evidence | Yes |
| **005 — Investigation, Impact Reasoning & Historical Replay** | Deterministic Investigation/Causal Claim/replay/Statement reasoning | Yes |
| **006 — Serving, Explanation, Basis Inspection & User Experience** | Governed API/UI product experience | Yes |
| **007 — Operationalization, Security, Resilience, SLO & Cost** | Production-shaped deployment/operations | Yes |
| **008 — MVP Pilot Validation & Release Candidate** | Full MVP scenario proof and pilot release candidate | Yes |
| **009 — Enterprise Expansion, Scale & Optional Integrations** | Multi-tenant/scale hardening plus optional integrations/accelerators | Enterprise |
| **010 — Active Control & Enterprise Control Plane** | Execution Gate / Propagation Safeguard realization | Conditional |
| **011 — Production Graduation & Operational Acceptance** | Production deployment, burn-in, runbooks, support ownership and final conformance | GA |

Completion profiles:

- MVP: 001–008;
- enterprise passive monitoring: 001–009 + 011, skipping 010 if active control is not committed;
- full active-control enterprise: 001–011.

## Dependency and implementation rules

The sequence is dependency-oriented. Downstream work may not invent independent semantics. Every implementation must preserve the accepted distinctions including execution success ≠ data health, freshness ≠ execution success, Observation ≠ Assessment, current ≠ historical/as-known, source availability ≠ authority, Lineage ≠ exposure ≠ Impact ≠ causality, missing evidence ≠ negative truth, and model/search output cannot manufacture truth/authority/confirmation/control decisions.

Reviewed vendor guidance does not alter these distinctions.

## Agent/developer routing

- shared constitution: root `AGENTS.md`;
- portable discovery: `../../knowledge/index.md` when needed;
- compact family/path/platform bridge: [`agent_reference_index.md`](agent_reference_index.md);
- canonical DMTZ workflows/overlays: `../../.agents/skills/`;
- conformance: `../agentic_development_foundation/conformance_policy.md` and `scripts/agentic/run_conformance.py`;
- Databricks addendum/profile: `../agentic_development_foundation/databricks_agent_skills_addendum.md` / `databricks_vendor_skills_profile.json`;
- runtime compatibility evidence: `../agentic_development_foundation/runtime_compatibility_evidence.json`;
- security/trust/lifecycle: `../agentic_development_foundation/security_trust_lifecycle_policy.md` / `agentic_change_governance.md`;
- foundation exit gates: `../agentic_development_foundation/execution_exit_criteria.md`.

Autonomous execution/orchestration remains outside the accepted foundation and Implementation 001 entry gate.

## Current state

**Agentic Development Foundation: ADF-A THROUGH ADF-H + DATABRICKS AGENT SKILLS ADDENDUM COMPLETE / ACCEPTED FOR EXIT REVIEW; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.**

**Implementation 001 — Executable Foundations & Walking Skeleton: PLANNED / READY AFTER AGENTIC FOUNDATION EXIT.**
