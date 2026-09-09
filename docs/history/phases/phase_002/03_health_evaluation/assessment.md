# Concept: Assessment

**Status:** Accepted — Phase 002 Group 03

## Purpose

Let users understand what authorized Observation evidence means relative to applicable normative Expectations and/or comparable descriptive Baselines for a defined subject, dimension, context, and time.

## Operational principle

Table C's latest row count is compared with a comparable historical Baseline and is materially atypical. Its last material update is separately compared with an applicable freshness Expectation and satisfies the deadline. The product therefore records two dimension-scoped Assessments: volume is atypical relative to history, while freshness meets its normative criterion. It does not call the table wholly healthy, degraded, or causally explained by combining those results implicitly.

## Actors

- Monitoring framework
- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Data Steward / Governance Steward

## State

- identified subject;
- assessed dimension/property and relevant context;
- evaluated event/interval time and assessment-produced time;
- evaluation basis type: normative Expectation, descriptive Baseline, or explicitly both;
- supporting Observation references;
- exact applicable Expectation version(s) and/or comparable Baseline version(s);
- basis-appropriate result/status;
- evaluation rationale and comparison details at an authorized abstraction level;
- evidence/reference sufficiency, ambiguity, conflicts, and limitations;
- evaluation rule/logic identity/version at a functional provenance level;
- supersession/reassessment relationship when newer evidence or corrected reference context produces a later Assessment;
- visibility/security context necessary for safe disclosure.

## Actions

### `assess`
- **Intent:** interpret authorized Observation evidence against explicit reference context.
- **Observable result:** a dimension-scoped Assessment whose result identifies its normative/comparative basis and limitations.
- **Failure / unknown behavior:** missing or conflicting evidence/reference context yields unresolved/insufficient rather than a fabricated health status.

### `reassess`
- **Intent:** produce a new Assessment when late/corrected evidence, a legitimate reference correction, or new evaluation context requires reevaluation.
- **State effect:** preserves the earlier Assessment and links the new one as a reassessment rather than silently rewriting what was previously concluded.

### `explainBasis`
- **Intent:** return the authorized Observations, Expectations/Baselines, evaluation logic context, and limitations supporting an Assessment.

## Invariants / behavioral expectations

- Assessment interprets evidence; it does not mutate Observations, Expectations, or Baselines.
- Every Assessment makes its evaluation basis explicit.
- An Expectation-based Assessment may say whether a normative criterion was met, violated, unresolved, or not applicable.
- A Baseline-based Assessment may say whether behavior is typical/atypical, within/outside reference behavior, non-comparable, or unresolved.
- Being within Baseline is not, by itself, evidence of normative health.
- Being outside Baseline is not, by itself, evidence of degradation, defect, or unacceptability.
- A normative `healthy`/`meets expectation` conclusion requires applicable normative evidence; it is not inferred solely from historical typicality.
- Assessment does not establish root cause, attribution, or downstream Impact.
- Missing Observation evidence is not automatically an expectation violation. A failure based on non-occurrence requires an Observation with sufficient coverage establishing that absence.
- No applicable Expectation and no comparable Baseline yields unassessed/insufficient-reference context, not healthy.
- Conflicting Expectations, Baselines, or Observations remain visible in the Assessment basis unless an accepted resolution rule exists.
- Current Expectations/Baselines are not retroactively substituted for the versions used in historical Assessments.
- Reassessment is append-only in meaning: later conclusions do not erase what the product concluded with earlier evidence.
- Assessments are dimension-scoped by default. One successful dimension does not imply success in another.
- Any future multi-dimensional/overall-health Assessment must identify its component Assessments and explicit aggregation rule; no implicit majority/average roll-up is allowed.
- An aggregation rule must not hide a severe child Assessment merely to produce a convenient overall status.

## Ambiguity and missing evidence

Assessment can legitimately resolve as insufficient evidence, insufficient reference, conflicting, non-comparable, not applicable, unauthorized, or unavailable. These are not error cases to be coerced into green/red status.

A viewer may be authorized to receive a derived Assessment while some supporting measurements or thresholds are restricted. The Assessment must communicate enough authorized basis/limitations to remain trustworthy without leaking hidden evidence.

## Synchronizations

- **Entity Identity** supplies the assessed subject.
- **Observation** supplies evidence.
- **Expectation** supplies normative criteria.
- **Baseline** supplies descriptive reference behavior.
- **Semantic Definition** can provide units/grain/business meaning needed to interpret the dimension.
- **Monitoring Scope** can explain why evidence is expected or why coverage may stop, without determining Assessment status itself.
- **Investigation** may later be initiated/enriched by degraded, violated, atypical, or unresolved Assessments without treating the Assessment as cause.
- **Explanation** can later present Assessment results and their evidence basis to an authorized audience.

## Security / privacy / governance considerations

Derived status can itself disclose restricted facts. A user may be permitted to know that a criterion was violated while not being permitted to see the threshold, raw values, or sensitive Baseline. Assessment disclosure must therefore operate over an authorized evidence/reference view and avoid reverse-inference where practical.

## Evidence / provenance considerations

An Assessment must retain the exact Observation references, Expectation/Baseline versions, evaluated time/context, assessment time, evaluation rule/logic identity, and known limitations used to produce it. Reassessment provenance must make clear why a later conclusion differs.

## Representative scenarios

### Normative success
A freshness Observation satisfies the applicable freshness Expectation. The Assessment says the criterion is met; it does not infer quality in unrelated dimensions.

### Successful run, stale data
A Databricks run succeeds, but the output's material-update Observation violates the freshness Expectation. Operational execution and freshness Assessments remain separate.

### Baseline deviation without normative failure
Table C falls from a typical 19–21 million rows to 14 million. With no approved volume Expectation, the Assessment says `atypical versus Baseline`, not `failed quality requirement`.

### Typical but unacceptable
A field has historically exhibited a 12% null rate, while an explicit Expectation requires at most 2%. The value may be typical relative to Baseline and simultaneously violate the Expectation. Both basis results remain visible.

### Missing telemetry
A run was expected by 7:00 AM, but the run source cannot be queried. The Assessment returns insufficient evidence rather than asserting a missed run. If a complete query establishes zero runs, a normative violation can be assessed.

### Conflicting reference context
Two active expectations conflict. The Assessment remains unresolved rather than choosing the latest synchronized value.

### Reassessment after correction
A faulty row-count Observation initially produces an atypical Assessment. The source later corrects the count. A new Assessment supersedes the earlier one while preserving both conclusions and why they changed.

### Unauthorized basis
A business analyst sees `quality criterion violated` and a safe explanation, while restricted thresholds/reference values remain hidden.

## Non-goals

- defining or measuring Observations;
- establishing Expectations;
- deriving Baselines;
- root-cause reasoning;
- downstream Impact determination;
- incident workflow;
- defining a vendor-specific scoring/quality framework;
- inventing an implicit overall-health score.

## Deferred questions

- What canonical basis-specific status vocabulary best serves engineering and business audiences?
- Which assessment dimensions are required for the first MVP?
- Do composite Assessments need their own later concept, or is an explicit aggregation rule within Assessment sufficient?
- How should statistical uncertainty be represented without overloading generic "confidence" language?
