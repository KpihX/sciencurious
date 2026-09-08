#!/usr/bin/env python3
"""Apply FORME red titles in ScienCurious raw twins (one-shot, high quality).

A raw twin (.md) records ink colors as trailing annotations: `... [rouge]`
or `... [rouge, souligné]`. This converts TITLE lines (headings `## `,
title lines `* `, numbered items `N/ `, short list titles `- `) whose
annotation is EXACTLY `[rouge]` or `[rouge, ...]` at end-of-line into
Docsify-rendered red spans:

>>> convert_line("## p.5 — * Équations [rouge, souligné]")
('## <span style="color:red"><u>p.5 — * Équations</u></span>', True)
>>> convert_line("2/ 1 + 2 + ... = −1 [rouge]")
('2/ <span style="color:red">1 + 2 + ... = −1</span>', True)

Lines whose annotation carries an explanation (`[rouge : ...]`,
`[rouge — ...]`) are left untouched — the note is fond info, not a title:

>>> convert_line("- Pour le demi-cercle l = π [rouge : π seul]")
('- Pour le demi-cercle l = π [rouge : π seul]', False)

Safety (never touches):
  - fenced code blocks (``` or ~~~)
  - inline code spans (`...`)
  - non-title lines (plain text, results inside paragraphs stay annotated)
  - annotations with explanations (`[rouge : ...]`, `[rouge — ...]`)

Usage:
  python3 scripts/apply-forme-titres.py [--write] [paths...]
  default (no --write): dry-run, prints EVERY fix as file:line: before -> after.
  --write: applies fixes, then auto-verifies each changed line.

Exit codes: 0 = clean (or write+verify OK), 1 = fixes pending (dry-run) / verify FAIL.
"""

import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")

# Title line: ## heading | * title | N/ numbered | - short title.
TITLE_RE = re.compile(r"^(##\s+|\*\s+|\d+/[\s]*|-\s+)(.+?)\s*\[(rouge(?:,\s*[^\]]+)?)\]\s*$")


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
    """Wrap a red title annotation in a span. Returns (new_line, changed)."""
    for is_code, chunk in split_code_spans(line):
        if is_code:
            continue
    m = TITLE_RE.match(line.rstrip("\n"))
    if not m:
        return line, False
    prefix, title, annot = m.group(1), m.group(2), m.group(3)
    # Explanatory notes stay as fond info, never converted.
    if annot.startswith("rouge :") or annot.startswith("rouge —"):
        return line, False
    underline = "souligné" in annot
    # Preserve side notes such as "raturé puis réécrit" after conversion
    # ("souligné" is consumed by the <u> wrap and must never reappear).
    side = re.sub(r"rouge,?\s*", "", annot)
    side = re.sub(r"souligné,?\s*", "", side).strip(" ,")
    inner = f"<u>{title}</u>" if underline else title
    new = f"{prefix}<span style=\"color:red\">{inner}</span>"
    if side:
        new += f" [{side}]"
    eol = "\n" if line.endswith("\n") else ""
    return new + eol, True


def scan_file(path):
    """Return list of (lineno, before, after) for convertible title lines."""
    fixes, in_fence = [], False
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
            if in_fence or line.lstrip().startswith("```"):
                continue
            new, changed = convert_line(line)
            if changed:
                fixes.append((i, line.rstrip("\n"), new.rstrip("\n")))
    return fixes


def main(argv):
    """CLI: dry-run by default, --write applies + verifies. Returns exit code."""
    write = "--write" in argv
    paths = [a for a in argv if not a.startswith("--")] or sorted(
        str(p) for p in Path("raw").rglob("*.md")
    )
    total_pending = 0
    for raw in paths:
        path = Path(raw)
        if not path.is_file():
            print(f"SKIP (not a file): {raw}")
            continue
        fixes = scan_file(path)
        total_pending += len(fixes)
        for lineno, before, after in fixes:
            print(f"{raw}:{lineno}: {before} -> {after}")
        if write and fixes:
            text = path.read_text(encoding="utf-8").splitlines(keepends=True)
            for lineno, before, after in fixes:
                assert text[lineno - 1].rstrip("\n") == before, (
                    f"verify FAIL {raw}:{lineno}"
                )
                eol = "\n" if text[lineno - 1].endswith("\n") else ""
                text[lineno - 1] = after + eol
            path.write_text("".join(text), encoding="utf-8")
            # Auto-verify: rescan must be clean.
            left = scan_file(path)
            if left:
                print(f"verify FAIL {raw}: {len(left)} fixes left")
                return 1
            print(f"WROTE {raw}: {len(fixes)} titles converted, verified clean.")
    if not write:
        print(f"DRY-RUN: {total_pending} convertible titles.")
        return 1 if total_pending else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
