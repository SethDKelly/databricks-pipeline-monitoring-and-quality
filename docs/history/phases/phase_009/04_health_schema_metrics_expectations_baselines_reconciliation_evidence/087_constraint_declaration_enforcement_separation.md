# INTG-087 — Constraint Declaration & Enforcement Separation

**Status:** Accepted — Phase 009 Group 04

Unity Catalog/Delta constraint metadata can evidence declared NOT NULL, CHECK, primary-key, foreign-key and unique constraints within documented feature scope.

Declared PK/FK constraints are informational and must not be treated as observed key integrity. Enforced constraints establish write-time enforcement behavior only for their exact semantics; declaration still differs from realized Observation and governed framework Expectation.
