# SYN-025 — Downstream Candidate + Health Evidence → Observed Effect

**Status:** Accepted — Phase 003 Group 05

## Outcome

Associate downstream Observation, Assessment, and realized Change evidence with an Impact candidate without requiring or fabricating causal attribution to the originating condition.

## Participating concepts and actions

- **Impact** — `linkDownstreamEffect`.
- **Observation** — downstream measured/retrieved facts.
- **Assessment** — downstream normative/comparative interpretation.
- **Change** — downstream realized material differences where justified.
- **Expectation** and **Baseline** remain the basis for downstream Assessment through previously accepted synchronization semantics.
- **Capability Authorization** controls disclosure of downstream-health detail.

## Trigger / initiating condition

A downstream Impact candidate has relevant health, timing, freshness, quality, or operational evidence during the incident/impact window.

## Preconditions

Candidate identity/time and the downstream evidence are traceable. Reference context for any Assessment is already correctly resolved.

## Coordination semantics

1. Resolve relevant downstream Observations, Assessments, and Changes for the candidate/time window.
2. Link those facts to the candidate's Impact state as downstream-effect evidence.
3. Preserve the evidence dimension: execution timing, freshness, completeness, volume, validity, availability, delivery, metric state, or another accepted dimension.
4. A downstream effect may be recorded even when exposure to the originating state remains `unknown`; the two branches do not block one another.
5. Exposure can also be established while downstream monitored dimensions remain healthy or unchanged.
6. If the product asserts that the origin caused the downstream effect, that proposition must synchronize through Causal Claim rather than being hidden in Impact.

## State and evidence effects

Observation/Assessment/Change own downstream facts. Impact owns the link that those facts are relevant to the downstream candidate picture. No causal truth is created.

## Ambiguity / failure propagation

Missing downstream monitoring produces unknown effect state, not `no effect`. Conflicting Assessments remain conflicts. Out-of-scope candidates can remain reachable/exposed with reduced or unavailable downstream-health evidence.

## Temporal semantics

Effect evidence is resolved for the downstream event time and retained with knowledge-time history. A later correction can change retrospective effect interpretation without mutating the prior incident view.

## Provenance / traceability

Every linked effect remains traceable to source Observation/Assessment/Change and exact reference basis where applicable.

## Security / authorization

The actor may be allowed to see `quality requirement violated` without seeing the exact threshold, raw value, protected metric, or consumer identity. Safe abstraction must be explicitly authorized rather than inferred from aggregation.

## Invariants

- exposure ≠ downstream degradation;
- observed downstream effect ≠ causal attribution;
- unknown exposure does not erase independently observed downstream effect;
- missing downstream monitoring ≠ no effect;
- Baseline atypicality ≠ normative violation;
- downstream Assessment keeps its original basis and epistemic meaning.

## Scenarios

**Exposed but healthy:** a Metric View consumes affected C but remains within its monitored Expectations.

**Effect with unknown exposure:** a report metric violates an Expectation, but consumed-version proof is unavailable; both truths remain explicit.

**Restricted health detail:** the analyst sees `freshness requirement violated` while exact timestamps are hidden.

## Non-goals

Causal attribution, business harm determination, alerting policy, or redefining health metrics.

## Deferred questions

Minimum downstream-health dimensions required for first-MVP Impact and how to summarize multi-dimensional effects without inventing composite health.