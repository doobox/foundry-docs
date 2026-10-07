#!/usr/bin/env python3
"""Check docs source, JSON examples, and optionally a Jekyll-rendered site.

Uses only Python's standard library. These are documentation contract checks,
not a replacement for importing example packs into Foundry.
"""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(location, message):
    errors.append(f"{location}: {message}")


def read_json(code):
    code = code.strip()
    if code.startswith('"'):
        # Key fragments shown without their enclosing object.
        return json.loads("{" + code + "}")
    try:
        return json.loads(code)
    except json.JSONDecodeError:
        # Sibling objects shown without their enclosing array.
        return json.loads("[" + code + "]")


def dictionaries(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from dictionaries(child)
    elif isinstance(value, list):
        for child in value:
            yield from dictionaries(child)


# Mirrors PartPackageControl.Kind.permitsOmittedID in the app.
ID_OPTIONAL_CONTROLS = {"divider", "note", "spacer"}
SPACER_HEIGHT_RANGE = (1, 30)

sources = {p.name: p.read_text() for p in (ROOT / "developer").glob("*.md")}
control_pages = {}
for name, source in sources.items():
    match = re.search(r'"type"\s*:\s*"([^"]+)"', source)
    if 'manifest.json · inspector' in source and match:
        keys = set(re.findall(r'<h3 class="property-heading"><code>([^<.]+)</code>', source))
        if {"type", "id"} <= keys:
            control_pages[match[1]] = (name, keys)

snippet_count = 0
control_count = 0
for name, source in sources.items():
    if name in {entry[0] for entry in control_pages.values()}:
        if source.count("## Quick example") != 1:
            fail(name, "expected exactly one Quick example")
        elif source.index("## Quick example") > source.index('class="property-heading"'):
            fail(name, "Quick example must precede the property reference")
    for index, match in enumerate(re.finditer(r'^```json\s*\n(.*?)^```', source, re.M | re.S), 1):
        location = f"{name}:JSON example {index}"
        code = match[1]
        # Explicitly illustrative fragments are not complete JSON documents.
        if "..." in code or "…" in code:
            continue
        try:
            value = read_json(code)
            snippet_count += 1
        except Exception as error:
            fail(location, f"invalid JSON syntax: {error}")
            continue
        section_names = []
        for item in dictionaries(value):
            if "groups" in item and isinstance(item["groups"], list):
                fail(location, "retired top-level groups array; declare sections inline in the inspector")
            kind = item.get("type")
            if kind is None and "group" in item and ("controls" in item or "systemImage" in item) and "id" not in item and "title" not in item:
                fail(location, "retired section wrapper key group; name the section with section")
                continue
            if (
                "controls" in item
                and isinstance(item["controls"], list)
                and "section" not in item
                and kind != "collection"
                and name != "collection-control.md"
            ):
                fail(location, "retired controls array; the Inspector array is now inspector")
            if kind is None and "section" in item and "id" not in item and "title" not in item:
                # An inspector entry without a type is an Inspector section wrapper.
                unknown = set(item) - {"section", "systemImage", "controls"}
                if unknown:
                    fail(location, f"section entry: undocumented keys {sorted(unknown)}")
                section = item["section"]
                if not isinstance(section, str) or not section:
                    fail(location, "section entry: section must be a non-empty section name")
                elif section in section_names:
                    fail(location, f"duplicate section name {section}")
                else:
                    section_names.append(section)
                members = item.get("controls", [])
                if not isinstance(members, list):
                    fail(location, "section entry: controls must be an array")
                    continue
                for member in members:
                    if not isinstance(member, dict) or "type" not in member:
                        fail(location, "sections cannot nest; every entry inside a section needs a type")
                    elif member["type"] == "advanced":
                        fail(location, "the advanced group is Foundry's own section; declare it at the top level")
                continue
            if isinstance(kind, str) and ("group" in item or "section" in item):
                fail(location, "controls no longer take group or section; wrap the control in a section entry")
            # Presentation-only items hold no value, so their id is optional.
            if not isinstance(kind, str) or ("id" not in item and kind not in ID_OPTIONAL_CONTROLS):
                continue
            if kind not in control_pages:
                # Other manifest objects also use type/id; reject known retired controls.
                if kind in {"padding", "margin", "themeBorderWidth", "fontStyle", "fontWeight"}:
                    fail(location, f"retired control type {kind}")
                continue
            control_count += 1
            _, permitted = control_pages[kind]
            unknown = set(item) - permitted
            if unknown:
                fail(location, f"{kind}: undocumented keys {sorted(unknown)}")
            if "height" in item:
                height = item["height"]
                low, high = SPACER_HEIGHT_RANGE
                if isinstance(height, bool) or not isinstance(height, (float, int)):
                    fail(location, f"{kind}: height must be a number")
                elif not low <= height <= high:
                    fail(location, f"{kind}: height must be between {low} and {high}")
            if "default" in item:
                fail(location, "use defaults.base, not default")
            if "defaults" in permitted and "defaults" not in item:
                fail(location, f"{kind}: missing defaults")
            defaults = item.get("defaults")
            if defaults is not None:
                if not isinstance(defaults, dict) or "base" not in defaults:
                    fail(location, "defaults must be a dictionary containing base")
                    continue
                allowed = {"base", "small", "medium", "large", "extraLarge", "doubleExtraLarge"}
                if set(defaults) - allowed:
                    fail(location, "unknown breakpoint in defaults")
                if len(defaults) > 1 and item.get("responsive") is not True:
                    fail(location, "breakpoint defaults require responsive: true")
                if kind in {"slider", "number"}:
                    for value in defaults.values():
                        for number in value if isinstance(value, list) else [value]:
                            if isinstance(number, bool) or not isinstance(number, (float, int)):
                                fail(location, f"{kind}: default must be numeric")
                            elif number < item.get("minimum", -float("inf")) or number > item.get("maximum", float("inf")):
                                fail(location, f"{kind}: default outside declared range")


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.headings = []
        self.heading = None
        self.feed(content)
        # Match app.js's property-anchor convention.
        for existing, text in self.headings:
            if existing:
                continue
            stem = re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-") or "section"
            anchor, suffix = stem, 2
            while anchor in self.ids:
                anchor = f"{stem}-{suffix}"
                suffix += 1
            self.ids.add(anchor)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in {"h2", "h3"}:
            self.heading = [attrs.get("id"), ""]
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])

    def handle_data(self, text):
        if self.heading is not None:
            self.heading[1] += text

    def handle_endtag(self, tag):
        if tag in {"h2", "h3"} and self.heading is not None:
            self.headings.append(self.heading)
            self.heading = None


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--site", type=Path, help="Jekyll output directory; enables rendered link and search-index checks")
args = parser.parse_args()
if subprocess.run([sys.executable, str(ROOT / "scripts/build-starters.py"), "--check"]).returncode:
    fail("quick-start.md", "starter downloads do not match the documented snippets")
if args.site:
    site = args.site.resolve()
    pages = {p.resolve(): Page(p.read_text()) for p in site.rglob("*.html")}
    search = json.loads((site / "search.json").read_text())
    # Infer GitHub Pages baseurl from the generated index, also supporting local /.
    prefix = urlsplit(search[0]["url"]).path.rsplit("/", 1)[0] + "/" if search else "/"
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(html.unescape(link))
            if url.scheme or url.netloc:
                continue
            target = unquote(url.path)
            if target.startswith("/"):
                target = target[len(prefix):] if target.startswith(prefix) else target.lstrip("/")
                destination = site / target
            else:
                destination = path.parent / target if target else path
            if destination.is_dir():
                destination /= "index.html"
            destination = destination.resolve()
            if not destination.exists():
                fail(path.name, f"missing link target {link}")
            elif url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                fail(path.name, f"missing anchor {link}")
    for entry in search:
        if not all(isinstance(entry.get(key), str) for key in ("title", "url", "html")):
            fail("search.json", "invalid search entry")
    print(f"Checked {len(pages)} rendered pages and {len(search)} search entries.")

print(f"Checked {len(control_pages)} control pages, {snippet_count} JSON snippets and {control_count} control declarations.")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Documentation checks passed.")
