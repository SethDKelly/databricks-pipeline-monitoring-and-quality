# 002 — Governance, Semantics, and Policy Transparency

## Goal

Make technical monitoring understandable and governable by attaching trustworthy context to the assets and relationships being monitored.

## Governance dimensions

The framework should discover and represent, where relevant:

- technical owner / maintaining team;
- business owner;
- data steward;
- escalation contact;
- source-of-truth designation;
- criticality or service tier;
- lifecycle state;
- business description;
- domain or subject area;
- authoritative terminology;
- expected update behavior;
- intended consumers;
- policy classifications and handling expectations.

Ownership is not a decorative metadata field. It is part of operational response and root-cause workflow.

## Semantic dimensions

A business analyst should not need to infer meaning from catalog.schema.table names.

Useful semantic context may include:

- plain-language description;
- business definition;
- grain of the dataset;
- important dimensions and measures;
- expected population or inclusion/exclusion rules;
- time semantics;
- source-system context;
- known caveats;
- relationships to business metrics;
- synonyms or alternate names.

## Policy transparency

The framework should be able to show sensitive-data context such as:

- PII classification;
- PHI classification;
- HIPAA-related handling context;
- confidentiality level;
- retention expectations;
- residency or location constraints where applicable;
- access-policy references;
- masking or de-identification expectations;
- sharing restrictions;
- other organization-defined classifications.

### Critical distinction

A classification label is not a compliance conclusion.

For example:

- “contains PHI” is a data classification statement;
- “subject to a HIPAA-related control expectation” is a policy statement;
- “access is enforced through a named control” is a control statement;
- “the control operated effectively during a period” is an evidence statement;
- “the organization is compliant” is a much broader conclusion that this monitoring framework should not infer merely from metadata.

The system should preserve these distinctions in both UI language and future reasoning behavior.

## Provenance of governance metadata

Governance facts may originate in more than one system. Discovery should identify authoritative sources and conflict rules rather than simply copying all metadata.

Potential sources include:

- Databricks / Unity Catalog metadata;
- repository-owned configuration or documentation;
- Collibra;
- Immuta;
- organizational directories or team ownership systems;
- manually curated framework metadata.

Collibra and Immuta are available tools, not assumed mandatory dependencies.

## Governance questions the system should support

- Who owns this dataset technically and from a business perspective?
- Who should investigate a failed or degraded quality expectation?
- What does this table represent?
- Which definition of a metric or field is authoritative?
- Does this asset contain or derive sensitive data?
- What handling expectations apply?
- Where did this classification or description come from?
- When did ownership or classification last change?
- Do upstream and downstream assets introduce different policy considerations?
