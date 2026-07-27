# Metrics workflow evidence basis

This note records the public sources and engineering principles behind the `metrics` skill. It is maintainer evidence, not runtime context required for every invocation.

## Decision-first measurement

The skill starts with the decision and desired outcome rather than a catalogue of available signals. This prevents easy-to-collect activity from becoming a proxy for success without an explicit validity argument. Outcome, driver, guardrail, and diagnostic roles keep the selected set small while exposing incentives and trade-offs.

## Reliability and alerting

Google's Site Reliability Engineering guidance identifies latency, traffic, errors, and saturation as useful core service signals and distinguishes symptom-oriented black-box monitoring from internal diagnostics. It also stresses simple monitoring and actionable outputs rather than paging on every unusual value.

Sources:

- [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Practical Alerting from Time-Series Data](https://sre.google/sre-book/practical-alerting/)

The skill treats these as lenses rather than mandatory metrics. Local user journeys and accepted service objectives still determine definitions and thresholds.

## Instrument and dimension semantics

OpenTelemetry defines metrics as runtime measurements with instruments, time, and associated metadata. Its documentation and specification distinguish instrument types, aggregation, semantic conventions, and cardinality. The skill therefore requires explicit instrument semantics, units, bounded dimensions, and verification through the repository's actual collection path.

Sources:

- [OpenTelemetry metrics concepts](https://opentelemetry.io/docs/concepts/signals/metrics/)
- [OpenTelemetry metric API specification](https://opentelemetry.io/docs/specs/otel/metrics/api/)
- [OpenTelemetry metrics semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/)
- [OpenTelemetry glossary: cardinality](https://opentelemetry.io/docs/concepts/glossary/)

The skill remains vendor-neutral and requires reuse of an existing telemetry stack unless the user explicitly accepts a new dependency.

## Software delivery outcomes

DORA's software delivery performance research measures delivery at a team/system boundary and balances throughput with instability. The skill uses that framing while requiring local definitions for deploys, changes, failures, recovery, and service scope. It rejects individual activity rankings because they invite gaming and local optimization.

Source:

- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/)

## Measurement validity and limitations

The workflow makes proxy limitations, compatible populations, time windows, attribution, missing data, deduplication, and confounding explicit. It separates instrumentation from causal inference and requires experiment assignment/exposure semantics before interpreting treatment outcomes.

The implementation guidance also reflects established time-series properties:

- counters represent cumulative additive events and are normally interpreted over a window;
- gauges represent current observations and are not automatically additive;
- distributions retain information needed for latency and size analysis;
- derived ratios require compatible source counts and denominator handling;
- high-cardinality identifiers belong in logs/traces or controlled analytical events, not metric dimensions.

## Skill-specific design decisions

- **Execution default:** wording such as "add", "create", "instrument", or "implement" authorizes repository implementation; "what should we measure" defaults to a plan.
- **No invented targets:** measurement can begin with a baseline and decision rule. Familiar framework thresholds do not become local requirements automatically.
- **End-to-end verification:** code compilation alone cannot prove metric semantics. The skill checks emission, dimensions, aggregation, queries, quality invariants, and owner response as far as available infrastructure permits.
- **Smallest useful set:** additional metrics need a decision, investigation, or guardrail role. This resists dashboard growth and telemetry cost.
- **Privacy and cardinality gates:** identifiers, free text, raw errors, prompts, URLs, and arbitrary labels are excluded from metric dimensions by default.

## Evaluation scope

The checked-in eval set covers:

- product outcome/driver/guardrail discovery;
- asynchronous reliability and alert redesign;
- semantic audit across mutable dimensions and retries;
- non-gameable software delivery measurement;
- AI-agent evaluation across offline and production evidence;
- privacy/cardinality redesign for unsafe dimensions;
- safe boundaries when no telemetry or analytics stack exists;
- repository implementation with retries, final outcomes, latency, bounded labels, tests, and real verification.

Trigger evals include adjacent negative cases for arithmetic, logs, traces, summaries, implementation specifications, existing SQL definitions, profiling, and dashboard presentation so the skill does not trigger on every mention of data or observability.
