# Group 01 — Scope & Identity

**Status:** Active review group

## Goal

Establish how the ecosystem says **what participates in monitoring** and **how the same thing is recognized across systems and time**.

These concepts come first because later observations, expectations, ownership assertions, lineage relationships, and explanations must reference something without assuming that a repository path, Databricks identifier, or human-readable name is globally stable.

## Concepts

- [Monitored Scope](monitored_scope.md)
- [Asset Identity](asset_identity.md)

## Boundary questions

- Does `Monitored Scope` apply only to assets, or also to logical pipelines, jobs, relationships, consumers, and expectations?
- What makes two external references the same logical entity?
- When should identity remain unresolved rather than guessed?
- How are splits, merges, renames, replacements, and environment-specific instances represented conceptually?
- Can an entity be known to exist but intentionally out of monitoring scope?

## Group exit gate

Advance only when later concepts can safely reference monitored entities without relying on vendor IDs or assuming that inclusion grants access.
