# Careless User E2E

**The tests passed. Then somebody clicked twice.**

![A distracted tester presses an oversized button and creates a shower of duplicate receipts.](assets/hero.png)

We built this skill because a feature can satisfy its tests and still leave a distracted person stuck. A stale tab, a similar-looking name, or an impatient second click can expose a path nobody thought to test. The most useful part is often what happens when the person tries to fix the mistake.

## What it does

The agent reads the intended workflow and permissions first, then writes down what should succeed, what must be refused, and what must remain unchanged. It uses requirements and user intent as the reference; a passing test or the current UI is not enough to establish that a restriction is correct.

It drives the actual interface through the usual order, legitimate alternative orders, mistakes, and attempts to bypass required steps or permissions. It repairs mistakes and checks saved records and their dependents after reloading. Targeted cases come before bounded, recorded random exploration.

This complements unit and API tests. Browser automation counts when it operates the real controls: a keyboard success does not prove a mouse click works, and an API move does not prove drag and drop works. Confirmed defects become permanent regression tests; reports distinguish passed, failed, partial, blocked, and untested journeys.

## Learn the flow, then challenge it

For a work board, distinguish the preferred setup order from actual constraints:

| Intended behavior | Try to break the assumption | Verify |
|---|---|---|
| A task can be organized later | Create task → create board → move existing task | Same task and children, correct board, preserved history |
| A board offers direct creation | Add through its column instead of global create | Correct destination persists after reload |
| Permissions apply when saving | Open a form, revoke test access, submit the stale form | Refused write with no protected changes |
| Cancel means abandon changes | Pick a different board, cancel, reopen | Original destination remains |

These are examples, not rules imposed on every product. The test contract states the actual product requirements. Missing controls and confusing recovery are findings even when the server supports the operation.

## A small example

The job is **“Create a draft order, notice the quantity is wrong, and correct it.”**

1. Enter 20 where you meant 2. Read the review screen and correct it.
2. Save, then read the order back. Confirm the quantity and total both changed.
3. Update the wrong similar-looking item, notice the mistake, and repair both items.
4. Attempt to delete a protected record in a test fixture. Confirm the UI refuses it and explains what to do instead.

The interesting question is whether the person can recover without leaving a second problem behind.

## Use it

Install the `careless-user-e2e` folder using the [collection instructions](../../README.md#install-in-codex), then ask:

```text
Use careless-user-e2e on the draft-order journey in this test environment.
Read its intended workflow and role rules first. Test the usual order,
valid alternative orders, forbidden shortcuts, and recovery. Run a bounded
random walk after targeted cases and check saved state after mutations.
Report exact paths and input methods, evidence, and remaining coverage gaps.
```

It needs tools that can operate the actual interface, authorized test access, and suitable test records for the lifecycle. Production actions remain within the user's authorization; the skill does not grant permission to attack unrelated systems, send messages, incur charges, or weaken controls. It does not supply browser automation. Use it after building a user-facing flow; skip pure library or algorithm work.

[Read the full skill](SKILL.md) · [Back to the collection](../../README.md)
