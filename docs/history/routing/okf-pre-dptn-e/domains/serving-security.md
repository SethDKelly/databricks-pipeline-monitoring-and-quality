---
type: "Domain Routing Reference"
title: "Serving, security, deployment, observability and cost"
description: "Route serving, disclosure, security, deployment, SLO, resilience and cost work to canonical owners."
resource: "../../docs/canonical/architecture/serving-security-deployment-operations.md"
tags: ["dmtz", "serving", "security", "operations", "cost"]
status: "stable"
---
# Routing

Start with the canonical [serving/security/deployment/operations architecture](../../docs/canonical/architecture/serving-security-deployment-operations.md). For disclosure governance use [AUTH disclosure governance](../../docs/canonical/authority/disclosure-governance.md); for authorization-aware projection use [EXPL audience/authorization/safe abstraction](../../docs/canonical/experience/audience-authorization-safe-abstraction.md); and for source/replay/disclosure feasibility use [INTG Explanation/replay/disclosure sources](../../docs/canonical/contracts/integration/explanation-replay-disclosure-sources.md).

Critical boundary: operational/platform health is not DMTZ domain health; serving applies current authorization/disclosure without rewriting historical truth. OKF is routing only.
