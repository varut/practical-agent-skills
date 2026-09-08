# Full Outcome-First Execution Protocol

## Governing principle

At all times, a project has one preserved Exact User Outcome, one Primary Outcome, one Delivery Tier, one authority, one bounded Active Build, sequential `DOD-N` criteria, and one mapped Next Single Action.

The protocol optimizes completed outcomes rather than idea count, file count, agent count, research volume, test volume, or visible busyness.

## Exact outcome and Primary Outcome

Preserve what the user asked for before translating it. The Primary Outcome describes the observable result that the current program is trying to create. It may be broader than one build; the Active Build may not.

A large request such as “do everything” is a program objective. Preserve every requested item in the roadmap/backlog, select the highest-value complete vertical slice, and state what is deferred. Do not silently drop scope and do not run the entire roadmap concurrently.

## Delivery tiers

Use exactly one tier for the Active Build:

- `NOT APPLICABLE`: no runtime or release claim, such as a bounded document or analysis artifact.
- `LOCAL`: works in the authoritative local environment only.
- `DEVELOPMENT PREVIEW`: works in the named development host/preview with development data and no production claim.
- `INTERNAL BETA`: authorized internal users can complete the selected journey with declared limitations.
- `PRODUCTION BETA`: selected real users/data are supported by production security, durability, monitoring, and rollback controls.
- `PRODUCTION`: the declared production workload and operational contract are supported.
- `GENERAL AVAILABILITY`: the full published support, reliability, compliance, and operating contract is satisfied.

A lower-tier result must not be described as a higher tier. Production-only gates must not delay a lower-tier acceptance criterion unless they protect security, tenant isolation, compliance, or data integrity required even at that tier.

## Authority

Bind both source and target:

- canonical repository/workspace and relevant branch/version/dirty state;
- runtime or output target;
- environment and data boundary;
- current externally observable state.

Recovery copies, staging candidates, generated artifacts, previews, deployment projects, and production are distinct. Work on the wrong authority is not progress.

## Active Build sizing

The Active Build is the smallest meaningful vertical slice that can be implemented, validated, and closed in one coherent pass.

Split it when it spans:

- more than one independent user journey;
- more than one delivery tier;
- unrelated product and infrastructure outcomes;
- independently releasable features;
- several external owners or approvals that can block independently; or
- more than seven binary acceptance criteria without explicit user approval.

Supporting work is allowed only when it closes a current criterion or removes a recorded blocker.

## Definition of Done and evidence

Label acceptance criteria sequentially as `DOD-1`, `DOD-2`, and so on. Each criterion must describe observable behavior, not activity.

Map every criterion to minimum sufficient evidence before implementation. Evidence may include a focused automated test, integration result, browser journey, query, screenshot, deployment probe, or operator confirmation. Choose evidence for the declared tier and risk.

Do not repeatedly run a broad suite merely because it exists. Run broader validation when changed bytes or external state justify it, or when a mandatory tier gate requires it.

## External-prerequisite first pass

During the first meaningful pass, enumerate:

- human identity or consent;
- credentials and access;
- paid resources or billing decisions;
- external providers;
- platform/deployment topology;
- security, legal, or business approval;
- data and migration authority; and
- independent verification or signing custody.

Mark each `READY`, `BLOCKED`, or `NOT-REQUIRED`. If a required prerequisite is blocked, Status is `BLOCKED`, the Next Single Action begins `BLOCKER:`, and adjacent work stops after safe preparation directly serving that blocker.

“Full access,” “finish,” or “do it all” does not authorize identity impersonation, credential invention, purchases, public-access changes, destructive operations, or other separately gated actions.

## Scope admission

Before any action:

1. Name the current `DOD-N` it advances.
2. Otherwise name the recorded blocker it removes.
3. Confirm it is the smallest safe action.

If it cannot pass this test, backlog it. A discovery is information, not permission to implement.

## Request classification

Classify every incoming request:

- `REQUIRED`: necessary for a current criterion.
- `BLOCKING DEFECT`: prevents safe completion; repair the minimum cause.
- `BACKLOG`: valuable but outside the current DOD.
- `REPLACEMENT`: the user explicitly replaces the priority; preserve and pause the old build.
- `EMERGENCY`: production outage, security vulnerability, data corruption/loss, legal exposure, or critical revenue failure; record the interrupted state and minimum recovery result.

An additive “also” request normally enters the backlog. An explicit “stop X and replace it with Y” changes the Active Build.

## Stall and budget control

A failed attempt is useful only when it narrows the next decision.

- After two failed approaches, stop and re-plan.
- After two meaningful updates without new DOD evidence, stop and re-plan.
- When an explicit or observable budget reaches 50%, re-evaluate the shortest path and remove optional work.
- At 80%, freeze scope, validate completed criteria, and produce a durable handoff.
- When budget is not observable, say so and hand off conservatively. Never invent a percentage.

Re-planning means identifying the exact failed assumption, current evidence, shortest remaining path, and one next action. It does not mean opening a broader audit.

## Research, refactoring, and UX work

Research only to answer a decision required by a current criterion. State the decision, missing information, sufficient evidence, and stopping condition before research.

Refactor only when existing structure blocks safe completion, testing, security, or data integrity for the Active Build.

UX review, competitor analysis, optimization, and hardening are backlog items unless a current criterion requires them. A visible broken journey is normally repaired before adjacent polish.

## Delegation

Every delegated task must name the `DOD-N` it serves, its read/write boundary, expected evidence, and stopping condition. Parallel agents may solve independent subproblems inside one build; they may not create competing builds or broad unbounded audits.

## Read-only work

Reviews, diagnostics, explanations, and status reports do not authorize project writes. Read existing state if present, hold any missing outcome contract in memory, and use the guard's `--diagnostic` mode. Report schema gaps without silently migrating files.

## Distribution and precedence

The canonical personal skill is installed under `$HOME/.agents/skills`, while `$HOME/.codex/AGENTS.md` requires Codex to apply it even when the user does not name it. This is a layered safeguard: implicit skill selection remains model-driven, while global guidance makes the rule explicit for every Codex run.

Codex reads global guidance at run start and then layers project instructions from broad to specific. A deeper project instruction can therefore refine or conflict with the global rule. Resolve explicit conflicts rather than claiming the guard is absolute, and start a new run after modifying global guidance.

Codex global guidance does not configure Claude Code, Replit Agent, or other agents. To share this protocol across agent products, place an equivalent block in that tool's supported global instruction file or in the repository instructions each tool reads.

## Legacy project migration

When authorized change/build work enters a project with an older focus schema:

1. Preserve existing outcome, evidence, blockers, and dirty work.
2. Add the missing outcome, tier, authority, prerequisite, evidence-plan, budget/handoff, and DOD mapping fields.
3. Split an oversized Active Build rather than forcing it into the new template.
4. Run the strict guard before substantive implementation.

Do not mass-edit every repository in advance. Upgrade each existing project when it next receives authorized non-trivial work.

## Completion

Completion requires the actual outcome to work at the declared tier, all criteria checked with mapped evidence, no critical unresolved blocker, and required deployment/documentation complete.

A plan, code diff, healthy process, rendered shell, local test, partial role, preview, or agent confidence cannot support a broader claim than the declared criterion and tier.

## Permanent rule

Finish the requested vertical slice before expanding. Surface external blockers before investing deeply. Validate proportionally. Preserve future ideas without obeying them.
