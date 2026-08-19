# Concept: Baseline

**Status:** Accepted — Phase 002 Group 03; synchronization refined by Group 04

## Purpose

Let the ecosystem represent descriptive reference behavior derived from evidence for a comparable subject/context without asserting that the reference behavior is normatively correct.

## Operational principle

Table C has produced 19–21 million rows on comparable business days over a sufficiently representative historical window. A planned filter Change Intent indicates that, if activated, C's population should structurally decrease and the existing volume Baseline will likely cease to be comparable. The intent can register that prospective comparability break, but the old Baseline remains applicable until realization evidence establishes the new operating context. After activation, sufficient post-change Observations are used to derive a new Baseline; the intended value itself never becomes a Baseline.

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
- prospective comparability-break context linked to registered Change Intent when known;
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

### `registerProspectiveBreak`
- **Intent:** record that an accepted Change Intent is expected to make the Baseline non-comparable if/when the structural change is realized.
- **State effect:** records a pending comparability boundary linked to the intent; it does not end current applicability by itself.
- **Important:** intended post-change values are not inserted into the Baseline.

### `markNonComparable`
- **Intent:** record that a Baseline should no longer be treated as comparable for a defined context because a structural break, realized change, scope change, or other justified limitation has been established.
- **State effect:** preserves the Baseline as historical evidence while constraining future use.

### `resolveComparable`
- **Intent:** determine which Baseline, if any, is suitable for comparison with a subject/dimension/context/time.
- **Observable result:** one or more comparable candidates, insufficient evidence, non-comparable, ambiguous, unauthorized, or unavailable.

## Invariants / behavioral expectations

- Baseline is descriptive, not normative.
- Typical behavior is not automatically healthy, acceptable, or correct.
- Atypical behavior is not automatically degraded, defective, or unacceptable.
- A Baseline is derived from evidence and retains the population/window/context that produced it.
- A Change Intent may identify a prospective structural break, but intent alone does not rewrite or terminate the active Baseline.
- A post-change Baseline is derived from post-change evidence; it is never manufactured from anticipated effects.
- Historical abnormality does not become an approved criterion merely because it is repeated.
- Insufficient history, sparse coverage, or poor comparability must not produce false precision.
- Baseline derivation does not own or mutate the supporting Observations.
- A refreshed Baseline creates a new reference version; it does not rewrite the reference used by an earlier Assessment.
- Structural breaks, seasonality, business-calendar effects, population changes, or realized pipeline changes can make a Baseline non-comparable even when historical data is plentiful.
- Baseline comparison must preserve direction/meaning: being numerically different does not by itself establish whether the difference is better or worse.
- Baseline is implementation-neutral and does not prescribe statistical or machine-learning algorithms.

## Ambiguity and missing evidence

More than one Baseline may be plausible for a context. A registered Change Intent may also predict a break that never activates. In that case the existing Baseline remains applicable unless other evidence changes comparability. Missing history is `insufficient evidence`, not a default Baseline.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Semantic Definition** can provide comparison meaning, grain, units, or business-calendar context.
- **Observation** supplies the evidence population used to derive a Baseline.
- **Assessment** may compare a current Observation with a comparable Baseline while preserving that the result is descriptive rather than normative.
- **Expectation** remains independent; an authority may establish a post-change Expectation informed by planned business behavior, but the product does not promote a Baseline automatically.
- **Change Intent** can register a prospective comparability break but cannot set post-change Baseline values.
- **Deployment/Change** provide realization evidence that can make the prospective break effective.
- **Annotation** may later add known business context without altering the underlying Baseline evidence.

## Security / privacy / governance considerations

Baselines can reveal sensitive volumes, business cycles, seasonality, operational cadence, and organizational behavior. Change Intent can also reveal future business behavior. A viewer may receive an abstract comparative result while being denied reference values or planned details.

## Evidence / provenance considerations

A Baseline retains its evidence window/population, comparison context, derivation meaning, sufficiency limitations, supporting Observation provenance, version, and any prospective/effective non-comparability decision. Historical replay must identify both the Baseline used and whether a planned/realized structural break was known at that time.

## Representative scenarios

### Stable volume reference
Table C produces approximately 19–21 million rows. A 14-million-row Observation is outside Baseline but is not automatically a quality failure.

### Planned filter transition
A Change Intent predicts a structural volume reduction. The old Baseline gets a prospective break linked to activation. After Deployment/Change evidence establishes realization, the old Baseline becomes non-comparable for the new context and a new one is derived from post-change Observations.

### Intent never activates
The planned filter is cancelled or never becomes active. The prospective break never takes effect; the old Baseline remains comparable.

### Immediate post-change validation
Before enough new history exists, a separately established post-change Expectation validates the first runs. Baseline remains insufficient until evidence supports derivation.

### Seasonal comparison
Month-end volume is much larger than ordinary weekdays. A weekday Baseline is not used for month-end merely because it is most recent.

### Structural break without registered intent
An upstream source legitimately changes population without a Change Intent. Realized Change can still mark the old Baseline non-comparable.

## Non-goals

- defining approved/required behavior;
- declaring normative health;
- selecting anomaly-detection algorithms;
- causal inference;
- silently adapting to recent behavior;
- accepting planned values as empirical Baseline evidence.

## Deferred questions

- first-MVP Baseline classes;
- evidence required to activate a prospective comparability break;
- automatic versus human structural-break decisions;
- stability/adaptation policy in later implementation design.
