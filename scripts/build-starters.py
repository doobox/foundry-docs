#!/usr/bin/env python3
"""Build deterministic starter downloads from quick-start.md; --check detects drift."""
import argparse
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def dump_json(value):
    return (json.dumps(value, indent=4, separators=(",", " : "), ensure_ascii=False) + "\n").encode()


def starter_files(source):
    pairs = re.findall(r'<!-- (starter|complete):([^ ]+) -->\s*```\w+\s*\n(.*?)```', source, re.S)
    snippets = {}
    for stage, name, content in pairs:
        key = (stage, name)
        if key in snippets:
            raise ValueError(f"Duplicate snippet: {stage}:{name}")
        snippets[key] = content.encode()
    expected = {("starter", name) for name in ("manifest.json", "part.html", "part.css")}
    expected |= {("complete", name) for name in ("inspector", "part.html", "part.css")}
    if set(snippets) != expected:
        raise ValueError(f"Unexpected or missing starter markers: {set(snippets) ^ expected}")
    basic = {name: snippets["starter", name] for name in ("manifest.json", "part.html", "part.css")}
    manifest = json.loads(basic["manifest.json"])
    additions = json.loads(b"{" + snippets["complete", "inspector"] + b"}")
    if set(additions) != {"inspector"} or "inspector" in manifest:
        raise ValueError("The inspector stage must add exactly one inspector entry to the basic manifest")
    complete = dict(basic)
    complete["manifest.json"] = dump_json({**manifest, **additions})
    for name in ("part.html", "part.css"):
        complete[name] = snippets["complete", name]
    return {"starter": basic, "complete": complete}


def archive(files):
    output = io.BytesIO()
    pack_manifest = dump_json({
        "formatVersion": 2,
        "id": "uk.co.example.callout-pack",
        "title": "Callout",
        "version": "1.0.0",
        "minimumAPIVersion": 1,
    })
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as zipped:
        root_info = zipfile.ZipInfo("Callout.foundrydevpack/manifest.json", (2026, 1, 1, 0, 0, 0))
        root_info.create_system = 3
        root_info.external_attr = 0o100644 << 16
        zipped.writestr(root_info, pack_manifest)
        for name, content in sorted(files.items()):
            relative = name if name == "manifest.json" else f"Resources/{name}"
            info = zipfile.ZipInfo(
                f"Callout.foundrydevpack/Parts/uk.co.example.callout/{relative}",
                (2026, 1, 1, 0, 0, 0),
            )
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            zipped.writestr(info, content)
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify committed ZIPs without writing files")
    args = parser.parse_args()
    for stage, files in starter_files((ROOT / "developer" / "quick-start.md").read_text()).items():
        destination = ROOT / "assets" / "downloads" / f"Callout-{stage}.zip"
        expected = archive(files)
        if args.check:
            if not destination.exists() or destination.read_bytes() != expected:
                raise SystemExit(f"{destination.name} is missing or stale. Run python3 scripts/build-starters.py")
            print(f"Verified {destination.name}: 4 files match the tutorial")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists() or destination.read_bytes() != expected:
                destination.write_bytes(expected)
            print(f"Built {destination.name}")


if __name__ == "__main__":
    main()
