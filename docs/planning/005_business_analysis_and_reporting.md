# 005 — Business Analysis, Question Answering, and Reporting

## Goal

Make pipeline and data-quality state understandable to business analysts while preserving enough detail for engineering follow-through.

## Primary interaction model

A central product idea is the ability to **ask questions of the ecosystem**.

The question-answering experience should ultimately support prompts such as:

- Is Customer Orders healthy today?
- When was this dataset last refreshed?
- Is this table stale relative to its normal behavior?
- Has its quality gotten worse this month?
- What changed yesterday?
- Why did row count drop?
- Which upstream source most likely explains the drop?
- Was there a deployment near the time the change began?
- What downstream reports may be affected?
- Who owns the affected assets?
- Does this data contain PII or PHI?
- What business definition should I use for this metric?
- Show me the evidence behind the conclusion.

## Layered explanation

Different audiences should be able to consume the same incident at different levels.

### Business summary

A concise statement of:

- what changed;
- when it changed;
- business significance;
- likely source;
- affected downstream assets;
- current status;
- owner / next action.

### Analytical detail

Supporting trends, comparisons, lineage paths, quality observations, and relevant business semantics.

### Engineering detail

Run history, deployment lineage, job/task context, exact upstream/downstream relationships, and technical observations used in the analysis.

## Reporting expectations

The project should later explore recurring and ad hoc reports such as:

- daily/weekly pipeline health summary;
- stale-data report;
- quality degradation report;
- top recurring quality problems;
- unresolved degradation by owner;
- critical asset health report;
- upstream incident impact report;
- sensitive-data asset health report;
- change summary after deployments;
- business-domain quality scorecard with explainable contributing measures.

## Trust requirements

Business-facing answers should not hide uncertainty.

The system should be able to say, in effect:

- **Observed:** Table C volume decreased 28% beginning August 17.
- **Observed:** Table B volume decreased 27% one upstream run earlier.
- **Observed:** Table A remained within its normal range.
- **Likely explanation:** The C reduction is primarily attributable to B.
- **Unresolved:** A smaller change in join match rate remains unexplained.

The exact presentation may differ, but the distinction between evidence and interpretation should remain.

## Business semantics in analysis

Technical changes should be translated through known semantics where possible. “Column `cust_status_cd` null rate increased” may be less useful than “Customer status is missing for 18% of new records, which affects the Active Customer metric.”

This requires semantic metadata to participate in monitoring and reasoning rather than living in a separate catalog that users must consult manually.
