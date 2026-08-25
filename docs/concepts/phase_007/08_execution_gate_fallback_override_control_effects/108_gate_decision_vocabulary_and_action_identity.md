# OPS-108 — Gate Decision Vocabulary & Action Identity

**Status:** Accepted — Phase 007 Group 08

## Purpose

Keep admission decisions, exceptional decision bases and opportunity terminal states from collapsing into one lifecycle flag.

## Accepted decision/action distinctions

For a bound opportunity:

- `hold` — barrier should remain constraining the opportunity;
- `admit` — Gate barrier should be removed/permissive for the opportunity;
- `override` — separately authorized opportunity-specific admission despite the normal readiness result;
- fallback-applied action — the explicit configured fallback selected after its defined trigger actually applied;
- escalation — request/route for intervention, not itself an admission decision unless explicit policy creates one;
- cancellation/expiry — terminal opportunity/control-action facts, not failed execution.

Decision records bind actor/control principal, basis, reason, criterion/result references, time, authorization and provenance.

## Invariants

- `hold` ≠ failed run;
- `admit` ≠ run occurred;
- `override` ≠ ready;
- escalation ≠ admit/hold by convenience;
- opportunity expiry/cancellation ≠ execution failure.