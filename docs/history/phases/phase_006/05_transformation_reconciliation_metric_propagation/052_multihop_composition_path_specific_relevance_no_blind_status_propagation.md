# HLTH-052 — Multi-Hop Composition, Path-Specific Relevance & No Blind Status Propagation

## Rule

Reconciliation relationships are local to the transformation semantics they bind. Multi-hop propagation across A→B→C requires an explicit valid composition of those relationships; it is not implied by path reachability.

## Invariants

- A metric, Baseline result, warning, normative violation, severity, waiver or exception does not recursively propagate through Lineage.
- A local upstream Observation becomes downstream-relevant only when a material path consumes the corresponding field/population/version under transformation semantics that make the evidence relevant.
- A valid A↔B reconciliation plus valid B↔C reconciliation does not automatically establish a direct A↔C equality/conservation rule.
- Different downstream consumers can have different relevant reconciliation relationships even when they share an upstream asset.
- Unused upstream fields/partitions/populations need not be material to a downstream reconciliation merely because asset-level Lineage exists.
- Partial/restricted Lineage can constrain path-specific relevance conclusions and must remain explicit.
- Propagated context remains evidence/context, not a duplicate downstream Observation unless a derived reconciliation Observation is actually computed/established.
