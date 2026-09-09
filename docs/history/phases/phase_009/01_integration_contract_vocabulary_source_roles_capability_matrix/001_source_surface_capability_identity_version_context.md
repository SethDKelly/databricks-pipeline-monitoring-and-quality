# INTG-001 — Source Surface Capability Identity & Version Context

A Phase 009 source contract binds an **exact source surface**, not merely a vendor/product name.

Minimum identity preserves system/provider, account/workspace/tenant context when semantically material, exact API/table/event/query/export/object class, feature/edition context when material, and the documented semantic/version context used for evaluation.

Different surfaces from one product may have different identity, time, coverage, authority, retention and disclosure semantics and therefore require separate capability rows.

A source-surface version change that materially changes identifiers, timestamps, population, retention or field meaning requires re-evaluation rather than silent inheritance.

This identity describes an integration capability, not a new product truth owner or implementation adapter.