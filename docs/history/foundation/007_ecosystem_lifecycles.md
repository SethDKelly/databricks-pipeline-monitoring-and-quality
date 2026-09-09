# 007 — Ecosystem Lifecycles

## Purpose

Define meaningful product lifecycles before technical workflow/storage architecture.

## 1. Planned change and realization lifecycle

1. intended modification is registered as Change Intent;
2. anticipated affected entities/dimensions/monitoring implications are recorded;
3. any prospective Expectation revision is explicitly established by appropriate authority;
4. any prospective Baseline comparability break is registered but remains pending;
5. source/configuration implementation is created;
6. Deployment attempt occurs;
7. activation is established or remains unknown/fails;
8. executions occur under active state;
9. Observations establish actual behavior;
10. realized Change describes what actually differed;
11. Assessment evaluates applicable Expectations/Baselines;
12. realized structural Change may activate Baseline non-comparability and later post-change evidence derives a new Baseline;
13. Investigation may compare intent, realization, and outcome without treating chronology as cause.

A plan can fail to activate, activated behavior can differ from intent, and unintended violations can coexist with expected changes.

## 2. Source-to-deployment lifecycle

Repository revision/configuration → Deployment attempt → runtime activation evidence → supersession/rollback history. Workflow success and activation are distinct.

## 3. Pipeline execution lifecycle

Actual execution instance begins/progresses/terminates; produced/consumed context is associated where supported. Expected-but-never-started work is evaluated through Expectation plus sufficient absence evidence, not fictional run records.

## 4. Data availability and consumption lifecycle

Produced data becomes observable; freshness/quality Observations are collected; Assessments determine status against applicable criteria; downstream consumption relationships remain historically discoverable.

## 5. Expectation lifecycle

Expectation is established/revised/excepted/retired with effective time/provenance. Change Intent may trigger prospective review; plan detail never becomes normative automatically.

## 6. Baseline lifecycle

Comparable evidence derives a versioned Baseline. Change Intent can register a prospective comparability break. Realization evidence may make the old Baseline non-comparable; sufficient post-change Observations later derive the new Baseline. Prior Assessments retain prior versions.

## 7. Observation and Assessment lifecycle

Evidence is recorded with event/knowledge time/provenance; applicable references resolve; Assessment is produced with explicit basis; later evidence may create reassessment without rewriting prior conclusions.

## 8. Lineage lifecycle

Relationships are asserted/observed/inferred with type, provenance, confidence, effective time, and correction history. Planned topology remains Change Intent until realized. Current/historical topology remain distinct.

## 9. Investigation lifecycle

1. a question, Assessment, Change-Intent realization mismatch, Impact concern, or other uncertainty opens an Investigation;
2. subject/time/question scope is established;
3. relevant evidence links are added without copying source truth;
4. scope may be refined with history preserved;
5. Causal Claims, Impact evaluations, and Annotations are linked;
6. evidence gaps/conflicts/restrictions remain explicit;
7. Investigation may close resolved, unresolved, multi-causal, or otherwise complete;
8. materially new evidence may reopen it without erasing prior closure/knowledge state.

## 10. Causal Claim lifecycle

1. a causal proposition is proposed;
2. supporting and contradicting evidence accumulate;
3. epistemic status may move among proposed/supported/weakened/rejected/unresolved states;
4. multiple contributing claims may coexist;
5. confirmation occurs only if an explicit accepted evidence/authority standard is satisfied;
6. later evidence may challenge/supersede prior status while preserving historical review provenance.

## 11. Impact lifecycle

1. downstream Lineage identifies candidates;
2. exposure/consumption evidence determines whether each candidate actually encountered affected state;
3. downstream Observation/Assessment/Change evidence records any observed effect;
4. technical/analytical/business consequence evidence is associated where available;
5. causal attribution from origin to downstream effect remains a Causal Claim when needed;
6. Impact state is revised as delayed consumer evidence arrives, preserving prior knowledge state.

## 12. Annotation lifecycle

Human context is added with author/time/referent; material revisions are traceable; disputed/withdrawn notes remain historical. If human input becomes structured planned/normative/governance/causal truth, the appropriate owning concept records it separately.

## 13. Governance metadata lifecycle

Semantic Definition, Responsibility Assignment, Classification, and Policy Context assertions retain provenance/effective time/conflict rather than last-write-wins mutation.

## 14. Explanation lifecycle

1. an audience asks a question or a reporting event requests communication;
2. an authorized evidence/context view and temporal perspective are established;
3. material statements are composed with epistemic labels and source-basis links;
4. safe redaction/omission is applied without implying hidden state is absent;
5. a contemporaneous view can answer `what was known then` using a knowledge-time cut;
6. a retrospective view may incorporate evidence learned later;
7. materially changed evidence produces refreshed Explanation rather than invisible rewrite if snapshots are retained.

## Lifecycle principle — ledger semantics

No lifecycle erases states needed to explain prior behavior. Corrections/supersessions preserve prior knowledge. Where material, record both when something was true/occurred and when monitoring learned it.
