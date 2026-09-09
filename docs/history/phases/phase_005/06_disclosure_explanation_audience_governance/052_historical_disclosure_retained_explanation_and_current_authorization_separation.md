# AUTH-052 — Historical Disclosure, Retained Explanation, and Current-Authorization Separation

**Status:** Accepted — Phase 005 Group 06

## Purpose
Preserve the distinction between what was disclosed historically, what can be reconstructed about historical truth, and what a requester is permitted to receive now.

## Contract
Historical disclosure reasoning distinguishes:
- underlying historical concept state at event/effective time;
- historical knowledge cut;
- historical Assertion Authority/Capability Authorization state;
- actual retained Explanation/communication, if one existed;
- present-day reconstructed `as-known-then` Explanation;
- present-day retrospective Explanation using later evidence;
- current requester/disclosure authorization and projection.

## Invariants

- Historical permission or historical disclosure does not grant current access.
- Current access does not imply the requester had access historically.
- A retained historical Explanation is evidence of what was actually communicated; a present reconstruction must be labeled reconstructed.
- Present authorization can require redaction of details that were historically visible to another audience; the product must not repeat them merely because they once appeared in an old Explanation.
- Later evidence/authority correction may change a retrospective Explanation without rewriting the retained historical communication.
- A retracted or superseded communication remains historically reconstructable when retention policy permits.
- Current disclosure restrictions must not be misrepresented as historical absence or lack of knowledge.
