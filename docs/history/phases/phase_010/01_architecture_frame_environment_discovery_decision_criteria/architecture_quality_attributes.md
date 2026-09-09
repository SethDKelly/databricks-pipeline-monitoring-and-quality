# Phase 010 Group 01 — Architecture Quality Attributes & Tradeoff Frame

## Hard constraints

These are architecture rejection gates rather than optimization weights:

| Hard constraint | Required behavior |
|---|---|
| Semantic fidelity | Preserve accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG distinctions. |
| Evidence traceability | Material conclusions retain proposition/source/basis provenance. |
| Degraded-evidence safety | Missing/failed/restricted telemetry never becomes benign negative truth. |
| Identity correctness | No convenience joining by mutable name/timestamp when exact identity is required. |
| Historical correctness | Current state is not silently projected backward; late evidence remains late for earlier K. |
| Authority/authorization separation | Availability, authority, permission and enforcement remain independent. |
| Security/disclosure | Least privilege and independent basis/detail visibility are preserved. |
| Control evidence | Gate/Safeguard configuration is not substituted for enforcement/effect evidence. |
| Optional-source safety | Optional vendor absence degrades exact capabilities rather than fabricating defaults. |

Any option that cannot satisfy a hard constraint is rejected before comparative optimization.

## Decision-specific optimization attributes

Later ADRs evaluate the subset materially affected by the decision:

| Attribute | Questions |
|---|---|
| Availability/resilience | Can supported sibling capabilities continue under source/component failure? |
| Latency | Does the option meet the relevant service class rather than an invented global SLA? |
| Durability/replay | Can required source/evidence/communication history survive intended horizons? |
| Scalability | How does the option behave as workspaces, runs, evidence volume and consumers grow? |
| Operational simplicity | What is the real deployment, upgrade, support and on-call burden? |
| Observability/testability | Can failures, partial reads, joins, replay and evidence provenance be verified? |
| Reversibility/evolvability | How hard is migration as environment facts and requirements change? |
| Quota efficiency | Does retrieval respect source-specific primary/secondary/query limits? |
| Cost efficiency | What ingestion/query/storage/compute/egress/control cost is created? |
| Portability | Which assumptions bind the design to one cloud, region, plan or vendor deployment? |
| Performance | What query/graph/replay/control workloads are material and how are they bounded? |
| Maintainability | Can source adapters and optional capabilities evolve without semantic drift? |

## Tradeoff discipline

- Do not sum attributes into one framework architecture score.
- State which attributes are decisive for each ADR and why.
- Distinguish measured facts, public defaults, contract facts, assumptions and unknowns.
- Record capability loss explicitly when choosing a simpler MVP path.
- Prefer reversible choices when evidence is weak unless doing so violates a hard constraint.
- A cheaper/faster option cannot win by reducing required evidence coverage without explicitly scoping out the dependent proposition.

## Default priority posture

Without a more specific decision context, Phase 010 treats these as highest-order constraints:

1. semantic/evidence correctness;
2. security/disclosure and least privilege;
3. safe degraded behavior and observability;
4. durable identity/provenance/history where promised;
5. service-class fitness;
6. operational simplicity, scalability and evolvability;
7. cost/quota efficiency.

This ordering is a starting posture, not a universal scoring formula. Individual decisions must document their own tradeoff rationale.
