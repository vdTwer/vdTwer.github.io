# vdTwer.github.io

A personal website in two pages: what I have been doing lately, and what I have done so far.

- `index.html` is Lately. `so-far.html` is So far. `404.html` catches the rest.
- Plain static HTML with inline styles. No scripts, no trackers, no cookies.
- The look is AiNKI Orchid, extended for the web. The pages stay plain; each has one large element, its own name in light Fraunces italic. Dark mode follows the system setting.

## Editing

The pages are written by `tools/build.py`, which holds the copy and the one shared stylesheet. Change it there, then run:

```bash
python tools/build.py
```

## Fonts

`fonts/` holds latin subsets of Source Serif 4, Schibsted Grotesk and Fraunces, cut from Orchid's variable fonts. To cut them again:

```bash
pip install fonttools brotli
python tools/subset_fonts.py <orchid-fonts-dir> fonts
```

## Photographs

Placeholders mark where photographs go: a 4:5 portrait on Lately and a 3:2 photograph on So far. Replace each placeholder `div` in `tools/build.py` with an `img` that carries `width`, `height` and `alt`. Leave `loading="lazy"` off the portrait so it shows at once.
