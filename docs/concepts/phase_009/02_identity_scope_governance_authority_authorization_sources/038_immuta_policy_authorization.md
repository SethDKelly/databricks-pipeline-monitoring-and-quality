# INTG-038 — Immuta Subscription & Data-Policy Authorization

**Status:** Accepted — Phase 009 Group 02

Immuta subscription policies govern table-level access for registered Immuta data sources/users and data policies can govern finer-grained access. Groups/attributes/tags are inputs to these decisions.

Immuta policy state is authoritative for Immuta-managed authorization propositions, not for every remote-platform user or unrelated framework capability. Integration-specific enforcement semantics must be preserved.
