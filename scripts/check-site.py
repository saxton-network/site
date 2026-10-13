#!/usr/bin/env python3
"""Site check: enforces the site rules in AGENTS.md on site/index.html.

It checks what the rules forbid and what the page must list. It is not a full HTML validator.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PAGE = SITE / "index.html"
PROJECTS = ROOT / "scripts" / "projects.txt"

LINK_PREFIX = "https://github.com/saxton-network/"
REPO_LINK = re.compile(r"https://github\.com/saxton-network/([A-Za-z0-9._-]+)")
# Elements that run code, load resources, or embed content.
FORBIDDEN_TAGS = {"script", "link", "img", "iframe", "frame", "frameset", "object", "embed", "audio",
                  "video", "source", "track", "picture", "svg", "math", "base", "form", "input", "button"}
# Attributes that can fetch a resource.
URL_ATTRS = {"src", "srcset", "data", "poster", "background", "action", "formaction", "manifest", "ping", "cite"}


class PageScanner(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.problems: list[str] = []
        self.links: list[str] = []
        self.styles: list[str] = []
        self._in_style = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_tag(tag, attrs)
        if tag == "style":
            self._in_style = True

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_tag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._in_style = False

    def handle_data(self, data: str) -> None:
        if self._in_style:
            self.styles.append(data)

    def _check_tag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in FORBIDDEN_TAGS:
            self.problems.append(f"forbidden element <{tag}>")
        for name, value in attrs:
            value = value or ""
            if name.startswith("on"):
                self.problems.append(f"event-handler attribute {name} on <{tag}>")
            if name in URL_ATTRS:
                self.problems.append(f"resource attribute {name} on <{tag}>")
            if name == "style":
                self.styles.append(value)
            if name == "http-equiv" and value.strip().lower() == "refresh":
                self.problems.append("meta refresh")
            if "javascript:" in value.replace(" ", "").lower():
                self.problems.append(f"javascript: URL in {name} on <{tag}>")
            if name == "href":
                self.links.append(value)


def main() -> int:
    problems: list[str] = []
    entries = sorted(p.name for p in SITE.iterdir()) if SITE.is_dir() else []
    if entries != ["index.html"]:
        problems.append(f"site/ must contain only index.html, found {entries}")
    if not PAGE.is_file():
        print("FAIL: site/index.html is missing", file=sys.stderr)
        return 1
    text = PAGE.read_text(encoding="utf-8")
    # Raw-text checks do not depend on how a given Python version's HTMLParser reads the page.
    raw = text.lower()
    if "<!--" in raw:
        problems.append("HTML comments are not allowed (parsers disagree on where they end)")
    for needle in ("<script", "javascript:", "url(", "@import"):
        if needle in raw:
            problems.append(f"page text contains {needle!r}")
    scanner = PageScanner()
    scanner.feed(text)
    scanner.close()
    problems.extend(scanner.problems)

    css = "\n".join(scanner.styles).lower()
    if "\\" in css:
        problems.append("CSS contains a backslash escape")
    for needle in ("url(", "@import", "expression(", "image-set("):
        if needle in css:
            problems.append(f"CSS contains {needle}")

    listed: list[str] = []
    for href in scanner.links:
        match = REPO_LINK.fullmatch(href)
        if not href.startswith(LINK_PREFIX) or not match:
            problems.append(f"link {href!r} is not https://github.com/saxton-network/<repo>")
        else:
            listed.append(f"saxton-network/{match.group(1)}")
    expected = [line.strip() for line in PROJECTS.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(set(listed)) != len(listed):
        problems.append(f"a repository is linked more than once: {listed}")
    if sorted(set(listed)) != sorted(expected) or len(set(expected)) != len(expected):
        problems.append(f"linked repositories {sorted(listed)} do not match scripts/projects.txt {sorted(expected)}")

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1
    print(f"PASS: site check ({len(listed)} repositories listed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
