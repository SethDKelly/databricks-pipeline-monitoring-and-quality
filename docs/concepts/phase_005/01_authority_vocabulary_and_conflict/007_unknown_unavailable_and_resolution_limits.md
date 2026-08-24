# AUTH-007 — Unknown, Unavailable, and Resolution Limits

**Status:** Accepted — Phase 005 Group 01

## Purpose

Prevent missing or unavailable authority information from silently becoming a default precedence rule.

## Contract

Authority resolution may legitimately return:

- authoritative/advisory/non-authoritative standing;
- conditional standing whose condition is unresolved;
- authority unknown because no applicable accepted rule is known;
- authority unavailable because required rule/source evidence cannot currently be obtained;
- authoritative assertion conflict;
- authority-rule conflict;
- unauthorized-to-view-detail while a safe authority result may still be disclosed.

## Invariants

- `unknown authority` is not `any source may decide`.
- `authority source unavailable` is not `next available source wins` unless an explicit fallback rule applies and its activation condition is evidenced.
- Failure to retrieve an authority rule is not evidence that no rule exists.
- Restricted authority-rule detail is not absent authority.
- If the framework cannot determine whether a fallback condition is satisfied, conditional/fallback authority remains unresolved unless the accepted rule itself defines behavior for that uncertainty.
- Operational urgency does not create authority. Emergency/break-glass authority, if later supported, must be explicit and is refined in a later Phase 005 group.
- Group 01 does not invent a universal safe default for unresolved authority.
