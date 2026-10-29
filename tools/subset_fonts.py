"""Cut Orchid's variable fonts down to what the site uses.

Usage: python tools/subset_fonts.py <orchid-fonts-dir> <out-dir>

Each font keeps the latin range and only the axis span the site sets,
so the three files stay small enough to preload.
"""

import sys
from pathlib import Path

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

LATIN = (
    list(range(0x20, 0x7F))
    + list(range(0xA0, 0x100))
    + [0x131, 0x152, 0x153, 0x2C6, 0x2DA, 0x2DC]
    + list(range(0x2000, 0x2070))
    + [0x20AC, 0x2122, 0x2190, 0x2192, 0x2212]
)

FONTS = {
    "source-serif-4-normal-latin.woff2": ("serif.woff2", {"wght": 400, "opsz": (8, 60)}),
    "schibsted-grotesk-normal-latin.woff2": ("sans.woff2", {"wght": (400, 600)}),
    "fraunces-italic-latin.woff2": ("italic.woff2", {"wght": (300, 400), "opsz": 72}),
}


def main(src: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    for name, (target, axes) in FONTS.items():
        font = TTFont(src / name)
        options = Options()
        options.flavor = "woff2"
        options.layout_features = ["kern", "liga", "lnum", "tnum", "pnum", "case", "ccmp", "locl", "mark", "mkmk"]
        options.name_IDs = [0, 1, 2, 3, 4, 5, 6]
        options.notdef_outline = True
        subsetter = Subsetter(options)
        subsetter.populate(unicodes=LATIN)
        subsetter.subset(font)
        font = instantiateVariableFont(font, axes)
        font.flavor = "woff2"
        font.save(out / target)
        print(f"{target}: {(out / target).stat().st_size / 1024:.1f} kB")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
