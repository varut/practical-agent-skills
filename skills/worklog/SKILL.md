---
name: worklog
description: Keep a running work journal in the repo (WORKLOG.md) and mirror it to the deploy destination when one exists, so the next session knows what was learned, what the plan is, what happened, what is next, and what went wrong. Apply automatically during any non-trivial build, debug, migration, or ops task - at session start to read context, and at each meaningful checkpoint to append. Also apply when resuming interrupted work, handing off between Claude and Codex, or when a session is about to end or be compacted. Skip for one-line edits and isolated factual questions.
---

# Worklog — continuity across sessions, agents, and machines

## Why

Work can span agents, sessions, machines, and multiple checkouts. Context does
not reliably travel with it. Anything not written down may be relearned at full
cost, usually by repeating the mistake. This skill makes the record a by-product
of the work.

This skill uses the planning-file convention provided by `single-thread-execution`.
Install that companion skill for the full workflow; it defines `PROJECT_FOCUS.md`,
`DECISIONS.md`, and `BACKLOG.md`.

## The one file

`WORKLOG.md` at the repo root, beside `PROJECT_FOCUS.md` / `BACKLOG.md` / `DECISIONS.md`.
Create it from `templates/WORKLOG.md` if absent. **Newest entry directly under the
header**, so resuming means reading the top, not scrolling.

Do not invent a second journal. Projects with an existing log
(for example, `docs/implementation-log.md`) keep using it — apply this
entry format there and skip `WORKLOG.md` entirely. One journal per repo, never two.

## Ownership — do not duplicate state

| Question | Lives in | Worklog carries |
|---|---|---|
| What is the plan? | `PROJECT_FOCUS.md` (Active Build, DOD-N) | one-line restatement in the file header |
| What next? | `PROJECT_FOCUS.md` Next Single Action | same sentence, copied |
| Why this way? | `DECISIONS.md` | pointer only |
| Deferred work | `BACKLOG.md` | pointer only |
| What happened, what was learned | **`WORKLOG.md`** | the entry itself |

If a worklog line and `PROJECT_FOCUS.md` disagree, `PROJECT_FOCUS.md` wins — fix the worklog.

## When to append

Append at a checkpoint, never per tool call. A session usually produces 1–4 entries.

1. **Session start:** read the top entry first. Do not append yet.
2. A `DOD-N` closes, or a real blocker clears.
3. **Expected ≠ actual** — the highest-value trigger. Write it while the surprise is fresh.
4. Before a risky or irreversible action, and again after, with the outcome.
5. The user corrects you, or a decision changes course.
6. Session end, handoff to the other agent, or context about to be compacted.

## Entry format

```markdown
## 2026-09-02 21:40 +07 · <slice or DOD-N> · <Claude|Codex> · mirror: synced|pending|n/a
**Done:** what changed, with the evidence that proves it (command output, count, URL).
**Learned:** expected X, got Y → root cause → the lesson. Seen before: yes/no.
**Went wrong:** the failure and what it cost. Write "nothing" only if true.
**Next:** one action, identical to PROJECT_FOCUS.md Next Single Action.
```

Rules that keep it worth reading:

- **Evidence, not adjectives.** "58,513 files, matches manifest" beats "transfer went well".
- **Learned is for transferable lessons**, not narration. If it would not change a future
  decision, leave it out. Reserve process changes for a lesson **seen twice** — a single
  observation is an anecdote. Mark the first occurrence `Seen before: no` and leave the
  process alone.
- **Went wrong is mandatory and specific.** Dead ends, wrong guesses, and wasted effort are
  the most expensive things to rediscover. Name yours plainly.
- Six lines per field, maximum. Long lists belong in the artifact they describe.
- **Never record secrets** — no tokens, keys, connection strings, or credentialed URLs.
  Service names only. This file may be mirrored to the declared destination.

## Mirroring to the destination

Use the authoritative repository and mirror destination recorded for the current
project. Do not assume a local or remote checkout is authoritative. After
appending, put the same entry on the declared destination when one exists.

- **Git-backed project:** include `WORKLOG.md` in the next commit. Nothing extra.
- **Remote workspace over SSH:** use the project's existing authorized connection to copy the entry. Substitute the actual destination in `scp WORKLOG.md <user>@<host>:<project-path>/WORKLOG.md`; do not invent hosts or credentials.
- **Neither available:** mark the entry `mirror: n/a` and say so in the entry.

**Never overwrite blind.** Read the destination's top entry first. If it has entries you
do not, the other agent or machine wrote them — merge both histories in time order, then
write back. Appending is safe; clobbering loses the other side's work. If mirroring fails,
mark the entry `mirror: pending` and say so in your reply rather than leaving it silent.

## Reading it back

On resume, read the top entry and the file header. That is the whole handoff: the plan,
the next action, and the last surprise. Only read further back when the current work
touches something older, or when a lesson says `Seen before: yes` and you need the first
occurrence.
