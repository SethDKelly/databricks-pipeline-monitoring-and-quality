# 010 — Open Questions

These questions are intentionally unresolved. Agents and contributors must not silently convert them into decisions.

## Ecosystem identity

- What is the stable identity of a logical pipeline across repositories and Databricks jobs?
- Can one logical pipeline span multiple jobs?
- Can one job implement multiple logical pipelines?
- How are environment-specific instances related to a logical pipeline identity?
- What represents a cross-repository dependency when no single repository declares it authoritatively?

## Data asset scope

- Which intermediate tables should be first-class monitored assets?
- Are views and Metric Views monitored in the same way as materialized tables?
- How should external sources that are not produced in Databricks participate?

## Expectations

- Who owns expected cadence/freshness?
- Who owns data-quality expectations?
- Are expectations source-controlled, governed centrally, defined in Databricks/DQX, or composed from several authorities?
- How are expectation versions made historically effective?
- How are temporary waivers represented without erasing a degradation?

## Baselines and degradation

- Which conditions use explicit thresholds versus historical baselines?
- What level of statistical/anomaly behavior is needed for MVP?
- How are expected seasonal/business changes distinguished from degradation?
- How should insufficient history be represented?

## Lineage

- What data lineage is already trustworthy in Databricks?
- How complete is job/task lineage for Spark ETL patterns in scope?
- Which lineage must be explicitly declared by repositories?
- How much historical lineage is available from source systems?

## Root-cause semantics

- What evidence standard allows a hypothesis to become a confirmed cause?
- Can the system confirm causes automatically, or only rank hypotheses?
- How should multiple contributing causes be represented?
- How should contradicting evidence affect confidence?
- How should business events be represented as possible expected causes of data changes?

## Governance authority

- Is Collibra authoritative for glossary/ownership/stewardship in the target environment?
- Is Immuta authoritative for classification/policy context?
- What governance metadata already exists in Unity Catalog?
- How are conflicts among systems resolved?
- Who may create local overrides, and how long may they live?

## Security and privacy

- Which monitoring metadata is sensitive by itself?
- Should users be allowed to see that a restricted asset exists if they cannot read it?
- Will any root-cause scenario require row-level examples?
- If samples are needed, how are they minimized/redacted/authorized?
- What audit/retention requirements apply to incident evidence and user questions?

## Question answering

- Is natural-language interaction required in the first MVP or is a structured question surface sufficient?
- Which question types must be deterministic versus explanatory?
- How will answers cite or link evidence?
- How should authorized-but-different audiences receive different detail without producing contradictory conclusions?

## Integration scope

- Which Databricks capabilities provide the needed job/run/lineage history today?
- Which DQX capabilities align with accepted quality concepts?
- Where do Metric Views add business-semantic/measurement value?
- What information can GitHub Actions reliably expose as deployment provenance?
- Are Collibra/Immuta necessary for MVP or later enrichment?

## MVP pilot

- Which 2–5 representative pipelines can exercise cross-repository dependencies and the canonical join scenario?
- Which business analyst/report provides a meaningful downstream consumer case?
- Which assets carry useful governance/policy classifications without requiring unsafe real data in development?
