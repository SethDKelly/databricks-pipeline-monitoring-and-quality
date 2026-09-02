# ADF-E — Context Discovery, Stable References & Knowledge Maintenance

**Status:** PLANNED / READY TO EXECUTE

## Objective

Make correct context easy to discover while keeping agent startup context small and preventing knowledge-routing artifacts from drifting away from canonical DMTZ sources.

## Default context path

Routine development should follow:

```text
shared agent constitution
  → knowledge/index.md
  → active implementation package/group
  → one domain routing entry
  → one or two canonical architecture/reference documents
  → exact stable IDs/tests as required
```

Preloading the entire DMTZ design corpus is explicitly discouraged.

## Stable-reference strategy

The accepted identifiers remain the primary semantic lookup keys:

- SYN-###;
- REF-###;
- AUTH-###;
- HLTH-###;
- OPS-###;
- EXPL-###;
- INTG-###;
- ARCH-###.

Implementation/test IDs may be added under their own implementation namespaces, but they do not replace the accepted contract IDs they realize.

A routing artifact should point to stable IDs and canonical file paths rather than copying full contract prose.

## Context budgets

ADF execution should establish measurable budgets rather than relying on subjective 'keep it small' guidance.

Recommended initial targets:

- universal instructions: only rules required for nearly every repository task;
- tool adapter persistent context: less than the shared constitution, preferably only a few dozen lines;
- one active scoped rule at a time where tooling supports it;
- one workflow skill plus supporting files on demand;
- OKF index descriptions concise enough to scan without pulling the linked source.

Exact token/line limits may be calibrated during compatibility tests. The important invariant is that detailed DMTZ semantics remain retrieval-on-demand.

## Search behavior

Agents should prefer, in order:

1. active package/group path known from implementation status;
2. OKF domain/implementation routing entry;
3. exact stable-ID repository search;
4. targeted canonical file read;
5. broader semantic search only when the exact reference is unknown.

Do not search public web for a DMTZ semantic answer that should come from the repository.

## Knowledge maintenance

When canonical documentation changes:

- determine whether one or more OKF routing entries reference the changed source;
- update only the routing metadata/description that became stale;
- retain canonical history in Git rather than copying retired semantics into a new knowledge layer;
- mark obsolete knowledge entries `deprecated` rather than leaving contradictory current entries;
- update `knowledge/log.md` for material routing changes if the log is adopted.

## Generated versus authored content

Mechanically derivable content should be generated where useful:

- directory indexes;
- lists of implementation packages;
- known contract ranges;
- link existence checks;
- compatibility-version metadata.

Interpretive summaries should be short and human-reviewable.

No generated summary should contain unique semantic requirements that are absent from canonical sources.

## Retrieval failure semantics

If an agent cannot resolve a referenced file/contract:

- report the missing/broken reference;
- do not infer the contract from memory;
- do not silently use a similar historical contract;
- do not treat inability to retrieve as evidence that no constraint exists.

## Deliverables

- updated `agent_reference_index.md` integrated with the OKF bundle or superseded by a generated view;
- deterministic stable-ID/link discovery helpers as useful;
- context-size checks/metrics for shared instruction surfaces;
- routing-entry maintenance process;
- broken-reference behavior documented and validated.

## Acceptance scenarios

ADF-E passes when:

- a developer can locate a referenced contract without loading the corresponding whole phase;
- stale/deprecated routing is surfaced explicitly;
- a broken link fails knowledge validation but does not mutate canonical docs;
- agents do not rely on chat/memory for missing contract text;
- tool startup context remains materially smaller than the historical always-applied Cursor-rule model.
