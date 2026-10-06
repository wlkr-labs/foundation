"""Combine the supplied mark and revised wordmark; outline supporting typography."""

from html import escape
from pathlib import Path
from xml.etree import ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "brand"
SOURCE = BRAND / "source/wlkrlabs-logo.original.svg"
WORDMARK_SOURCE = BRAND / "source/wlkrlabs-wordmark.svg"
WORDMARK_ORIGINAL_SOURCE = BRAND / "source/wlkrlabs-wordmark.original.svg"
SVG_NS = "http://www.w3.org/2000/svg"
INK, GREEN, WHITE, PAPER = "#010101", "#33F282", "#FFFFFF", "#F0F3F0"
FONTS = {}
MARK_INK = (63.25, 61.5, 777.5, 781)
WORDMARK_INK = (3.88625, 33.2, 72.97375, 13.58)


def font(weight=650):
    if weight not in FONTS:
        variable = TTFont(BRAND / "fonts/geist-latin-wght-normal.woff2")
        FONTS[weight] = instantiateVariableFont(variable, {"wght": weight})
    return FONTS[weight]


def lettering(text, x, y, size, color=INK, weight=650, tracking=0):
    face = font(weight)
    glyphs, cmap = face.getGlyphSet(), face.getBestCmap()
    units = face["head"].unitsPerEm
    cursor, paths = 0, []
    for char in text:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor:g} 0)" d="{pen.getCommands()}"/>')
        cursor += face["hmtx"][name][0] + tracking * units
    scale = size / units
    return (f'<g aria-label="{escape(text)}" fill="{color}" '
            f'transform="translate({x:g} {y:g}) scale({scale:g} {-scale:g})">'
            + "".join(paths) + "</g>", cursor * scale)


def text(value, x, y, size, color=INK, weight=650, tracking=0):
    return lettering(value, x, y, size, color, weight, tracking)[0]


def centered_text(value, center, y, size, color=INK, weight=650, tracking=0):
    width = lettering(value, 0, 0, size, color, weight, tracking)[1]
    return text(value, center - width / 2, y, size, color, weight, tracking)


def mark(x=0, y=0, size=904, dark=False, mono=False):
    root = ET.parse(SOURCE).getroot()
    blocks = root.find(f".//{{{SVG_NS}}}g[@id='ascending-rounded-blocks']")
    rectangles = list(blocks.iter(f"{{{SVG_NS}}}rect"))
    shapes = []
    for rect in rectangles:
        fill = (WHITE if dark else INK) if mono or rect.attrib["id"] != "top-lime-block" else GREEN
        attrs = " ".join(f'{key}="{rect.attrib[key]}"' for key in ("x", "y", "width", "height", "rx"))
        shapes.append(f'<rect {attrs} fill="{fill}"/>')
    return (f'<g transform="translate({x:g} {y:g}) scale({size / 904:g})">'
            '<g transform="translate(53.25 51)">' + "".join(shapes) + "</g></g>")


def wordmark(x=0, y=0, width=800, dark=False, mono=False):
    root = ET.parse(WORDMARK_SOURCE).getroot()
    left, top, source_width, _ = map(float, root.attrib["viewBox"].split())
    ink = WHITE if dark else INK
    mode = ("white" if dark else "black") if mono else ("reverse" if dark else "primary")
    paths = []
    for path in root.iter(f"{{{SVG_NS}}}path"):
        transform = f' transform="{path.attrib["transform"]}"' if "transform" in path.attrib else ""
        paths.append(f'<path d="{path.attrib["d"]}" fill="{ink}"{transform}/>')
    return (f'<g data-wordmark="{mode}" aria-label="WLKR Labs" '
            f'transform="translate({x:g} {y:g}) scale({width / source_width:.15g})">'
            f'<g transform="translate({-left:.15g} {-top:.15g})">'
            + "".join(paths) + "</g></g>")


def wordmark_height(width):
    box = ET.parse(WORDMARK_SOURCE).getroot().attrib["viewBox"].split()
    return width * float(box[3]) / float(box[2])


def mark_ink(x, y, height, dark=False, mono=False):
    left, top, _, source_height = MARK_INK
    scale = height / source_height
    return mark(x - left * scale, y - top * scale, 904 * scale, dark, mono)


def wordmark_ink(x, y, height, dark=False, mono=False):
    box = list(map(float, ET.parse(WORDMARK_SOURCE).getroot().attrib["viewBox"].split()))
    left, top, _, source_height = WORDMARK_INK
    scale = height / source_height
    return wordmark(x - (left - box[0]) * scale, y - (top - box[1]) * scale,
                    box[2] * scale, dark, mono)


def lockup_height(width):
    return width * 1.16 / (1.16 * MARK_INK[2] / MARK_INK[3] + .45 + WORDMARK_INK[2] / WORDMARK_INK[3])


def stacked_lockup(center, y, width, dark=False, mono=False):
    height = width * WORDMARK_INK[3] / WORDMARK_INK[2]
    symbol_height = height * 2.1
    symbol_width = symbol_height * MARK_INK[2] / MARK_INK[3]
    return (mark_ink(center - symbol_width * .6, y, symbol_height, dark, mono)
            + wordmark_ink(center - width / 2, y + symbol_height + height * .6,
                           height, dark, mono))


def rect(x, y, w, h, fill, radius=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"/>'


def svg(w, h, content, title="WLKR Labs"):
    return (f'<svg xmlns="{SVG_NS}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{content}</svg>\n')


def write(relative, w, h, content, title="WLKR Labs"):
    target = BRAND / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    document = svg(w, h, content, title)
    if relative.startswith("print/"):
        document = document.replace(f'width="{w}" height="{h}"', f'width="{w}pt" height="{h}pt"', 1)
    target.write_text(document)


def lockup(x, y, width, dark=False, mono=False):
    height = lockup_height(width) / 1.16
    symbol_height = height * 1.16
    symbol_width = symbol_height * MARK_INK[2] / MARK_INK[3]
    return (f'<g data-lockup="horizontal" data-wordmark-height="{height:.15g}">'
            + mark_ink(x, y, symbol_height, dark, mono)
            + wordmark_ink(x + symbol_width + height * .45,
                           y + (symbol_height - height) / 2 + height * .06,
                           height, dark, mono) + '</g>')
