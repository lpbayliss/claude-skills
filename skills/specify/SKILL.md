---
name: specify
description: Create, review, repair, or transform software specifications into decision-ready and implementation-ready contracts. Use for new projects, features, services, migrations, architecture changes, RFCs, PRDs, design docs, implementation plans, issue sets, diagrams, rough notes, or existing specs—even when the user only asks to plan, scope, improve, formalize, critique, or make work ready for humans or coding agents.
license: MIT
compatibility: Designed for Claude Code and compatible Agent Skills clients; repository-aware work requires file and search tools.
metadata:
  author: lpbayliss
  version: "1.0.0"
---

# Software Specification Workflow

Produce the smallest artifact that safely resolves uncertainty and can govern implementation. Preserve intent, expose ambiguity, and connect every important claim to evidence and verification.

The default deliverable is the specification, not code. Implement only when the user explicitly requests execution and the readiness gate permits it; otherwise stop at the accepted implementation slices.

## Core chain

Do not turn a vague request directly into an implementation checklist. Build:

```text
problem evidence → goals/non-goals → requirements → design decisions →
verification → rollout/operations → implementation slices
```

For small work, compress this chain into a mini-spec; do not omit it.

## Select the operating mode

Choose from the supplied material and request:

- **Create** — derive a new specification from an idea, problem, issue, or repository.
- **Transform** — convert existing artifacts into a stronger specification while preserving provenance and accepted intent.
- **Review** — assess readiness and return findings before proposing corrections.
- **Update** — revise an accepted spec using new evidence or implementation discoveries, preserving change history.

When transforming prose, diagrams, tickets, ADRs, screenshots, or mixed artifacts, read the [artifact transformation guide](references/artifact-transformation.md) before drafting. When reviewing, read the [review checklist](references/review-checklist.md). For a full specification, use the [full template](references/spec-template.md). For a compact evidence-poor example, read the [mini-spec example](references/mini-spec-example.md).

## Choose artifact depth

Use the smallest useful form:

- **Issue contract** — routine, local, reversible work with an established repository pattern.
- **Mini-spec** — bounded but non-obvious work, usually 1–3 pages.
- **Full specification** — cross-component, high-risk, security-sensitive, migration-heavy, long-lived, or multi-agent work.
- **Spike brief** — evidence is too weak to choose a design; define a hypothesis, experiment, evidence, and decision rule.
- **Review report** — readiness and gaps are needed before rewriting.

Template size is not rigor. Scale depth with ambiguity, blast radius, reversibility, and cost of being wrong.

## Workflow

### 1. Establish the decision boundary

Extract:

- desired outcome and affected users;
- stakeholders and acceptance authority;
- fixed constraints and known non-goals;
- deadlines or sequencing;
- decisions requested now;
- whether the user wants planning only or implementation too.

Ask only when missing information materially changes product behaviour, architecture, safety, public interfaces, destructive scope, or rollback. For low-risk unknowns, continue with explicit assumptions.

### 2. Inspect sources of truth

For an existing project, inspect before designing:

- `CLAUDE.md`, `AGENTS.md`, contribution guidance, and local rules;
- module boundaries and comparable features;
- public interfaces, schemas, migrations, events, and generated files;
- tests, fixtures, build scripts, CI, lint, and type-check commands;
- deployment, feature-control, telemetry, and rollback conventions;
- relevant ADRs, issues, incidents, support evidence, and existing specs;
- current branch and working-tree constraints if execution may follow.

Use exact paths and real commands. Do not invent repository structure. If no repository is available, label the work greenfield. If only prose or images are supplied, keep repository-specific details unresolved and do not claim implementation readiness.

### 3. Preserve provenance and classify statements

Maintain a short evidence table:

| Claim | Evidence/source | Confidence | Implication |
|---|---|---:|---|

Classify consequential source statements as:

- **Fact** — evidenced current state.
- **Requirement** — agreed observable obligation.
- **Constraint** — fixed boundary on valid solutions.
- **Decision** — selected option with authority.
- **Assumption** — believed but unproven.
- **Risk** — possible harmful outcome.
- **Open question** — unresolved information or decision.

Do not silently promote proposals or examples into requirements. Do not erase conflicting source material; surface the conflict and name the authority needed to resolve it.

### 4. Frame the problem before the solution

Write:

- a one-paragraph decision summary;
- current state and problem evidence;
- stakeholders and audience;
- goals as observable outcomes;
- plausible adjacent non-goals;
- success measures and constraints;
- glossary where terms could be misunderstood.

If the source embeds an unvalidated technology or architecture, treat it as a candidate unless the user, accepted decision, or hard constraint fixes it. Preserve the intended outcome, not the premature mechanism.

### 5. Model behaviour and boundaries

Cover proportionately:

- primary journeys;
- alternate, error, cancellation, and recovery flows;
- administration, support, and operations;
- concurrency, retries, idempotency, ordering, timeouts, and backpressure;
- lifecycle, migration, compatibility, deletion, and rollback;
- abuse and threat scenarios;
- system, trust, data, ownership, and external dependency boundaries.

Use diagrams only when they clarify a decision. Explain each diagram in prose and label relationships and trust boundaries.

### 6. Write requirements as testable contracts

Give consequential requirements stable IDs:

- `FR-*` functional behaviour;
- `QR-*` quality and SLO targets;
- `SEC-*` security and privacy;
- `DATA-*` integrity and lifecycle;
- `INT-*` interfaces and compatibility;
- `OPS-*` operations and readiness.

Use:

```text
[Condition] + [subject] + must/should/may + [observable behaviour] +
[object] + [measurable limit or qualification].
```

