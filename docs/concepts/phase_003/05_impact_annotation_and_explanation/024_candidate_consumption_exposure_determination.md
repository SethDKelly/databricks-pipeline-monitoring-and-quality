# SYN-024 — Impact Candidate + Consumption Evidence → Exposure Determination

**Status:** Accepted — Phase 003 Group 05

## Outcome

Determine whether a downstream candidate actually encountered the relevant affected output/state/version/time window, keeping proven exposure, proven non-exposure, and insufficient evidence distinct.

## Participating concepts and actions

- **Impact** — `evaluateExposure`.
- **Execution History** — actual downstream execution/refresh lifecycle evidence.
- **Observation** — version, refresh, read/consumption, publication, or other encounter facts where available.
- **Deployment** and **Lineage** — contextual evidence when relevant to identifying the active consumer/producer relationship.
- **Capability Authorization** — controls disclosure of consumer identity and exposure basis.

## Trigger / initiating condition

An Impact candidate exists and an actor needs to know whether it actually consumed or encountered the affected state.

## Preconditions

The originating state/time window and candidate identity are sufficiently defined. The relevant consumption relationship is known or explicitly uncertain.

## Coordination semantics

1. Resolve the candidate and relevant historical relationship/path.
2. Collect evidence capable of showing actual encounter/consumption: version association, refresh provenance, execution input/output linkage, publication state, or another source appropriate to the consumer class.
3. Record `exposed` only when evidence sufficiently establishes that the candidate encountered the affected state or relevant condition.
4. Record `not exposed` only when evidence coverage is sufficient to establish the negative for the relevant window.
5. Timing overlap, graph reachability, or a downstream run occurring after the upstream event may support inquiry but does not by itself prove consumption.
6. Where the available evidence only establishes possible encounter, preserve `unknown/insufficient` rather than inferring exposure.
7. Exposure determination remains separate from whether the downstream candidate's own health changed.

## State and evidence effects

Impact owns exposure/consumption state and references source evidence. Execution History/Observation/Deployment/Lineage retain ownership of their respective facts.

## Ambiguity / failure propagation

Unknown consumed version, missing refresh provenance, incomplete telemetry, conflicting execution records, or restricted evidence can leave exposure unresolved. `Not exposed` cannot be inferred from missing telemetry.

## Temporal semantics

Exposure is resolved for the relevant originating-state interval and candidate consumption time. Later-arriving version/refresh evidence can revise the retrospective exposure state while preserving the earlier knowledge-time result.

## Provenance / traceability

Exposure/not-exposure results retain the exact evidence basis and its coverage/limitations.

## Security / authorization

A viewer may be allowed to know `an additional restricted consumer was exposed` without seeing the consumer identity or version details. Conversely, exposure state itself may be restricted.

## Invariants

- candidate/reachable ≠ exposed;
- downstream-after-upstream timing ≠ consumed affected state;
- exposed ≠ degraded;
- exposed ≠ caused downstream effect;
- missing consumption evidence ≠ not exposed;
- `not exposed` requires adequate negative evidence coverage.

## Scenarios

**Report refreshed from affected C:** refresh/version evidence establishes exposure.

**Reachable report not refreshed:** reliable refresh history shows no qualifying refresh; `not exposed` is supported.

**Unknown version:** the report refreshed in the window but consumed-version evidence is unavailable; exposure remains unresolved.

**Opaque consumer:** exposure is visible at an aggregate/opaque level while identity remains restricted.

## Non-goals

Health Assessment, causal inference, business consequence, consumer-technology implementation, or universal version-tracking requirements.

## Deferred questions

Evidence sufficiency standards for each consumer class and minimum first-MVP version/consumption evidence.