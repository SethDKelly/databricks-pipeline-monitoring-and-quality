# DMTZ Implementation Program

**Status:** PLANNED / BLOCKED ON AGENTIC FOUNDATION — ADF-A complete; ADF-B / ADF-C next; Implementation 001 follows foundation exit

## Purpose

This directory is the system of record for realization of the frozen DMTZ product, integration and technical architecture. It translates the accepted design stack through Phase 010 into executable software, infrastructure, automated validation and production-readiness work.

Implementation does **not** create a new truth model. The accepted semantic/architecture stack remains authoritative:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

The Phase 010 implementation handoff is the immediate upstream contract: [`../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md).

For implementation-agent context routing, use [`agent_reference_index.md`](agent_reference_index.md). The Agentic Development Foundation is evolving this routing into a portable OKF v0.2 knowledge plane while preserving canonical `docs/` as authority.

## Status authority

- `docs/README.md` remains the sole living authority for design-phase progression.
- **This file is the sole living authority for implementation-program progression.**
- [`../agentic_development_foundation/README.md`](../agentic_development_foundation/README.md) owns the pre-implementation agentic-enablement execution sequence ADF-A–ADF-H.
- Each implementation package may state its own internal group status.
- Completed implementation packages must include an exit review with executable evidence.
- Code behavior is never allowed to silently supersede an accepted design/architecture contract.

## Pre-implementation enabling foundation

Before Implementation 001-A, complete the **Agentic Development Foundation** defined in [`../agentic_development_foundation/README.md`](../agentic_development_foundation/README.md).

Current ADF state:

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: NEXT / READY.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: NEXT / READY.**
- ADF-D–ADF-H remain planned behind their dependency gates.

ADF-A's shared action/authority policy is [`../agentic_development_foundation/authority_scope_policy.md`](../agentic_development_foundation/authority_scope_policy.md).

The foundation's purpose is operational/tooling portability only:

- shared repository agent authority;
- OKF v0.2 knowledge routing/progressive disclosure;
- thin Cursor/Claude/Codex adapters;
- portable human-directed workflow skills;
- context minimization and stable-reference retrieval;
- validation/drift/CI controls;
- tool compatibility/onboarding;
- security/trust/lifecycle governance.

It does not alter DMTZ product semantics or add autonomous development. Autonomous execution/orchestration is explicitly deferred.

## Program outcome

The program is complete when an enterprise deployment can:

1. acquire bounded evidence from supported sources with explicit capability, coverage, health and quota state;
2. preserve canonical identity, provenance, time, governance and historical semantics without rewriting history;
3. evaluate health/quality/change/Lineage/Impact propositions deterministically and preserve unknown/conflicting/partial states;
4. organize Investigations and Causal Claims without manufacturing confirmation;
5. reconstruct historical/as-known state by knowledge cut;
6. produce authorization-aware Statement IR / Answer IR and basis inspection;
7. serve business and engineering users through governed APIs/UI;
8. operate with measurable SLOs, security, resilience, cost/quota governance and recovery procedures;
9. pass the accepted MVP proof scenarios and the applicable design scenario corpus as executable tests;
10. optionally add model/search assistance and active control without changing passive truth semantics;
11. graduate through production operational acceptance and architecture-conformance review.

## Implementation sequence

| Implementation | Outcome | Required for core MVP? |
|---|---|---:|
| **001 — Executable Foundations & Walking Skeleton** | Buildable repo, executable contracts/invariants, minimal Delta history, first Databricks slice, first evidence-to-Statement-IR question | Yes |
| **002 — Identity, Scope, Authority & Authorization Runtime** | Enterprise identity/governance/policy runtime and disclosure boundary | Yes |
| **003 — Source Acquisition, Capability & Evidence Reliability** | Production-shaped Databricks/GitHub acquisition, reconciliation, coverage and integration health | Yes |
| **004 — Runtime Provenance, Health, Quality, Change & Lineage** | Full passive monitoring evidence spine and representative Impact evidence | Yes |
| **005 — Investigation, Impact Reasoning & Historical Replay** | Deterministic Investigation/Causal Claim/replay/Statement reasoning | Yes |
| **006 — Serving, Explanation, Basis Inspection & User Experience** | Governed API/UI product experience | Yes |
| **007 — Operationalization, Security, Resilience, SLO & Cost** | Production-shaped deployment/operations | Yes |
| **008 — MVP Pilot Validation & Release Candidate** | Full MVP scenario proof and pilot release candidate | Yes |
| **009 — Enterprise Expansion, Scale & Optional Integrations** | Multi-tenant/scale hardening plus optional Collibra/Immuta/search/model/graph accelerators as justified | Enterprise |
| **010 — Active Control & Enterprise Control Plane** | Execution Gate / Propagation Safeguard realization | Optional unless control is a product commitment |
| **011 — Production Graduation & Operational Acceptance** | Production deployment, burn-in, runbooks, support ownership and final conformance | Yes for GA |

Implementations 001–008 define the bounded MVP realization path. Implementation 009 extends the passive enterprise product. Implementation 010 is conditional on active-control scope. Implementation 011 graduates whichever product profile is actually committed to production.

## Dependency rule

The sequence is dependency-oriented. Limited overlap is allowed only when the upstream contract needed by the downstream work is executable and stable. A team may parallelize within an implementation, but must not bypass the entry gate of a dependent capability.

Examples:

- UI shell work may begin before all reasoning features exist, but production Explanation rendering cannot define its own epistemic model.
- Databricks and GitHub adapters may be developed in parallel after the adapter contract is stable.
- Model/search assistance may be prototyped separately, but cannot become required for deterministic MVP acceptance.
- Active-control adapters cannot be accepted before deterministic Gate/Safeguard state and authorization contracts are executable.

## Cross-program non-negotiables

Every implementation must preserve:

- execution success ≠ data health;
- freshness ≠ execution success;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- current state ≠ historical state;
- source availability ≠ authority;
- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization;
- Lineage ≠ exposure ≠ Impact ≠ causality;
- correlation ≠ cause;
- missing evidence ≠ negative truth;
- unknown/conflicting/stale/partial/unavailable/withheld remain first-class states;
- retained historical communication ≠ retrospective reconstruction;
- Gate readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Safeguard configuration ≠ enforcement ≠ prevention ≠ recovery;
- model/search output cannot manufacture truth, authority, evidence sufficiency, confirmation or control decisions.

## Standard implementation package

Each `00X_*` package should contain, at minimum:

1. `README.md` — goal, scope, entry dependencies, group sequence and exit gate;
2. group plans (`00X-A` etc.) when the implementation requires iterative design/execution;
3. executable acceptance criteria;
4. scenario/contract traceability to accepted design IDs;
5. implementation ADRs for concrete technology choices that do not alter frozen semantics;
6. risk/debt register updates;
7. exit review showing test/deployment evidence rather than design-only PASS declarations.

## Agent/tool architecture

- Root `AGENTS.md` is the shared repository constitution.
- Completed ADF-A defines the common human-directed A1–A4 action model and authority precedence.
- `.cursor/rules/*.mdc` remains a small scoped routing/guardrail layer, not a duplicate of the design corpus.
- ADF-B/C will add portable OKF knowledge and thin tool-adapter mechanics; ADF-D/E will add portable human-directed workflows and retrieval discipline.
- No agentic adapter, skill, knowledge entry or tool memory may become a DMTZ truth owner.
- Autonomous execution/orchestration remains outside the accepted foundation and Implementation 001 entry gate.

## Change control

When implementation encounters a constraint:

1. change concrete technology/configuration within frozen contracts;
2. explicitly narrow the deployment/product capability if the source cannot support the stronger claim;
3. add instrumentation/attestation if the stronger proposition is required;
4. raise an architecture change request only when no compliant realization exists;
5. reopen functional semantics only when the product requirement itself intentionally changes.

No developer may silently weaken a contract because it is easier to implement.

## Current state

**Agentic Development Foundation: IN EXECUTION — ADF-A COMPLETE / ACCEPTED; ADF-B and ADF-C NEXT / READY.** Complete ADF-B–ADF-H and the foundation implementation exit review before beginning Implementation 001-A.

**Implementation 001 — Executable Foundations & Walking Skeleton: PLANNED / READY AFTER AGENTIC FOUNDATION EXIT.** Groups 001-A–001-H remain defined in [`001_executable_foundations_walking_skeleton/README.md`](001_executable_foundations_walking_skeleton/README.md).

Implementations 002–011 remain mapped at an intentionally general/abstract level so an enterprise team has a durable forward path without premature low-level design.
