---
name: careless-user-e2e
description: Test a feature the way a real, careless user meets it — driving the actual UI, making a plausible mistake at every step, then correcting it. Use after building any user-facing flow, before calling it done, and whenever a green test suite has not been backed by someone actually clicking the thing. Covers CRUD lifecycles where each step is done wrong first and then repaired. Do not use for pure library or algorithm work with no user-facing surface.
metadata:
  short-description: Find what green suites miss by using the product badly
---

# Careless-User End-to-End Testing

## Purpose

Find the defects a passing test suite cannot see, by using the product the way
the person who has to use it will: in a hurry, with a stale tab open, typing the
wrong thing into the right box, and needing to undo it afterwards.

The premise is not that tests are bad. It is that **a suite tests what the author
already understood.** Every defect this skill is for was sitting behind a green
build.

## When to apply

Apply after building any user-facing flow and before reporting it finished.
Apply again whenever you are about to say "tested" and the evidence is only
automated. Skip it for library internals, pure algorithms, and anything with no
human surface.

## The method

### 1. Name the real journeys first, in the user's words

Before touching anything, write down what the person is actually trying to do,
in their vocabulary, not the system's. "Record today's order for an agent who
paid half up front" — not "POST /orders with a partial settlement". If you
cannot state the journey in the user's words, you do not yet know what to test.

Ask what the **job** is. A wholesale clerk keys twelve agents' orders in a row;
a stockroom worker counts boxes onto a truck; an owner fixes a number they know
is wrong. Each has a different failure appetite and a different tolerance for
being blocked.

### 2. Make a plausible mistake at every step

Not random fuzzing. The mistakes a competent, distracted person actually makes:

- Typing a value into the adjacent field (quantity into price, satang into a
  baht box)
- Leaving a tab open overnight so the date is yesterday
- Double-tapping a save button on a slow connection
- Picking the wrong record from a list of similar names, and noticing at review
- Filling half a form, changing their mind, and switching a mode that hides
  fields they already filled
- Coming back to a screen whose underlying record someone else already changed
- Entering the same thing twice because the first attempt looked like it failed

For every one, ask three questions:
1. Is it **refused**, or silently accepted?
2. Is the refusal in **the user's language**, naming what to fix?
3. Can they **recover** without help, or is the record now permanently wrong?

### 3. Then correct the mistake, and check the correction

Half the value is in step two, all the danger is in step three. Drive the repair:
edit it, reverse it, supersede it. Then verify **the correction did not create a
second problem** — money counted twice, a payment stranded on a superseded
record, an agent dropped off a list because their record was fixed.

Ask: *what else pointed at the thing I just corrected?*

### 4. Do the whole CRUD lifecycle wrong, in order

Create it wrong → fix it. Read it back and confirm the fix is visible. Update it
wrong → fix that. Delete something that must not be deletable and confirm the
refusal explains why. A lifecycle where only the happy path was walked is
untested.

### 5. Drive the real interface

Click the product. Not the API. An API test cannot see a control that never
rendered, a gate stricter than the server's, a toast covering the save button,
or a confirmation that says the wrong thing. If automation cannot drive a
control reliably, say so plainly and do not report the journey as passed.

## What this reliably catches

Recorded from real sessions, as the shapes to look for:

- **A UI gate stricter than the server**: the feature exists, is authorised, and
  never renders — because the client required a stronger condition than the API
  does. A journey that runs in the permissive state will never see it.
- **Silent magnitude errors**: a field whose stored unit differs from its label,
  so a plausible keystroke multiplies a figure by 100 and nothing objects.
- **The right message with the wrong remedy**: an error whose headline is a
  guess and whose real reason is demoted to a subtitle, sending the user to
  reload forever when reloading cannot help.
- **Silent partial writes**: a form that filters out the entries it could not
  parse, submits the rest, and reports success.
- **Failure rendered as good news**: a failed load with no error state, showing
  an empty list that means "we do not know" as though it meant "nothing owed".
- **Asymmetric repairs**: correcting a record carries one dependent thing
  forward and drops another. If you fix one direction, immediately check the
  mirror.
- **Instructions the product cannot carry out**: a message telling the user to
  do something for which no control exists.

## Reporting

State which journeys you drove and what happened, separately from what
automation covered. If you could not drive something, say that rather than
implying coverage. A defect found this way is worth writing down with the
mistake that revealed it — the mistake is the reproduction.

Turn each confirmed defect into a permanent test, so the next regression fails
the build rather than waiting for the next careless user.
