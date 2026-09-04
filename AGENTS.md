# Repository Agent / Developer Instructions

## Authority and live state

DMTZ current product/design semantics remain repository-owned. During the Canonical Knowledge & Documentation Authority Retrofit (CKR), current ownership is determined **record by record** by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`:

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current authority;
- `canonicalized` → inventoried target under `docs/canonical/` is current authority;
- `history_only` → provenance/rationale, not current semantic authority.

Design-phase progression remains in `docs/README.md`; CKR progression is owned by `docs/canonical_knowledge_retrofit/README.md`; implementation progression is owned by `docs/implementation/README.md`; the completed ADF is owned by `docs/agentic_development_foundation/README.md` and `execution_exit_review.md`.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: IN EXECUTION CKR-A; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR is a later documentation-authority dependency inserted before product code begins. **Implementation 001-A is not active and remains blocked until CKR-K exit acceptance.**

Phase 010 architecture and accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meanings remain frozen unless explicit A4 change control says otherwise. CKR changes owner paths/routing, not semantics by convenience.

Use `knowledge/index.md` for portable discovery only when the authoritative resource is not already known. OKF is routing, not semantic authority.

## Shared authority precedence

When instructions or documents conflict, preserve:

1. the current semantic owner selected by the CKR ownership inventory plus accepted DMTZ stable-ID contracts;
2. root `AGENTS.md`;
3. live CKR / implementation status and explicitly active group;
4. accepted ADF authority/scope/security mechanics;
5. DMTZ-owned portable workflows/platform overlays;
6. reviewed vendor operational guidance and thin tool-specific adapters;
7. personal/user-level preferences and tool memory.

A human request establishes the current task and action, but does not weaken higher semantic/security authority.

## Canonical knowledge vs design history

`docs/canonical/` is the future current-truth namespace. Its presence alone does not make a file authoritative. Follow `docs/canonical_knowledge_retrofit/migration_contract.md`.

Once a record is `canonicalized`:

- answer current semantic questions from its canonical owner;
- treat former phase/decision sources as provenance/design history for that record;
- do not reconstruct current meaning by reading chronological phases;
- use history for rationale, historical comparison, rejected alternatives, scenario evidence or explicit change review.

Before cutover, continue to use the inventoried legacy owner. A candidate canonical file cannot silently override it.

There is no accepted dual-current-authority state.

## Human-directed action classes

Follow `docs/agentic_development_foundation/authority_scope_policy.md`:

- **A1 — read/review/plan:** inspect, resolve, validate and report; do not edit unless changes are also requested.
- **A2 — change/build/fix:** perform in-scope repository edits plus directly necessary validation/status/traceability.
- **A3 — external/destructive/scope-expanding:** requires explicit task-specific human authorization plus normal gates.
- **A4 — architecture/semantic change:** follows DMTZ change control; never hide semantic change inside canonicalization/refactoring.

Do not create unrelated follow-on work, reprioritize the backlog, delegate repository implementation to other agents, merge/deploy unattended, or auto-start the next group.

Tool memory, auto-memory, chat history and generated summaries are advisory only. Correctness-critical facts belong in repository artifacts.

## Context and stable-reference discipline

Use the shortest authoritative path:

`human task → live CKR/implementation authority → known explicit current owner/path/ID; otherwise ownership inventory or one OKF route → current semantic owner → exact IDs/tests as needed`.

Do not preload all phases, contracts, knowledge entries, DMTZ/vendor skills or design history.

Accepted stable ranges remain:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

During CKR-A–I, `scripts/agentic/resolve_stable_id.py` still discovers exact occurrences without manufacturing canonicality. CKR-J will make canonicalized stable-ID owner lookup deterministic. Search order is never authority.

If a reference cannot be resolved, report the failure; do not reconstruct it from memory or assume no constraint exists.

## Knowledge and workflow discipline

The OKF bundle remains a discovery plane governed by the accepted ADF policies. During CKR, some OKF routes may still terminate at legacy current owners until their domains are canonicalized and CKR-J completes routing conversion.

- canonical/current owners beat OKF summaries;
- OKF metadata is not DMTZ truth, health, evidence sufficiency or causality;
- candidate canonical resources are not promoted by OKF;
- design-history resources are not normal current-truth targets after cutover;
- generated/routing artifacts never push semantic change into current authority.

Canonical workflows under `.agents/skills/` include `resolve-context`, `implement-group`, `resolve-contract`, `run-conformance`, `review-change`, `update-traceability`, and `exit-review`. Databricks overlays remain environment discovery, acquisition, persistence, Lineage, runtime provenance and governance.

Selecting a skill inside an existing human task does not create scope or permission.

## Databricks Agent Skills discipline

The accepted Databricks vendor profile remains core, DABs, Jobs, Pipelines, data discovery, DBSQL, Unity Catalog and Lakeflow Connect. Vendor skills are operational guidance, never semantic or authorization authority. Model/AI skills remain deferred; managed Databricks MCP servers require separate review.

`DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation after CKR unlocks implementation. CKR does not perform or waive it.

