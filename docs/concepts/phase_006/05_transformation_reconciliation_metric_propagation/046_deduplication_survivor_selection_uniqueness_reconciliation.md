# HLTH-046 — Deduplication, Survivor Selection & Uniqueness Reconciliation

## Rule

Deduplication reconciliation binds the duplicate-equivalence definition, input grain, candidate groups, survivor-selection rule/version, and output grain.

Useful derived observations can include:

- candidate duplicate-group count;
- records participating in duplicate groups;
- records removed;
- survivors retained;
- post-dedup uniqueness under the intended key;
- survivor-selection outcome characteristics where relevant.

## Invariants

- For a pure dedupe operation, output population can be less than or equal to eligible input population, but the exact relationship depends on duplicate-group semantics.
- `input - output` does not by itself prove the number of business duplicates unless the dedupe scope/rule is established.
- Successful dedupe can improve output uniqueness without proving the upstream source was healthy.
- Survivor selection can change completeness, distribution, freshness or business values even when duplicate removal count is expected.
- A changed key or survivor rule creates a material reconciliation/version boundary.
- Deduplication metrics do not automatically propagate as downstream health outcomes.
