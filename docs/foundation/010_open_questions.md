# 010 — Open Questions

These questions are intentionally unresolved. Accepted Phase 002/003 boundaries constrain the answers but do not silently decide them. **Phase 004 — Evidence, Time, and Causality Refinement is next.**

## Evidence, historical time, and replay — Phase 004 priority

- What evidence sufficiency/completeness vocabulary is needed across positive, negative, absence, exposure, readiness, enforcement, and contradiction evidence?
- What source/query coverage is enough to assert `not observed`, `not exposed`, `did not run`, or `not known by knowledge cutoff` rather than merely `evidence unavailable`?
- What exact query semantics select event/effective time and recorded/knowledge cutoff across concepts with different validity models?
- Which historical states require retained snapshots versus reconstructible version history?
- How should replay-derived Assessment/Impact/Explanation be labeled and retained relative to actually recorded historical state?
- What materiality rules trigger dependent reassessment, Investigation reopen prompts, or updated Explanation after late/corrected evidence?
- How should corrected identity/Lineage/reference/authorization state affect retrospective analysis without rewriting contemporaneous conclusions?
- What retention/audit requirements apply to actual historical Explanation versus reconstructed historical Explanation?

## Causal Claim and confirmation — Phase 004 priority

- What operational evidence/authority standard permits `confirmed` cause?
- Which first-MVP epistemic statuses are required?
- Can automated systems ever confirm a cause or only propose/support/rank claims?
- How should multiple primary/contributing/enabling causes be displayed/reviewed?
- When does quantitative attribution become necessary, and what evidence standard would justify percentages?
- How should materially new evidence challenge a previously confirmed claim?
- What support/contradiction/alternative-explanation coverage is required before a claim status changes?

## Exposure, absence, and readiness evidence — Phase 004 priority

- What evidence establishes exposure for reports, Metric Views, pipelines, applications, and business processes?
- What evidence is sufficient to establish `not exposed` for each consumer class?
- What evidence proves a current qualifying upstream output for an Execution Gate: completion, output identity/version, freshness, or combinations?
- What proves an external gate hold/admission or safeguard activation actually enforced the intended boundary?
- How should late readiness/enforcement telemetry alter retrospective interpretation while preserving actual historical control action?

## Entity identity and scope realization

- Which entity kinds require first-MVP Entity Identity beyond pipelines, jobs/tasks, data assets, repositories, consumers, and deployment-related entities?
- How are logical pipeline identities established when one pipeline spans multiple jobs or one job hosts multiple logical pipelines?
- Which cross-source identity associations may be inferred versus requiring explicit/authoritative assertion?
- Which intermediate/external assets are independently included in Monitoring Scope for MVP?

## Authority and governance conflict

- What source/actor is authoritative for each metadata/normative category and context?
- Is Collibra authoritative for Semantic Definition/Responsibility Assignment in the target environment?
- Is Immuta authoritative for Classification/Policy Context?
- What Unity Catalog/Databricks metadata is authoritative versus enriching?
- How are conflicting assertions resolved without deleting provenance?
- Do repeated authority semantics justify a future standalone authority concept or remain integration contracts?

## Expectations, Baselines, and health

- Who may establish/revise each class of Expectation?
- Which first-MVP Expectation dimensions and bounded-exception states are required?
- Which Baseline classes are required: ranges, distributions, cadence/duration profiles, seasonal cohorts, or others?
- What evidence is sufficient to mark Baseline non-comparability after structural Change?
- What statistical/anomaly behavior is needed beyond transparent comparisons?
- What Assessment status vocabulary is appropriate for normative versus comparative results?
- What evidence coverage is sufficient to establish observed absence?
- Does composite/overall health eventually warrant a dedicated concept or only explicit aggregation synchronization?

## Change Intent, Deployment, execution, and gating

- Which source/actor may register authoritative Change Intent?
- What minimum anticipated-effect/monitoring-implication fields are required for MVP?
- How should Change Intent relate to pull requests, tickets, config changes, release metadata, or other planning systems?
- What evidence proves Deployment activation rather than attempt/workflow success?
- How are configuration-only changes related when source revision is unchanged?
- What minimum logical execution reconstruction is needed when pipelines span jobs/tasks?
- Which dependency/readiness criteria are safe for automatic gating?
- What gate classes need explicit fail-open/fail-closed/hold/escalate behavior?
- What maximum wait, timeout, escalation, expiry, and override semantics are required?

## Lineage and historical topology

- What minimal Lineage relationship taxonomy is required for MVP?
- What Lineage is already trustworthy/historical in Databricks for the relevant Spark patterns?
- Which relationships must repositories/integrations assert explicitly?
- How should inferred relationship confidence and topology completeness be communicated?
- Which graph-compatible technical realization is appropriate later, if any?

## Investigation

- What lifecycle/status vocabulary is required for MVP?
- Are related/nested Investigations needed or are explicit cross-references sufficient?
- Which Assessments/change mismatches automatically open Investigation versus merely surface a prompt?
- What closure/reopen/retention rules are appropriate?

## Downstream Impact

- What exact first-MVP vocabulary represents candidate/reachability, exposure, downstream effect, and business consequence?
- Which business processes/decisions need first-class Entity Identity?
- How should criticality prioritize Impact without being mistaken for consequence evidence?

## Annotation

- Which actors may annotate which referents?
- Are structured annotation types needed in MVP in addition to free text?
- What moderation/retention rules prevent unsafe or low-quality sensitive notes?
- Which annotations may appear in business-facing Explanation without explicit review?

## Explanation and question answering

- Is natural-language interaction required in MVP or is a structured question surface sufficient?
- Which question types must be deterministic versus generative?
- Which material statements require visible evidence citations/links by audience?
- Should generated Explanations be dynamically resolved, retained snapshots, or both?
- How should authorization differences across a path be explained without inference leakage?
- What rules govern high-consequence causal/business claims in generated explanations?
- How should UI distinguish contemporaneous, retrospective, comparison, actual-retained, and reconstructed historical Explanation?

## Security and privacy

- Which monitoring metadata, intent, topology, causal claims, Impact details, control state, or Annotations are sensitive by themselves?
- May users know a restricted entity/path exists if they cannot inspect it?
- Will any Investigation require row-level examples, and if so how are they minimized/redacted/authorized?
- What audit/retention requirements apply to evidence, investigations, claims, annotations, questions, control state, and retained explanations?

## Integration scope

- Which Databricks capabilities provide required job/run/Lineage/history evidence today?
- Which DQX capabilities align with accepted Expectation/Observation/Assessment concepts?
- Where do Metric Views add semantic/measurement value?
- What can GitHub Actions reliably prove about Deployment attempt and activation?
- Which systems can provide Change Intent?
- Are Collibra/Immuta necessary for MVP or later enrichment?
- Which sources provide sufficiently historical/authoritative evidence for event-time + knowledge-cut replay?
- Can optional Execution Gate semantics be realized without modifying production repositories/GitHub Actions, and where would exceptions be unavoidable?

## MVP pilot

- Which 2–5 representative pipelines exercise cross-repository dependencies, A+B→C, planned change, unintended side effect, downstream Impact, and optional gating?
- Which business analyst/report/Metric View provides a meaningful exposure/consequence case?
- Which assets carry useful governance/policy context without unsafe real data in development?
- Which pilot incident can validate both contemporaneous and retrospective replay after intentionally late/corrected synthetic evidence?
