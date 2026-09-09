# Phase 010 Group 03 — Disclosure Projection Architecture

## Purpose

Realize AUTH-044–AUTH-053 and EXPL-101–EXPL-120 so current requester visibility does not alter internal truth or historical state.

## Disclosure request

A disclosure request binds:

- requester principal;
- target audience if different;
- purpose;
- delivery channel;
- onward-use/export context;
- requested proposition/subject/time perspective;
- requested detail/basis action.

## Independently authorized dimensions

Evaluate at least:

1. conclusion/result;
2. material context;
3. material limitations;
4. basis identity/reference;
5. provenance metadata;
6. exact evidence content/detail;
7. export/forward/publish action.

A conclusion can be visible while exact basis is not. A conclusion cannot be shown in a way that requires suppressing a material limitation and therefore strengthens it.

## Projection forms

- `exact`;
- `coarse` / generalized;
- `redacted`;
- `opaque_reference`;
- `withheld`.

Projection form is not evidence strength. It describes permitted disclosure detail.

## Safe abstraction

A transformation must preserve subject/proposition identity or explicitly narrow it. It may remove names, paths, exact timestamps or basis detail, but cannot:

- broaden population/path coverage;
- upgrade unknown/insufficient/conflicting status;
- merge materially distinct subjects;
- imply direct Lineage/path when hidden evidence is opaque;
- remove a limitation required to understand the result;
- manufacture a new inference from hidden evidence simply because the result is coarser.

## Basis inspection

Each basis relation remains internally complete. Visible basis is filtered item-by-item. Existence/count/type/source/timestamp/path/redaction markers can themselves require authorization.

If disclosing `3 hidden items` would leak sensitive source structure, the visible projection can omit the count entirely.

## Historical basis

A retained basis is not current permission. Each current request is authorized under current disclosure rules. Historical actor permission and historical actual communication remain separate facts.

If a payload is archived, authorization to inspect may permit a restore request but restore itself is a separately auditable operation. A provenance stub can be visible while its payload remains expired/unavailable.

## Mosaic defense

Projection policy may consider repeated-query/differencing context. A series of individually coarse answers may require further narrowing or withholding when their composition would reveal restricted detail.

## Cross-audience consistency

Different audiences can see different detail, but DMTZ must not intentionally issue contradictory statements about the same bounded visible proposition merely because authorization differs.