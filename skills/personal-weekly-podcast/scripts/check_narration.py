#!/usr/bin/env python3
"""Read-only narration lint and approximate timing for space-delimited text."""

import argparse
import json
import math
import re
from pathlib import Path

WORD = re.compile(r"[^\W_]+(?:[’'ʼ\-][^\W_]+)*", re.UNICODE)
BLOCKERS = {
    "url": re.compile(r"https?://|www\.", re.I),
    "markdown_heading": re.compile(r"(?m)^\s{0,3}#{1,6}\s"),
    "markdown_link": re.compile(r"\[[^\]\n]+\]\([^\n)]+\)"),
    "code_fence": re.compile(r"(?m)^\s*(?:```|~~~)"),
    "table_row": re.compile(r"(?m)^\s*\|.*\|\s*$"),
    "list_marker": re.compile(r"(?m)^\s*(?:[-*+]\s+|\d+[.)]\s+)"),
    "timestamp": re.compile(r"(?m)^\s*\[?\d{1,2}:\d{2}(?::\d{2})?\]?"),
    "citation_token": re.compile(r"||\[\^\w+\]"),
    "stage_direction": re.compile(r"\[(?:pause|music|пауза|музика|sfx)\b", re.I),
}


def analyze(text, slow=110.0, fast=125.0, target=None):
    if not all(math.isfinite(v) and v > 0 for v in (slow, fast)) or slow > fast:
        raise ValueError("Require 0 < slow_wpm <= fast_wpm, both finite.")
    if target is not None and (not math.isfinite(target) or target <= 0):
        raise ValueError("target_minutes must be finite and positive.")
    words = len(WORD.findall(text))
    issues = [{"kind": kind, "line": text.count("\n", 0, match.start()) + 1}
              for kind, pattern in BLOCKERS.items() for match in pattern.finditer(text)]
    if not words:
        issues.append({"kind": "empty_narration", "line": 1})
    warnings = []
    if re.search(r"\d", text):
        warnings.append("Review pronunciation of digits, dates and units.")
    if re.search(r"\[[0-9,; –-]+\]", text):
        warnings.append("Possible numeric citation; inspect manually.")
    if re.search(r"[\u3400-\u9fff\u3040-\u30ff\u0e00-\u0e7f]", text):
        warnings.append("Tokenization may be unsuitable; calibrate duration from audio.")
    low, high = words / fast, words / slow
    result = {
        "word_count": words,
        "count_method": "Unicode alphanumeric tokens; apostrophes/hyphens retained",
        "slow_wpm": slow,
        "fast_wpm": fast,
        "estimated_minutes": {"min": round(low, 2), "max": round(high, 2)},
        "blocking_issues": issues,
        "warnings": warnings,
        "technical_lint_pass": not issues,
        "audio_verified": False,
        "note": "Estimate only. Manual content/pronunciation review and real audio QA remain required.",
    }
    if target is not None:
        result["target_minutes"] = target
        result["target_within_estimated_range"] = low <= target <= high
        if not low <= target <= high:
            warnings.append("Target outside estimated range; revise content or agree a shorter/longer episode.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--slow-wpm", type=float, default=110.0)
    parser.add_argument("--fast-wpm", type=float, default=125.0)
    parser.add_argument("--target-minutes", type=float)
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding="utf-8-sig")
        result = analyze(text, args.slow_wpm, args.fast_wpm, args.target_minutes)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["technical_lint_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
