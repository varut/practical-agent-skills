# Worklog

**Yesterday you solved this. Yesterday is unavailable.**

![A sleepy developer hands a notebook to their relieved future self.](assets/hero.png)

We built this skill because context disappears between sessions, agents, and machines. The expensive part is losing the reason something failed, then paying to discover it again. Worklog leaves a short record while the evidence is still fresh.

## What it does

The agent reads the latest entry before editing and writes at meaningful checkpoints. Each entry has four fields:

| Field | What belongs there |
|---|---|
| **Done** | What changed and the evidence for it |
| **Learned** | Expected versus actual, the cause, and whether this has happened before |
| **Went wrong** | The specific failure, wrong guess, or wasted effort |
| **Next** | The exact next action from the project focus file |

The newest entry goes at the top. If a project already has a journal, the agent uses it. If there is a declared mirror destination, it reads that destination before merging and copying entries.

## A small example

```markdown
## 2026-09-08 · DOD-2 · Agent · mirror: n/a
**Done:** Corrected the filter and verified the range after refresh in the UI.
**Learned:** Expected the URL to preserve the date; the reset handler cleared it.
The reset path also needs to preserve unrelated filters. Seen before: no.
**Went wrong:** The first fix covered initial load but missed refresh.
**Next:** DOD-3: Verify the empty-result message in the UI.
```

The journal records events and lessons. The plan, rationale, and deferred work stay in their own files, so the same state does not drift across several documents.

## Use it

Install `worklog` and its companion `single-thread-execution` using the [collection instructions](../../README.md#install-in-codex). Keep Worklog's `templates/` directory.

```text
Use worklog for this task. Read the latest entry before editing,
and leave the next session the evidence, surprises, and exact next action.
```

It needs file access to the project journal. Mirroring also needs an existing authorized route to the declared destination. No remote host is assumed, and secrets do not belong in the journal.

Use it for substantial builds, debugging, migrations, operations, and handoffs. A one-line edit rarely needs a diary entry.

[Read the full skill](SKILL.md) · [Entry template](templates/WORKLOG.md) · [Back to the collection](../../README.md)
