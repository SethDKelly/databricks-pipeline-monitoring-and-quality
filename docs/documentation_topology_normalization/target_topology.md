# DPTN Target Topology

**Status:** DPTN-A TARGET / NOT YET PHYSICAL AUTHORITY

The target is intentionally DMTZ-shaped rather than a mechanical copy of another repository.

```text
docs/
├── index.md
├── README.md
├── authority/
├── architecture/
├── concepts/
├── contracts/
├── decisions/
├── experience/
├── invariants/
├── policies/
├── reference/
├── implementation/
├── agentic/
└── history/
    ├── README.md
    ├── phase-status.md
    ├── phases/
    ├── foundation/
    ├── planning/
    ├── reference-legacy/
    ├── foundations/
    │   └── adf/
    └── retrofits/
        └── ckr/
```

## First-class current categories

The eight semantic families currently nested below `docs/canonical/` are planned for first-class promotion: `architecture`, `authority`, `concepts`, `contracts`, `experience`, `invariants`, `policies`, and `reference`.

`docs/decisions/` and `docs/implementation/` remain first-class.

`docs/agentic/` is reserved for durable current ADF/CKR-derived operational policy, routing metadata and tool evidence after DPTN-D decomposition. It is not a product-semantic authority namespace unless an individual resource is already explicitly authoritative for agent/developer behavior.

## History

`docs/history/` physically realizes the design-history role CKR previously kept logical. Historical files retain their accepted-at-the-time narrative. Relocation does not rewrite them to match final current truth.

## Discovery

`docs/index.md` is planned as the primary maintained discovery surface.

`docs/README.md` remains as a compact GitHub-friendly orientation/compatibility surface rather than a second full knowledge index.

Top-level `knowledge/` should be removed if no real provider/tool requirement exists. If compatibility requires it, it must be generated from current docs/routing metadata rather than hand-maintained as a peer knowledge tree.

## Collision order

- `docs/concepts/phase_002..phase_010` → history before `docs/canonical/concepts` → `docs/concepts`;
- legacy `docs/reference` → history before `docs/canonical/reference` → `docs/reference`;
- CKR/ADF mixed directories split only after current semantic paths stabilize.

This file is a target topology contract for DPTN execution planning, not evidence that any target path exists yet.
