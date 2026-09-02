# ADF-E — Execution Review

**Status:** ACCEPTED — ADF-E COMPLETE

## Review question

Has ADF-E made DMTZ agent/developer context discovery, exact stable-reference resolution, context-size control, and OKF routing maintenance deterministic enough to support later integrated conformance without creating another semantic authority?

**Conclusion: yes.**

ADF-E establishes repository policy, registries, workflow integration, deterministic helper seams, and bounded helper-level execution evidence. It does not claim that the whole repository conformance suite is yet enforced in CI; ADF-F owns that integration and the single agentic drift/conformance report.

## Delivered artifacts

- `context_discovery_policy.md` — shortest-path progressive disclosure and retrieval-failure behavior;
- `stable_reference_policy.md` — exact stable-ID resolution policy;
- `stable_id_registry.json` — machine-readable accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH ranges;
- `context_budget_policy.md` and `context_budget.json` — deterministic UTF-8 byte budgets;
- `knowledge_maintenance_workflow.md` — changed-source routing review process;
- refined `okf_maintenance_policy.md`;
- `fixtures/adf_e_context_scenarios.yaml` — reusable ADF-E conformance scenarios;
- `scripts/agentic/resolve_stable_id.py` — exact occurrence/range resolver;
- `scripts/agentic/measure_context_budget.py` — deterministic context budget measurement;
- `scripts/agentic/knowledge_impact.py` — canonical-change → OKF routing review-candidate mapping;
- updated `resolve-context` and `resolve-contract` canonical workflows.

## Findings

### 1. Shortest-path discovery — PASS

ADF-E formalizes progressive disclosure without requiring ceremonial traversal of every routing layer.

The preferred path is:

`human-selected task → live authority → explicit path/ID when known; otherwise one OKF route → canonical resource → exact stable IDs/tests as needed`.

A directly supplied path or stable ID may bypass unnecessary OKF routing. Another file should be loaded only when it answers a concrete unresolved question.

### 2. Repository semantics before web/memory — PASS

A DMTZ semantic question is resolved from repository authority first. Public web is reserved for current external/vendor reality that canonical DMTZ sources intentionally do not own.

Tool memory, chat history, prior summaries, and OKF descriptions remain advisory. Missing contract text is not reconstructed from memory.

### 3. Stable accepted ranges — PASS

`stable_id_registry.json` records the frozen accepted ranges:

- SYN-001–035;
- REF-001–030;
- AUTH-001–053;
- HLTH-001–066;
- OPS-001–123;
- EXPL-001–160;
- INTG-001–270;
- ARCH-001–500.

A range-invalid token is reported as invalid/unaccepted rather than treated as a convenient future contract.

### 4. Exact lookup without first-match canonicality — PASS

`resolve_stable_id.py` searches exact tokens under canonical `docs/` and reports every occurrence with file/line information.

It mechanically distinguishes `definition_candidate` lines from ordinary references, but explicitly states that this classification does not establish canonical ownership. Live repository authority and the accepted owning document remain controlling because the same ID may appear in indexes, matrices, examples, handoffs, or historical artifacts.

### 5. Stable-reference failure semantics — PASS

ADF-E explicitly preserves:

- no occurrence → unresolved retrieval, not remembered reconstruction;
- multiple occurrences → candidate set requiring authority resolution;
- historical/deprecated occurrence → not automatically current;
- conflicting accepted sources → change-control issue;
- inability to retrieve → not evidence that no constraint exists.

### 6. Context budgets — PASS at policy/helper layer

ADF-E adopts deterministic UTF-8 byte budgets rather than provider-specific token guesses.

Hard limits include:

- root `AGENTS.md` ≤ 16 KiB;
- `.claude/CLAUDE.md` ≤ 2 KiB;
- one Cursor rule ≤ 6 KiB and all Cursor rules ≤ 32 KiB;
- Cursor root baseline ≤ 20 KiB;
- Claude root baseline ≤ 18 KiB;
- Codex root baseline ≤ 16 KiB;
- one skill ≤ 7 KiB;
- one Claude workflow bridge ≤ 1 KiB;
- bounded OKF index/concept sizes.

