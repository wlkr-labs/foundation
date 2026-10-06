# WLKR Labs logo suite

Built October 6, 2026 from Shane's supplied SVG. The six rounded rectangles, proportions, spacing and corner radii are preserved. The original is retained byte for byte in `source/`.

Open [the asset gallery](index.html) or [the overview](overview.png). The overview is a presentation of the actual exported vectors. Every wordmark uses outlined Geist lettering, so SVG/PDF logo files need no installed font.

## Choose an asset

| Use | Files |
| --- | --- |
| Primary mark on white/light surfaces | `logos/mark-primary.svg` and `.png` |
| Mark on dark surfaces | `logos/mark-reverse.svg` and `.png` |
| One-color printing | `logos/mark-black.*` or `logos/mark-white.*` |
| Mark + name | `logos/horizontal-*` or `logos/stacked-*`, SVG/PNG/PDF |
| Profile image | `icons/avatar-light.png` or `avatar-dark.png`, 1024 × 1024 |
| App/website icons | `icons/app-*`, PNG sizes 16–512, adaptive SVG favicon, ICO and 180px Apple icon |
| Website social preview | `social/open-graph-*`, 1200 × 630 |
| Square announcement | `social/square-*`, 1080 × 1080 |
| X / LinkedIn headers | `social/x-header.*`, 1500 × 500; `linkedin-header.*`, 1584 × 396 |
| YouTube banner | `social/youtube-banner.*`, 2560 × 1440; content within the central desktop/mobile safe area |
| Business card | `print/business-card-front.*` / `back.*`; 3.75 × 2.25in artboard, trim 3.5 × 2in, 0.125in bleed |
| Letterhead | `print/letterhead-us-letter.*` / `letterhead-a4.*`, SVG/300dpi PNG/PDF |

## Color and typography

- Ink: **#010101**, RGB 1 / 1 / 1.
- Green: **#33F282**, RGB 51 / 242 / 130. Preserve it on the top block in full-color versions.
- White: **#FFFFFF**. Supporting paper: **#F0F3F0**.
- Use Ink for text on light backgrounds and White on dark backgrounds. Green is a logo/accent color; it is too light for small text on white.
- Geist Regular (400) for body copy; 650 for the wordmark and strong headings. The included original variable font and OFL license support editable brand applications; production logo lettering is already outlined.

## Spacing and sizes

Keep at least one quarter of a block's width clear around the visible mark. The mark exports include this padding. Do not crop or stretch them. Keep the ascending 3 / 2 / 1 arrangement and one green top block. Do not add gradients, outlines or new effects.

Use a mark at 24px or larger in ordinary interfaces. The supplied 16px favicon is a compact browser exception. For a horizontal lockup, use at least 180px width; use the mark alone when space is tighter. Circle-cropped avatars have additional safety padding.

The print PDFs contain vector shapes and outlined type. They use RGB color; request a printer proof and the printer's color conversion before a print order. There is no promise of exact neon-green reproduction in ordinary CMYK printing, and no print purchase is part of this setup.

These assets describe WLKR Labs' identity; they do not claim incorporation, nonprofit recognition or new product availability. The font retains its included OFL license; existing project licenses are unchanged.

## Rebuild and verify

The generator reads `source/wlkrlabs-logo.original.svg` and the included licensed Geist font. It does not redraw the logo. Python tools stay in ignored `.local/`; Node uses the existing website's Sharp dependency.

```sh
python3 -m venv .local/brand-tools
.local/brand-tools/bin/python -m pip install -r brand/requirements.txt
./project brand:build
./project brand:check
./project docs:check
```

`manifest.json` records file sizes and SHA-256 hashes. Checks validate hashes, unchanged rectangle geometry and fills, outlined lettering, icon/social dimensions, transparent logo alpha, ICO contents, and physical print PDF sizes. The completed zip is saved under ignored `.local/foundation-2026-10-06/support/`.
