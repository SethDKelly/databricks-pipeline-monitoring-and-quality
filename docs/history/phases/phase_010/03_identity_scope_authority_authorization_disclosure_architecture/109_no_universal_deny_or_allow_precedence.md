# ARCH-109 — No Universal Deny or Allow Precedence

**Status:** Accepted

DMTZ introduces no universal deny-wins, allow-wins, direct-user-wins, role-wins, latest-wins or most-specific-wins authorization rule.

Conflict resolution belongs to the governing authorization policy for that capability/context.

Absent an explicit resolver, materially conflicting grants remain conflicting.