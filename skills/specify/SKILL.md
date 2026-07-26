---
name: specify
description: Creates, reviews, repairs, and transforms software specifications into decision-ready, implementation-ready contracts. Use when the user needs a spec, RFC, PRD, technical design, implementation plan, scoped issue contract, architecture or migration proposal, or wants rough notes, tickets, diagrams, screenshots, or an existing document made ready for humans or coding agents. Also use when asked to plan, scope, formalize, critique, or assess readiness before non-trivial software work. Do not use for straightforward coding, debugging, or explanation when no specification, planning, or design decision is needed.
license: MIT
compatibility: Designed for Claude Code and compatible Agent Skills clients; repository-aware work requires file and search tools.
metadata:
  author: lpbayliss
  version: "1.1.0"
---

# Software Specification Workflow

Produce the smallest specification that safely resolves the decision at hand. Preserve intent, expose uncertainty, and connect consequential claims to evidence and verification.

The default deliverable is a specification, not code. Implement only when the user explicitly asks and the readiness gate passes.

## Non-negotiables

- Inspect supplied artifacts and available repository evidence before designing.
- Preserve source provenance and accepted intent; never silently rewrite history.
- Do not invent product decisions, numeric targets, repository paths, commands, interfaces, or diagram semantics.
- Scale detail with ambiguity, blast radius, reversibility, and cost of error.
- Stop at unresolved security, privacy, destructive migration, public-interface, data-loss, or hard-to-rollback decisions.
- Do not call work ready merely because a template is complete.

## Choose mode and depth

Choose one primary mode:

| Mode | Use when | Default result |
|---|---|---|
| **Create** | Starting from an idea, problem, issue, or repository | New specification |
| **Transform** | Existing prose, tickets, diagrams, screenshots, or mixed artifacts need improvement | Revised specification plus change summary |
| **Review** | The user wants readiness, gaps, or critique | Verdict and prioritized findings; rewrite only if requested |
| **Update** | New evidence or implementation discoveries change an accepted spec | Revised spec, changed decisions, and supersession note |

Choose the smallest sufficient depth. These are ceilings to resist bloat, not quotas:

| Depth | Use when | Typical size |
|---|---|---:|
| **Issue contract** | Routine, local, reversible work with a proven repository pattern | Up to about 700 words |
| **Mini-spec** | Bounded, non-obvious work with a few decisions | Up to about 1,800 words |
| **Full specification** | Cross-component, security-sensitive, migration-heavy, long-lived, or multi-agent work | As needed for material decisions |
| **Spike brief** | Evidence is too weak to select a design | Hypothesis, experiment, evidence, decision rule |
| **Review report** | Readiness must be assessed before rewriting | Findings only unless correction is requested |

Exceed a typical ceiling only when added detail resolves a material risk or decision. Do not expand a small request into a generic architecture dossier.

## Load only what the task needs

- For **Transform**, read the [artifact transformation guide](references/artifact-transformation.md).
- For **Review** or any readiness claim, read the [review checklist](references/review-checklist.md).
- For a **full, high-risk, migration, or multi-agent specification**, read the [detailed workflow](references/specification-workflow.md).
- Use the [full template](references/spec-template.md) only for a full spec or when the user requests that structure.
- Read the [mini-spec example](references/mini-spec-example.md) only to calibrate a compact, evidence-poor output.

Keep references one level deep. Do not load every reference by default.

## Progress loop

Track this loop for multi-step work; report the artifact rather than narrating the process:

- [ ] Frame the decision and choose mode/depth
- [ ] Inspect and normalize sources
- [ ] Draft the contract
- [ ] Design verification and change safety
- [ ] Review, repair, and issue the verdict

### 1. Frame the decision

Extract the desired outcome, affected users, acceptance authority, fixed constraints, known non-goals, decisions needed now, and whether implementation is requested.

Ask only when a missing answer materially changes behavior, architecture, safety, a public interface, destructive scope, or rollback. Otherwise continue with an explicit assumption or unresolved marker.

### 2. Inspect and normalize sources

For an existing project, inspect local rules, comparable features, interfaces, schemas, migrations, tests, build/CI commands, deployment controls, telemetry, ADRs, incidents, and existing specs. Use exact paths and commands.

When a decision depends on an external API, standard, library, platform, or current operational fact, consult the authoritative current source when tools permit. Record its URL, version, or access date; if it cannot be verified, label it unresolved rather than relying on memory.

If no repository is available, say the work is greenfield. If repository evidence is required but unavailable, keep paths and commands unresolved and do not claim implementation readiness.

Build a compact evidence map for consequential claims:

