# Metric Contracts

Use this reference to make a metric unambiguous enough to implement, query, review, and maintain.

## Contents

- Contract
- Instrument semantics
- Definition checks
- Quality invariants

## Contract

```markdown
### `<stable_name>` — Outcome | Driver | Guardrail | Diagnostic

**Intent**
- Question/decision:
- Owner and response:
- Construct represented:
- Known proxy limitation:

**Definition**
- Entity and population:
- Numerator/value:
- Denominator (if any):
- Inclusion rules:
- Exclusion rules:
- Timestamp basis:
- Window and aggregation:
- Unit:
- Directionality:

**Collection**
- Source of truth:
- Instrument/event type:
- Instrumentation point:
- Allowed dimensions and bounded values:
- Retry, duplicate, reset, late-data, and missing-data behaviour:
- Privacy classification and retention:

**Interpretation**
- Baseline:
- Target/threshold status: accepted | baseline first | unresolved
- Segments needed for a decision:
- Confounders and limitations:
- Guardrail relationship:

**Quality and lifecycle**
- Validation/reconciliation checks:
- Freshness/completeness expectations:
- Version/definition owner:
- Migration or removal plan:
```

Omit fields that genuinely do not apply, but do not omit them merely because the answers are unknown. Mark consequential unknowns explicitly.

## Instrument semantics

### Counter

A monotonically increasing total, normally interpreted through a rate or increase over a window. Define process-reset handling and whether the count represents attempts, completed actions, or unique outcomes.

Good uses: requests, completed jobs, bytes sent, failures.

### Up/down counter

Tracks additive changes to a current total. Define every increment and decrement path and how leaks are detected.

Good uses: active operations or queue occupancy when transitions are authoritative.

### Gauge

A sampled current value. Define when it is observed, whether stale values expire, and whether values can be summed across instances.

Good uses: temperature, current queue depth, configuration state.

### Histogram or distribution

Records individual values so a backend can aggregate count, sum, buckets, and quantiles. Define unit, boundaries when explicit buckets are used, and expected range.

Good uses: latency, payload size, batch size.

Do not average precomputed percentiles across hosts or time. Prefer aggregation from distributions with compatible boundaries and temporality.

### Derived metric

A query or recording rule calculated from source measurements. Version the definition and keep numerator, denominator, unit, population, and window visible.

Good uses: error ratio, completion rate, cost per successful task.

### Business/product event

A domain transition used to derive product metrics. Define actor/entity identity, event time, authoritative transition, deduplication key, schema version, and consent/privacy treatment.

Good uses: onboarding completed, subscription activated, task outcome accepted.

## Definition checks

Before implementation, verify:

- A reader can calculate the same value independently from the contract.
- Numerator and denominator use compatible populations and windows.
- The metric does not change meaning across dimensions.
- The name, unit, and directionality agree.
- `zero`, `missing`, `not applicable`, and `unknown` are distinct where needed.
- Retries, replays, bot traffic, test traffic, and internal users have explicit treatment.
- The target is sourced or marked unresolved; it is not inferred from a familiar framework.
- The metric can trigger a named decision or action.

## Quality invariants

Prefer cheap invariants that reveal semantic drift:

- subset counts do not exceed parent counts;
- success + classified failure equals completed attempts;
- funnel stage N does not exceed the eligible previous stage without documented re-entry;
- derived totals reconcile with an authoritative store within a stated tolerance;
- event schema versions and unknown enum values are visible;
- freshness, completeness, duplicate rate, and invalid-record rate stay observable;
- dimensions remain within an expected cardinality budget.

A reconciliation difference is evidence to investigate, not permission to silently rewrite one source to match another.
