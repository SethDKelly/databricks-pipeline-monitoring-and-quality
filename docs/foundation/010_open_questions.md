# 010 — Open Questions

These questions are intentionally unresolved. Accepted Phase 002/003 boundaries constrain the answers but do not silently decide them. **Phase 004 — Evidence, Time, and Causality Refinement is active; Groups 01–03 are accepted and Group 04 is next.**

## Evidence, historical time, and replay — Phase 004

Accepted through Groups 01–02:

- evidence sufficiency is conclusion-relative rather than a universal score;
- evidence applicability, bounded coverage, corroboration/conflict, and conclusion sufficiency remain distinct;
- negative/absence/exclusion evidence requires adequate opportunity-to-observe and coverage;
- event/effective time, source availability, framework knowledge time, and evaluation time remain distinct;
- `as-known` cuts use evidence known to the framework by the cutoff;
- source availability does not backdate framework knowledge;
- `known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are distinct claims;
- late evidence, source correction, independent conflict, reinterpretation, and later authority resolution remain distinct;
- dependent reevaluation is basis/materiality driven;
- actual historical state requires evidence that it existed then; otherwise replay is reconstructed.

Remaining temporal/replay questions include:

- Which historical states require retained snapshots/events versus reconstructible version history in MVP?
- What exact source/integration evidence is needed to establish source-availability time when it differs from framework knowledge time?
- What retention/coverage is needed before `not recorded by` or `not known by` is safely available for each evidence class?
- What notification/escalation behavior should occur when retrospective conclusions materially change?
- What retention/audit requirements apply to actual historical Explanation versus reconstructed historical Explanation?
- Which high-consequence historical states must be retained rather than merely reconstructible?

## Monitoring result availability and execution timing

Phase 004 Group 02 accepts progressive analytical availability as a functional requirement. Exact targets remain open:

- Which validations should be available on an **immediate operational** path—for example job start/completion/success/failure, queue/duration, direct output existence, or dependency state?
- Which health results can reasonably be **near-real-time/enriched** versus delayed because they depend on Metric Views, DQX, Baseline comparison, semantic context, or source refresh?
- What evidence is required before **RCA** should begin automatically, and which RCA outputs should be available incrementally versus after a fuller evidence window?
- What belongs specifically in **post-operations review** because it depends on late/corrected consumption, consequence, or historical evidence?
- What maximum evidence age/result age is acceptable for each health dimension and consumer audience?
- How should the UI/API communicate `available now`, `pending evidence`, `enriched`, `RCA in progress`, and `retrospectively updated` without implying service/workflow architecture?
- Which source availability/collection latencies are inherent to Databricks job metadata, Metric Views, DQX, GitHub/deployment evidence, Lineage, consumption evidence, and governance systems?
- Which analyses can be precomputed/cached versus reconstructed on demand without violating historical truth?
- What latency budgets preserve useful near-real-time monitoring without putting passive monitoring on the ungated production critical path?
- Which explicitly gated decisions require synchronous evidence/control behavior even if ordinary health analysis is asynchronous?

These questions are handed primarily to Phases 006, 009, 010, and 011.

## Causal Claim and confirmation — accepted Phase 004 Group 03; remaining authority/profile questions

Accepted in Group 03:

- causal propositions bind cause, effect, role, context/time, and material mechanism/transmission assumptions;
- status vocabulary is `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- `unresolved` is evaluated-but-non-discriminating, not merely proposed;
- `rejected` requires sufficient contradiction/exclusion evidence rather than lack of support;
- causal evidence is evaluated across applicable dimensions without a universal confidence score;
- stronger causal status considers a bounded material alternative set rather than every imaginable cause;
- `confirmed` is a separate claim-class confirmation gate, not `strongly supported`/leading hypothesis;
- confirmation requires explicit profile/standard provenance, required causal evidence, contradiction/alternative review, adequate exclusion coverage where relied upon, resolved confirmation capability/authority, and a provenance-bearing confirmation action;
- Phase 004 does not grant confirmation authority to a human title or automated process;
- multiple compatible contributors may coexist; one root cause is not required;
- qualitative causal roles do not imply percentage attribution; `primary` requires comparative evidence;
- RCA may mature progressively without latency-driven status inflation;
- confirmed claims remain challengeable while historical confirmation remains reconstructable.

Remaining causal questions include:

