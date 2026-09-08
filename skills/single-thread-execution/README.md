# Single-Thread Execution

**Your tiny fix has applied for planning permission.**

![A determined robot carries one parcel past a huge pile of tempting unfinished projects.](assets/hero.png)

We built this skill to keep an agent's effort attached to the result we asked for. A small change can accumulate research, new abstractions, extra options, and another round of testing long after the required behavior is clear. This skill makes scope and completion explicit.

## What it does

Before substantive work, the agent binds an authoritative checkout and target, declares the delivery tier, and defines a small set of observable acceptance criteria. It keeps one active build and one next action. A new action must satisfy a criterion or remove a recorded blocker; other ideas go into the backlog.

The simplicity rules favor the smallest verified change. The stall rules require a new plan after repeated failed approaches. The completion rules distinguish a local pass from an actual published result.

The name describes ownership of the outcome. Independent, bounded peer work is still allowed when it serves a stated criterion.

## The files it maintains

| File | Purpose |
|---|---|
| `PROJECT_FOCUS.md` | Requested outcome, acceptance criteria, evidence, and next action |
| `BACKLOG.md` | Useful ideas outside the current build |
| `DECISIONS.md` | Reasons for choices and explicit scope exceptions |

For a read-only task, the agent keeps the contract in memory and leaves these files unchanged.

## Use it

Install the entire `single-thread-execution` folder using the [collection instructions](../../README.md#install-in-codex), then ask:

```text
Use single-thread-execution to fix the date filter.
Done means the selected date range is applied, survives refresh,
and works in the existing UI. Keep other improvements in the backlog.
```

The included guard requires Python 3. It checks the structure and consistency of the project contract. For the manual installation above, run:

```bash
python3 "$HOME/.agents/skills/single-thread-execution/scripts/focus_guard.py" --path .
```

If you used `skill-installer`, use the destination it reported instead; its default is `$CODEX_HOME/skills` (normally `$HOME/.codex/skills`).

The guard does not prove the product works; the acceptance criteria still need their own evidence. The folder includes the guard's existing tests, templates, and full protocol.

For default use across projects, review the included [instruction block](templates/AGENTS.md.block) and add it to the instruction file your agent reads. Installation alone does not configure every agent or guarantee invocation.

[Read the full skill](SKILL.md) · [Full protocol](references/FULL_PROTOCOL.md) · [Back to the collection](../../README.md)
