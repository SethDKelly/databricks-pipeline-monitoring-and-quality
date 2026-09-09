# OPS-110 — HOLD Enforcement, Wait Interval & Contradictory Start

**Status:** Accepted — Phase 007 Group 08

## Purpose

Make a HOLD conclusion sufficiently specific to support operational reasoning without turning absence of a run into automatic control success.

## Contract

An enforced HOLD binds:

- exact opportunity;
- effective hold interval;
- Gate/configuration/decision identity;
- control-boundary evidence;
- relevant execution-start coverage;
- superseding admit/override/cancel/expiry facts.

## Rules

- reliable execution-start evidence during an otherwise applicable HOLD, without a valid superseding action, materially contradicts full HOLD enforcement;
- no execution start supports HOLD only when the opportunity and Execution History coverage are sufficient;
- missing run telemetry is not successful HOLD evidence;
- a held opportunity can later be admitted, overridden, cancelled or expire without rewriting the hold interval;
- HOLD suppresses admission at the start boundary; it does not stop an execution that already began before effective enforcement.

Wait duration is an operational timing fact derived from opportunity/hold/start evidence, not a Gate health score.