"""Build a practical logo suite from the supplied vector, without redrawing it."""

import hashlib
import json
import subprocess
from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab import rl_config
from svglib.svglib import svg2rlg

from brand_geometry import BRAND, GREEN, INK, PAPER, ROOT, SOURCE, WHITE, centered_text, lettering, lockup, mark, rect, text, write

rl_config.invariant = 1


def logos():
    for mode in ("primary", "reverse", "black", "white"):
        dark, mono = mode in ("reverse", "white"), mode in ("black", "white")
        write(f"logos/mark-{mode}.svg", 904, 904, mark(dark=dark, mono=mono))
        write(f"logos/horizontal-{mode}.svg", 930, 300,
              lockup(30, 30, 240, dark, mono=mono))
        name_width = lettering("WLKR Labs", 0, 0, 129, tracking=-.025)[1]
        write(f"logos/stacked-{mode}.svg", 800, 600,
              lockup((800 - name_width) / 2, 68, 300, dark, stacked=True, mono=mono))
    for mode, background in (("light", WHITE), ("dark", INK)):
        write(f"icons/avatar-{mode}.svg", 1024, 1024,
              rect(0, 0, 1024, 1024, background) + mark(162, 162, 700, mode == "dark"))
        write(f"icons/app-{mode}.svg", 1024, 1024,
              rect(0, 0, 1024, 1024, background) + mark(90, 90, 844, mode == "dark"))
    adaptive = mark()
    adaptive = adaptive.replace(f'fill="{INK}"', 'class="ink" fill="#010101"')
    write("icons/favicon-adaptive.svg", 904, 904,
          '<style>@media(prefers-color-scheme:dark){.ink{fill:#fff}}</style>' + adaptive)


def social():
    for mode, background, color in (("light", WHITE, INK), ("dark", INK, WHITE)):
        dark = mode == "dark"
        write(f"social/open-graph-{mode}.svg", 1200, 630,
              rect(0, 0, 1200, 630, background) + mark(70, 75, 270, dark)
              + text("WLKR Labs", 390, 265, 105, color, tracking=-.025)
              + text("Free software. Useful technology.", 88, 445, 44, color, 500)
              + text("Biblical purpose.", 88, 505, 44, color, 500)
              + text("wlkrlabs.com", 90, 574, 20, color, 500))
        write(f"social/square-{mode}.svg", 1080, 1080,
              rect(0, 0, 1080, 1080, background) + mark(330, 120, 420, dark)
              + centered_text("WLKR Labs", 540, 695, 116, color, tracking=-.025)
              + centered_text("Free software. Useful technology.", 540, 840, 43, color, 500)
              + centered_text("Biblical purpose.", 540, 901, 43, color, 500))
    for name, w, h in (("x-header", 1500, 500), ("linkedin-header", 1584, 396)):
        write(f"social/{name}.svg", w, h,
              rect(0, 0, w, h, INK) + lockup(w * .24, h * .17, h * .48, dark=True)
              + text("Free software. Useful technology. Biblical purpose.", w * .24, h * .83, 28, WHITE, 500))
    write("social/youtube-banner.svg", 2560, 1440,
          rect(0, 0, 2560, 1440, INK) + lockup(640, 550, 270, dark=True)
          + text("Free software. Useful technology. Biblical purpose.", 650, 905, 42, WHITE, 500))


def print_assets():
    write("print/business-card-front.svg", 270, 162,
          rect(0, 0, 270, 162, WHITE) + lockup(23, 45, 64))
    write("print/business-card-back.svg", 270, 162,
          rect(0, 0, 270, 162, INK)
          + text("Free software.", 22, 43, 19, WHITE)
          + text("Useful technology.", 22, 68, 19, WHITE)
          + text("Biblical purpose.", 22, 93, 19, WHITE)
          + text("wlkrlabs.com", 22, 136, 10, WHITE, 500))
    for name, w, h in (("letterhead-us-letter", 612, 792), ("letterhead-a4", 595.276, 841.89)):
        write(f"print/{name}.svg", w, h,
              rect(0, 0, w, h, WHITE) + lockup(42, 33, 50)
              + rect(42, 105, w - 84, .75, "#CED6CE")
              + text("wlkrlabs.com", 42, h - 35, 9, INK, 500)
              + text("Free software. Useful technology. Biblical purpose.", 210, h - 35, 9, INK, 500))


