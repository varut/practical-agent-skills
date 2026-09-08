---
name: claude-codex-pairing
description: "Coordinate a bounded second opinion between Claude Code and Codex for non-trivial coding, debugging, implementation research, or code review. Use automatically when an independent peer review can close a current acceptance criterion or remove a recorded blocker. The current session remains the sole writer; skip trivial edits and factual questions."
---

# Claude-Codex Pairing

Use the other coding agent as a bounded reviewer, not as a second concurrent owner.

## Routing Gate

Delegate only when all are true:

- The task is non-trivial coding, debugging, implementation research, or review.
- A concrete artifact, diff, failure, or narrow question already exists.
- The peer result closes a current acceptance criterion or removes a recorded blocker.
- The payload can exclude secrets, credentials, customer records, health/payment data, and private conversations.

Do not delegate tiny edits, isolated facts, open-ended brainstorming, or work that would only repeat the owner's checks.

## Authority Contract

1. The agent in the user's active session is the owner.
2. Only the owner may edit source, install dependencies, run migrations, deploy, or make external changes.
3. The peer is read-only and returns findings with exact evidence. It may not call Claude, Codex, a subagent, or another external model.
4. Run at most one peer call for the same question. If it fails or returns no new evidence, report that result; do not recurse.
5. The owner verifies every adopted finding locally before changing code.

Prefix every peer request with this sentinel:

```text
PAIRING_SENTINEL=peer-read-only-v1
You are the read-only peer. Do not edit files, install anything, invoke another model or agent, or broaden scope. Return concise evidence tied to the stated acceptance criterion.
```

## Claude Code Owner to Codex Peer

When a concrete Git working-tree diff exists, invoke the installed first-party `codex:adversarial-review` command once with `--wait --scope working-tree`. Put the pairing sentinel and the bounded acceptance criterion in its focus text. The command is review-only and its foreground companion returns structured Codex output. Include only:

- the single acceptance criterion;
- the bounded question;
- the minimum relevant paths or diff;
- commands/evidence already observed;
- the pairing sentinel.

Claude remains responsible for edits and verification. If there is no reviewable Git diff, do not auto-delegate; keep the work single-agent unless the user explicitly asks for an interactive rescue.

Never invoke a second command to retrieve a missing result. If the foreground review returns no verdict payload, report the peer check as failed and stop. Do not use the proactive `codex:codex-rescue` Agent route for this default one-shot pairing path.

## Codex Owner to Claude Code Peer

First run `claude auth status --json`. If Claude is signed out, mark this peer check blocked and give the user the exact action `claude auth login`; do not substitute a second Codex agent.

When authenticated, make one non-persistent safe-mode call from the trusted project directory:

```bash
claude -p --safe-mode --no-session-persistence --permission-mode dontAsk --tools "Read,Glob,Grep" --output-format json "<sentinel plus bounded review request>"
```

`--safe-mode` disables user plugins, hooks, MCP servers, skills, and instruction files inside the peer process, preventing a callback loop. The explicit prompt supplies all required scope. Codex remains responsible for edits and verification.

## Result Gate

Accept a peer result only when it:

- directly addresses the named acceptance criterion;
- cites a path, line, command result, or reproducible observation;
- stays within the bounded question; and
- contains no claim that the peer edited or deployed anything.

Record the peer result separately from the owner's own verification. A peer opinion is not test evidence.
