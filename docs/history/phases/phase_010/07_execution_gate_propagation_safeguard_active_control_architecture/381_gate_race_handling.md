# ARCH-381 — Gate Race Handling

**Status:** Accepted

Concurrent opportunities, changing readiness and late decisions use opportunity IDs, decision revisions and compare-and-set/idempotent enforcement semantics to avoid stale action.

A later readiness change cannot rewrite the decision known/applied to an earlier opportunity.
