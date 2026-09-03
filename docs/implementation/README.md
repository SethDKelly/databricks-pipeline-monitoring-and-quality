# DMTZ Implementation Program

**Status:** PLANNED / BLOCKED ON AGENTIC FOUNDATION EXIT — ADF-A THROUGH ADF-H COMPLETE; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT

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

The immediate upstream architecture handoff is [`../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md).

Status authority:

- `docs/README.md` — design progression;
- **this file** — implementation-program progression;
- `../agentic_development_foundation/README.md` — ADF progression/exit status;
- active implementation package README/group plan — package-local progression.

Code, tests, knowledge, skills, adapters, security policy or CI may not silently supersede accepted design/architecture contracts.

## Pre-implementation Agentic Development Foundation

Completed / accepted for exit review:

- ADF-A — shared authority and human-directed A1–A4 scope;
- ADF-B — OKF v0.2 portable knowledge routing;
- ADF-C — thin Cursor/Claude/Codex instruction adapters;
- ADF-D — canonical portable workflows under `.agents/skills/`;
- ADF-E — shortest-path context, exact stable references, knowledge maintenance and context budgets;
- ADF-F — unified agentic conformance, drift detection, negative controls and CI;
- ADF-G — compatibility/onboarding baseline accepted for progression with **ADF-EX-17 deferred verification**;
- ADF-H — security, trust, lifecycle and governance.

Cursor, Claude Code and Codex remain runtime-`unverified` until actual `ADF-G-XT01` evidence is recorded. That is a bounded deferred-verification condition, not PASS.

Current required work:

- **Agentic Development Foundation execution exit review** — evaluate ADF-EX-01–ADF-EX-20 and explicitly accept/reject the ADF-EX-17 waiver.

Implementation 001-A begins only after that exit passes under the documented mandatory-gate/waiver rule.

Canonical conformance command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Agentic configuration PASS/FAIL is distinct from DMTZ domain/runtime health. Provider runtime evidence is recorded separately in `../agentic_development_foundation/runtime_compatibility_evidence.json`; ADF-H security/lifecycle authority is `../agentic_development_foundation/security_trust_lifecycle_policy.md`.

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

The sequence is dependency-oriented. Limited overlap is allowed only after the upstream contract needed by dependent work is executable and stable. UI or adapters may progress in parallel where appropriate, but downstream work may not invent independent semantics.

Every implementation must preserve, among other accepted distinctions:

- execution success ≠ data health;
- freshness ≠ execution success;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- current state ≠ historical/as-known state;
- source availability ≠ authority;
- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization;
- Lineage ≠ exposure ≠ Impact ≠ causality;
- correlation ≠ cause;
- missing evidence ≠ negative truth;
- unknown/conflicting/stale/partial/unavailable/withheld remain legitimate;
- Gate readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Safeguard configuration ≠ enforcement ≠ prevention ≠ recovery;
- model/search output cannot manufacture truth, authority, evidence sufficiency, confirmation or control decisions.

## Standard implementation package

Each package should include:

1. README with goal/scope/dependencies/group sequence/exit gate;
2. group plans where iterative execution is required;
3. executable acceptance criteria;
4. scenario/contract traceability;
5. implementation ADRs for concrete choices that preserve frozen semantics;
6. risk/debt updates;
7. exit review with actual test/deployment evidence rather than design-only PASS.

## Agent/developer routing

- shared constitution: root `AGENTS.md`;
- portable discovery: `../../knowledge/index.md` when needed;
- exact stable-ID policy/helper: ADF-E `stable_reference_policy.md` / `scripts/agentic/resolve_stable_id.py`;
- compact family/path bridge: [`agent_reference_index.md`](agent_reference_index.md);
- canonical workflows: `../../.agents/skills/`;
- conformance: `../agentic_development_foundation/conformance_policy.md` and `scripts/agentic/run_conformance.py`;
- runtime compatibility evidence: `../agentic_development_foundation/runtime_compatibility_evidence.json`;
- bounded ADF-G progression exception: `../agentic_development_foundation/adf_g_progression_exception.md`;
- security/trust/lifecycle: `../agentic_development_foundation/security_trust_lifecycle_policy.md` and `agentic_change_governance.md`;
- foundation exit gates: `../agentic_development_foundation/execution_exit_criteria.md`.

Autonomous execution/orchestration remains outside the accepted foundation and Implementation 001 entry gate.

## Change control

When implementation encounters a target constraint:

1. change concrete technology/configuration within frozen contracts;
2. explicitly narrow deployment/product capability if source support is insufficient;
3. add instrumentation/attestation if the stronger proposition is required;
4. raise architecture change only when no compliant realization exists;
5. reopen functional semantics only for an intentional product requirement change.

No developer or agent may silently weaken a contract because it is easier to implement.

## Current state

**Agentic Development Foundation: GROUP EXECUTION COMPLETE — ADF-A THROUGH ADF-H COMPLETE / ACCEPTED FOR EXIT REVIEW; ADF-EX-17 DEFERRED VERIFICATION; EXECUTION EXIT REVIEW NEXT.** Complete the foundation execution exit review before beginning Implementation 001-A.

**Implementation 001 — Executable Foundations & Walking Skeleton: PLANNED / READY AFTER AGENTIC FOUNDATION EXIT.**