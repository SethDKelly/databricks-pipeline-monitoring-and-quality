# Group 08 — Observability & SLO Architecture

## No global health score

Runtime observability is multidimensional across acquisition/integration, canonical persistence, derived projections, serving, reasoning/replay, optional model/search, archive/restore and active control.

## Service-class SLOs

Group 08 keeps SC-01–SC-06 as the SLO unit. Numeric targets are deployment ADR values after real publication lag, quota, workload and product promises are measured.

- **SC-01:** source publication → acquisition → canonical persistence → near-current projection.
- **SC-02:** scheduled evidence/check completion within profile cadence.
- **SC-03:** bounded Investigation/RCA enrichment; partial leads remain useful.
- **SC-04:** correct historical replay/restore; correctness outranks interactivity.
- **SC-05:** retained communication/basis retrieval by retention tier.
- **SC-06:** decision/authorization/delivery/enforcement within opportunity-specific applicability horizon.

An SLO miss is an operational proposition; it is not evidence that the monitored pipeline/data is unhealthy.

## Correlation and tracing

Operational traces correlate request, acquisition, reasoning, control and canonical identities where useful, while retaining that traces themselves are not source truth. Sensitive values are minimized.

## Required dashboards/alerts

Operational views expose the individual health dimensions and their source watermarks. Alerting may aggregate routing priorities but must preserve the underlying dimensions and cannot become a domain conclusion.