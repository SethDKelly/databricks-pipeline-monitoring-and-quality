# EXPL-021 — Explicit Cross-Concept Join Logic & Non-Transitive Composition

**Status:** Accepted — Phase 008 Group 02

## Requirement

When a material statement depends on multiple concepts, preserve the accepted semantic join that licenses the derived proposition.

Examples of valid joins are those already defined by SYN/REF/AUTH/HLTH/OPS contracts, such as:

- Observation + Expectation/Baseline context → Assessment;
- historical path + encounter/version evidence → Impact exposure state;
- Safeguard enforcement + opportunity/path/non-exposure coverage → bounded prevented-exposure determination;
- Gate decision/delivery/enforcement + execution evidence → bounded Gate enforcement interpretation.

## Invariants

Cross-concept composition is not generally transitive. In particular:

- Lineage + failure ≠ downstream failure;
- Deployment + post-deployment deviation ≠ cause;
- confirmed upstream Causal Claim ≠ downstream exposure/effect;
- Safeguard active + not exposed ≠ prevented exposure;
- Gate HOLD + no run ≠ proven enforcement without coverage.

Explanation must reference the accepted join logic rather than rely on prose adjacency.
