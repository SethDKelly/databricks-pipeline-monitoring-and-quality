# ARCH-073 — Payload Expiry with Provenance Stub

**Status:** Accepted

Ordinary TTL MAY expire payload bytes/detail while retaining a minimal provenance stub containing evidence identity, source identity/locator, time coordinates, digest where safe, retention action/reason and dependency state for its configured horizon.

The stub proves retained metadata about prior evidence, not the expired payload contents.
