# Contributing

DMTZ separates current semantic authority, implementation state, and historical provenance. Contributions should preserve those boundaries rather than reintroducing phase-order or search-order authority.

## Start here

Before changing the repository:

1. read [`docs/index.md`](docs/index.md) to locate the current owning documentation;
2. read [`AGENTS.md`](AGENTS.md) for repository-wide authority, workflow, and change-control rules;
3. for implementation work, read [`docs/implementation/README.md`](docs/implementation/README.md) and the explicitly selected implementation package;
4. when an accepted stable ID is involved, resolve it with `python3 scripts/agentic/resolve_stable_id.py <ID>` rather than relying on search order or historical occurrences.

Generated `knowledge/` content is an OKF compatibility projection and should not be edited directly.

## Contribution boundaries

- Change the smallest current owner that actually governs the behavior or meaning in question.
- Preserve accepted concept independence, stable-ID meaning, authority boundaries, temporal semantics, and evidence requirements unless the contribution explicitly proposes a governed semantic change.
- Treat `docs/history/` as provenance and rationale, not as current authority. Preserve historical records rather than rewriting them to match current terminology or state.
- Keep implementation decisions subordinate to current semantic and architecture contracts. Implementation difficulty is not permission to weaken an accepted requirement.
- Do not infer authority, causation, identity, exposure, health, readiness, or enforcement from convenience signals such as repository ownership, source count, recency, naming similarity, or execution success.
- Record material implementation choices and intentional semantic/architecture changes through the repository's applicable ADR, traceability, and change-control mechanisms.

## Design and documentation

Functional concepts follow Daniel Jackson's Concept Design method documented at [`docs/reference/concept-design-method.md`](docs/reference/concept-design-method.md). A concept should have an independent purpose and operational principle rather than merely representing a vendor feature or implementation component.

Current documentation is organized by responsibility under `docs/concepts/`, `docs/architecture/`, `docs/authority/`, `docs/contracts/`, `docs/experience/`, `docs/invariants/`, `docs/policies/`, and `docs/reference/`. Use [`docs/index.md`](docs/index.md) when ownership is unclear.

Historical design progression, prior decisions, reviews, and superseded material are retained under [`docs/history/`](docs/history/README.md) for audit and rationale.

## Implementation and validation

Implementation begins only from an explicitly human-selected package or task. Follow the package's documented acceptance boundary and stop rather than automatically continuing into the next package.

Use the lowest-cost executable evidence appropriate to the change: unit/property checks, contract/schema tests, persistence tests, adapter/integration tests, product scenarios, or end-to-end validation as justified. Prior design acceptance is not executable proof.

For repository agentic/documentation conformance, use:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

When changing documentation progression/status rendering, also run:

```bash
python3 scripts/check_docs_consistency.py
```

Do not claim Databricks runtime support, deployment capability, provider compatibility, or production readiness without corresponding executable or environment-specific evidence.

## Security and examples

Never commit secrets, credentials, production data, or real PII/PHI. Use synthetic examples and least-privilege test identities. Security, policy, and governance documentation should state what DMTZ requires without presenting design intent as a compliance certification.
