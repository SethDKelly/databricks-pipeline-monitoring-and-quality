# INTG-142 — Explicit Time-Travel / Version-Read Evidence

**Status:** Accepted — Phase 009 Group 05

Where retained statement text/parameters or workload metadata explicitly selects a table version/timestamp and table history resolves that selector, the consumer read can be conditionally bound to that historical state.

Truncated/encrypted/unavailable statement text, dynamic resolution or expired history leaves exact version use unresolved rather than inferred from query time.
