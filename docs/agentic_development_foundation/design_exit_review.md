# Agentic Development Foundation — Design Exit Review

**Status:** ACCEPTED — DESIGN COMPLETE / EXECUTION MAY BEGIN AT ADF-A

## Review question

Does the Agentic Development Foundation provide enough bounded design for an enterprise team to implement a tool-neutral, human-directed coding-agent environment across Cursor, Claude Code and Codex without another broad design pass before Implementation 001?

**Conclusion: yes.**

## Exit findings

### 1. Scope and authority are explicit — PASS

ADF-A establishes that the foundation is an implementation-enablement layer beneath frozen DMTZ semantics. It defines one authority hierarchy and makes human-directed execution the current boundary.

Autonomous task generation, multi-agent delegation, unattended merge/deploy and autonomous architecture reopening are explicitly excluded.

### 2. Portable knowledge plane is defined — PASS

ADF-B adopts upstream OKF v0.2 as the knowledge interchange format and defines a deliberately thin DMTZ profile. The knowledge bundle routes to canonical authority instead of reproducing it.

The design explicitly prevents OKF verification/trust/lifecycle signals from being confused with DMTZ Assertion Authority, evidence sufficiency, causal confirmation, health or freshness semantics.

### 3. Tool-specific instruction duplication is prevented — PASS

ADF-C keeps root `AGENTS.md` as shared repository authority and restricts Cursor/Claude/Codex adapters to native mechanics. Claude is expected to import/reference shared authority; Cursor keeps scoped rules; Codex consumes `AGENTS.md` directly where supported.

No tool is semantically privileged.

### 4. Reusable workflows are separated from persistent instructions — PASS

ADF-D defines a portable, human-invoked skill/workflow source so repeated procedures do not expand universal prompts. The initial workflow set covers context resolution, group implementation, exact contract retrieval, conformance, review, traceability and exit review.

Skills cannot self-authorize scope expansion or automatic continuation.

### 5. Context-minimization and retrieval are explicit — PASS

ADF-E defines progressive disclosure, stable-ID retrieval and failure behavior. Agents are expected to load only the active group/domain/exact contract set they need.

The design preserves the successful lean Cursor-rule refactor rather than recreating a large always-on knowledge prompt.

### 6. Deterministic enforcement exists in the design — PASS

ADF-F defines OKF/profile validation, link/contract checks, tool-adapter validation, context budgets, workflow fixtures and CI/drift reporting.

Agent instructions are therefore not the only control plane.

### 7. Developer tool freedom is preserved — PASS

ADF-G defines a common artifact/test/review acceptance model for Cursor, Claude Code and Codex while retaining ordinary non-agent development as a supported path.

Tool-specific feature loss degrades convenience rather than changing semantic correctness.

### 8. Security/trust/lifecycle boundaries are explicit — PASS

ADF-H covers least privilege, secret/sensitive-data exclusion, tool-memory non-authority, OKF trust semantics, vendor compatibility lifecycle and agentic-artifact governance.

Removing AI tooling still leaves DMTZ understandable and buildable by human developers.

### 9. External-standard assumptions are isolated — PASS

`external_standards_baseline.md` records version-sensitive OKF/Cursor/Claude/Codex assumptions separately from DMTZ truth and defines reverification triggers.

The design does not freeze transient vendor behavior into product architecture.

### 10. Autonomous scope is retained without leaking into the foundation — PASS

`autonomous_backlog.md` contains a small set of future candidates and a re-entry gate. No autonomous capability is required for ADF completion or Implementation 001.

## Design completeness

The design is intentionally sufficient to execute ADF-A–H without another broad agentic architecture exercise. Execution may still make narrow implementation choices such as:

- exact validator implementation language/library;
- precise DMTZ OKF metadata requirements after fixture testing;
- whether native skill adapters are generated, copied or referenced;
- exact context-size thresholds;
- exact compatibility manifest format;
- which tool-in-the-loop smoke checks are practical in CI versus documented/manual validation.

Those are implementation decisions below this foundation and do not require reopening the design unless the common-authority/tool-neutral model proves unrealizable.

## Execution order

Recommended next work:

**ADF-A — Authority, Scope & Human-Directed Operating Boundary**

Then:

- ADF-B / ADF-C may proceed in parallel;
- ADF-D / ADF-E consume A–C;
- ADF-F adds deterministic conformance;
- ADF-G proves cross-tool developer compatibility;
- ADF-H consolidates governance and lifecycle;
- an implementation exit review should then verify the actual artifacts before Implementation 001-A begins.

## Exit decision

**Agentic Development Foundation design: ACCEPTED.**

No additional broad design phase is required before ADF-A execution. Autonomous development remains deferred and must not be inferred from this acceptance.
