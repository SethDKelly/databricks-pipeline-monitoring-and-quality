# DPTN Topology Authority

**Status:** DPTN-A CANDIDATE — PLANNING AUTHORITY ONLY

## Purpose

Documentation Physical Topology Normalization (DPTN) removes accidental filesystem complexity left by the design/CKR evolution while conserving accepted DMTZ meaning and provenance.

DPTN answers a physical question:

> Where should current truth, current operational policy, implementation authority, derived routing, and historical provenance live so a human or agent can infer lifecycle role from the path without reconstructing project chronology?

It does not reopen any accepted semantic or architecture decision.

## Authority order during DPTN

1. accepted current DMTZ semantic owner selected by the CKR ownership inventory;
2. root `AGENTS.md` and live DPTN/implementation status;
3. accepted ADF human-directed/security/change-control rules;
4. DPTN topology inventory and move map for physical relocation planning only;
5. historical provenance;
6. derived OKF/search/tool memory.

The DPTN inventory cannot make a historical source current, make a derived projection authoritative, change stable-ID meaning, or override the CKR owner selected for a semantic question.

## Frozen semantic baseline

DPTN-A is based on `main` commit `6ac773ad2eeb5678773d1ee7c39f0492dbaeb29f`.

The following are frozen for topology purposes:
- 24 accepted concepts;
- SYN-001–035;
- REF-001–030;
- AUTH-001–053;
- HLTH-001–066;
- OPS-001–123;
- EXPL-001–160;
- INTG-001–270;
- ARCH-001–500 plus the frozen reference architecture;
- all accepted semantic distinctions and current CKR ownership state.

A later DPTN phase may change a path. It may not change the accepted meaning associated with that path/ID without separate normal DMTZ change control.

## Lifecycle roles

DPTN uses the smallest useful set of physical roles:

- **current semantic authority** — accepted product/domain/architecture meaning;
- **current operational policy** — durable development, security, routing and workflow rules;
- **current implementation authority** — implementation plan/progression/evidence;
- **living orientation** — compact current status/discovery surface, not an independent semantic owner;
- **derived routing projection** — generated/index/routing aid, rebuildable from current authority;
- **historical provenance** — accepted-at-the-time design, planning, migration and review evidence;
- **mixed / requires split** — a migration-era directory containing both durable current material and history;
- **validation tooling / provider adapter** — executable guard or thin tool bridge.

## Target-path invariant

After DPTN exit, the intended default inference is:

- `docs/<domain>/...` = current accepted meaning or current durable operational policy;
- `docs/implementation/...` = current implementation authority/evidence;
- `docs/history/...` = historical provenance/rationale/accepted-at-the-time records;
- `docs/index.md` = primary maintained discovery surface;
- top-level `knowledge/` = absent or generated-only if a verified tool/provider requirement exists.

## Collision policy

A current target path must never be populated while incompatible historical material still occupies that namespace.

Therefore:
1. relocate history first;
2. validate provenance reachability;
3. promote current canonical owners;
4. update ownership/routing metadata atomically with the relevant promotion;
5. rebind agents after the physical topology is stable.

`docs/concepts/` and `docs/reference/` are explicit collision families and must be cleared by DPTN-B before DPTN-C promotion.

## Mixed-directory policy

`docs/canonical_knowledge_retrofit/` and `docs/agentic_development_foundation/` may not be recursively bulk-moved.

They require explicit decomposition because:
- CKR contains durable authority/routing assets as well as migration evidence;
- ADF contains durable human-directed/security/context/tooling policies as well as design/execution history.

DPTN-D must enumerate the current set before moving any member.

## Anti-bloat rule

DPTN may add temporary execution metadata needed to prove safe relocation, but it must not create a new permanent semantic registry parallel to CKR/current owners. The move map is an execution ledger and becomes historical/derived at DPTN exit.

## DPTN-A physical-change prohibition

While DPTN-A is the active group:
- all pre-existing documentation paths remain physically unchanged;
- no old path is retired;
- no canonical owner is promoted to a new first-class path;
- no agent resolver is rebound to a future path.

DPTN-A completes only when inventory and move-map completeness are validated. Physical relocation begins only after a separately selected DPTN-B task.
