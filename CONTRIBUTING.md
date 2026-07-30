# Contributing

Thanks for helping improve these notes! This project is plain Python + Jinja2 + static HTML/CSS/JS — no build
tools, no npm, nothing to install beyond `pip install -r requirements.txt`.

## Before you start

1. Fork/clone the repo.
2. `pip install -r requirements.txt`
3. `python3 src/generate.py` to build `docs/` and confirm it works before you change anything.

## Adding a solved example, derivation, or exam question to an existing chapter

1. Open `src/data_class11.py` or `src/data_class12.py` and find the `chapter(...)` call for the chapter you want
   to edit (search for its id, e.g. `"ch08"`).
2. Each chapter has a `sections=[...]` list. Add your new content as a block inside the relevant `section(...)`,
   using the helpers imported at the top of the file:

   ```python
   solved(
       "A 2 kg block slides down a frictionless incline of angle 30°. Find its acceleration.",
       [
           "Component of gravity along incline = g sinθ = 10 × sin30°",
           "a = g sinθ = 10 × 0.5",
       ],
       "a = 5 m/s²",
   ),
   ```

3. To add an Exam Corner question, find the chapter's `exam_corner=[...]` list (at the end of the `chapter(...)`
   call) and add a `pyq(marks, "question text")` — `marks` must be `1`, `2`, `3`, or `5` to match CHSE's format.
4. Rebuild and check your addition renders: `python3 src/generate.py`, then open the relevant page in
   `docs/<class>/<chapter-id>.html`.

## Adding a brand-new chapter

1. Add a `chapter(...)` call inside the right `add_unit(...)` block (or create a new `add_unit(...)` if it's a
   new syllabus unit) in `data_class11.py` / `data_class12.py`.
2. Give it a unique `id` (e.g. `"ch16"`), the next `number`, a `title`, a one-line `tagline`, `tags`, `sections`,
   `recap`, and ideally an `exam_corner`.
3. `CHAPTERS_FLAT` at the bottom of the file is derived automatically — you don't need to touch it.
4. Rebuild (`python3 src/generate.py`) and check the new chapter appears on the class index page, and that
   prev/next navigation on neighbouring chapters links correctly.

## Adding a new hand-drawn diagram

Diagrams are drawn live in the browser with [rough.js](https://roughjs.com/), defined in
`src/assets/js/sketch.js`.

1. Add a new function to the `DIAGRAMS` object, e.g. `DIAGRAMS.myNewDiagram = function(id) { ... }`. Look at
   existing functions for the pattern — you get a Rough.js canvas (`rc`), a 2D context (`ctx`), and helper
   functions `arrow()`, `label()`, `axes()`, `sineWave()` already defined in the file.
2. Reference it in content with `diagram("myNewDiagram", "Caption text", width, height)`.
3. Rebuild and open the chapter page — if the canvas is blank, check the browser console for the diagram name
   typo (the generator's link-checker only verifies internal `href`s, not diagram names, so double-check by eye).

## Style guidelines

- Keep explanations conversational but precise — this is exam-prep material, factual accuracy matters more than
  flourish.
- Stick to the official CHSE rationalised syllabus scope (see the syllabus PDF linked in `README.md`) — don't
  add topics that have been explicitly excluded (e.g. radioactive decay law is *not* in the current Nuclei
  chapter's scope).
- Exam Corner questions should be written **in CHSE's question style**, not copied from any specific year's
  actual paper — label things as "CHSE-style practice questions," not "previous year questions," unless you can
  verify the source.
- Always include units in solved-example answers.
- Run `python3 src/generate.py` and skim the changed page before opening a pull request.

## Reporting an error

If you spot a factual or numerical error, please open an issue with the chapter id (e.g. `ch08`) and a short
description — physics content errors get priority review.
