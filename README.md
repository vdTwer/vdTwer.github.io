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

## Icon

`favicon.svg` is a K in Fraunces italic, drawn from Orchid's font as a path. The build inlines it into every page. To draw it again:

```bash
python tools/make_icon.py <orchid-fonts-dir>/fraunces-italic-latin.woff2
```

## Photographs

The portrait on Lately lives in `images/`, cropped to 4:5 and exported as WebP at 256 and 384 pixels wide, with metadata stripped. The 3:2 photograph on So far sits in the student council entry of the timeline, exported the same way at 560 and 1120 pixels wide. It loads lazily, since it sits below the first screen.