Keep one independently-failable obligation per requirement. For each mandatory requirement, record its rationale/source and an objective verification method with a pass condition.

Avoid `fast`, `scalable`, `robust`, `seamless`, `user-friendly`, `where possible`, and similar terms unless objectively defined. Do not invent numeric targets. Use `[BLOCKING: owner-approved target]` or `[DELEGATED: named measurement]` and explain how it will be resolved.

### 7. Compare credible designs

Start with the simplest solution satisfying accepted requirements. Include the status quo when credible. For each serious option compare:

- requirements covered;
- responsibilities, interfaces, state, and data ownership;
- failure and degraded behaviour;
- security and privacy boundaries;
- operational load and observability;
- migration, rollback, and compatibility;
- cost, complexity, and maintenance;
- assumptions and unknowns.

Do not create straw alternatives. Capture consequential choices as linked ADRs with context, decision, status, consequences, alternatives, and supersession rules.

### 8. Design verification before implementation

Create a requirement-to-evidence matrix:

| Requirement | Evidence | Level | Command/location | Pass condition |
|---|---|---|---|---|

Include existing regressions and proportionate unit, integration, contract, end-to-end, migration, performance, security, accessibility, resilience, property, and production evidence. Passing tests is insufficient if the tests encode the wrong interpretation; validate evidence against requirements and invariants.

### 9. Define change and operating safety

For production-facing work, address:

- enable/disable and blast-radius controls;
- staged rollout and objective success/degradation/rollback signals;
- data behaviour on rollback;
- upgrade, downgrade, and version skew;
- dependency, capacity, resource exhaustion, and cost impact;
- telemetry, alerts, dashboards, runbooks, and ownership;
- backup, restore, disaster recovery, retention, and deletion where relevant.

Write `None — [reason]` for a risk area considered and found irrelevant.

### 10. Classify uncertainty

Label every open question:

- **Blocking** — implementation stops until answered.
- **Delegated** — an agent may resolve it through a named investigation and decision rule.
- **Deferred** — deliberately outside current scope.

Label solution latitude:

- **Fixed** — invariant, accepted decision, compatibility contract, or mandatory behaviour.
- **Preferred** — established pattern; deviation needs rationale.
- **Open** — implementation may choose after inspection.

Never convert a blocking product decision into an implementation assumption.

### 11. Decompose accepted work

Only after requirements and design are sufficiently accepted, create small ordered tasks. Each task includes:

```text
ID and objective
Requirements covered
Expected files/components
Preconditions and dependencies
Implementation steps
Tests to add or update
Exact verification command
Expected observable result
Rollback or cleanup
Parallel-safety and shared-write warnings
```

Prefer independently verifiable vertical slices. Parallelise only independent decisions and write sets. Give shared schemas, migrations, contracts, and public interfaces one authoritative owner.

### 12. Run the readiness gate

Begin every review with exactly one verdict:

- **Ready** — implementation may proceed within accepted constraints.
- **Conditionally ready** — only named non-blocking evidence or approvals remain.
- **Not ready** — blocking reasons are listed before corrections.

Do not mark ready when any mandatory requirement lacks verification, a blocking question remains, product behaviour must be invented during implementation, a material security/privacy/public-interface/destructive decision is unresolved, rollback is not credible, repository paths or commands are unknown, or required specialist review is missing.

For high-impact security, privacy, distributed-system, data-governance, migration, or causal-inference work, require independent specialist review before declaring readiness. An early public draft must say `Draft — independent review pending` rather than pretending to be an implementation contract.

## Output rules

Lead with decision-ready material, not process narration. Use this compact shape unless risk requires the full template:

```markdown
# [Title]
**Status:** Ready | Conditionally ready | Not ready — [reasons]
**Decision owner / acceptance authority:** [name, role, or BLOCKING]
## Decision summary
## Context and evidence
## Goals / non-goals
## Requirements and acceptance
## Proposed design and alternatives
## Risks, rollout, and rollback
## Verification
## Open questions
## Implementation slices
## Source transformation summary (when applicable)
```

When transforming existing material, include a concise summary of what was preserved, corrected, reclassified, removed, and left unresolved. Preserve the original artifact unless the user explicitly asks for in-place editing.

## Agentic safeguards

- State invariants and forbidden outcomes, not only positive examples.
- Preserve traceability from need → requirement → decision → task → code → evidence.
- Require exact repository paths and commands before declaring execution readiness.
- Stop autonomous work at unresolved security, privacy, destructive migration, public API, data-loss, or hard-to-rollback decisions.
- Update or supersede the spec when implementation invalidates an assumption; do not hide divergence in code-review comments.
- Never mark a spec ready merely because every template heading contains text.

## Anti-patterns

- Implementation plans written before validating the problem.
- Generic architecture detached from the repository.
- Feature lists without non-goals, priorities, or pass conditions.
- Existing artifacts rewritten without provenance or change rationale.
- Vague quality adjectives and fabricated targets.
- Happy-path-only flows.
- Tests defined after implementation to approve whatever was built.
- One agent inventing intent, implementation, and acceptance without review.
- Frozen specs that are neither maintained nor explicitly superseded.

## References

- Read the [artifact transformation guide](references/artifact-transformation.md) when adapting existing material.
- Read the [full specification template](references/spec-template.md) for a full specification.
- Read the [review checklist](references/review-checklist.md) for readiness reviews.
- Read the [mini-spec example](references/mini-spec-example.md) for a compact worked example.
- Read the [source basis](references/source-basis.md) for the standards and evidence behind the workflow.
