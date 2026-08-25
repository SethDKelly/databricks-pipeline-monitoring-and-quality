# Phase 009 Group 07 — Explanation, Historical Replay, Basis Inspection & Disclosure Source Contracts

**Status:** Review complete — accepted

## Result

Group 07 accepts **INTG-201–INTG-238** and **EBR07-01–EBR07-64**. No new product concept is required.

The group maps the accumulated Phase 009 source contracts onto the completed Phase 008 Explanation model and determines what can be reconstructed, retained, inspected and safely disclosed without turning source convenience into an Explanation truth model.

The central source chain is:

**source-owned proposition/evidence + stable provenance → event/effective state + source availability/knowledge coordinates → as-known-at-cut basis eligibility → statement-relative basis assembly → internal inspectability → current requester-specific authorized projection → retained actual communication where independently evidenced → later retrospective re-evaluation without historical rewrite**.

No stage automatically creates the next.

## Accepted contracts

1. **INTG-201** — Explanation Statement ↔ Source-Basis Identity
2. **INTG-202** — Stable Source Reference & Provenance
3. **INTG-203** — Basis Role, Status & Limitation Retention
4. **INTG-204** — Explanation Temporal Coordinates: T / K / Availability
5. **INTG-205** — As-Known-at-Cut Source Inclusion Rule
6. **INTG-206** — Late Evidence & Backfill Non-Rewriting
7. **INTG-207** — Source Correction & Supersession History
8. **INTG-208** — Current Retrospective Re-Evaluation
9. **INTG-209** — Historical Source-State Replay Support
10. **INTG-210** — History Loss, Deletion & Truncation
11. **INTG-211** — Retained Communication ≠ Reconstruction
12. **INTG-212** — Communication Identity, Audience, Context & Time
13. **INTG-213** — Delivery Evidence vs Exact Communication Content
14. **INTG-214** — Mutable Communication & Edit History
15. **INTG-215** — Missing Retained Communication
16. **INTG-216** — Statement Identity Across Refresh
17. **INTG-217** — Basis Enrichment & Explanation Delta
18. **INTG-218** — Partial Answerability Under Source Gaps
19. **INTG-219** — Source Outage / Degraded Explanation Limitation
20. **INTG-220** — Internal Basis Inspectability
21. **INTG-221** — Source Retrievability vs Visible Reference
22. **INTG-222** — Current Requester Authorization for Historical Basis
23. **INTG-223** — Historical Actor Authorization vs Current Disclosure
24. **INTG-224** — Result / Context / Limitation / Basis / Detail Authorization
25. **INTG-225** — Safe Coarse / Redacted / Opaque Basis Projection
26. **INTG-226** — Sensitive Existence / Count / Type / Provenance Metadata
27. **INTG-227** — Sensitive Query Text, Parameters & Error Detail
28. **INTG-228** — Sensitive Actor / Consumer Identity
29. **INTG-229** — Observer-Relative Source Filtering
30. **INTG-230** — Databricks System-History Retention
31. **INTG-231** — Databricks Query-Content Inspectability
32. **INTG-232** — Databricks Alert Delivery Evidence
33. **INTG-233** — GitHub Audit History & Replay
34. **INTG-234** — GitHub Comment / Discussion Edit History
35. **INTG-235** — Collibra Resource History & Visibility
36. **INTG-236** — Immuta Audit Retention, Export & Inspection
37. **INTG-237** — Comparative Explanation Source Equivalence
38. **INTG-238** — Group 07 Source Matrix & Group 08 Handoff

## Four Explanation views require different source evidence

Group 07 operationalizes the Phase 008 four-view model without creating a fifth source of truth:

1. **Historical source state** requires time-valid source history sufficient for the exact proposition.
2. **As-known-at-cut Explanation** additionally requires evidence that each basis item was available by knowledge cutoff `K`; an old event timestamp returned later is insufficient.
3. **Actual retained communication** requires an authentic retained communication/snapshot or equivalent evidence of the exact content/context actually communicated.
4. **Current retrospective Explanation** may use later accepted evidence/corrections but remains explicitly separate from what was known or communicated then.

Current authorized projection is evaluated independently for whichever view is requested.

## Stable statement-to-basis traceability

A material Explanation statement retains internal links to exact source-owned propositions, source-surface identity, source-local object/event/result identity, subject reconciliation, evidence role and limitations.

Names, URLs, current labels and rendered citations can aid navigation but do not substitute for basis identity where objects can be renamed, recreated or mutated.

Supporting, contradicting and limiting basis roles remain **statement-relative**. Source count or basis count never becomes confidence. Common-derived records retain common derivation and do not become independent corroboration through Explanation composition.

## Historical replay and knowledge cuts

Group 07 preserves at least four time coordinates when material:

- event/effective time `T`;
- source-recorded / first-reliably-available time;
- requested knowledge cutoff `K`;
- communication time for actual retained communication.

Retrieval time can prove current availability; it cannot by itself prove earlier availability.

Late-arriving telemetry, delayed system-table publication, corrected metadata, backfilled audit exports or newly integrated sources may change a **current retrospective** answer while leaving the earlier as-known answer historically valid.

Expired retention, disabled history, deleted revisions, truncation, encryption-driven blank fields or overwritten source state remain explicit replay limitations. Group 07 does not reconstruct missing detail from current state or timestamp proximity.

## Retained communication versus reconstruction

A major Group 07 conclusion is that **source replay and communication retention are separate capabilities**.

A perfectly reconstructible incident-time source state can establish what the framework can now infer was explainable at that cut. It cannot prove the exact wording, detail, limitations, audience or basis visibility that was actually delivered unless that communication was retained.

