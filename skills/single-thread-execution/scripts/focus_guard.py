#!/usr/bin/env python3
"""Validate outcome-first, single-thread project state.

Usage:
  focus_guard.py [--path PROJECT_ROOT] [--completion] [--diagnostic]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = ("PROJECT_FOCUS.md", "BACKLOG.md", "DECISIONS.md")
REQUIRED_SECTIONS = (
    "Exact User Outcome",
    "Primary Outcome",
    "Why This Matters",
    "Success Metric",
    "Delivery Tier",
    "Authority",
    "Active Build",
    "Status",
    "Definition of Done",
    "External Prerequisites",
    "Evidence Plan",
    "Budget and Handoff",
    "In Scope",
    "Out of Scope",
    "Current Evidence",
    "Current Blockers",
    "Next Single Action",
    "Last Updated",
)
ALLOWED_STATUSES = {
    "NOT STARTED",
    "IN PROGRESS",
    "BLOCKED",
    "VALIDATING",
    "DONE",
    "PAUSED",
    "ABANDONED",
}
ALLOWED_TIERS = {
    "NOT APPLICABLE",
    "LOCAL",
    "DEVELOPMENT PREVIEW",
    "INTERNAL BETA",
    "PRODUCTION BETA",
    "PRODUCTION",
    "GENERAL AVAILABILITY",
}
PLACEHOLDERS = {"", "UNSET", "TBD", "TODO"}
MAX_DOD_ITEMS = 7
DOD_LINE = re.compile(r"(?m)^- \[([ xX])\] (DOD-(\d+)): (.+)$")


def section(text: str, heading: str) -> str:
    pattern = rf"(?ms)^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def meaningful_lines(value: str) -> list[str]:
    return [
        line.strip()
        for line in value.splitlines()
        if line.strip() and not line.lstrip().startswith("<!--")
    ]


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped.upper() in PLACEHOLDERS or bool(
        re.fullmatch(r"\[[^\]\n]+\]", stripped)
    )


def labeled_value(value: str, label: str) -> str:
    """Return a Markdown list label's value, or an empty string when absent."""
    match = re.search(rf"(?m)^- {re.escape(label)}:\s*(.*?)\s*$", value)
    return match.group(1).strip() if match else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default=".", help="Project or repository root")
    parser.add_argument("--completion", action="store_true", help="Apply completion checks")
    parser.add_argument(
        "--diagnostic",
        action="store_true",
        help="Report contract gaps but return success; use only for read-only work",
    )
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    errors: list[str] = []

    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    focus_path = root / "PROJECT_FOCUS.md"
    if focus_path.is_file():
        text = focus_path.read_text(encoding="utf-8")

        for heading in REQUIRED_SECTIONS:
            if not re.search(rf"(?m)^## {re.escape(heading)}\s*$", text):
                errors.append(f"PROJECT_FOCUS.md is missing section: {heading}")

        for heading in (
            "Exact User Outcome",
            "Primary Outcome",
            "Why This Matters",
            "Success Metric",
            "Authority",
            "Active Build",
            "External Prerequisites",
            "Evidence Plan",
            "Budget and Handoff",
            "Next Single Action",
            "Last Updated",
        ):
            value = section(text, heading)
            if is_placeholder(value):
                errors.append(f"{heading} is empty or still a placeholder")

        tier_lines = meaningful_lines(section(text, "Delivery Tier"))
        tier = tier_lines[0].upper() if len(tier_lines) == 1 else ""
        if tier not in ALLOWED_TIERS:
            errors.append(
                "Delivery Tier must be exactly one of: "
                + ", ".join(sorted(ALLOWED_TIERS))
            )

        status_lines = meaningful_lines(section(text, "Status"))
        status = status_lines[0] if len(status_lines) == 1 else ""
        if status not in ALLOWED_STATUSES:
            errors.append(f"Invalid Status: {status!r}")

        authority = section(text, "Authority")
        source_value = labeled_value(authority, "Source")
        runtime_value = labeled_value(authority, "Runtime/target")
        if is_placeholder(source_value):
            errors.append("Authority must include a non-placeholder '- Source:' value")
        if is_placeholder(runtime_value):
            errors.append("Authority must include a non-placeholder '- Runtime/target:' value")

        active_lines = meaningful_lines(section(text, "Active Build"))
        if len(active_lines) != 1:
            errors.append("Active Build must be exactly one non-empty line")

        dod = section(text, "Definition of Done")
        dod_matches = list(DOD_LINE.finditer(dod))
        checkbox_lines = re.findall(r"(?m)^- \[[ xX]\] .+$", dod)
        if not dod_matches:
            errors.append("Definition of Done must contain at least one labeled DOD checklist item")
        if len(checkbox_lines) != len(dod_matches):
            errors.append("Every Definition-of-Done checkbox must use 'DOD-N: description'")
        for match in dod_matches:
            if is_placeholder(match.group(4)):
                errors.append(f"{match.group(2)} must have a non-placeholder description")
        dod_ids = [match.group(2) for match in dod_matches]
        expected_ids = [f"DOD-{index}" for index in range(1, len(dod_ids) + 1)]
        if dod_ids and dod_ids != expected_ids:
            errors.append("Definition-of-Done IDs must be unique and sequential from DOD-1")
        scope_exception = section(text, "Approved Scope Exception")
        if len(dod_ids) > MAX_DOD_ITEMS and is_placeholder(scope_exception):
            errors.append(
                f"Active Build has {len(dod_ids)} DOD items; maximum is {MAX_DOD_ITEMS} "
                "without a non-empty user-approved 'Approved Scope Exception'"
            )

        prerequisites = meaningful_lines(section(text, "External Prerequisites"))
        if not prerequisites:
            errors.append("External Prerequisites must contain at least one explicit status line")
        blocked_prerequisite = False
        for line in prerequisites:
            match = re.match(r"^- (READY|BLOCKED|NOT-REQUIRED)\b", line)
            if not match:
                errors.append(
                    "Each External Prerequisites line must begin '- READY', "
                    "'- BLOCKED', or '- NOT-REQUIRED'"
                )
                continue
            detail = line[match.end() :].strip(" \t—:-")
            if is_placeholder(detail):
                errors.append("Each External Prerequisites status must describe the prerequisite")
            blocked_prerequisite = blocked_prerequisite or match.group(1) == "BLOCKED"
        if blocked_prerequisite and status != "BLOCKED":
            errors.append("A BLOCKED external prerequisite requires Status BLOCKED")

        evidence_plan = section(text, "Evidence Plan")
        for dod_id in dod_ids:
            if is_placeholder(labeled_value(evidence_plan, dod_id)):
                errors.append(f"Evidence Plan is missing a non-placeholder mapping for {dod_id}")

        budget = section(text, "Budget and Handoff")
        for label in ("Budget", "Stop/replan", "Handoff"):
            if is_placeholder(labeled_value(budget, label)):
                errors.append(
                    f"Budget and Handoff must include a non-placeholder '- {label}:' value"
                )

        next_lines = meaningful_lines(section(text, "Next Single Action"))
        if len(next_lines) != 1:
            errors.append("Next Single Action must contain exactly one non-empty line")
            next_action = ""
        else:
            next_action = next_lines[0]

        if status == "DONE":
            if next_action and not next_action.startswith("DONE:"):
                errors.append("DONE status requires Next Single Action to start with 'DONE:'")
            elif next_action and is_placeholder(next_action.partition(":")[2]):
                errors.append("DONE Next Single Action must not be a placeholder")
        elif status == "BLOCKED":
            if next_action and not next_action.startswith("BLOCKER:"):
                errors.append("BLOCKED status requires Next Single Action to start with 'BLOCKER:'")
            elif next_action and is_placeholder(next_action.partition(":")[2]):
                errors.append("BLOCKER Next Single Action must describe the required action")
        elif next_action:
            action_match = re.match(r"^(DOD-\d+):\s*\S.+$", next_action)
            if not action_match:
                errors.append("Next Single Action must start with one current 'DOD-N:'")
            elif action_match.group(1) not in dod_ids:
                errors.append("Next Single Action references a DOD ID not in the current build")
            elif is_placeholder(next_action.partition(":")[2]):
                errors.append("Next Single Action must not be a placeholder")

        last_updated = section(text, "Last Updated")
        if is_placeholder(last_updated):
            errors.append("Last Updated is empty or still a placeholder")

        if args.completion or status == "DONE":
            if re.findall(r"(?m)^- \[ \] DOD-\d+: .+", dod):
                errors.append("Cannot declare DONE while Definition of Done has unchecked items")
            evidence = section(text, "Current Evidence")
            if not meaningful_lines(evidence) or evidence.lower() in {"- none yet.", "none", "none yet."}:
                errors.append("Completion requires recorded evidence")
            for dod_id in dod_ids:
                if is_placeholder(labeled_value(evidence, dod_id)):
                    errors.append(
                        f"Current Evidence is missing non-placeholder completion evidence for {dod_id}"
                    )
            if args.completion and status != "DONE":
                errors.append("--completion requires Status to be DONE")

    if errors:
        heading = (
            "Outcome-first focus diagnostic found issues:"
            if args.diagnostic
            else "Outcome-first focus check failed:"
        )
        stream = sys.stdout if args.diagnostic else sys.stderr
        print(heading, file=stream)
        for item in errors:
            print(f"- {item}", file=stream)
        return 0 if args.diagnostic else 1

    print(f"Outcome-first focus check passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
