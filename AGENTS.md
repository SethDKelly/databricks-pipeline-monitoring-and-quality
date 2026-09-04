# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-C has completed its 24-concept + SYN-001–SYN-035 atomic authority cutover and awaits closure validation. Product implementation remains blocked until CKR-K.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`: `canonicalized` → inventoried `docs/canonical/` owner; `legacy_authoritative` / `candidate_ready` → inventoried legacy owner; `history_only` → provenance/rationale only.

The 24 accepted concepts now resolve to `docs/canonical/concepts/`; SYN-001–SYN-035 resolve to `docs/canonical/contracts/synchronization/`. Phase 002/003 are provenance for those migrated meanings. REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain later-group legacy authority.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 bounded change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit authorization; A4 semantic/architecture change requires explicit change control.

Completing one CKR group does not authorize the next. Do not autonomously select backlog work, merge/deploy unattended, delegate implementation, or reopen architecture.

## Context and semantic conservation

Use `human task → live CKR authority → ownership inventory when unclear → current owner → exact IDs/tests as needed`. OKF is routing only; search order, phase recency, path presence, vendor guidance, model/tool memory, or synchronization order never establish semantic authority.

Preserve Observation ≠ Assessment; Expectation ≠ Baseline; Change Intent ≠ Deployment ≠ Change; execution success ≠ output existence ≠ freshness/data quality; missing evidence ≠ negative truth; Lineage/reachability ≠ exposure ≠ Impact ≠ cause; Investigation closure ≠ causal confirmation; authentication ≠ Capability Authorization ≠ Assertion Authority; Capability Authorization ≠ evidence sufficiency ≠ enforcement; Gate readiness ≠ decision ≠ delivery ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevented exposure ≠ release/recovery; current ≠ historical/as-known.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500. Only SYN has cut over in CKR-C.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not domain health, provider-runtime proof, Databricks capability or production readiness.