Likewise, delivery metadata can establish that an alert, snapshot, webhook or other communication was delivered without proving the exact content received. The valid intermediate result is therefore:

**delivery evidenced; exact retained communication unavailable/unresolved**.

Missing retained communication remains missing. A reconstruction may be offered under a reconstruction label; it never becomes an authentic prior snapshot.

## Databricks source support

Databricks provides substantial but heterogeneous source history. Current system-table documentation gives many material audit/query/lineage/job/alert surfaces a roughly 365-day free retention period, while other system tables have different horizons or indefinite retention. `system` therefore does not imply one historical-replay contract.

`system.query.history` provides strong statement identity/execution context for covered SQL warehouse/serverless queries and can expose statement text and parameters. Exact basis inspection is still conditional: the table is Public Preview, access is privileged by default, long text/parameters can be truncated, and statement/error content can be blank under customer-managed-key configurations.

The new `system.alert` surfaces are useful for Explanation history: alert configuration is SCD2 and alert evaluation history records evaluated state plus notification-delivery status. That can support **definition-at-time**, **evaluation**, and bounded **delivery** propositions. It does not prove exact rendered notification content, human reading or business reliance.

System-table lag/region/permission boundaries remain material to as-known replay. A record appearing later in the day is not backfilled into an earlier knowledge cut merely because its event time is earlier.

## GitHub source support

GitHub can contribute several different forms of Explanation evidence:

- commits/PRs/reviews/issues/comments can retain change/review/communication context;
- comment edit history can preserve earlier content revisions;
- enterprise audit history can preserve governed actions;
- audit export/streaming can extend retention externally.

These are not one immutable ledger. Current GitHub Enterprise Cloud documentation describes about 180 days for ordinary enterprise audit events and seven days for Git events unless externally retained. Audit streaming uses at-least-once delivery, so exported duplicates retain common derivation rather than becoming independent corroboration.

GitHub comment history is also mutable governance data: a maximum of 100 edits is retained per content item, and authorized users can delete sensitive revision content from edit history. A current issue/comment body therefore cannot automatically prove the historical body at an arbitrary cut.

## Collibra source support

Collibra resource history can be strong governance/semantic replay evidence where enabled. It records many resource/characteristic/status/comment/workflow/responsibility/view-permission changes with actor/time context.

Limitations are material: some edits can appear as delete + create, inherited-responsibility changes are not fully represented in resource history, and current releases allow history logging to be disabled for selected attribute assignments. View permission also controls whether a resource is visible at all.

Therefore **Collibra history present for one facet ≠ complete history for every governed facet**, and a current user's inability to view a resource cannot support historical absence.

## Immuta source support

Immuta audit can provide rich basis for access/policy Explanation, including query/policy/entitlement context for supported integrations. Query text and security/policy context can be sensitive and disclosure-governed.

Current SaaS documentation retains audit for about 90 days by default and recommends/permits export for long-term retention. Integration/version/scope materially change coverage: for example, Databricks Spark audit requires registered users/data sources, while current Unity Catalog audit has different population/query filtering semantics.

Long-horizon `inspectBasis` therefore requires verified exported-history coverage/integrity or another retained source; native UI availability is insufficient by itself.

## Basis inspection and disclosure

`inspectBasis` is two independent questions:

1. **Can the system internally resolve the exact basis?**
2. **May this requester/audience/purpose/delivery context see it, and at what detail?**

A visible citation/reference does not grant source access. Current authorization governs current disclosure of historical basis; historical actor access does not grant current access, and current revocation does not erase authentic retained communication history.

Conclusion, context, material limitation, basis existence, provenance class and exact basis detail can have separate visibility decisions. Query text, parameters, errors, actor identities, consumer identities, source names, timestamps, counts and even the fact that restricted basis exists can themselves be sensitive.

Safe coarse/redacted/opaque projection remains epistemically monotone: it may say less but cannot strengthen, reverse or broaden the internal proposition.

## Partial answers and source degradation

Group 07 confirms that partial Explanation is necessary for enterprise operation. A source outage, expired history, unavailable query text, missing retained snapshot or current authorization restriction can make one statement or subquestion unanswerable while siblings remain valid.

Source outage/lag/permission failure remains a **basis availability limitation**, never a product-level negative fact. Explanation cannot smooth over missing causal/control stages, unavailable history or hidden evidence to produce a reassuring complete narrative.

## Comparative Explanation

Each comparison side independently binds subject/proposition, event/effective window, knowledge cut, source set, source retention/coverage and current disclosure authorization before a delta is computed.

A difference caused by one side having richer retained history is recorded as a **basis/availability difference**, not silently represented as a source-truth change. More visible detail on one side likewise does not mean stronger truth.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — EBR07-01–EBR07-64 pass.
- [`../../../decisions/phase_009_group_07_explanation_replay_basis_disclosure_sources.md`](../../../decisions/phase_009_group_07_explanation_replay_basis_disclosure_sources.md) — D-1173–D-1218.

## Architecture boundary

Group 07 does not choose snapshot persistence, event sourcing, archival storage, source materialization, retrieval/indexing, citation UI, redaction engine, LLM/template composition, cache invalidation, communication channels or authorization implementation. Those are Phase 010 choices informed by Group 07's required retained evidence.

## Handoff

**Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Consolidation / Exit Review is next.**

Group 08 must consolidate source feasibility while preserving the distinction among source history, as-known replay, retained communication and current retrospective Explanation. In particular, it must identify where Phase 010 needs product-owned long-horizon retention, communication snapshots, provenance/identity records or authorization-history support rather than pretending vendor-native retention is sufficient.
