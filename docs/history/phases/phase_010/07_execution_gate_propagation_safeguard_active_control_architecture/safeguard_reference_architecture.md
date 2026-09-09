# Propagation Safeguard Reference Architecture

## Objective

Constrain propagation or delivery of exact affected/suspect state on bounded paths/cohorts while preserving the distinction between enforcement, non-exposure, REF-028 prevention and recovery.

## Logical components

1. **Protected-state registry** — exact affected/suspect state/version set and effective interval.
2. **Path/cohort registry** — delivery surfaces, consumers/cohorts and alternate-path topology relevant to protection.
3. **Safeguard profile** — eligible actions, adapters, authorization, expiry/release rules and degradation behavior.
4. **Protection decision journal** — proposal/authorization/request identity.
5. **Enforcement adapters** — deployment-specific mechanisms capable of constraining exact path/state/cohort.
6. **Enforcement reconciler** — proves actual effective enforcement and partial/bypass conditions.
7. **Opportunity reconciler** — identifies actual consumer encounter/exposure opportunities.
8. **Prevention evaluator** — applies REF-028 using exact opportunity/path/enforcement/alternate-path evidence.
9. **Release/recovery reconciler** — distinguishes effective release from recovered state.

## Enforcement patterns

Deployment-specific adapters may include policy denial, serving-route suppression, view/table/path substitution, cache invalidation/hold, delivery disablement, export suppression, or other mechanisms. The architecture does not assign universal semantics to any one vendor feature.

An adapter qualifies only if the target enterprise deployment exposes the capability and evidence exists to observe whether it actually applied.

## Partial protection

Safeguard coverage is represented per path/cohort. If dashboard path A is protected but export path B remains open, the system records path A enforcement and unresolved/open B rather than global `protected=true`.

## Safe stale serving

Serving a prior known-safe version is represented as a separate result state. It may reduce exposure to the affected current version while still violating freshness/currentness requirements. Health remains use/profile specific.

## Prevention

Prevention requires an opportunity that would otherwise have encountered affected state. A control that happened to be active during an interval with no consumer opportunity receives no prevention credit.

Alternate paths are checked before global prevention/non-exposure claims. Multi-hop protection is evaluated hop-by-hop.

## Release and recovery

A request to release protection is authorized and journaled. Effective release requires evidence from the enforcement adapter. Recovery then requires independently observed healthy/current/usable state and may be consumer/use specific.

## Degraded telemetry

If enforcement telemetry is missing, DMTZ reports enforcement unknown/partial as appropriate. It does not assume a fail-open or fail-closed outcome from configuration alone.
