# SYN-018 — Evidence Candidate → Historical Evidence Assembly

**Status:** Accepted — Phase 003 Group 04

## Outcome

Assemble the historical facts needed to evaluate a candidate explanation using the correct event-time context while preserving source ownership, missing evidence, and contradictory facts.

## Participating concepts and actions

- **Investigation** — `linkEvidence`, `refineScope`.
- **Execution History** — `resolveAt`.
- **Observation** — `retrieve`.
- **Assessment** — `explainBasis` where relevant.
- **Change** — `resolveWindow`.
- **Deployment** — `resolveActiveAt`.
- **Change Intent** — `resolvePlannedAt`.
- **Baseline** / **Expectation** — relevant historical reference context.
- **Propagation Safeguard** — `resolveAt` where protection changed propagation/timing.
- **Lineage** — historical relationship evidence.

## Trigger / initiating condition

SYN-017 yields one or more candidate entities/paths, or an analyst introduces a specific candidate for investigation.

## Preconditions

Candidate identity/path and Investigation time/question context are known enough to request relevant historical evidence.

## Coordination semantics

1. Retrieve candidate execution, output, timing, quality, change, deployment, intent, and safeguard evidence relevant to the outcome being explained.
2. Keep event/effective time aligned across sources and preserve collection/knowledge time separately.
3. Retrieve both supporting-looking and contradicting-looking facts; do not filter evidence to match an initiating theory.
4. Distinguish factual absence established with sufficient coverage from missing telemetry.
5. Preserve the exact Expectation/Baseline versions used in contemporaneous Assessments rather than substituting current references.
6. Link evidence into the Investigation by source reference instead of copying/mutating source truth.
7. Expand or narrow Investigation scope if assembled evidence establishes that the original window/subject boundary was inadequate.

## State and evidence effects

Source concepts own the retrieved facts. Investigation owns only the relevance links and inquiry history.

## Ambiguity / failure propagation

Conflicting measurements, ambiguous execution association, uncertain activation time, non-comparable states, restricted evidence, or incomplete coverage remain explicit. An evidence gap never becomes a reassuring negative.

## Temporal semantics

Historical evidence is assembled for the incident interval and can also preserve what was known at a selected contemporaneous knowledge time versus what became known later.

## Provenance / traceability

Every linked item retains source concept, subject, time, evidence provenance, and limitations.

## Security / authorization

Restricted evidence may contribute only through allowed opaque/derived context. Investigation aggregation is not an authorization bypass.

## Invariants

- evidence assembly ≠ causal conclusion;
- missing evidence ≠ negative fact;
- current state ≠ incident-time state;
- evidence supporting the leading theory must not suppress contradiction;
- safeguard state may explain operational delay without proving protected-data defect.

## Scenarios

For C row loss, assemble B row count, join-key nulls, A row count, C execution/order, relevant Deployment, Change Intent, and historical reference context. For a delivery delay, assemble upstream duration, readiness deadlines, safeguard activation, and downstream start/completion facts.

## Non-goals

Automatic hypothesis ranking, raw-data replication, evidence-authority precedence, or causal confirmation.
