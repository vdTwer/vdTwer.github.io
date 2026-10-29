# vdTwer.github.io

A personal website in two pages: what I am doing now, and what I did until now.

- `index.html` is Now. `until-now.html` is Until now. `404.html` catches the rest.
- Plain static HTML with inline styles. No build step, no scripts, no trackers.
- The look is AiNKI Orchid, extended for the web: a serif display line, a portrait in the margin column, a Fraunces timeline and a phone layout. Dark mode follows the system setting.

## Fonts

`fonts/` holds latin subsets of Source Serif 4, Schibsted Grotesk and Fraunces, cut from Orchid's variable fonts. To cut them again:

```bash
pip install fonttools brotli
python tools/subset_fonts.py <orchid-fonts-dir> fonts
```

## Photographs

Placeholders mark where photographs go: a 4:5 portrait on Now and a 3:2 photograph on Until now. Replace each placeholder `div` with an `img` that carries `width`, `height` and `alt`, and keep `loading="lazy"` off the portrait so it shows at once.
