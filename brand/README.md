# WLKR Labs logo suite

Built October 6, 2026 from Shane's supplied official logo and wordmark SVGs. The six rounded rectangles, proportions, spacing and corner radii are preserved. Both originals are retained byte for byte in `source/`.

Open [the asset gallery](index.html) or [the overview](overview.png). The overview presents the actual exported vectors. At Shane's request, the lowercase wordmark has no accent slash: the **r** has a complete vertical stem and the **k–r** spacing is repaired. The remaining letter shapes are preserved; **r** and the following letters move together to keep the rest of the spacing intact. The revised master is `source/wlkrlabs-wordmark.svg`, entirely Ink (or White in reverse). SVG/PDF logo files need no installed font.

## Choose an asset

| Use | Files |
| --- | --- |
| Primary mark on white/light surfaces | `logos/mark-primary.svg` and `.png` |
| Mark on dark surfaces | `logos/mark-reverse.svg` and `.png` |
| One-color printing | `logos/mark-black.*` or `logos/mark-white.*` |
| Official name without symbol | `logos/wordmark-*`, SVG/PNG/PDF |
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
- Green: **#33F282**, RGB 51 / 242 / 130. Preserve it on the top block in full-color versions. The wordmark has no green accent.
- White: **#FFFFFF**. Supporting paper: **#F0F3F0**.
- Use Ink for text on light backgrounds and White on dark backgrounds. Green is a logo/accent color; it is too light for small text on white.
- The wordmark is the official custom outlined artwork; do not retype or substitute its letters. Use the written name **WLKR Labs** in ordinary copy.
- Geist Regular (400) for body copy; 650 for strong headings. The included original variable font and OFL license support editable brand applications; supporting lettering in exported graphics is outlined.

## Spacing and sizes

Keep at least one quarter of a block's width clear around the visible mark. The mark exports include this padding. Do not crop or stretch them. Keep the ascending 3 / 2 / 1 arrangement and one green top block. Do not add gradients, outlines or new effects.

Use a mark at 24px or larger in ordinary interfaces. The supplied 16px favicon is a compact browser exception. Use the wordmark at 120px width or larger, preserving its original viewBox padding; keep additional clear space of at least half its visible letter height. For a horizontal lockup, use at least 180px width; use the mark alone when space is tighter. Circle-cropped avatars have additional safety padding.

The print PDFs contain vector shapes and outlined type. They use RGB color; request a printer proof and the printer's color conversion before a print order. There is no promise of exact neon-green reproduction in ordinary CMYK printing, and no print purchase is part of this setup.

These assets describe WLKR Labs' identity; they do not claim incorporation, nonprofit recognition or new product availability. The font retains its included OFL license; existing project licenses are unchanged.

## Lockup construction

Size from visible artwork, excluding the SVG canvas padding. Let **H** be the official wordmark's full visible letter height, including its ascenders.

- Horizontal: symbol height **1.16H**, visible gap **0.45H**. Raise the symbol **0.06H** relative to geometric center alignment to compensate for the heavier bottom rows. The former pairing made the symbol about **2.10H** tall.
- Stacked: symbol height **2.10H**, vertical gap **0.60H**. Shift the symbol left by **10% of its visible width** relative to the wordmark center, accounting for the staircase's right-heavy shape.
- Scale each finished lockup uniformly. Do not reconstruct it by independently resizing the mark and wordmark. All branded social/print templates and the gallery header use these same masters.

These ratios are WLKR-specific design choices, evaluated on light/dark backgrounds and at small sizes; they are not universal logo rules. The research informed the method: [Docusign's guidance](https://brand.docusign.com/logo) considers visual weight and fixed icon/wordmark relationships; [Williams' guidance](https://identity.williams.edu/) calls for optical alignment and margins; [Atlassian's guidance](https://atlassian.design/foundations/logos) measures clearance using letterforms. No other brand's artwork is included.

## Rebuild and verify

The generator reads the original mark and the revised wordmark master in `source/`, with the included licensed Geist font for supporting typography. It preserves the approved artwork rather than retyping it. Python tools stay in ignored `.local/`; Node uses the existing website's Sharp dependency.

```sh
python3 -m venv .local/brand-tools
.local/brand-tools/bin/python -m pip install -r brand/requirements.txt
./project brand:build
./project brand:check
./project docs:check
```

`manifest.json` records file sizes and SHA-256 hashes. Checks validate hashes, unchanged rectangle geometry, the repaired r/spacing and removed slash, exact production wordmark paths and fills in every application, portable outlined lettering, rendered lockup proportions/spacing/alignment, icon/social dimensions, transparent logo alpha, ICO contents, and physical print PDF sizes. The completed zip is saved under ignored `.local/foundation-2026-10-06/support/`.
