"""Preserve the supplied SVG geometry and outline licensed Geist lettering."""

from html import escape
from pathlib import Path
from xml.etree import ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "brand"
SOURCE = BRAND / "source/wlkrlabs-logo.original.svg"
SVG_NS = "http://www.w3.org/2000/svg"
INK, GREEN, WHITE, PAPER = "#010101", "#33F282", "#FFFFFF", "#F0F3F0"
FONTS = {}


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


def lockup(x, y, size, dark=False, stacked=False, mono=False):
    color = WHITE if dark else INK
    name, width = lettering("WLKR Labs", 0, 0, size * .43, color, 650, -.025)
    if stacked:
        return (mark(x + (width - size) / 2, y, size, dark, mono)
                + f'<g transform="translate({x:g} {y + size * 1.48:g})">{name}</g>')
    return (mark(x, y, size, dark, mono)
            + f'<g transform="translate({x + size * 1.22:g} {y + size * .66:g})">{name}</g>')
