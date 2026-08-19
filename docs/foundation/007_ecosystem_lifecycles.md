# 007 — Ecosystem Lifecycles

## Purpose

Define the meaningful product lifecycles for this monitoring domain before designing technical workflows.

## 1. Source-to-deployment lifecycle

A conceptual path from a maintained pipeline definition to an executable Databricks state.

Typical stages:

1. pipeline/code/configuration exists in a Git repository;
2. a code revision is selected/merged according to that repository's process;
3. GitHub Actions executes a deployment workflow;
4. a Databricks job/task/configuration is created or updated;
5. the deployment becomes the active definition for subsequent execution;
6. later deployments supersede it while historical association remains discoverable.

Monitoring concern: connect code/deployment change to later run/data behavior without assuming the deployment caused every coincident anomaly.

## 2. Pipeline execution lifecycle

A logical pipeline moves through expected and observed execution states.

Conceptually:

1. execution is expected according to schedule/dependency/event semantics;
2. prerequisite conditions become available or not;
3. run begins;
4. tasks progress;
5. run succeeds, fails, is cancelled, times out, or otherwise terminates;
6. produced assets are observed;
7. freshness/quality effects are assessed separately from execution success;
8. run history remains available for comparison.

A successful terminal state does not imply healthy output.

## 3. Data availability and consumption lifecycle

A produced data asset becomes available for downstream use.

Conceptually:

1. a producing pipeline writes/materializes an asset;
2. the materialization becomes observable;
3. freshness and quality evidence is collected;
4. the asset is considered available for its intended consumers according to applicable expectations;
5. downstream pipelines, metrics, reports, or applications consume it;
6. later materializations supersede the current state without erasing history;
7. deprecation/retirement removes or changes intended consumption while preserving relevant lineage/history.

## 4. Expectation lifecycle

A quality/freshness/operational expectation is not timeless.

Conceptually:

1. expectation is proposed or discovered;
2. scope, owner, purpose, and definition are established;
3. expectation becomes active;
4. observations are evaluated against it;
5. expectation may be revised, waived, superseded, or retired;
6. historical assessments retain which expectation version applied.

This prevents a changed threshold from silently rewriting the interpretation of past runs.

## 5. Observation and assessment lifecycle

1. evidence is observed or retrieved;
2. provenance/time/scope are attached;
3. observation is normalized enough for comparison without losing source meaning;
4. applicable expectations/baselines are resolved;
5. an assessment is produced: healthy, degraded, stale, anomalous, unresolved, etc.;
6. later observations may confirm recovery or continued degradation;
7. historical evidence remains available for trend and RCA.

Observation and assessment are deliberately separate lifecycles.

## 6. Investigation / root-cause lifecycle

1. a symptom, question, or degraded assessment triggers investigation;
2. relevant time window is established;
3. upstream lineage/dependencies are traversed;
4. data, execution, schema, deployment, and governance changes are compared;
5. hypotheses are generated or recorded;
6. supporting and contradicting evidence is attached;
7. downstream impact is evaluated;
8. confidence/uncertainty is communicated;
9. a human or agreed evidence standard may confirm a cause;
10. resolution/recovery is recorded;
11. incident/report remains available historically.

A valid investigation may end `unresolved` or `multiple contributing causes`.

## 7. Governance metadata lifecycle

1. description/definition/owner/steward/classification is asserted by an authoritative source or authorized actor;
2. provenance and effective time are known;
3. monitoring uses the metadata in analysis/presentation;
4. updates or conflicting assertions are detected;
5. authority resolution determines the effective view without deleting provenance;
6. superseded states remain historically discoverable where required.

## 8. Lineage lifecycle

Lineage itself changes over time.

1. a relationship is observed/asserted;
2. relationship type and provenance are recorded;
3. relationship becomes valid for a time range or version;
4. pipeline/data/deployment changes may add, alter, or remove the relationship;
5. current lineage and historical lineage remain distinguishable;
6. RCA can query the topology applicable to the incident time.

## 9. Business communication lifecycle

1. an analyst or stakeholder asks a question or receives a scheduled report;
2. authorized evidence and context are assembled;
3. a layered explanation is produced;
4. uncertainty and affected scope are communicated;
5. ownership/next investigation action is identified where appropriate;
6. status changes are reflected in subsequent reports;
7. the explanation can be traced to evidence used at the time.

## Lifecycle principle

No lifecycle should erase the states needed to explain prior behavior. "Current state" and "current truth" are useful views, but the product thesis requires history.
