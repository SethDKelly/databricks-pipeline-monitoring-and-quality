# INTG-046 — Disclosure Filtering & Observer-Relative Metadata

**Status:** Accepted — Phase 009 Group 02

Some metadata sources intentionally filter results according to the querying principal. Unity Catalog Information Schema, Collibra view permissions and Immuta discovery/access controls can all create observer-relative visibility.

`not returned to requester` is therefore not equivalent to `does not exist`. Internal basis retrieval and visible Explanation projection remain independently authorized.
