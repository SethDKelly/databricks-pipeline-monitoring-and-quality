# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; IN EXECUTION CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-D is human-selected and in execution. Product implementation remains blocked until CKR-K.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`: `canonicalized` → inventoried `docs/canonical/` owner; `legacy_authoritative` / `candidate_ready` → inventoried legacy owner; `history_only` → provenance/rationale only.

The 24 concepts and SYN-001–SYN-035 are canonicalized. During CKR-D candidate review, `reference.authority_vocabulary`, REF-001–030 and AUTH-001–053 remain legacy-authoritative under Phase 004/005 until atomic cutover.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 bounded change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit authorization; A4 semantic/architecture change requires explicit change control.

Completing CKR-D does not authorize CKR-E. Do not autonomously select backlog work, merge/deploy unattended, delegate implementation, or reopen architecture.

## Context and semantic conservation

Use `human task → live CKR authority → ownership inventory when unclear → current owner → exact IDs/tests as needed`. `knowledge/index.md` is optional routing only; search order, recency, path presence, vendor guidance, tool memory or synchronization order never establish authority.

Preserve Observation ≠ Assessment; Expectation ≠ Baseline; missing evidence ≠ negative truth; applicability ≠ coverage ≠ sufficiency; event/effective time ≠ source availability ≠ framework knowledge; Lineage/reachability ≠ exposure ≠ Impact ≠ cause; causal `confirmed` requires REF-017 + AUTH-034; Assertion Authority ≠ Capability Authorization ≠ Responsibility Assignment; authentication ≠ authorization; governed meaning ≠ normative Expectation ≠ realized state; permission/approval ≠ issuance ≠ enforcement ≠ outcome; Gate readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevented exposure ≠ release/recovery; current disclosure ≠ historical authorization/communication.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS is repository agentic/documentation-authority conformance, not domain health, provider-runtime proof, Databricks capability or production readiness.
