# AUTH-002 — Authority Rule Provenance and Governing Basis

**Status:** Accepted — Phase 005 Group 01

## Purpose

Require every material authority rule to be provenance-bearing and explainable rather than allowing precedence to appear as an undocumented property of synchronization or implementation order.

## Contract

An authority rule should identify:

- the bound authority target;
- authority holder(s);
- standing/precedence/conditions granted;
- source/actor that established the rule;
- governing basis or parent governance reference where one exists;
- effective interval;
- recorded/knowledge time;
- revision/correction/supersession state;
- disclosure restrictions where relevant.

## Governing-basis rule

Authority rules cannot prove their own legitimacy merely by asserting it. Their accepted use must trace to an explicit governing basis or configured trust root appropriate to the environment. Phase 005 does not select how that trust root is technically implemented.

If two authority rules conflict and no accepted higher-order/governing rule resolves the conflict, the result is `authority conflict` rather than choosing whichever rule arrived last, is more specific, or is easier to query.

## Invariants

- synchronization/ingestion order is not authority-rule provenance;
- a rule source being highly available does not make the rule authoritative;
- a source cannot self-promote by emitting an assertion that it is authoritative unless an accepted governing basis already gives that assertion standing;
- governing-basis history is preserved for historical replay;
- current authority-rule validity is not projected backward into earlier knowledge cuts;
- restricted rule provenance may be safely abstracted for an authorized requester without making the rule provenance-free.
