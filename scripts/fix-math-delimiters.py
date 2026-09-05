#!/usr/bin/env python3
"""Fix LaTeX math delimiters in ScienCurious articles (one-shot, high quality).

docsify-katex only understands $...$ (inline) and $$...$$ (display).
This converts \\(...\\) -> $...$ and \\[...\\] -> $$...$$ directly in .md files.

Safety (never touches):
  - fenced code blocks (``` or ~~~)
  - inline code spans (`...`)
  - escaped delimiters (\\() — literal backslash-paren stays as-is
  - multi-line spans (inline math must close on the same line)

Usage:
  python3 scripts/fix-math-delimiters.py [--write] [paths...]
  default (no --write): dry-run, prints EVERY fix as file:line: before -> after.
  --write: applies fixes, then auto-verifies each changed line.

Exit codes: 0 = clean (or write+verify OK), 1 = fixes pending (dry-run) / verify FAIL.
"""

import re
import sys
from pathlib import Path

INLINE_RE = re.compile(r"(?<!\\)\\\((.+?)(?<!\\)\\\)")
DISPLAY_RE = re.compile(r"(?<!\\)\\\[(.+?)(?<!\\)\\\]")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
DOLLAR_RE = re.compile(r"(?<!\\)\$")


def split_code_spans(line):
    """Yield (is_code, text) chunks: inline code spans are left untouched."""
    parts, last = [], 0
    for m in INLINE_CODE_RE.finditer(line):
        if m.start() > last:
            parts.append((False, line[last:m.start()]))
        parts.append((True, m.group(0)))
        last = m.end()
    if last < len(line):
        parts.append((False, line[last:]))
    return parts


def convert_line(line):
    """Convert delimiters outside code spans. Returns (new_line, [(before, after)])."""
    fixes, out = [], []
    for is_code, chunk in split_code_spans(line):
        if is_code:
            out.append(chunk)
            continue
        new_chunk = INLINE_RE.sub(lambda m: "$" + m.group(1) + "$", chunk)
        new_chunk = DISPLAY_RE.sub(lambda m: "$$" + m.group(1) + "$$", new_chunk)
        if new_chunk != chunk:
            fixes.append((chunk.strip(), new_chunk.strip()))
        out.append(new_chunk)
    return "".join(out), fixes


def scan_file(path):
    """Dry-run scan. Returns list of (lineno, before, after)."""
    findings, in_fence = [], False
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        _, fixes = convert_line(line)
        for before, after in fixes:
            findings.append((lineno, before, after))
    return findings


def verify_file(path):
    """Post-write check. Returns list of problems (empty = OK)."""
    problems, in_fence = [], False
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = INLINE_CODE_RE.sub("", line)
        if "\\(" in stripped or "\\)" in stripped or "\\[" in stripped or "\\]" in stripped:
            problems.append((path, lineno, "leftover delimiter", line.strip()[:100]))
        if len(DOLLAR_RE.findall(line)) % 2 == 1:
            problems.append((path, lineno, "unbalanced $", line.strip()[:100]))
    return problems


def collect_targets(args):
    if args:
        return [Path(a) for a in args if Path(a).suffix == ".md"]
    root = Path(__file__).resolve().parent.parent
    return sorted(p for p in root.rglob("*.md") if ".venv" not in p.parts and "node_modules" not in p.parts)


def main(argv):
    write = "--write" in argv
    targets = collect_targets([a for a in argv if not a.startswith("-")])
    total_fixes, changed_files = 0, []
    for path in targets:
        for lineno, before, after in scan_file(path):
            total_fixes += 1
            print(f"{path}:{lineno}:\n  - {before}\n  + {after}")
        if scan_file(path):
            changed_files.append(path)
    if not write:
        print(f"\nDRY-RUN: {total_fixes} fixes in {len(changed_files)} file(s). Re-run with --write to apply.")
        return 1 if total_fixes else 0
    for path in changed_files:
        lines = path.read_text(encoding="utf-8").splitlines()
        in_fence, out = False, []
        for line in lines:
            if FENCE_RE.match(line):
                in_fence = not in_fence
                out.append(line)
                continue
            out.append(convert_line(line)[0] if not in_fence else line)
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\nWROTE: {total_fixes} fixes in {len(changed_files)} file(s). Verifying each fix...")
    problems = [p for path in changed_files for p in verify_file(path)]
    for path, lineno, kind, ctx in problems:
        print(f"FAIL {path}:{lineno} [{kind}]: {ctx}")
    if problems:
        print(f"VERIFY: {len(problems)} problems — NOT clean.")
        return 1
    print(f"VERIFY OK: all {total_fixes} fixes balanced, zero leftovers.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
