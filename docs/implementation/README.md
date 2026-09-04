# DMTZ Implementation Program

**Status:** BLOCKED — CANONICAL KNOWLEDGE & DOCUMENTATION AUTHORITY RETROFIT IN PROGRESS

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: IN EXECUTION CKR-A; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose and authority

This directory is the system of record for realization of the frozen DMTZ product, integration and technical architecture. It translates accepted design semantics into executable software, infrastructure, validation and production-readiness work; it does not create a new truth model.

Implementation is temporarily blocked while the repository performs the **Canonical Knowledge & Documentation Authority Retrofit (CKR)**. The retrofit changes where current documentation authority lives and how it is discovered before code/test traceability begins. It does not itself change accepted product semantics.

Status authority:

- `docs/README.md` — completed design-phase progression plus CKR pre-implementation note;
- `../canonical_knowledge_retrofit/README.md` — live CKR progression and documentation-authority migration;
- **this file** — implementation-program progression;
- `../agentic_development_foundation/README.md` / `execution_exit_review.md` — completed ADF/addendum/exit authority;
- active implementation package README/group plan — package-local progression after CKR unlocks implementation.

## Documentation authority during CKR

Use `../canonical_knowledge_retrofit/canonical_ownership_inventory.json` when semantic ownership is unclear.

- `legacy_authoritative` — current meaning remains in the inventoried legacy owner;
- `candidate_ready` — canonical candidate is review-only;
- `canonicalized` — target under `docs/canonical/` is the sole current owner for that record;
- `history_only` — provenance/rationale only.

No current semantic question should be reconstructed from design chronology after its record is canonicalized. Conversely, the existence of a target path under `docs/canonical/` does not override a `legacy_authoritative` owner.

Accepted incoming stable-ID ranges remain unchanged:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

CKR migrates owner paths and routing without renumbering or silently changing these contracts.

## Agentic Development Foundation — EXIT ACCEPTED

ADF-A through ADF-H, the Databricks Agent Skills Integration Addendum and the ADF execution exit remain accepted.

Final ADF disposition remains:

- ADF-EX-01–ADF-EX-16 — **PASS**;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — **PASS**.

`ADF-G-XT01` remains open and Cursor/Claude Code/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains a future **Implementation 001-A** environment obligation once CKR unlocks implementation.

## CKR dependency

Current required work:

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: IN EXECUTION**;
- CKR-B through CKR-K follow as declared in `../canonical_knowledge_retrofit/README.md`;
- **Implementation 001-A remains blocked until CKR-K exit acceptance.**

The accepted ADF exit is not reopened by CKR. CKR is a later documentation-authority dependency intentionally inserted before code begins.

## Databricks developer dependency profile

The accepted vendor profile remains core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Model/AI skills and managed Databricks MCP servers remain deferred. Vendor operational guidance never becomes DMTZ semantic authority.

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

Completion profiles remain unchanged: MVP 001–008; enterprise passive monitoring 001–009 + 011; full active-control enterprise 001–011.

## Current implementation state

**Implementation 001 — Executable Foundations & Walking Skeleton: PLANNED / BLOCKED ON CKR EXIT.**

**001-A — Developer Environment, Repository Structure & Engineering Standards: NOT ACTIVE / BLOCKED ON CKR-K.**

No product code should be introduced as part of CKR unless a later explicit semantic/change-control task separately requires executable migration tooling. CKR-A is documentation-authority infrastructure only.

## Agent/developer routing

- CKR status/authority: `../canonical_knowledge_retrofit/README.md`;
- CKR ownership ledger: `../canonical_knowledge_retrofit/canonical_ownership_inventory.json`;
- target canonical namespace: `../canonical/README.md`;
- logical history layer: `../design_history/README.md`;
- shared constitution: root `AGENTS.md`;
- portable discovery: `../../knowledge/index.md` when needed;
- compact bridge: [`agent_reference_index.md`](agent_reference_index.md);
- canonical workflows/overlays: `../../.agents/skills/`;
- conformance: `../agentic_development_foundation/conformance_policy.md` and `scripts/agentic/run_conformance.py`;
- ADF exit: `../agentic_development_foundation/execution_exit_review.md`.

## Canonical conformance command

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Agentic/documentation-authority conformance is distinct from DMTZ domain/runtime health, provider-runtime certification and target Databricks capability.
