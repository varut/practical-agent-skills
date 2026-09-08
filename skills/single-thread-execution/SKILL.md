---
name: single-thread-execution
description: Apply automatically before every non-trivial project task, even when the user does not name this skill. Preserve the exact requested outcome, bind one authority and delivery tier, choose one bounded vertical slice, surface external prerequisites early, map every action to one Definition-of-Done item, stop scope expansion, and enforce stall and handoff gates. Also apply when implementation risks overengineering — new abstraction layers, wrappers, config options or flags nobody requested, error hierarchies, defensive handling of impossible states, speculative generality, gold-plated tests, "robust"/"extensible"/"future-proof" framing, or a rewrite where a small patch would do — and enforce the smallest verified diff instead. Use for builds, bug fixes, deployments, migrations, implementation research, scope changes, and resumed work. Do not use for isolated factual answers or tiny one-line edits.
metadata:
  short-description: Finish one outcome without scope drift
---

# Outcome-First Single-Thread Execution

## Purpose

Finish the user's requested result before expanding the project. Optimize for a working, observable outcome—not research volume, file count, agent count, test count, or architectural completeness. Spend surplus reasoning proving the smallest correct change and deleting code — not constructing abstractions, options, or handling that no criterion demands.

## Activation and write boundary

- Apply this skill automatically to every non-trivial project task, whether or not the user invokes it.
- Skip it for isolated factual questions, simple rewrites, or tiny bounded edits that need no project state.
- For change/build work, read or create the project state files before substantive editing.
- For review, diagnosis, explanation, or other read-only work, read existing state if present but do not create or modify state files. Hold the delivery contract in memory and use `focus_guard.py --diagnostic` when useful.
- Project-specific user instructions may replace the active priority. Do not infer a replacement from an additive request.

## Scope and precedence

- The user-level skill plus `$HOME/.codex/AGENTS.md` makes this the default for Codex projects. Skill matching is model-driven; the global instruction is the second enforcement layer, not an operating-system hook.
- Codex loads global guidance at the start of a run, and more-specific project guidance is layered afterward. Start a new run after changing global guidance, and resolve any deeper project instruction that explicitly conflicts with this protocol.
- This configuration does not govern Claude Code, Replit Agent, or other coding agents. Give those tools the equivalent repository or user-level instruction before expecting the same behavior.

## Outcome contract start gate

Before broad research, planning, editing, delegation, or deployment:

1. Bind the authoritative source and target runtime. Record the repository/workspace, branch or version when applicable, dirty state, and deployment target. A wrapper, recovery copy, preview, and production system are different authorities.
2. Read `PROJECT_FOCUS.md`, `BACKLOG.md`, and `DECISIONS.md`. For authorized change/build work, create missing files from this skill's templates. Upgrade an older focus file before the next substantive edit; never rewrite it during a read-only task.
3. Preserve the user's exact requested outcome, then translate it into one observable Primary Outcome.
4. Declare one Delivery Tier: `NOT APPLICABLE`, `LOCAL`, `DEVELOPMENT PREVIEW`, `INTERNAL BETA`, `PRODUCTION BETA`, `PRODUCTION`, or `GENERAL AVAILABILITY`.
5. List external prerequisites before implementation: identity, consent, credentials, access, paid resources, provider services, approvals, and deployment topology. Mark each `READY`, `BLOCKED`, or `NOT-REQUIRED`.
6. Define one Active Build as the smallest demonstrable vertical slice. If it spans multiple user journeys, environments, delivery tiers, or independently releasable outcomes, split it.
7. Write at most seven binary acceptance criteria labeled `DOD-1` through `DOD-N`. More requires an explicit user-approved scope exception.
8. Map every criterion to minimum sufficient evidence in `Evidence Plan`.
9. Record the user's explicit/observable budget and handoff threshold. If no meter or budget is available, say so; never invent a percentage.
10. Set exactly one Next Single Action referencing one `DOD-N`, or use `BLOCKER:` when progress requires external action.
11. Run `scripts/focus_guard.py --path <root>` for change/build work. Do not proceed while it fails.

## Scope admission test

Before every new action, ask:

1. Which current `DOD-N` does this close?
2. If none, which recorded blocker does it remove?
3. Is it the smallest safe action that advances that item?
4. If it adds an abstraction, file, dependency, option, or defensive branch, does that addition pass the Simplicity gate's admission test?

If the action cannot answer 1 or 2, put it in `BACKLOG.md` and do not perform it. Cleanup, refactoring, research, UX polish, hardening, integration work, and additional tests do not become required merely because they are useful.

When the user says “do everything” or gives a large program, preserve the whole request in the Primary Outcome/backlog but select one first complete vertical slice. Do not redefine a multi-week roadmap as one Active Build.

## Simplicity gate

Surplus reasoning goes into finding, shrinking, and verifying the smallest correct diff — never into construction that no criterion ordered. "Thorough" means certain the minimal diff is correct, not more layers, cases, options, or tests.

