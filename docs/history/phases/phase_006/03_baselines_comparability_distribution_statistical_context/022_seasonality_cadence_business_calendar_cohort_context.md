# HLTH-022 — Seasonality, Cadence, Business Calendar & Cohort Context

**Status:** Accepted — Phase 006 Group 03

## Purpose

Prevent valid recurring operating patterns from being misclassified by references drawn from the wrong temporal or population context.

## Contract

Reference context may include, where material:

- weekday/weekend;
- month-end/quarter-end/year-end;
- holiday/business-calendar class;
- scheduled batch/cycle position;
- region, product, customer, source-system or other governed cohort;
- known operating mode or market/session context.

A comparison must use the context that materially affects the measured dimension. Context that does not affect the proposition should not be added merely to create finer segmentation.

## Invariants

- Recency is not a substitute for calendar/cadence comparability.
- A global Baseline does not automatically override a better-defined seasonal/cohort reference.
- A narrow cohort with insufficient history remains insufficient rather than borrowing a broader population without an explicit valid comparison rule.
- Cohort membership uncertainty remains explicit.
- Calendar/cohort segmentation describes behavior; it does not make that behavior acceptable.
- Over-segmentation that destroys reference sufficiency is not automatically preferable to a broader valid reference.

## Example

Month-end C volume may be 3x ordinary weekday volume. The ordinary weekday Baseline is not evidence that month-end is anomalous. If only two month-end observations exist, the result may be `insufficient reference` rather than falling back silently to weekday history.