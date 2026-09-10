# DMTZ Documentation & Knowledge Index

**AUTHORITY: CURRENT ROUTING / DISCOVERY ROOT ONLY — NOT A SEMANTIC OWNER**

This is the single authored human/tool-neutral discovery root for the DMTZ repository. It tells readers and tools where current authority lives; it does not replace the current semantic ownership ledger or make routing text authoritative.

**DPTN state:** DPTN-A–F COMPLETE / ACCEPTED — DPTN-G NEXT / READY / NOT STARTED — IMPLEMENTATION 001-A BLOCKED / NOT STARTED ON DPTN EXIT.

## Fastest route

- **Known stable ID:** run `python3 scripts/agentic/resolve_stable_id.py <ID>` for the deterministic current `owner_path::STABLE-ID`. Use `--history` only for explicit provenance/rationale work.
- **Unknown semantic location:** start with the current semantic families below, then narrow to the smallest owning document.
- **Repository/developer authority:** start with [`../AGENTS.md`](../AGENTS.md).
- **Implementation state:** use [`implementation/README.md`](implementation/README.md).
- **Design-phase progression:** use [`README.md`](README.md); it remains the sole living authority for completed Phase 002–010 progression.

## Current semantic authority

Current semantic ownership is selected by [`canonical_knowledge_retrofit/canonical_ownership_inventory.json`](canonical_knowledge_retrofit/canonical_ownership_inventory.json). A current semantic question resolves to one current owner. Search order, redirects, history, path recency, OKF metadata, vendor guidance and model/tool memory do not override that ledger.

- [Concepts](concepts/README.md)
- [Architecture](architecture/README.md)
- [Authority](authority/README.md)
- [Contracts](contracts/README.md)
- [Experience / questioning / explanation](experience/README.md)
- [Cross-cutting invariants](invariants/README.md)
- [Policies](policies/README.md)
- [Reference](reference/README.md)

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 across 1,237 stable IDs. The accepted concept catalog remains 24 concepts.

## Current operational authority and policy

- [Agentic Development Foundation](agentic_development_foundation/README.md) — durable human-directed authority, context, workflow, conformance, compatibility, security and lifecycle policy.
- [Canonical Knowledge / ownership mechanics](canonical_knowledge_retrofit/README.md) — durable ownership/routing mechanics; completed CKR execution evidence is historical.
- [Documentation Physical Topology Normalization](documentation_topology_normalization/README.md) — active pre-implementation topology program.
- [Implementation program](implementation/README.md) — implementation planning/progression; currently blocked on DPTN exit.

## History and provenance

[`history/README.md`](history/README.md) is explicitly **HISTORY / PROVENANCE ONLY**. It contains preserved Phase 001–010 material, prior reference/foundation/planning/design-history trees, completed CKR/ADF program evidence, and the pre-DPTN-E authored OKF routing tree. Historical occurrences never become current owners because they exist or appear first in search.

## Generated OKF v0.2 projection

Top-level `knowledge/` remains for generic OKF v0.2 consumers as a **deterministically generated compatibility projection**, not a separately maintained routing plane.

- Projection specification: [`routing/okf_projection.json`](routing/okf_projection.json)
- Generator/checker: `scripts/agentic/generate_okf_projection.py`
- Generated compatibility entry: `knowledge/index.md`
- Generated output: `../knowledge/`
- Preserved pre-convergence authored tree: [`history/routing/okf-pre-dptn-e/`](history/routing/okf-pre-dptn-e/)

Do not hand-edit generated `knowledge/` files. Change the current owning documentation, workflow/implementation catalog, or bounded projection specification as appropriate, then regenerate and validate the projection. Generated OKF `stable`, `verified`, routing text or provenance never carries DMTZ proposition authority.

## DPTN-F routing result

MOVE-019 has rebound current stable-reference, agent/rule/link and drift-analysis consumers to normalized first-class paths. Repository-native discovery now consistently starts here; current link validation does not substitute history; scoped rules no longer route through Phase 010/pre-DPTN paths. Completed CKR checks may still reconstruct their accepted-era routing only inside the dedicated ephemeral compatibility wrapper.

`canonical/README.md` and legacy `docs/canonical/<family>` redirects remain compatibility-only pending DPTN-G retirement. They are not semantic owners or stable-ID locators.

## Current next dependency

**DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: NEXT / READY / NOT STARTED.**

DPTN-F acceptance does not authorize DPTN-G or product implementation automatically. Implementation 001-A remains blocked until DPTN-G exit acceptance and a later explicit human-selected implementation task.
