# DPTN Topology Authority

**Status:** CANDIDATE — DPTN-A / NOT PHYSICAL CUTOVER AUTHORITY

## Purpose

DPTN normalizes the physical documentation tree after CKR without reopening accepted semantics. Its unit of change is **path/lifecycle/routing**, not product meaning.

## Authority order during DPTN

1. Accepted current semantic owner selected by the CKR ownership inventory.
2. Accepted stable-ID resolver and canonical owner content.
3. Live DPTN program status for topology work only.
4. Existing implementation status and agentic development rules.
5. DPTN move map as future-location planning evidence only.
6. Historical design material and Git history as provenance only.

A proposed target path never becomes authoritative before the relevant DPTN cutover is accepted.

## Allowed changes

DPTN may:

- create and populate `docs/history/` as an explicitly non-current namespace;
- move preserved design/provenance material without altering its historical content except links/banners required to preserve navigation and role;
- promote accepted canonical-owner files from `docs/canonical/<family>/` into first-class `docs/<family>/` paths after collisions are cleared;
- update the CKR ownership inventory, stable-ID resolver, OKF routes, agent rules and link/validation machinery only to reflect accepted physical moves;
- split mixed-lifecycle ADF/CKR directories into durable current policy versus historical program/execution evidence;
- converge the manually maintained `knowledge/` plane into `docs/` or a generated projection if DPTN-E proves compatibility;
- create temporary migration manifests, validators and exit evidence required to execute DPTN safely.

## Forbidden changes

DPTN may not:

- change the meaning of any accepted concept or stable contract;
- add, remove or renumber SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH IDs;
- change the accepted 24-concept catalog or ARCH-001–500 partition semantics;
- rewrite architecture, authority, evidence, temporal, health, lineage, impact, explanation, integration or control contracts merely for aesthetic consolidation;
- create product source code, schemas, migrations, adapters, runtime configuration, deployment assets or implementation evidence;
- treat a move, redirect, generated index or OKF entry as proof of product implementation;
- delete historical evidence merely because Git history exists;
- bulk-move mixed ADF/CKR program directories before DPTN-D classifies durable policy versus history;
- start Implementation 001-A before DPTN-G exit acceptance and a subsequent explicit human-selected implementation task.

## Conservation invariants

Throughout DPTN:

- semantic owner meaning before = semantic owner meaning after;
- stable-ID meaning before = stable-ID meaning after;
- accepted ranges and counts remain unchanged;
- one current semantic question resolves to one current owner;
- history remains provenance and cannot compete with current authority;
- current-vs-history lookup remains explicit;
- agent context budgets may not materially regress merely because paths changed;
- current policy and implementation planning remain distinguishable from design history;
- physical relocation does not strengthen epistemic, authority, authorization, causal, health or implementation status.

## Target topology principle

The target path should communicate lifecycle role:

```text
docs/<current-domain>/...     current accepted meaning/current operational policy
docs/implementation/...      current implementation planning/execution state
docs/history/...             provenance, design chronology, superseded plans, reviews and handoffs
```

`docs/index.md` is intended to become the single human/tool-neutral discovery root. Whether top-level `knowledge/` is removed or retained as a generated projection is a DPTN-E decision, not a DPTN-A assumption.

## Cutover discipline

DPTN-A creates no physical moves. Later move phases must use dependency-safe cutovers:

1. validate source role and target vacancy/registered collision resolution;
2. create/move historical destinations before reclaiming their old first-class names;
3. move current owners only with synchronized ownership/routing/stable-reference updates;
4. validate exact-head conformance after each logical cutover;
5. never leave two reachable current semantic owners for the same meaning;
6. never leave a stable ID resolving only to a history path.

## Temporary-artifact rule

DPTN manifests and migration execution evidence are not new semantic authority. On DPTN exit they must either:

- move under `docs/history/retrofits/dptn/` as execution/provenance evidence; or
- be retained only if they are demonstrably needed as generated operational routing/validation inputs.

No temporary move-map registry may become a second permanent semantic ownership ledger.
