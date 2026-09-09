# ARCH-451 — Control Authorization Freshness

**Status:** Accepted

SC-06 enforcement binds the authorization decision/revision and its applicability horizon; where revocation-sensitive policy or elapsed opportunity time requires it, authorization is revalidated immediately before the irreversible enforcement action.

A decision-time authorization cannot be presumed valid indefinitely after revocation, expiry or material policy revision.