At ADF-E execution, GitHub reported root `AGENTS.md` at 12,699 bytes and `.claude/CLAUDE.md` at 1,054 bytes, both within policy limits.

`measure_context_budget.py` implements repository measurement. ADF-F must execute it against the real checkout in CI before ADF-EX-15 is closed.

### 7. Context-budget semantics — PASS

Budget failure is treated as an agentic configuration/context problem, not permission to delete requirements. Detailed procedures and semantics should move to on-demand skills/OKF/canonical docs rather than be truncated.

Large aggregate repository documentation is acceptable when startup/retrieval context remains bounded.

### 8. Knowledge-change impact semantics — PASS

A canonical resource change creates a **routing review candidate**, not an automatic declaration that every referencing OKF entry is stale.

`knowledge_impact.py` builds the direct reverse resource map and identifies concepts to review for changed canonical paths. This avoids brittle universal hash-pinning while still making routing-impact review deterministic.

### 9. Knowledge maintenance directionality — PASS

Canonical sources may require OKF routing corrections. OKF never generates semantic changes back into canonical DMTZ authority.

Broken/moved resources must be repaired only when the correct canonical replacement is established. Otherwise the knowledge layer fails explicitly.

### 10. Workflow integration — PASS

`resolve-context` now applies the ADF-E shortest-path/context-budget policy and exact-ID helper seam.

`resolve-contract` now validates accepted ranges, treats all text hits as candidates, rejects first-match canonicality, and resolves accepted meaning through live repository authority.

### 11. Secondary reference index role — PASS

`docs/implementation/agent_reference_index.md` remains useful as a compact human range/path bridge, but does not become an exact semantic registry or replace the stable-ID helper/canonical documents.

This avoids maintaining a second copy of all contract meanings.

### 12. Helper-level execution evidence — PASS

During ADF-E execution the three new Python helpers were syntax-parsed successfully.

They were also exercised against a controlled synthetic repository fixture:

- exact `AUTH-034` lookup returned both a definition candidate and an ordinary reference;
- out-of-range `AUTH-054` returned the expected accepted-range error;
- context-budget measurement completed with zero errors under the synthetic configured limits;
- a changed canonical resource produced the expected OKF routing review candidate.

This demonstrates the helper behavior itself. It is not a substitute for ADF-F running the checks against the real repository/CI environment.

### 13. Scenario corpus — PASS

`fixtures/adf_e_context_scenarios.yaml` covers exact lookup, invalid future IDs, bounded semantic discovery, direct-path routing, broken/ambiguous references, source-change review, moved resources, deprecated routes, budget overflow, scoped context, repository-vs-web authority, memory disagreement, OKF conflicts, interacting contracts, and external capability facts.

ADF-F owns automated scenario execution.

### 14. No new semantic authority — PASS

The stable-ID registry records accepted identifier ranges only. It does not contain contract prose.

Context budgets describe agent-facing artifact size only. Knowledge-impact reports describe maintenance review candidates only. None of these artifacts becomes DMTZ domain truth, Assertion Authority, evidence sufficiency, health, or causal authority.

## Relationship to foundation exit gates

ADF-E strengthens the implementation basis for:

- **ADF-EX-05** — progressive disclosure without full-corpus preload;
- **ADF-EX-07** — explicit broken/deprecated/stale routing behavior;
- **ADF-EX-14** — deterministic canonical-reference/metadata validation seam;
- **ADF-EX-15** — deterministic context-budget policy/check.

These remain whole-foundation gates until ADF-F executes/integrates them and ADF-G supplies relevant runtime evidence where required.

## Residual obligations

- **ADF-F:** integrate the OKF, adapter, skill, stable-reference/context-budget/maintenance checks and ADF-A–E fixtures into one deterministic conformance/CI path; produce the non-domain agentic health report required by ADF-EX-16.
- **ADF-G:** observe actual Cursor/Claude Code/Codex loading, workflow discovery, and context behavior and record supported/degraded runtime states.
- **ADF-H:** consolidate long-term security/trust/lifecycle governance and compatibility review horizons.

## Exit decision

**ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**

The next required foundation group is **ADF-F — Conformance, Validation, Drift Detection & CI**.
