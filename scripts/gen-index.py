#!/usr/bin/env python3
"""Regenerate the machine-generated section of INDEX.md.

Everything above the AUTOGEN marker is hand-curated (intro + curated
sections). Everything at and below the marker is rebuilt from
`git ls-files '*.md'` grouped by top-level directory, sorted.

Usage: python3 scripts/gen-index.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- AUTOGEN:BEGIN -->"
EXCLUDED = {"INDEX.md", "SUMMARY.md"}  # SUMMARY = GitBook TOC; listed elsewhere


def tracked_md() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return sorted(line for line in out.splitlines() if line.strip() and line.strip() not in EXCLUDED)


def label(path: str) -> str:
    stem = path.rsplit("/", 1)[-1]
    return "README" if stem == "README.md" else stem[:-3]


def build_generated(files: list[str]) -> str:
    root_files = [f for f in files if "/" not in f]
    by_top: dict[str, list[str]] = {}
    for f in files:
        if "/" in f:
            by_top.setdefault(f.split("/", 1)[0], []).append(f)

    lines: list[str] = [MARKER, "", "## Root"]
    for f in sorted(root_files + ["INDEX.md"]):
        lines.append(f"- [{label(f)}](./{f})")
    lines.append("")
    for top in sorted(by_top):
        lines.append(f"## {top}")
        for f in sorted(by_top[top]):
            lines.append(f"- [{label(f)}](./{f})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    index = ROOT / "INDEX.md"
    text = index.read_text()
    if MARKER in text:
        head = text.split(MARKER, 1)[0].rstrip() + "\n\n"
    else:
        head = (
            "# INDEX — PhysicianBuilder Master Searchable Index\n\n"
            "> Auto-generated manifest. Regenerate with `python3 scripts/gen-index.py`.\n\n"
        )
    files = tracked_md()
    index.write_text(head + build_generated(files))
    print(f"INDEX.md regenerated: {len(files)} tracked markdown files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