def board():
    content = rect(0, 0, 1600, 1200, "#171B17")
    panels = [(40 + col * 512, 40 + row * 373) for row in range(3) for col in range(3)]
    for i, (x, y) in enumerate(panels):
        dark = i in (2, 3, 6, 8)
        content += rect(x, y, 496, 357, INK if dark else PAPER, 6)
        color = WHITE if dark else INK
        label = ["01 / PRIMARY", "02 / GEOMETRY", "03 / DIGITAL", "04 / PURPOSE", "05 / PALETTE",
                 "06 / TYPE", "07 / PROFILE", "08 / PRINT", "09 / REVERSE"][i]
        content += text(label, x + 25, y + 32, 13, color, 500)
        if i == 0:
            content += mark(x + 154, y + 58, 188) + text("WLKR Labs", x + 114, y + 307, 52)
        elif i == 1:
            for k in range(4):
                content += rect(x + 105 + 90 * k, y + 67, .5, 255, "#CFD8CF")
                content += rect(x + 105, y + 67 + 85 * k, 270, .5, "#CFD8CF")
            content += mark(x + 90, y + 56, 290)
        elif i == 2:
            content += rect(x + 22, y + 76, 452, 250, "#181D18", 12)
            content += text("wlkrlabs.com", x + 45, y + 105, 17, WHITE, 500)
            content += lockup(x + 48, y + 151, 80, dark=True)
            content += text("Build. Share. Teach.", x + 50, y + 290, 24, WHITE, 500)
        elif i == 3:
            for j, line in enumerate(("Free software.", "Useful technology.", "Biblical purpose.")):
                content += text(line, x + 30, y + 133 + j * 70, 45, WHITE)
        elif i == 4:
            for j, (value, name) in enumerate(((INK, "INK / 010101"), (GREEN, "GREEN / 33F282"), (WHITE, "WHITE / FFFFFF"))):
                content += rect(x + 25 + j * 151, y + 86, 141, 164, value, 8)
                content += text(name, x + 25 + j * 151, y + 282, 11, INK, 500)
        elif i == 5:
            content += text("Geist", x + 28, y + 178, 108, INK)
            content += text("Aa Bb Cc 0123", x + 28, y + 245, 40, INK, 500)
            content += text("Clear, practical, readable.", x + 28, y + 307, 21, INK, 500)
        elif i == 6:
            content += rect(x + 40, y + 91, 184, 184, WHITE, 40) + mark(x + 65, y + 116, 134)
            content += rect(x + 265, y + 91, 184, 184, "#202820", 40) + mark(x + 290, y + 116, 134, True)
        elif i == 7:
            content += rect(x + 52, y + 99, 392, 205, WHITE, 8) + lockup(x + 85, y + 167, 80)
        else:
            content += lockup(x + 35, y + 113, 120, dark=True)
            content += text("Six blocks. One accent.", x + 37, y + 293, 23, WHITE, 500)
    write("overview.svg", 1600, 1200, content, "WLKR Labs identity suite overview")


def main():
    logos()
    social()
    print_assets()
    board()
    subprocess.run(["node", str(ROOT / "scripts/render_brand.mjs")], check=True)
    for source in [*sorted((BRAND / "logos").glob("*.svg")), *sorted((BRAND / "print").glob("*.svg")), BRAND / "overview.svg"]:
        boxes = {"trimBox": (9, 9, 261, 153), "bleedBox": (0, 0, 270, 162)} if source.name.startswith("business-card-") else {}
        renderPDF.drawToFile(svg2rlg(str(source)), str(source.with_suffix(".pdf")), **boxes)
    files = []
    for item in sorted(BRAND.rglob("*")):
        if item.is_file() and item.name != "manifest.json":
            files.append({"path": str(item.relative_to(BRAND)), "bytes": item.stat().st_size,
                          "sha256": hashlib.sha256(item.read_bytes()).hexdigest()})
    manifest = {"source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                "colors": {"ink": INK, "green": GREEN, "white": WHITE, "paper": PAPER}, "files": files}
    (BRAND / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Built {len(files)} brand files from unchanged supplied SVG geometry.")


if __name__ == "__main__":
    main()
