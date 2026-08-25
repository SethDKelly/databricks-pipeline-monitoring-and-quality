# Phase 009 Group 07 — Explanation, Historical Replay, Basis Inspection & Disclosure Source Contracts

**Status:** Not started

## Goal

Determine whether source capabilities across Groups 02–06 can support the completed Phase 008 Explanation contract, including time-cut replay, statement-to-basis traceability, safe abstraction and retained communication distinctions.

## Primary questions

- Can each material statement retain enough stable source identity/provenance to support internal basis inspection later?
- Which sources preserve event/effective and recorded/knowledge timestamps sufficiently for `composeAt` and as-known-at-cut reconstruction?
- What source history is immutable, corrected/superseded, overwritten or unavailable?
- What evidence can be reconstructed retrospectively versus what must be retained independently to prove actual prior communication?
- Can current requester authorization be evaluated for historical data/basis without treating historical access as current permission?
- Which exact/coarse/redacted/opaque basis views can source permissions support safely?
- What source metadata itself is sensitive, including existence, counts, paths, provenance class and redaction markers?
- Where do missing retention or inaccessible historical authorization records make Phase 008 questions only partially answerable?
- How can source outages/late evidence be surfaced as unavailable/unknown instead of reassuring narrative completion?

## Boundary

This group maps source support for Explanation semantics. It does not choose retrieval architecture, snapshot persistence, LLM/template composition, caching, citation UI or report/chat delivery.

## Handoff

Group 08 consolidates all source contracts into a feasibility/gap/cost/retention matrix for the Phase 010 architecture handoff.
