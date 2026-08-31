# 001-F — First Health Question: Freshness Observation → Assessment → Statement IR

**Status:** Planned

## Goal

Prove DMTZ's first complete deterministic evidence-to-answer vertical slice.

## Question

> **Is subject X stale at requested effective time T / knowledge cut K, and what evidence supports the answer?**

## Required chain

```text
canonical Entity reference
   ↓
Monitoring Scope seam / pilot configuration
   ↓
applicable freshness Expectation revision
   ↓
eligible freshness Observation(s)
   ↓
evidence suitability / knowledge-cut filter
   ↓
freshness Assessment
   ↓
Statement IR
   ↓
deterministic human-readable rendering
```

Full enterprise Monitoring Scope/authorization engines arrive in 002. In 001, use explicit pilot configuration/stub interfaces whose contract matches the future boundary; do not replace them with `True` constants hidden in domain code.

## Freshness semantics

The first slice should use an explicit freshness criterion such as:

- maximum age since an evidenced relevant update/publication event; or
- a bounded expected update window.

The exact pilot criterion must be versioned as an Expectation. Do not infer the normative threshold from historical regularity.

A successful Databricks run may be shown as separate context but cannot be used as proof of data freshness.

## Observation

The freshness Observation records the evidenced relevant time/value and provenance. If the measurement/source is unavailable, emit no fake age/zero value; the evaluation becomes unknown/unavailable/partial as appropriate.

## Assessment

Assessment binds:

- subject;
- Expectation revision;
- eligible Observation(s);
- requested effective/time window;
- knowledge cut;
- outcome;
- evidence suitability/limitations.

The result must distinguish at least:

- meets freshness Expectation;
- violates freshness Expectation;
- insufficient/unknown/unavailable evidence.

## Statement IR

Construct a minimum Statement IR that captures:

- proposition: freshness status of subject;
- subject ID/display projection;
- effective time and knowledge cut;
- Assessment result/status;
- basis Evidence/Expectation/Observation/Assessment IDs;
- limitations/coverage/integration-health context;
- current rendering schema/version.

The deterministic renderer turns IR into prose without changing status or basis.

## Required scenario cases

1. fresh evidence → meets Expectation;
2. stale evidence → violates Expectation;
3. run succeeded but freshness violated → still stale;
4. acquisition unavailable → freshness unknown/unavailable;
5. late evidence excluded at K1 but included at K2;
6. corrected evidence changes retrospective Assessment without rewriting the prior recorded Assessment/Explanation state if retained.

## Acceptance gates

- all cases pass as structured IR assertions;
- prose rendering is secondary to IR correctness;
- every statement has exact basis references;
- no LLM/search/vector/graph dependency;
- no current-state backfill into historical K;
- at least one case runs end to end against development Databricks evidence by 001-H.
