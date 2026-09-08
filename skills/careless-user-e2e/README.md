# Careless User E2E

**The tests passed. Then somebody clicked twice.**

![A distracted tester presses an oversized button and creates a shower of duplicate receipts.](assets/hero.png)

We built this skill because a feature can satisfy its tests and still leave a distracted person stuck. A stale tab, a similar-looking name, or an impatient second click can expose a path nobody thought to test. The most useful part is often what happens when the person tries to fix the mistake.

## What it does

The agent names a journey in the user's words, drives the real interface, makes a plausible mistake at every step, and corrects it. It checks both the correction and anything that depended on the original value. For a CRUD flow, it follows creation, read-back, update, and a deletion that the product should refuse.

This is a companion to automated tests. A confirmed defect becomes a permanent regression test; the report keeps the journeys actually driven separate from automated coverage.

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
Make realistic mistakes, repair them, and check the dependent totals.
Report exactly what you drove and anything you could not reach.
```

It needs tools that can operate the actual interface, authorized test access, and suitable test records for the lifecycle. The skill does not supply browser automation. Use it after building a user-facing flow; skip pure library or algorithm work.

[Read the full skill](SKILL.md) · [Back to the collection](../../README.md)
