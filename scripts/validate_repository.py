"""Validate the repository foundation without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "proposal/Second_1PagePitch.pdf",
    "docs/product/PRODUCT_BASELINE.md",
    "docs/architecture/SYSTEM_ARCHITECTURE.md",
    "docs/security/THREAT_MODEL.md",
    "docs/testing/TEST_STRATEGY.md",
    "docs/delivery/ROADMAP.md",
    "docs/delivery/ISSUE_BACKLOG.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/research.yml",
)

CANONICAL_MARKDOWN = tuple(
    ROOT / path
    for path in REQUIRED_PATHS
    if path.endswith(".md")
)

CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKIPPED_LINK_PREFIXES = ("http://", "https://", "mailto:", "#")
FORBIDDEN_FILE_NAMES = {".env", "id_rsa", "id_ed25519"}
FORBIDDEN_SUFFIXES = {".pem", ".p12", ".pfx"}


def validate_required_paths(errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"missing required path: {relative}")


def validate_markdown(errors: list[str]) -> None:
    for document in CANONICAL_MARKDOWN:
        if not document.exists():
            continue

        text = document.read_text(encoding="utf-8")
        for marker in CONFLICT_MARKERS:
            if marker in text:
                errors.append(
                    f"merge conflict marker {marker!r} found in "
                    f"{document.relative_to(ROOT)}"
                )

        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(SKIPPED_LINK_PREFIXES):
                continue

            target = unquote(target.split("#", 1)[0])
            if not target:
                continue

            resolved = (document.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"local link escapes repository in {document.relative_to(ROOT)}: "
                    f"{raw_target}"
                )
                continue

            if not resolved.exists():
                errors.append(
                    f"broken local link in {document.relative_to(ROOT)}: {raw_target}"
                )


def validate_secret_filenames(errors: list[str]) -> None:
    ignored_roots = {".git", "node_modules", ".venv", "venv", "tmp"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_roots for part in path.relative_to(ROOT).parts):
            continue
        if path.name in FORBIDDEN_FILE_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden secret-like file: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required_paths(errors)
    validate_markdown(errors)
    validate_secret_filenames(errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Repository validation passed: required files, canonical local links, "
        "conflict markers, and secret-like filenames checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
