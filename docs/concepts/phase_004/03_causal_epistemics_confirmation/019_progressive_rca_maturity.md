# REF-019 — Progressive RCA Maturity and Fast-Path Causal Communication

**Status:** Accepted — Phase 004 Group 03

## Purpose

Allow RCA to produce useful causal information progressively as evidence becomes available while preventing low-latency results from overstating causal maturity.

## Functional progression

Causal reasoning may mature through states such as:

1. **candidate discovery / proposed claims** — fast structural/timing evidence identifies plausible propositions worth evaluating;
2. **early support/weakened/unresolved evaluation** — applicable operational/health/change evidence begins discriminating claims;
3. **deeper investigative RCA** — Lineage, encounter/consumption, alternatives, contrasts, analyst research, and richer health evidence strengthen or weaken propositions;
4. **retrospective/post-operations causal review** — late/corrected evidence, broader coverage, downstream evidence, and explicit confirmation review may revise status.

These are evidence-maturity horizons, not mandatory services or fixed latency tiers.

## Rules

- Surface the strongest status currently justified by the evidence known at the current cutoff; do not wait for perfect completeness when a narrower result is already useful.
- A leading fast-path hypothesis is labeled `proposed` unless evidence already satisfies `supported` semantics.
- `supported` may be surfaced early when its applicable evidence standard is satisfied; it is never paraphrased as `root cause confirmed`.
- `RCA complete` or Investigation closure must not imply `confirmed` if claims remain supported/unresolved.
- Direct deterministic evidence can justify a strong result quickly when the applicable evidence/confirmation profile is genuinely satisfied; elapsed time itself is not a maturity requirement.
- Conversely, long-running analysis does not earn stronger status without stronger evidence.
- Causal results carry knowledge/evaluation time and material limitations so later enrichment can be compared honestly.
- High-consequence automation, gate/safeguard decisions, or business communication may require a causal/evidence status stronger than an early hypothesis; operational policy for those uses is later refinement.

## Example

At 07:12, historical timing and Lineage make `B contributed to C row loss` a proposed claim. At 07:18, evidence that B materially declined and C consumed the affected B version supports the claim. At 07:30, join-key evidence supports a second contributor. Post-ops evidence may later strengthen, weaken, or confirm claims under an explicit confirmation profile. The 07:18 supported result remains historically valid and was not a confirmation.

## Timing handoff

- Phase 006 defines health evidence/result timing needs feeding RCA.
- Phase 008 defines audience-facing communication of causal maturity.
- Phase 009 characterizes source availability/latency for RCA evidence.
- Phase 010 selects implementation/performance architecture.
- Phase 011 sets MVP latency/availability acceptance criteria.

## Non-goals

- fixed RCA SLA;
- causal engine/LLM selection;
- requiring post-ops review before every supported claim;
- lowering confirmation evidence requirements for speed.
