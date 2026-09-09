# DPTN-B Execution Review

**Status:** IN EXECUTION

## Scope

DPTN-B prepares the normalized historical namespace and clears the first-class path collisions assigned by DPTN-A. It executes MOVE-001 through MOVE-006 only. It does not promote current canonical owners, change stable-ID meaning, decompose mixed ADF/CKR directories, converge OKF, rebind current stable-ID locators, or start product implementation.

## Candidate design

The physical relocation is intentionally content-conservative:

- create `docs/history/` with an explicit HISTORY / PROVENANCE ONLY authority contract;
- attach the six existing source Git trees beneath their accepted history targets without regenerating their contents;
- remove the six legacy source roots in the same atomic Git-tree commit;
- preserve original provenance identity while making physical history location explicit to relocation-aware validation;
- keep `docs/canonical/` unchanged as the current semantic root throughout DPTN-B;
- keep Implementation 001-A blocked on DPTN exit.

## Bound moves

- MOVE-001 — `docs/concepts` → `docs/history/phases`;
- MOVE-002 — `docs/reference` → `docs/history/reference-legacy`;
- MOVE-003 — `docs/foundation` → `docs/history/foundation`;
- MOVE-004 — `docs/planning` → `docs/history/planning`;
- MOVE-005 — `docs/decisions` → `docs/history/decisions`;
- MOVE-006 — `docs/design_history` → `docs/history/design-history`.

The source tree SHAs are frozen in `dptn_b_relocation_manifest.json`. This permits exact-tree validation and avoids semantic rewriting of historical records.

## Collision result sought

DPTN-B closes the historical/collision responsibilities of COL-001 through COL-005 only. In particular, clearing `docs/concepts/`, `docs/reference/` or `docs/decisions/` does not itself assign those paths current authority. Reuse is controlled by later explicitly selected DPTN phases.

## Conservation baseline

- current semantic root: `docs/canonical/`;
- accepted concepts: 24;
- accepted stable IDs: 1,237 across eight families;
- architecture family: ARCH-001–ARCH-500;
- CKR ownership lifecycle: `ckr_complete`;
- ADF/CKR mixed-lifecycle directories remain in place;
- Implementation 001-A remains blocked / not started.

## Candidate validation

Pending exact-head Agentic conformance and Documentation consistency after the atomic relocation cutover.

## Acceptance

Not yet accepted. DPTN-B remains IN EXECUTION until the relocated candidate, adversarial guards and closure state pass exact-head validation.
