# INTG-123 — `direct_access` & Intermediate Dependency Semantics

**Status:** Accepted — Phase 009 Group 05

Unity Catalog lineage `direct_access` distinguishes directly referenced sources from intermediate dependencies discovered through view expansion. It is a source traversal property, not a universal semantic-directness, causal-strength or exposure-strength ranking.

An intermediate dependency may still be materially relevant; a direct reference does not prove actual suspect-state exposure.
