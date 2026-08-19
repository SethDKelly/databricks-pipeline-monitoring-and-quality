# Concept: Baseline

**Status:** Accepted — Phase 002 Group 03

## Purpose

Let the ecosystem represent descriptive reference behavior derived from evidence for a comparable subject/context without asserting that the reference behavior is normatively correct.

## Operational principle

Table C has produced 19–21 million rows on comparable business days over a sufficiently representative historical window. A new 14-million-row Observation is materially outside that reference behavior even though no approved row-count Expectation exists. The product can therefore say that the result is atypical relative to the Baseline, but it cannot call the value unacceptable or unhealthy solely from that comparison. After a structural business change, the old Baseline can become non-comparable and a new version can be derived without rewriting prior assessments.

## Actors

- Monitoring framework
- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Data Steward / Governance Steward

## State

- identified subject;
- measured dimension/property;
- reference population and evidence window;
- comparison context, such as environment, calendar, cohort, operating window, or other comparability factors;
- derived reference characteristics, ranges, distributions, frequencies, or other descriptive summaries;
- derivation meaning/method context at the functional level;
- evidence coverage and sufficiency limitations;
- creation/derivation time and version;
- comparability/applicability limitations or retirement state;
- provenance and supporting Observation references;
- ambiguity when multiple plausible Baselines exist.

## Actions

### `derive`
- **Intent:** establish descriptive reference behavior from a defined evidence population/context.
- **State effect:** records a versioned Baseline with supporting evidence, comparison context, derivation basis, and limitations.
- **Failure / unknown behavior:** insufficient or non-representative evidence yields `insufficient evidence` rather than artificial precision.

### `refresh`
- **Intent:** derive a new prospective Baseline version from newer or changed evidence/context.
- **State effect:** preserves the earlier Baseline and the assessments that referenced it.
- **Important:** refresh does not silently absorb anomalous recent behavior into an existing Baseline.

### `markNonComparable`
- **Intent:** record that a Baseline should no longer be treated as comparable for a defined context because of a structural break, scope change, or other justified limitation.
- **State effect:** preserves the Baseline as historical evidence while constraining future use.

### `resolveComparable`
- **Intent:** determine which Baseline, if any, is suitable for comparison with a subject/dimension/context/time.
- **Observable result:** one or more comparable candidates, insufficient evidence, non-comparable, ambiguous, unauthorized, or unavailable.

## Invariants / behavioral expectations

- Baseline is descriptive, not normative.
- Typical behavior is not automatically healthy, acceptable, or correct.
- Atypical behavior is not automatically degraded, defective, or unacceptable.
- A Baseline is derived from evidence and retains the population/window/context that produced it.
- Historical abnormality does not become an approved criterion merely because it is repeated.
- Insufficient history, sparse coverage, or poor comparability must not produce false precision.
- Baseline derivation does not own or mutate the supporting Observations.
- A refreshed Baseline creates a new reference version; it does not rewrite the reference used by an earlier Assessment.
- Structural breaks, seasonality, business-calendar effects, or population changes can make a Baseline non-comparable even when historical data is plentiful.
- Baseline comparison must preserve direction/meaning: being numerically different does not by itself establish whether the difference is better or worse.
- Baseline is implementation-neutral and does not prescribe statistical or machine-learning algorithms.

## Ambiguity and missing evidence

More than one Baseline may be plausible for a context, for example weekday versus month-end behavior. When the product cannot determine comparability, it returns ambiguous/non-comparable rather than selecting the most convenient window. Missing history is `insufficient evidence`, not a zero-width or default Baseline.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Semantic Definition** can provide comparison meaning, grain, units, or business-calendar context.
- **Observation** supplies the evidence population used to derive a Baseline.
- **Assessment** may compare a current Observation with a comparable Baseline while preserving that the result is descriptive rather than normative.
- **Expectation** remains independent; a human/authority may establish an Expectation informed by a Baseline, but the product does not promote it automatically.
- **Change** can later identify structural shifts relevant to Baseline comparability.
- **Annotation** may later add known business context without altering the underlying Baseline evidence.

## Security / privacy / governance considerations

Baselines can reveal sensitive volumes, business cycles, seasonality, operational cadence, and organizational behavior. A viewer may be authorized to receive an abstract comparative result while being denied the underlying reference values or historical distribution.

Supporting observations must not be broadened beyond their authorized use merely to derive or display a Baseline.

## Evidence / provenance considerations

A Baseline must retain its evidence window/population, comparison context, derivation meaning, sufficiency limitations, supporting Observation provenance, version, and any non-comparability decision. Historical replay must be able to identify the Baseline that was available and used at the time of an Assessment.

## Representative scenarios

### Stable volume reference
Table C produces approximately 19–21 million rows on comparable business days. A 14-million-row Observation is outside the Baseline but is not automatically a quality failure without a normative criterion.

### Seasonal comparison
Month-end volume is much larger than ordinary weekdays. A weekday Baseline is not used for month-end merely because it is the most recent reference.

### Structural break
A legitimate business migration permanently changes volume. The old Baseline is preserved for history but marked non-comparable for the new operating context.

### Sparse history
A newly onboarded asset has too little representative history. The Baseline resolves as insufficient rather than manufacturing a threshold.

### Multiple plausible references
Two comparison cohorts are both plausible and produce materially different references. The ambiguity is exposed until context can resolve it.

### Unauthorized reference values
A business user may see `atypical versus comparable history` while detailed sensitive volume ranges remain restricted.

## Non-goals

- defining approved/required behavior;
- declaring normative health;
- selecting a specific anomaly-detection algorithm;
- causal inference;
- silently adapting itself to recent behavior;
- replacing semantic/business-calendar context.

## Deferred questions

- Which Baseline classes are necessary for the first MVP: ranges, distributions, cadence/duration profiles, seasonal cohorts, or others?
- What evidence is sufficient to mark a structural break/non-comparability automatically versus requiring human context?
- How should Baseline version stability be balanced against changing business behavior in later implementation design?
