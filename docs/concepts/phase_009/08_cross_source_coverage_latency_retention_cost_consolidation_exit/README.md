# Phase 009 Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Consolidation / Exit Review

**Status:** Next — not started

## Goal

Compose the Phase 009 source contracts into one explicit feasibility and gap model, then determine whether technical architecture can begin without reopening accepted functional semantics.

## Group 07 entry contract

Group 08 may consume Explanation/replay/basis/disclosure support **only where INTG-201–INTG-238 establish it**, with all source-specific retention, availability-time, mutability, authorization and communication-retention limitations attached.

Material Group 07 limitations must remain explicit during consolidation:

- retrospective source reconstruction is not proof of actual prior communication;
- exact as-known-at-cut replay requires basis availability by the knowledge cut, not merely old event timestamps;
- Databricks/GitHub/Immuta/Collibra histories have heterogeneous retention and mutation semantics;
- exact query/content basis can be blank, truncated, expired or restricted;
- notification/delivery evidence does not automatically retain exact rendered Explanation content;
- GitHub discussion history and selected Collibra history are mutable/configurable rather than immutable ledgers;
- current requester disclosure remains separate from historical actor authorization;
- exact prior `inspectBasis` presentation is generally unavailable unless independently retained;
- observer-relative source filtering cannot support absence by non-return;
- comparative Explanation can be asymmetric because source retention differs, without implying a truth difference.

Group 08 must identify which of these gaps require Phase 010 to retain additional product-owned provenance/history/communication artifacts and which product capabilities remain partial or unsupported with the evaluated source set.

## Primary questions

- Which accepted propositions are fully supportable, partially supportable, unsupported, unknown or dependent on optional integrations?
- Where do multiple sources overlap, conflict or share common derivation?
- Are cross-system identity/join keys reliable enough for deployment/run/version/consumer/control reasoning?
- What clock/time-cut limitations prevent exact ordering or historical reconstruction?
- What are the effective coverage boundaries for strong negatives across runs, paths, consumers and controls?
- What latency/freshness envelopes constrain current monitoring versus slower investigative/retrospective answers?
- Which source histories have sufficient retention for intended replay, and where must architecture retain additional product-owned evidence/communication?
- Which sources can support as-known-at-cut replay with reliable availability timing rather than event time alone?
- Which historical questions require authentic retained communication rather than reconstruction?
- What basis/provenance must remain resolvable after vendor-native history expires?
- What current authorization/disclosure constraints apply to historical basis inspection and comparative answers?
- What quotas, rate limits, query/computation costs or licensing dependencies materially shape architecture choices?
- How is integration health itself observed so source outage is distinguishable from source-level negative facts?
- What graceful-degradation/partial-answer behavior follows directly from the accepted source gaps?
- Does the evaluated source set support the MVP boundary, or are product-scope/integration choices required before Phase 010?

## Exit target

Phase 009 should exit with a concrete integration capability matrix and residual-gap register. Phase 010 receives facts about source capability, authority applicability, identity joins, time, coverage, latency, retention, communication retention, basis inspectability, disclosure, cost and observability; it—not Phase 009—selects ingestion/persistence/service/deployment architecture.

## Boundary

Do not hide unsupported requirements through architectural optimism or rewrite the accepted product semantics to make the matrix look complete. Retrospective reconstructability must not be used to claim historical communication retention, and planned product-owned retention must not be counted as a current source capability.
