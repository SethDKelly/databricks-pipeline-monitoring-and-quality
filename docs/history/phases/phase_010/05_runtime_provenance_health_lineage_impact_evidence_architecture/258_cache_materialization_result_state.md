# ARCH-258 — Cache / Materialization / Result State

**Status:** Accepted

Cached, materialized, copied or served results have their own state/version provenance distinct from current upstream state.

A consumer may encounter safe stale, affected stale, fresh, or unknown prior state.