---
type: "Documentation Authority Reference"
title: "Canonical knowledge and design history"
description: "Route to live CKR authority, canonical ownership and accepted stable-reference routing."
resource: "../../docs/canonical_knowledge_retrofit/README.md"
tags: ["dmtz", "canonical", "knowledge", "authority", "history"]
status: "stable"
---
# Use

Use the [CKR authority](../../docs/canonical_knowledge_retrofit/README.md) and [ownership inventory](../../docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json) to determine current semantic ownership.

All accepted semantic families through ARCH are canonicalized. For a known stable ID, use the accepted resolver: `python3 scripts/agentic/resolve_stable_id.py <ID>`. It returns the current locator `owner_path::ID`; `--history` adds separate provenance occurrences only.

Use [design history](../../docs/design_history/README.md) for provenance/rationale/history, not as an alternate current owner. This OKF entry and the stable-reference machinery are routing only and cannot change semantic authority.
