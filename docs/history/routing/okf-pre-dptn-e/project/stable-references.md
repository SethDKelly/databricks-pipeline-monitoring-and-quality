---
type: "Stable Reference Routing"
title: "Canonical stable-ID resolution"
description: "Route exact stable IDs to deterministic canonical owners and optional historical occurrence discovery."
resource: "../../docs/agentic_development_foundation/stable_reference_policy.md"
tags: ["dmtz", "stable-id", "canonical", "routing"]
status: "stable"
---
# Use

For a known accepted ID, run:

`python3 scripts/agentic/resolve_stable_id.py <ID>`

The default result is the deterministic current locator `owner_path::STABLE-ID`, derived from the accepted range registry, CKR ownership inventory and unique canonical stable definition.

Use `--history` only when provenance/rationale/history is actually needed. Historical occurrences remain separate and never establish current ownership.

The resolver, registry and this OKF entry are routing aids only; canonical owner content remains the semantic authority.
