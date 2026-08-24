# AUTH-049 — High-Consequence Communication Review, Approval, Release, Correction, and Retraction

**Status:** Accepted — Phase 005 Group 06

## Purpose
Govern when a truthful and viewable statement still requires additional communication review before being released to a high-consequence audience or channel.

## Contract
High-consequence communication policy may independently govern:
- compose/draft;
- review;
- approve for release;
- publish/disclose;
- correct/supersede;
- retract/withdraw a communication while preserving history.

Potential high-consequence statement classes include causal confirmation, client/business consequence, regulatory/compliance-adjacent statements, production-control/break-glass posture, external incident summaries, or other explicitly governed classes.

## Invariants
- Permission to see a fact does not imply permission to publish it.
- Review/approval to communicate does not make the statement true, authoritative, causally confirmed, compliant, healthy, or enforced.
- A communication reviewer cannot upgrade underlying Causal Claim/Assessment/Impact/control state for presentation convenience.
- Approved language remains bound to the evidence/knowledge cut and authorized projection reviewed.
- Material correction should create a superseding communication/history rather than silently rewrite a retained prior Explanation.
- Communication approval is independently auditable from the underlying authority/action that created the state being described.
- Group 06 does not select a workflow, ticketing, publishing, report, or approval engine.