Before writing code for a criterion:

1. Search the repository for an existing mechanism that already does this. Reuse or extend it, or name the search that proved it absent.
2. State the smallest plausible diff: files touched and rough line count.
3. Spend remaining effort verifying that diff against the inputs the criteria actually name — not extending it.

Admission tests — each addition is banned until its test passes; failed moves go to `BACKLOG.md`:

- New abstraction (interface, base class, wrapper, layer, registry): two concrete call sites in the current diff. One caller means inline it.
- New file or module: name the existing file the change could not fit. Otherwise extend that file.
- New dependency: one named failed attempt with the standard library or an existing dependency.
- New config option, flag, parameter, or env var: a current `DOD-N` reads both values. Otherwise hardcode the one known value.
- New error type or defensive branch: a real input that reaches it today. Impossible states get an assert or nothing.
- Rewrite of a working unit: an explicit user request, or a `DOD-N` demonstrably unreachable by patching.

Banned outright: "while I'm here" refactors, renames or file moves no `DOD-N` requires, and tests for behavior outside the acceptance criteria — backlog them.

Diff proportionality: if the real diff exceeds roughly 3x the stated estimate, stop; shrink it or record a one-line justification in `DECISIONS.md` before continuing. A recorded justification unblocks; silent overshoot does not.

When two designs close the same `DOD-N`, take the one with fewer new names — files, types, functions, options. Count; do not argue taste. Lines deleted count as progress.

## External-prerequisite gate

Surface human or external blockers during the first meaningful pass. If the next required criterion needs a missing identity, consent, credential, paid resource, provider, access decision, or approval:

- set Status to `BLOCKED`;
- name the exact owner action and consequence;
- complete only safe preparation that directly serves that blocker;
- ask for the one required action; and
- stop adjacent implementation.

Authorization for the overall outcome does not silently authorize paid purchases, public access changes, identity use, credential handling, or other separately gated external actions.

## Execution loop

1. Select the smallest action mapped to one `DOD-N`.
2. Make the smallest complete change.
3. Validate the actual user-visible or operational behavior with the evidence planned for that criterion.
4. Record new evidence and mark the criterion only when it passes.
5. Update exactly one Next Single Action.
6. Put discoveries outside the active criteria into `BACKLOG.md`.
7. Repeat until complete or genuinely blocked.

Before step 2, state the smallest plausible diff and take the smallest design that passes the Simplicity gate; after step 3, delete any added line, parameter, or branch the evidence never exercised.

Prefer a usable vertical slice before broad optimization or exhaustive audit. A visible blocker outranks adjacent product expansion.

## Stall, budget, and handoff gates

- After two failed approaches, or two meaningful progress updates without new acceptance evidence, stop and re-plan the critical path. Do not broaden the investigation to create activity.
- When a user-specified or observable budget reaches 50%, re-check the shortest path and remove optional work.
- At 80%, freeze scope, validate completed criteria, and write a continuation handoff before further implementation.
- If the budget is not observable, state that and hand off conservatively; never claim an exact remaining percentage.
- A terminal instruction such as “finish” increases persistence, not scope or authorization.

## Evidence proportionality

Use the least evidence that is sufficient for the declared tier and risk. Do not let production-only evidence delay a local or internal-beta criterion that makes no production claim. Never weaken security, compliance, tenant isolation, data-integrity, migration, or readiness gates required by the selected tier.

Do not rerun a broad suite when relevant bytes or external state have not changed. Distinguish static, unit, integration, browser, deployment, and production evidence.

## Incoming requests and delegation

Classify each new request as:

- `REQUIRED`: necessary for a current criterion;
- `BLOCKING DEFECT`: minimum repair, then return to the build;
- `BACKLOG`: useful but not required;
- `REPLACEMENT`: explicitly authorized new priority; preserve and pause the old build;
- `EMERGENCY`: production outage, security, data loss/corruption, legal exposure, or critical revenue failure; record the interrupted work and minimum recovery outcome.

Parallel agents may work only on independent subproblems that each name the `DOD-N` they serve. Do not delegate broad “review everything” work before the critical path is stable.

## Completion gate

Declare `DONE` only when every criterion passes with its planned evidence, the intended user/business outcome works at the declared tier, no critical blocker remains, and required deployment/documentation is complete. Code written, a healthy process, a rendered shell, a local pass, or an agent's confidence is not enough unless that is the declared outcome.

Run `scripts/focus_guard.py --path <root> --completion` before the claim.

## Progress report

Report only:

- requested outcome and delivery tier;
- user-visible state now;
- criteria closed since the last update;
- deferred scope;
- one real blocker, if any; and
- exactly one Next Single Action.

Do not substitute a list of activities for progress.

## Detailed reference

Read [references/FULL_PROTOCOL.md](references/FULL_PROTOCOL.md) when defining a launch tier, splitting a large “do everything” request, resolving a priority conflict, recovering from a stall, handling an emergency override, or making a completion claim.
