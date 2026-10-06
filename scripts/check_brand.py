"""Verify deliverable hashes, exact mark geometry, portable vectors and print size."""

import hashlib
import json
import re
import struct
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "brand"
NS = "{http://www.w3.org/2000/svg}"
manifest = json.loads((BRAND / "manifest.json").read_text())
source = BRAND / "source/wlkrlabs-logo.original.svg"
assert hashlib.sha256(source.read_bytes()).hexdigest() == manifest["source_sha256"]
for entry in manifest["files"]:
    target = BRAND / entry["path"]
    assert target.stat().st_size == entry["bytes"], target
    assert hashlib.sha256(target.read_bytes()).hexdigest() == entry["sha256"], target

original = ET.parse(source).find(f".//{NS}g[@id='ascending-rounded-blocks']")
geometry = [tuple(rect.attrib[k] for k in ("x", "y", "width", "height", "rx"))
            for rect in original.iter(f"{NS}rect")]
for mode, ink, accent in (("primary", "#010101", "#33F282"), ("reverse", "#FFFFFF", "#33F282"),
                          ("black", "#010101", "#010101"), ("white", "#FFFFFF", "#FFFFFF")):
    root = ET.parse(BRAND / f"logos/mark-{mode}.svg")
    rectangles = list(root.iter(f"{NS}rect"))
    assert len(rectangles) == 6
    assert [tuple(rect.attrib[k] for k in ("x", "y", "width", "height", "rx"))
            for rect in rectangles] == geometry
    assert [rect.attrib["fill"] for rect in rectangles] == [accent, *([ink] * 5)]

for item in [*sorted((BRAND / "logos").glob("*.svg")), *sorted((BRAND / "social").glob("*.svg")),
             *sorted((BRAND / "print").glob("*.svg")), BRAND / "overview.svg"]:
    root = ET.parse(item)
    assert not list(root.iter(f"{NS}text")), f"Lettering must be outlined: {item}"
    assert not list(root.iter(f"{NS}image")), f"External raster dependency: {item}"
    assert not list(root.iter(f"{NS}script")), f"Script inside vector: {item}"

for name, dimensions in (("business-card-front", (270, 162)), ("business-card-back", (270, 162)),
                         ("letterhead-us-letter", (612, 792)), ("letterhead-a4", (595.276, 841.89))):
    pdf = (BRAND / f"print/{name}.pdf").read_bytes()
    box = re.search(rb"/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*\]", pdf)
    assert box, name
    assert all(abs(float(value) - expected) < .01 for value, expected in zip(box.groups(), dimensions)), name
    if name.startswith("business-card-"):
        assert re.search(rb"/TrimBox\s*\[\s*9\s+9\s+261\s+153\s*\]", pdf), name

def png_size(path):
    content = path.read_bytes()
    assert content[:8] == b"\x89PNG\r\n\x1a\n", path
    return struct.unpack(">II", content[16:24])

for size in (16, 32, 48, 64, 180, 192, 256, 512):
    assert png_size(BRAND / f"icons/icon-{size}.png") == (size, size)
for name, size in (("open-graph-light", (1200, 630)), ("open-graph-dark", (1200, 630)),
                   ("square-light", (1080, 1080)), ("square-dark", (1080, 1080)),
                   ("x-header", (1500, 500)), ("linkedin-header", (1584, 396)),
                   ("youtube-banner", (2560, 1440))):
    assert png_size(BRAND / f"social/{name}.png") == size, name
ico = (BRAND / "icons/favicon.ico").read_bytes()
assert struct.unpack("<HHH", ico[:6]) == (0, 1, 5)
for index in range(5):
    length, offset = struct.unpack_from("<II", ico, 6 + index * 16 + 8)
    assert ico[offset:offset + 8] == b"\x89PNG\r\n\x1a\n" and offset + length <= len(ico)
subprocess.run(["node", str(ROOT / "scripts/check_brand_images.mjs")], check=True)
print(f"PASS: {len(manifest['files'])} file hashes, source geometry/fills, outlined vectors, icon/social dimensions and physical print PDFs")