| Claim | Classification | Source | Confidence | Implication |
|---|---|---|---:|---|

Classify statements as **fact, requirement, constraint, decision, assumption, risk,** or **open question**. Treat examples and proposed technologies as proposals unless an accepted decision or hard constraint fixes them.

When sources disagree, preserve the conflict, identify the affected decision, and name who or what can resolve it. Do not average incompatible claims or silently choose the most convenient source.

### 3. Draft the contract

Frame the problem before the solution. Include only sections that help decide or verify the work:

- decision summary and evidence;
- goals and plausible non-goals;
- relevant journeys, failure/recovery behavior, boundaries, and invariants;
- testable requirements and acceptance evidence;
- selected design, credible alternatives, and consequential trade-offs;
- material risks, rollout, rollback, and operations;
- open questions and implementation slices when ready.

For consequential requirements, use stable IDs when traceability adds value. Keep one independently failing obligation per requirement, include its source/rationale, and define an observable pass condition.

Replace vague terms such as `fast`, `scalable`, `robust`, or `user-friendly` with evidence-backed measures. If no measure is accepted, use `[BLOCKING: owner-approved target]` or `[DELEGATED: named measurement and decision rule]`; never manufacture precision.

### 4. Select the design proportionately

Default to the simplest solution that satisfies accepted requirements. Compare only credible alternatives; include the status quo when it is credible. Explain why the selected option wins and what evidence could change the decision.

Separate solution latitude:

- **Fixed** — invariant, accepted decision, mandatory behavior, or compatibility contract.
- **Preferred** — established pattern; deviation needs rationale.
- **Open** — implementation may choose after bounded investigation.

Use diagrams only when they clarify a decision. Explain them in prose and label relationships, ownership, data movement, and trust boundaries.

### 5. Design evidence and safe change

Map mandatory requirements to evidence and pass conditions. Prefer real repository commands and test locations. Cover only materially relevant test levels and operating concerns; a long generic checklist is not evidence.

For production-facing change, define staged enablement, observable success/degradation signals, rollback triggers, and data behavior after rollback. Address migration, compatibility, capacity, cost, backup/restore, retention, or runbooks only where the change creates those obligations.

Decompose work only after the contract is accepted enough to implement. Each slice should identify requirements covered, dependencies, expected components, tests, exact verification, rollback/cleanup, and shared-write hazards. Parallelize independent decisions and write sets; give shared schemas, migrations, and public contracts one owner.

### 6. Review, repair, and issue the verdict

Use the [review checklist](references/review-checklist.md) as a semantic validator:

1. Draft the artifact.
2. Check it against the relevant checklist sections.
3. Repair omissions, contradictions, unsupported claims, and excess detail.
4. Repeat until no fixable issue remains.
5. Lead with exactly one verdict when reviewing or claiming readiness:
   - **Ready** — implementation may proceed within accepted constraints.
   - **Conditionally ready** — only named non-blocking evidence or approval remains.
   - **Not ready** — blocking reasons appear before proposed corrections.

A blocking question, invented product behavior, missing mandatory verification, unknown required repository command, unsafe rollback, or missing specialist review prevents **Ready**.

For high-impact security, privacy, distributed-system, data-governance, migration, or causal-inference work, require independent specialist review before readiness. Label early public work `Draft — independent review pending`.

## Output rules

- Lead with the decision, verdict, or corrected artifact—not process narration.
- Omit irrelevant headings. If a selected template requires a considered risk area, use `None — [reason]` rather than filler.
- Preserve the original artifact unless the user explicitly requests in-place editing.
- For Transform, summarize what was preserved, corrected, reclassified, removed, conflicted, and left unresolved.
- For Review, prioritize findings by impact and cite exact source sections; do not rewrite the whole document unless asked.
- Mark unknowns as **Blocking**, **Delegated**, or **Deferred**. Never turn a blocking product decision into an implementation assumption.
- Maintain traceability from need → requirement → decision → task → evidence without repeating the same prose in every section.

## Gotchas

- A technology named in a rough proposal is often a hypothesis, not a requirement.
- A diagram arrow without a label has direction at most; it does not prove protocol, data, ownership, trust, or timing.
- Existing tests prove current behavior, not necessarily desired behavior.
- A feature flag is not a rollback plan unless the old path remains safe and data stays compatible.
- Passing tests cannot rescue a requirement that encodes the wrong interpretation.
- More sections and longer task lists can reduce readiness by hiding unresolved decisions.
- Parallel-agent plans fail when multiple slices own the same schema, migration, contract, or generated file.
- Implementation discoveries must update or explicitly supersede the spec; divergence should not remain hidden in code comments.