- Which **claim classes** need distinct confirmation profiles for MVP—for example deterministic control-mechanism causation, version/consumption-mediated propagation, pipeline data transformation, Deployment causation, or business consequence causation?
- Which evidence dimensions are mandatory versus optional for each confirmation profile?
- Which principals/processes may hold **causal-confirmation capability** for each subject/context, and how is that authority resolved? (Phase 005)
- Under what narrowly defined conditions may an automated process be authorized to confirm a causal claim, if any? (Phase 005/010)
- What source/actor authority conflicts matter when confirmation depends on contradictory evidence? (Phase 005/009)
- Which causal statuses or confirmation actions require explicit human review for the MVP even if automation could technically satisfy evidence conditions?
- When does quantitative attribution become necessary, and what evidence/model standard would justify percentages?
- How should causal chains among several claims be represented/displayed if simple claim references become insufficient?
- What notification/escalation behavior should follow a materially challenged or reversed previously confirmed claim?
- What exact availability/latency objectives should apply to proposed/support-level RCA versus deeper confirmation review?

## Exposure, absence, readiness, and control evidence — Phase 004 Group 04 priority

- What evidence establishes exposure for reports, Metric Views, pipelines, applications, and business processes?
- What evidence is sufficient to establish `not exposed` for each consumer class?
- How should `no refresh`, `refresh of a safe prior version`, `refresh of the affected version`, `unknown refresh`, and restricted/inaccessible consumer state remain distinct?
- What evidence proves a current qualifying upstream output for an Execution Gate: completion, output identity/version, freshness, or combinations?
- What proves an external gate decision/request was actually enforced as a hold or admission?
- What proves a safeguard activation was actually enforced at the intended output/consumption boundary?
- What evidence is sufficient for `prevented exposure` rather than merely `safeguard active`?
- How should unavailable/degraded control telemetry affect gate/safeguard truth without inventing fail-open/fail-closed behavior?
- When can direct gate/safeguard enforcement evidence support a causal claim that the control contributed to delay/non-delivery?
- How should late readiness/enforcement/consumption telemetry alter retrospective interpretation while preserving actual historical control action?

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
- Which actor/system is authoritative for causal-confirmation permission and confirmation-profile assignment by claim/context?
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
- Which health Assessments are expected to be available immediately, near-real-time, delayed, or post-ops?

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
- What operational workflow should follow a causal claim becoming confirmed, challenged, or rejected without making Investigation own causal truth?

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
- How should UI distinguish `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, and `confirmed` without implying numeric confidence?
- How should UI distinguish contemporaneous, retrospective, comparison, actual-retained, and reconstructed historical Explanation?
- How should progressive result maturity and evidence-pending state be communicated across audiences?

## Security and privacy

- Which monitoring metadata, intent, topology, causal claims, Impact details, control state, or Annotations are sensitive by themselves?
- May users know a restricted entity/path exists if they cannot inspect it?
- Will any Investigation require row-level examples, and if so how are they minimized/redacted/authorized?
- What audit/retention requirements apply to evidence, investigations, claim status/confirmation actions, annotations, questions, control state, and retained explanations?

## Integration scope

- Which Databricks capabilities provide required job/run/Lineage/history evidence today?
- Which DQX capabilities align with accepted Expectation/Observation/Assessment concepts?
- Where do Metric Views add semantic/measurement value?
- What can GitHub Actions reliably prove about Deployment attempt and activation?
- Which systems can provide Change Intent?
- Are Collibra/Immuta necessary for MVP or later enrichment?
- Which sources provide sufficiently historical/authoritative evidence for event-time + knowledge-cut replay?
- What are the production-to-queryable and queryable-to-framework latency characteristics of each evidence source?
- Which evidence sources can support each causal confirmation profile without requiring raw-data access or production code changes?
- Can optional Execution Gate semantics be realized without modifying production repositories/GitHub Actions, and where would exceptions be unavoidable?

## MVP pilot

- Which 2–5 representative pipelines exercise cross-repository dependencies, A+B→C, planned change, unintended side effect, downstream Impact, and optional gating?
- Which business analyst/report/Metric View provides a meaningful exposure/consequence case?
- Which assets carry useful governance/policy context without unsafe real data in development?
- Which pilot incident can validate both contemporaneous and retrospective replay after intentionally late/corrected synthetic evidence?
- Which pilot should validate progressive result availability from job validation through health metrics, RCA, and post-ops review?
- Which pilot should validate multiple simultaneous causal contributors and a later challenge/reversal of a previously stronger causal conclusion?