## Provider-runtime residual

ADF-EX-17 remains **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**. `ADF-G-XT01` remains open for Cursor, Claude Code and Codex, all of which remain runtime-`unverified` until actual evidence exists. Ordinary IDE/CLI development remains supported.

## CKR semantic-conservation rules

CKR is a documentation-authority retrofit, not a semantic redesign.

- preserve all accepted concepts, stable IDs, invariants and architecture boundaries;
- omitted accepted meaning is a migration defect, not simplification;
- do not choose “newest file wins” or “first search hit wins” when legacy sources appear inconsistent;
- genuine contradictions require explicit change-control adjudication before cutover;
- preserve design-history provenance rather than rewriting old phases to match final current truth;
- physical history relocation is optional; authority separation is mandatory;
- once a record is canonicalized, normal current-truth routing must stop treating its legacy phase source as the current owner.

## Conformance

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

It validates documentation consistency, OKF, adapters, skills, stable references, ADF status, **canonical knowledge authority/inventory, CKR status**, fixtures, context budgets, provider evidence, Databricks vendor profile, security/lifecycle and negative controls.

The report describes repository agentic/documentation-authority conformance only. It is not DMTZ domain health, data quality, provider-runtime proof, target Databricks capability or production readiness.

## Frozen semantic invariants

Implementation and CKR migration must preserve at minimum:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Entity Identity ≠ source-local identity/name;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- evidence sufficiency ≠ authority ≠ authorization ≠ enforcement;
- source assertion ≠ authoritative assertion;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- execution success ≠ timely run ≠ freshness ≠ structural compatibility ≠ data quality;
- missing telemetry/evidence ≠ observed absence/negative truth;
- current state ≠ historical state;
- later evidence ≠ evidence known then;
- event/effective time ≠ source availability ≠ framework knowledge/recorded time;
- Lineage ≠ exposure ≠ Impact ≠ cause;
- deployment/correlation timing ≠ causation;
- Investigation/leading hypothesis ≠ confirmed cause;
- reachability ≠ encounter/exposure;
- exposure ≠ downstream effect ≠ business consequence;
- authentication ≠ Capability Authorization;
- Capability Authorization ≠ Assertion Authority;
- current disclosure permission ≠ historical truth/communication;
- passive monitoring ≠ active Execution Gate;
- Gate readiness ≠ Gate decision ≠ enforcement ≠ actual execution;
- Safeguard proposal/configuration ≠ enforcement ≠ prevention ≠ recovery;
- model/search output cannot manufacture truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions;
- unknown/conflicting/stale/partial/unavailable/withheld remain first-class states.

Exact current owner paths may change through CKR, but these accepted meanings may not change silently.

## Implementation state

**Product implementation is blocked until CKR-K.** Do not create `src/dmtz`, executable schemas, product tests or Databricks deployment artifacts as part of CKR unless an explicit separate task authorizes a needed migration tool or semantic change.

Once implementation is unlocked, implementation engineering/test/security rules in `docs/implementation/` apply against canonical current-truth resources rather than phase chronology.
