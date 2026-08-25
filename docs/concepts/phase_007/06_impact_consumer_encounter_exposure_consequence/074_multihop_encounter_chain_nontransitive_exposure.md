# OPS-074 — Multi-Hop Encounter Chain & Non-Transitive Exposure

**Status:** Accepted — Phase 007 Group 06

## Purpose

Prevent exposure from propagating automatically through downstream topology.

## Contract

If A suspect state is encountered by B and B later produces B2, C is not automatically exposed to A merely because C consumes some B output.

An indirect exposure chain requires sufficient evidence linking each material transmission step, for example:

**A suspect V → B consumed V → B output B2 materially derives from that encounter → C consumed B2**.

The exact burden depends on the proposition. If the question is only whether C consumed B2, the A→C causal/transmission claim is unnecessary. If the question is exposure to A's affected state through B, intermediary state/version and semantic transmission evidence may be required.

## Invariants

- upstream exposure ≠ transitive downstream exposure.
- multi-hop Lineage ≠ multi-hop encounter proof.
- intermediary output identity matters where state propagation is claimed.
- indirect exposure ≠ downstream degradation or causal effect.
