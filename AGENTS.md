# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-I; IN EXECUTION CKR-J; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-A–I are complete/accepted. CKR-J is in execution/routing-cutover validation. Product implementation remains blocked until CKR-K.

Current semantic ownership is selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`. All accepted semantic families through ARCH are canonicalized; Phase 001–010 sources are provenance for migrated meanings.

Authority order: current semantic owner → root `AGENTS.md` → live CKR/implementation status → accepted ADF scope/security mechanics → DMTZ workflows/overlays → reviewed vendor operational guidance → tool/personal memory.

## Human-directed boundary

Follow `docs/agentic_development_foundation/authority_scope_policy.md`: A1 review; A2 bounded change plus required validation/status/traceability; A3 external/destructive/scope-expanding requires explicit authorization; A4 semantic/architecture change requires explicit change control. CKR-J does not authorize CKR-K or product implementation.

## Canonical routing

Use `human task → live CKR authority → current canonical owner → exact IDs/tests as needed`.

When an exact stable ID is known, use `python3 scripts/agentic/resolve_stable_id.py <ID>` to obtain its deterministic **canonical owner** locator `owner_path::ID`. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.

When semantic location is unknown, `knowledge/index.md` may route through one bounded domain concept to the canonical owner. OKF, the stable-ID resolver, search order, recency, path presence, vendor guidance, tool memory and synchronization order never establish semantic authority themselves.

Do not preload the full stable-ID corpus or OKF bundle. Read only the smallest canonical context required for the task.

## Semantic conservation

Preserve documented capability ≠ deployment support; framework retention authority ≠ source Assertion Authority; copied evidence ≠ independent corroboration; Observation ≠ Assessment; Expectation ≠ Baseline; authentication ≠ Capability Authorization ≠ Assertion Authority; Monitoring Scope ≠ accessibility ≠ authorization ≠ successful observation; timestamp/name proximity ≠ exact cross-system join; integration failure ≠ monitored-product negative; execution success ≠ output existence ≠ currentness/freshness ≠ health; Lineage/reachability ≠ encounter/consumption ≠ exposure; exposure ≠ effect ≠ consequence ≠ causal attribution; Investigation/localization ≠ Causal Claim; `confirmed` requires REF-017 + AUTH-034; graph/search/vector/model output ≠ truth or authority; historical source state ≠ as-known-at-cut Explanation ≠ retained actual communication ≠ current retrospective Explanation; Gate evidence suitability ≠ readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Safeguard enforcement ≠ prevention ≠ release ≠ recovery.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

## Residuals / conformance

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future Implementation 001-A work. Databricks vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
