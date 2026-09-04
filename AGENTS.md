# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-F; IN EXECUTION CKR-G; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-G has completed atomic EXPL cutover and remains in execution pending closure validation. Product implementation remains blocked until CKR-K.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`: `canonicalized` → inventoried `docs/canonical/` owner; `legacy_authoritative` / `candidate_ready` → inventoried legacy owner; `history_only` → provenance/rationale only.

Foundation/glossary, all 24 concepts, SYN-001–035, authority vocabulary, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123 and EXPL-001–160 are canonicalized. Phase 001–008 sources are provenance for migrated meanings. INTG/ARCH remain later-group legacy authority.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 bounded change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit authorization; A4 semantic/architecture change requires explicit change control. CKR-G does not authorize CKR-H.

## Context and semantic conservation

Use `human task → live CKR authority → ownership inventory when unclear → current owner → exact IDs/tests as needed`. `knowledge/index.md` is optional routing only; search order, recency, path presence, vendor guidance, tool memory or synchronization order never establish authority.

Preserve question ≠ truth ≠ authorization; answer statement ≠ independent truth; basis count ≠ confidence; sibling statements remain independent; ran ≠ succeeded ≠ output ≠ current/fresh output ≠ healthy; Change Intent ≠ Deployment ≠ Change; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; candidate/reachable ≠ opportunity ≠ exposure ≠ effect ≠ consequence ≠ causal attribution; Safeguard administration ≠ enforcement ≠ prevention ≠ recovery; readiness ≠ Gate decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; unknown/unresolved ≠ false/absent/safe; restricted/redacted ≠ absent; safe abstraction cannot strengthen truth; elapsed time/rewording ≠ evidence or maturity; retained actual communication ≠ reconstructed historical Explanation; historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
