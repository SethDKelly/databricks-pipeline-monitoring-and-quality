# HLTH-032 — Warning Bands, Tolerance Margins & Proximity Semantics

## Purpose

Separate criterion satisfaction from proximity, warning and tolerance interpretation.

## Rule

A warning/tolerance band is an explicitly defined secondary normative region around or within a criterion. It may communicate approach to a limit, tolerated deviation, or graduated response without changing the underlying comparison semantics.

Examples include:

- freshness required by 07:00, warning after 06:45;
- null rate must be <=2%, warning above 1.5%;
- expected total 100 with tolerated operational band 98–102 and failure outside 95–105 only when that structure is explicitly governed.

## Invariants

- `warning` is not a synonym for `violation` or `low severity`.
- A value may meet the hard criterion while being in a warning/proximity band.
- A value that violates the hard criterion remains a violation even if response severity is low.
- Tolerance/margin behavior must state whether it changes the criterion itself, defines a secondary band, or affects only response/escalation.
- Hidden platform defaults must not invent margins or hysteresis.
- Warning bands and tolerance margins are versioned with their governing Expectation context.

## Non-goals

- notification routing;
- composite health coloring;
- operational alert suppression implementation.