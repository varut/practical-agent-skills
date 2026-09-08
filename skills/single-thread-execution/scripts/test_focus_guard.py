#!/usr/bin/env python3
"""Regression tests for the outcome-first project focus guard."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


GUARD = Path(__file__).with_name("focus_guard.py")


def focus_document(
    *,
    dod_count: int = 2,
    status: str = "IN PROGRESS",
    tier: str = "LOCAL",
    prerequisite: str = "- READY — Local test environment is available.",
    next_action: str | None = None,
    checked: bool = False,
    evidence_ids: tuple[int, ...] = (),
    approved_scope_exception: str | None = None,
) -> str:
    checkbox = "x" if checked else " "
    dod = "\n".join(
        f"- [{checkbox}] DOD-{index}: Observable criterion {index} passes."
        for index in range(1, dod_count + 1)
    )
    evidence_plan = "\n".join(
        f"- DOD-{index}: Run focused proof {index}."
        for index in range(1, dod_count + 1)
    )
    current_evidence = (
        "\n".join(f"- DOD-{index}: PASS." for index in evidence_ids)
        if evidence_ids
        else "- None yet."
    )
    if next_action is None:
        if status == "DONE":
            next_action = "DONE: All acceptance criteria have passed."
        elif status == "BLOCKED":
            next_action = "BLOCKER: Obtain the named prerequisite."
        else:
            next_action = "DOD-1: Run the first focused proof."
    exception = ""
    if approved_scope_exception is not None:
        exception = f"\n## Approved Scope Exception\n{approved_scope_exception}\n"

    return f"""# Project Focus

## Exact User Outcome
Make the selected user journey work without unrelated expansion.

## Primary Outcome
The selected user can complete one bounded journey.

## Why This Matters
The broken journey prevents useful operation.

## Success Metric
The journey completes with the expected persisted result.

## Delivery Tier
{tier}

## Authority
- Source: /tmp/example-authority
- Runtime/target: local disposable runtime
- Branch/version/dirty state: test fixture

## Active Build
Repair and verify the selected journey.

## Status
{status}

## Definition of Done
{dod}

## External Prerequisites
{prerequisite}

## Evidence Plan
{evidence_plan}

## Budget and Handoff
- Budget: NOT OBSERVABLE.
- Stop/replan: After two failed approaches.
- Handoff: Before continuation becomes unsafe.

## In Scope
- Work required for the selected journey.

## Out of Scope
- Adjacent redesign and unrelated features.

## Current Evidence
{current_evidence}

## Current Blockers
- None.

## Next Single Action
{next_action}

## Last Updated
2026-08-26
{exception}"""


class FocusGuardTests(unittest.TestCase):
    def run_guard(
        self,
        focus: str | None,
        *extra_args: str,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="outcome-focus-test-") as temp_dir:
            root = Path(temp_dir)
            if focus is not None:
                (root / "PROJECT_FOCUS.md").write_text(focus, encoding="utf-8")
                (root / "BACKLOG.md").write_text("# Backlog\n", encoding="utf-8")
                (root / "DECISIONS.md").write_text("# Decisions\n", encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(GUARD), "--path", str(root), *extra_args],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_valid_active_build_passes(self) -> None:
        result = self.run_guard(focus_document())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("focus check passed", result.stdout)

    def test_invalid_delivery_tier_fails(self) -> None:
        result = self.run_guard(focus_document(tier="SOMEDAY"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Delivery Tier must be exactly one of", result.stderr)

    def test_authority_placeholders_fail(self) -> None:
        invalid = focus_document().replace(
            "- Source: /tmp/example-authority\n- Runtime/target: local disposable runtime",
            "- Source: UNSET\n- Runtime/target: TBD",
        )
        result = self.run_guard(invalid)
        self.assertEqual(result.returncode, 1)
        self.assertIn("non-placeholder '- Source:'", result.stderr)
        self.assertIn("non-placeholder '- Runtime/target:'", result.stderr)

    def test_more_than_seven_criteria_requires_user_exception(self) -> None:
        result = self.run_guard(focus_document(dod_count=8))
        self.assertEqual(result.returncode, 1)
        self.assertIn("maximum is 7", result.stderr)

        approved = self.run_guard(
            focus_document(
                dod_count=8,
                approved_scope_exception="User approved eight criteria on 2026-08-26.",
            )
        )
        self.assertEqual(approved.returncode, 0, approved.stderr)

    def test_next_action_must_map_to_current_criterion(self) -> None:
        result = self.run_guard(
            focus_document(next_action="DOD-9: Explore a useful adjacent idea.")
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("references a DOD ID not in the current build", result.stderr)

    def test_blocked_prerequisite_requires_blocked_state(self) -> None:
        prerequisite = "- BLOCKED — Provider owner must grant access."
        result = self.run_guard(
            focus_document(status="IN PROGRESS", prerequisite=prerequisite)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires Status BLOCKED", result.stderr)

        aligned = self.run_guard(
            focus_document(status="BLOCKED", prerequisite=prerequisite)
        )
        self.assertEqual(aligned.returncode, 0, aligned.stderr)

    def test_done_requires_checked_criteria_and_evidence_for_each(self) -> None:
        incomplete = self.run_guard(
            focus_document(
                status="DONE",
                checked=True,
                evidence_ids=(1,),
            ),
            "--completion",
        )
        self.assertEqual(incomplete.returncode, 1)
        self.assertIn(
            "Current Evidence is missing non-placeholder completion evidence for DOD-2",
            incomplete.stderr,
        )

        complete = self.run_guard(
            focus_document(
                status="DONE",
                checked=True,
                evidence_ids=(1, 2),
            ),
            "--completion",
        )
        self.assertEqual(complete.returncode, 0, complete.stderr)

    def test_done_rejects_placeholder_evidence(self) -> None:
        invalid = focus_document(
            status="DONE",
            checked=True,
            evidence_ids=(1, 2),
        ).replace("- DOD-1: PASS.", "- DOD-1: UNSET").replace(
            "- DOD-2: PASS.", "- DOD-2: TBD"
        )
        result = self.run_guard(invalid, "--completion")
        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "Current Evidence is missing non-placeholder completion evidence for DOD-1",
            result.stderr,
        )
        self.assertIn(
            "Current Evidence is missing non-placeholder completion evidence for DOD-2",
            result.stderr,
        )

    def test_done_accepts_markdown_link_evidence(self) -> None:
        linked = focus_document(
            status="DONE",
            checked=True,
            evidence_ids=(1, 2),
        ).replace(
            "- DOD-1: PASS.",
            "- DOD-1: [browser proof](/tmp/browser-proof.md)",
        )
        result = self.run_guard(linked, "--completion")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_read_only_diagnostic_reports_but_does_not_block(self) -> None:
        result = self.run_guard(None, "--diagnostic")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("diagnostic found issues", result.stdout)
        self.assertIn("Missing required file", result.stdout)


if __name__ == "__main__":
    unittest.main()
