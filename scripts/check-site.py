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
                  "video", "source", "track", "picture", "svg", "math", "base", "form", "input", "button", "applet"}
# Characters folded before looking for repository names in decoded text: hyphen and dot look-alikes,
# and invisible characters that could split a name.
FOLD = str.maketrans({**{c: "-" for c in "\u2010\u2011\u2012\u2013\u2014\u2015\u2212\ufe58\ufe63\uff0d"},
                      **{c: "." for c in "\u2024\ufe52\uff0e"},
                      **{c: "" for c in "\u00ad\u200b\u200c\u200d\u2060\ufeff"}})
# Attributes that can fetch a resource.
URL_ATTRS = {"src", "srcset", "data", "poster", "background", "action", "formaction", "manifest", "ping", "cite"}


class PageScanner(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.problems: list[str] = []
        self.links: list[str] = []
        self.styles: list[str] = []
        self.anchors: list[tuple[str, str]] = []  # (href, link text)
        self.decoded: list[str] = []  # decoded text and non-href attribute values
        self._in_style = False
        self._anchor: list[str] | None = None
        self._anchor_href = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_tag(tag, attrs)
        if tag == "style":
            self._in_style = True
        if tag == "a":
            if self._anchor is not None:
                self.problems.append("nested <a> elements")
            self._anchor = []
            self._anchor_href = dict(attrs).get("href") or ""

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_tag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._in_style = False
        if tag == "a" and self._anchor is not None:
            self.anchors.append((self._anchor_href, "".join(self._anchor).strip()))
            self._anchor = None

    def handle_data(self, data: str) -> None:
        self.decoded.append(data)
        if self._in_style:
            self.styles.append(data)
        if self._anchor is not None:
            self._anchor.append(data)

    def _check_tag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in FORBIDDEN_TAGS:
            self.problems.append(f"forbidden element <{tag}>")
        for name, value in attrs:
            value = value or ""
            if name != "href":
                self.decoded.append(value)
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

    # Repositories may be named only as the target and text of an allowed link: every mention of the
    # organisation or of GitHub in the page must come from those links' hrefs.
    if scanner._anchor is not None:
        problems.append("unclosed <a> element")
    if len(scanner.anchors) != len(scanner.links):
        problems.append("every href must belong to a closed <a> element")
    for href, label in scanner.anchors:
        match = REPO_LINK.fullmatch(href)
        if match and label != match.group(1):
            problems.append(f"link text {label!r} does not match its repository {match.group(1)!r}")
    for needle in ("saxton-network", "github.com"):
        if raw.count(needle) != len(scanner.links):
            problems.append(f"{needle!r} appears outside the repository links")
    # The same names, as a browser would show them: entities decoded and look-alike characters folded.
    shown = " ".join(scanner.decoded).lower().translate(FOLD)
    for needle in ("saxton-network", "github.com"):
        if needle in shown:
            problems.append(f"{needle!r} appears in page text or attributes outside the repository links")

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1
    print(f"PASS: site check ({len(listed)} repositories listed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
