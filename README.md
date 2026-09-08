# Practical Agent Skills

**Small habits for agents with very large ambitions.**

We built these four skills around the parts of AI-assisted development that kept needing a human reminder: try the awkward path, finish the requested thing, write down what happened, and keep one person at the keyboard.

Each skill is a set of instructions an agent can read and follow. They add working habits to the tools you already use. Start with the one that solves a problem you recognize.

| Skill | The habit | Start here |
|---|---|---|
| **Careless User E2E** | Make a believable mistake in the real UI, repair it, and check the repair. | [Guide](skills/careless-user-e2e/) · [Instructions](skills/careless-user-e2e/SKILL.md) |
| **Single-Thread Execution** | Bind one outcome, one authority, and one next action. Finish the smallest sufficient change. | [Guide](skills/single-thread-execution/) · [Instructions](skills/single-thread-execution/SKILL.md) |
| **Worklog** | Leave the next session evidence, lessons, and an exact next step. | [Guide](skills/worklog/) · [Instructions](skills/worklog/SKILL.md) |
| **Claude–Codex Pairing** | Ask for one bounded second opinion while keeping a single writer. | [Guide](skills/claude-codex-pairing/) · [Instructions](skills/claude-codex-pairing/SKILL.md) |

## The tests passed. Then somebody clicked twice.

[![A distracted tester launches duplicate receipts while a tiny robot raises an eyebrow.](skills/careless-user-e2e/assets/hero.png)](skills/careless-user-e2e/)

**Careless User E2E** treats recovery as part of the feature. Enter the wrong value, choose the similar-looking record, click again because nothing seemed to happen. Then fix it and see what else changed. [Read the guide →](skills/careless-user-e2e/)

## Your tiny fix has applied for planning permission.

[![A focused robot delivers one small parcel beside a mountain of unfinished ideas.](skills/single-thread-execution/assets/hero.png)](skills/single-thread-execution/)

**Single-Thread Execution** gives an ambitious agent a stopping point. Every action has to close a stated acceptance criterion or remove a real blocker. Extra ideas go in the backlog. [Read the guide →](skills/single-thread-execution/)

## Yesterday you solved this. Yesterday is unavailable.

[![A sleepy developer passes a notebook to an equally sleepy future self.](skills/worklog/assets/hero.png)](skills/worklog/)

**Worklog** makes continuity a habit: what happened, what surprised us, what went wrong, and exactly what comes next. A short useful entry beats another hour of archaeological research. [Read the guide →](skills/worklog/)

## Two brains. One keyboard.

[![One robot types while a second inspects a tiny detail with an enormous magnifying glass.](skills/claude-codex-pairing/assets/hero.png)](skills/claude-codex-pairing/)

**Claude–Codex Pairing** keeps collaboration bounded. One agent owns the work; the peer reviews a specific question, returns evidence, and keeps its hands off the files. [Read the guide →](skills/claude-codex-pairing/)

## Install in Codex

Ask Codex to use its skill installer with the repository path for the skill you want:

```text
Use skill-installer to install careless-user-e2e from
https://github.com/varut/practical-agent-skills/tree/main/skills/careless-user-e2e
```

Replace the final folder name with another skill from the table. Install `single-thread-execution` alongside `worklog`; it defines the planning files that Worklog references.

For a manual installation, download this repository with **Code → Download ZIP**, unzip it, and copy the chosen folder from `skills/` into `$HOME/.agents/skills/`. Keep the whole folder, including its scripts, templates, and references. Review an existing installation before replacing it.

The resulting layout should include, for example:

```text
$HOME/.agents/skills/careless-user-e2e/SKILL.md
```

Codex discovers skills automatically. Restart it if a newly installed skill does not appear. See the [official skills guide](https://learn.chatgpt.com/docs/build-skills) for supported locations and invocation.

Other agents can use the instructions where they support the Agent Skills format; use that agent's installation documentation. Automatic triggering and tool availability vary by host. Installing a skill does not install a browser driver, sign in to another agent, or grant access to a service.

## Try one

```text
Use careless-user-e2e to test creating and correcting a draft order
in our test environment. Report the mistakes and repairs you actually drove.
```

```text
Use single-thread-execution for this change. Define done first,
then make the smallest change that meets it.
```

The guides contain more examples and the prerequisites for each skill. Start with a bounded task and read the resulting evidence; these are behavioral instructions, so execution still depends on the agent and its tools.

## About the collection

These are our working methods, shared as portable skills with generic examples. Third-party skills installed in our environment are excluded from this collection. The four illustrations were generated specifically for this release; the [artwork notes](ARTWORK.md) include the prompts.
