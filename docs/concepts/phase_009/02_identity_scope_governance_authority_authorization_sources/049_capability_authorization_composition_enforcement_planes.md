# INTG-049 — Capability Authorization Composition Across Enforcement Planes

**Status:** Accepted — Phase 009 Group 02

Effective Capability Authorization can require composition of upstream identity, Databricks privileges/ownership/ABAC/workspace restrictions, Immuta policy state and framework-specific capabilities for the exact action.

For Immuta-registered Unity Catalog data, Immuta may alter/revoke remote grants for registered users while unregistered users follow different semantics. The population and enforcement path are part of the authorization proposition; there is no universal `Immuta wins` or `Unity Catalog wins` rule.
