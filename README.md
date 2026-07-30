# CHSE Odisha +2 Physics Notes

Free, handwritten-style Physics notes for CHSE Odisha Class XI & XII (+2 1st and 2nd year), built as a static
website. Every chapter follows the official rationalised CHSE Physics syllabus (2023–24) and includes:

- Full concept notes in a "handwritten notebook" style (Kalam/Caveat fonts, ruled paper, sticky notes)
- Hand-drawn-style diagrams for every major concept, rendered live with [rough.js](https://roughjs.com/)
- Step-by-step **derivations** for every result the CHSE syllabus expects you to derive
- Fully **worked numerical examples**, solved the way CHSE expects marks to be shown
- **Common mistake** and **score booster** callouts pulled from real exam-answer pitfalls
- A mark-wise **Exam Corner** (1/2/3/5-mark practice questions) at the end of every chapter
- A consolidated **Formula Sheet** per class for last-week revision
- A dedicated **Exam Strategy** page: the official marking scheme, answer-writing habits, and a study plan

**Live site:** once you enable GitHub Pages (see below), your site will be at
`https://<your-username>.github.io/<repo-name>/`

## Project structure

```
.
├── docs/                  # The built static website — THIS is what GitHub Pages serves
│   ├── index.html
│   ├── exam-strategy.html
│   ├── class11/           # 14 chapters + formula sheet + chapter index
│   ├── class12/           # 14 chapters + formula sheet + chapter index
│   └── assets/            # css/js, shared by every page
├── src/                    # Source of truth — edit THIS, not docs/, then rebuild
│   ├── generate.py         # Static site generator (Python + Jinja2)
│   ├── helpers.py          # Small helper functions used to build content blocks
│   ├── data_class11.py     # All Class XI content (14 chapters) as structured Python data
│   ├── data_class12.py     # All Class XII content (14 chapters) as structured Python data
│   ├── templates/          # Jinja2 HTML templates (base layout, chapter page, etc.)
│   └── assets/             # Source CSS/JS — copied into docs/assets/ on build
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

**Important:** `docs/` is generated output. If you want to change site content, edit files under `src/` and
re-run the build (below) — don't hand-edit `docs/*.html` directly, your changes will be overwritten next build.

## Building the site locally

Requires Python 3.8+.

```bash
pip install -r requirements.txt
python3 src/generate.py
```

This regenerates the entire `docs/` folder from the templates and content in `src/`. Open `docs/index.html`
directly in a browser to preview, or serve it locally:

```bash
cd docs && python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploying with GitHub Pages (free hosting)

1. Push this repository to GitHub (see **Getting this onto GitHub** below if you haven't already).
2. On GitHub, go to **Settings → Pages**.
3. Under "Build and deployment", set **Source: Deploy from a branch**.
4. Set **Branch: main**, folder **`/docs`**, then click **Save**.
5. GitHub will give you a live URL within a minute or two — that's your free, public physics notes site.

Every time you push an update to `docs/` (after rebuilding from `src/`), the live site updates automatically.

## Getting this onto GitHub

If this project isn't a GitHub repo yet:

```bash
cd chse-physics-notes        # this folder
git init
git add .
git commit -m "Initial commit: CHSE Odisha +2 Physics notes site"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Then enable Pages as described above.

## How the content is organised

Content lives as structured Python data (not raw HTML) so it's easy to extend consistently. Each chapter is
built from small helper functions in `src/helpers.py`:

| Helper | Renders as |
|---|---|
| `p(text)` | A paragraph |
| `lst([...])` / `olist([...])` | Bullet / numbered list |
| `formula(title, lines)` | A boxed formula callout |
| `diagram(name, caption, w, h)` | A hand-drawn diagram (see `src/assets/js/sketch.js` for available diagram names) |
| `sticky(title, text, color)` | A sticky-note style aside |
| `mnemonic(text)` | A "Yaad Rakho" memory-aid box |
| `derivation(title, given, steps, result)` | A full step-by-step derivation |
| `solved(problem, steps, answer)` | A fully worked numerical example |
| `mistake(text)` / `tip(text)` | Red "don't lose marks" / green "score booster" callouts |
| `pyq(marks, question)` | One Exam Corner practice question, tagged by mark value |

See `CONTRIBUTING.md` for exactly how to add a new chapter or extend an existing one.

## Content accuracy & license

- Chapter scope follows the official CHSE Odisha rationalised Physics syllabus (Class XI–XII, 2023–24), sourced
  from `chseodisha.nic.in`. The Exam Corner questions are written **in the board's question style** for practice —
  they are not reproductions of any specific year's actual question paper.
- **Code** (generator, templates, CSS/JS) is MIT licensed — see `LICENSE`.
- **Written notes content** (chapter text, derivations, explanations, questions) is offered under
  [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — free to share and adapt for
  non-commercial educational use, with attribution, under the same license.
- Please cross-check chapter weightage and the latest exam pattern against the current year's official CHSE
  circular before relying on this for exam planning — syllabi are occasionally revised.

## Roadmap ideas

- [ ] Add previous-year CHSE question paper links (official, once sourced) for extra practice
- [ ] Add a printable/PDF export per chapter
- [ ] Add short answer-key hints for the Exam Corner questions
- [ ] Chemistry / Biology / Maths notes as sibling sections, same handwritten style
