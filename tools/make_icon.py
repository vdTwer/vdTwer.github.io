"""Draw the site icon: an Orchid K in Fraunces italic.

Usage: python tools/make_icon.py <fraunces-italic-latin.woff2> [out.svg]

The letter is taken from Orchid's own Fraunces and written as a path,
so the icon renders the same everywhere without loading a font.
"""

import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

# Heavier and at a small optical size, so the K holds up at 16 pixels.
AXES = {"wght": 560, "opsz": 9}
LIGHT, DARK = "#a8336d", "#e183b3"


def main(src: str, out: str) -> None:
    font = instantiateVariableFont(TTFont(src), AXES)
    glyphs = font.getGlyphSet()
    name = font.getBestCmap()[ord("K")]

    bounds = BoundsPen(glyphs)
    glyphs[name].draw(bounds)
    x0, y0, x1, y1 = bounds.bounds
    side = max(x1 - x0, y1 - y0) * 1.08
    dx = (side - (x1 - x0)) / 2 - x0
    dy = (side - (y1 - y0)) / 2 + y1

    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.0f}")
    glyphs[name].draw(TransformPen(pen, (1, 0, 0, -1, dx, dy)))

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side:.0f} {side:.0f}">'
        f"<style>path{{fill:{LIGHT}}}@media (prefers-color-scheme:dark){{path{{fill:{DARK}}}}}</style>"
        f'<path d="{pen.getCommands()}"/></svg>\n'
    )
    with open(out, "w") as f:
        f.write(svg)
    print(f"{out}: {len(svg)} bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "favicon.svg")
