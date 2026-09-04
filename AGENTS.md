# Repository Agent / Developer Instructions

## Live state and authority

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. The **Canonical Knowledge & Documentation Authority Retrofit (CKR)** is the active pre-implementation dependency. CKR-A is complete; CKR-B is in execution. Product implementation remains blocked until CKR-K exit acceptance.

Current DMTZ semantic ownership is determined record-by-record by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`:

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current authority;
- `canonicalized` → inventoried target under `docs/canonical/` is current authority;
- `history_only` → provenance/rationale only.

A path under `docs/canonical/`, a newer phase file, an OKF entry, a search hit, vendor guidance or model memory does **not** independently establish semantic authority.

Primary live authorities:

1. current semantic owner selected by the CKR inventory plus accepted stable-ID semantics;
2. this `AGENTS.md`;
3. `docs/canonical_knowledge_retrofit/README.md` / active CKR group;
4. `docs/implementation/README.md` for implementation progression;
5. accepted ADF authority/scope/security mechanics;
6. DMTZ workflows/platform overlays;
7. reviewed vendor operational guidance;
8. personal/tool memory.

## CKR-B boundary

CKR-B owns only the nine inventoried foundation/glossary records. Their current state is `candidate_ready`, so the legacy foundation/glossary owners remain current authority until the atomic cutover is accepted.

Do not promote CKR-C concept resources, REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH domains, implementation code, or unrelated documentation as part of CKR-B.

CKR-B may consolidate accepted wording, remove obsolete future-phase/open-question language from the canonical candidates, add provenance, and strengthen deterministic migration validation. It may not invent new product semantics, concept boundaries, stable IDs, authority, or architecture.

## Current-truth vs design-history rule

Once a record is `canonicalized`, answer current semantic questions from its canonical owner. Use phase/decision/scenario/exit history for provenance, rationale, historical comparison, rejected alternatives or explicit semantic-change review—not to reconstruct current meaning.

Before cutover, use the inventoried legacy owner. `candidate_ready` is review-only. There is no accepted dual-current-authority state.

CKR migration follows:

- `docs/canonical_knowledge_retrofit/authority_model.md`;
- `docs/canonical_knowledge_retrofit/migration_contract.md`;
- `docs/canonical_knowledge_retrofit/canonical_document_template.md`.

Atomic cutover must update authority marker, ownership inventory, required routing and provenance together. Genuine semantic contradictions require explicit A4 change control; never resolve them by newest-file/search-order preference.

## Human-directed action classes

Follow `docs/agentic_development_foundation/authority_scope_policy.md`:

- **A1** review/inspect/plan — no edits unless changes are also requested;
- **A2** change/build/fix — in-scope edits plus directly necessary validation/status/traceability;
- **A3** external/destructive/scope-expanding — explicit task-specific authorization plus normal gates;
- **A4** architecture/semantic change — explicit DMTZ change control.

Completing one group does not authorize the next. Do not autonomously select backlog work, delegate implementation to other agents, merge/deploy unattended, or reopen architecture.

## Context and stable references

Use the shortest authoritative path:

`human task → live CKR/implementation authority → known current owner/path/ID; otherwise ownership inventory or one OKF route → current semantic owner → exact IDs/tests as needed`.

Do not preload all phases, contracts, knowledge entries, DMTZ/vendor skills or history.

Accepted stable ranges remain frozen:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

`scripts/agentic/resolve_stable_id.py` discovers exact occurrences and exposes CKR family state; it does not manufacture exact canonical ownership. CKR-J will add deterministic canonical owner/anchor resolution after substantive migration.

`knowledge/` remains OKF v0.2 routing only. It cannot promote candidates or history into current truth.

## Semantic conservation

Preserve at minimum:

- Entity Identity ≠ source-local identity/name;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- evidence sufficiency ≠ authority ≠ authorization ≠ enforcement;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- execution success ≠ freshness ≠ data quality;
- missing evidence ≠ observed absence/negative truth;
- current state ≠ historical/as-known state;
- later evidence ≠ evidence known then;
- event/effective time ≠ source availability ≠ framework knowledge time;
- Lineage ≠ encounter/exposure ≠ Impact ≠ cause;
- deployment/correlation timing ≠ causation;
- Investigation/hypothesis ≠ confirmed cause;
- authentication ≠ Capability Authorization ≠ Assertion Authority;
- current disclosure permission ≠ historical truth;
- passive monitoring ≠ active Execution Gate;
- Gate readiness ≠ decision ≠ enforcement ≠ execution;
- Safeguard configuration ≠ enforcement ≠ prevention ≠ recovery;
- model/search output cannot manufacture truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions;
- unknown/conflicting/stale/partial/unavailable/withheld remain first-class states.

Omitted accepted meaning is a migration defect, not simplification.

## Tool / Databricks residuals

ADF-EX-17 remains **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**. `ADF-G-XT01` remains open; Cursor, Claude Code and Codex remain runtime-`unverified` until actual evidence exists.

The reviewed Databricks skill set remains core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Vendor skills are operational guidance only. Model/AI skills and managed Databricks MCP servers remain deferred.

`DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation after CKR-K unlocks implementation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

This validates repository agentic/documentation-authority configuration, including CKR ownership/status. PASS is not DMTZ domain health, provider-runtime proof, target Databricks capability or production readiness.

## Implementation gate

**Do not start product implementation while CKR is incomplete.**
