# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–F COMPLETE / ACCEPTED — DPTN-G NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-F; NEXT DPTN-G; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge, operational policy, routing projections and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

Current semantic authority remains selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` at first-class `docs/<family>/` paths. `docs/index.md`, generated OKF, history, redirects, move maps and routing helpers are never semantic owners.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: COMPLETE / ACCEPTED.**
- **DPTN-E — OKF / Documentation Root Convergence: COMPLETE / ACCEPTED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: COMPLETE / ACCEPTED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: NEXT / READY.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## Accepted DPTN-A–E baseline

DPTN-A accepted the topology authority/inventory/move map. DPTN-B established `docs/history/` and relocated historical roots through MOVE-001–006. DPTN-C promoted the eight current semantic owner families through MOVE-007–014. DPTN-D decomposed durable CKR/ADF operational policy from completed program evidence through MOVE-015/016. DPTN-E converged discovery through MOVE-017/018: `docs/index.md` became the single authored discovery root and top-level `knowledge/` became deterministic generated OKF compatibility.

## Accepted DPTN-F result

DPTN-F executed **MOVE-019 — in-place routing rebinding** after physical topology stabilization:

- repository-native agents/tools now use `docs/index.md` for unknown-location discovery;
- generated `knowledge/index.md` remains explicit OKF v0.2 compatibility only;
- exact stable-ID lookup remains `scripts/agentic/resolve_stable_id.py <ID>` → one current `owner_path::ID`; historical discovery requires explicit `--history`;
- durable CKR authority/migration/template/human-inventory routing now names first-class `docs/<family>/` owners and `docs/history/` provenance;
- Cursor scoped-rule reference headers now point to first-class current semantic owners and current implementation packages rather than Phase 010 or pre-DPTN roots;
- current agentic link validation requires real current targets and no longer substitutes DPTN-D history paths;
- generated-OKF impact analysis derives current body-link scope from the ownership inventory's `canonical_owner_roots`;
- current agentic reference validation now runs against the real topology, while completed CKR validators alone retain their bounded ephemeral accepted-era projection.

**COL-009 and COL-011 are resolved by DPTN-F.** The generated DPTN-E OKF tree remains unchanged. The eight substantive semantic owner trees retain their accepted DPTN-E identities; the catalog remains 24 concepts and 1,237 stable IDs across eight families, including ARCH-001–ARCH-500.

Accepted evidence: [`dptn_f_rebinding_manifest.json`](dptn_f_rebinding_manifest.json), [`fixtures/dptn_f_rebinding_scenarios.yaml`](fixtures/dptn_f_rebinding_scenarios.yaml) and [`dptn_f_execution_review.md`](dptn_f_execution_review.md).

## Conservation baseline

DPTN-F changes routing only. It preserves:

- 24 accepted concepts;
- SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500;
- 1,237 stable IDs across eight families;
- the frozen reference architecture;
- accepted ADF and CKR exits;
- ADF-EX-17 / ADF-G-XT01 as bounded deferred runtime verification;
- Implementation 001-A as BLOCKED / NOT STARTED.

## DPTN-G handoff boundary

**DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: NEXT / READY / NOT STARTED.** DPTN-F acceptance does not authorize it automatically.

DPTN-G owns MOVE-020, final legacy-path/redirect retirement, migration-scaffolding disposition, whole-program conservation audit and DPTN exit decision. Until that exit is accepted, Implementation 001-A remains blocked.
