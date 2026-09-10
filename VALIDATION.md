# Validation

Rechecked locally on 6 September 2026 using **pdfLaTeX / TeX Live 2025 and 2026**
(`pdfTeX 1.40.28` and `1.40.29`) and Poppler. No Overleaf project was created or
uploaded. The 2025 run used a TinyTeX 2025.09 base with the required packages from
the frozen TeX Live 2025 archive; it is not a copy of Overleaf's server image.

## Compilation checks

Each of the seven template ZIPs is extracted into a fresh temporary directory
and compiled twice with shell escape disabled. Compilation uses only the files
in that ZIP and standard TeX Live packages. No parent-directory imports,
Resume Matcher app, downloaded fonts, or network access are needed at build time.

The release script rejects TeX errors, overfull horizontal/vertical boxes,
missing characters, and LaTeX font warnings. All seven release builds passed.

The wider checks in `scripts/verify.py` compiled **42 cases per TeX Live version**,
each twice: **84 successful cases** across both versions. Results agreed on both:

| Template            | A4 sample | US Letter sample | Contact icons and location edit | Long content |
| ------------------- | --------- | ---------------- | ------------------------------- | ------------ |
| Swiss Single Column | 1 page    | 1 page           | 1 page                          | 3 pages      |
| Swiss Two Column    | 1 page    | 1 page           | 1 page                          | 4 pages      |
| Modern              | 1 page    | 1 page           | 1 page                          | 3 pages      |
| Modern Two Column   | 1 page    | 1 page           | 1 page                          | 4 pages      |
| LaTeX Classic       | 1 page    | 1 page           | 1 page                          | 3 pages      |
| Clean               | 1 page    | 1 page           | 1 page                          | 3 pages      |
| Vivid               | 1 page    | 1 page           | 1 page                          | 4 pages      |

Each template also passed two one-page cases on both versions:

- **Omissions:** empty role/company/degree/location/date/URL fields, with extracted
  text checked for dangling pipe separators.
- **Edits:** a longer accented name, raw UTF-8 accented Latin text, a custom
  section, and a URL with query parameters and a fragment. The full hyperlink
  destination is checked with `pdfinfo -url`.

These checks confirm expected names, institutions, achievements, edited locations,
and end-of-content markers survive PDF text extraction. Long samples exercise
long role/company names, accented Latin characters, escaped special characters,
plain description rows, repeated custom sections, and independent overflow in
both columns. The actual accented names and escaped characters are asserted in
the extracted text, not just the surrounding sentence. US Letter dimensions are
checked explicitly. All 42 PDFs from each version passed physical text bounding-box
checks against page edges. The documented `latexmk -pdf` command also passed in
a clean standalone directory.

## Sample data and archive audit

The resume content was written as fictional demonstration data. No uploaded
applicant resume or application database was used. The sample uses Alex Morgan,
Northstar Labs, Meridian Systems, invented achievements, and placeholder contacts.
Real city and technology names provide context; coincidental matches to people or
organizations are possible.

PDF titles/authors also use Alex Morgan. All resume web-link targets now use
`example.com`, including the social/profile placeholders. Project attribution
links in the documentation and notices refer to the real Resume Matcher project.
The seven individual ZIPs contain only their six documented project files; the
collection contains 71 files, including the individual ZIPs. Archives are checked
for CRC errors, unsafe paths, stale contents, and stray local build files. No
private applicant details or local filesystem paths were found in delivered resume
sources, PDF metadata, text, or link annotations.

## Visual review

All seven final sample PDFs were rendered to PNG for inspection of alignment,
column widths, rules, typography, spacing, wrapping, and page boundaries.
Additional icon-enabled and multi-page samples were inspected for continuation
behavior. Omission and accented-edit samples were also rendered and inspected.
The included preview files show the final A4 samples.

An independent source review identified and prompted fixes for location values
being duplicated in contacts, education hierarchy in Swiss/Modern, ignored ZIPs,
and build artifacts leaking into repository handoff archives.

This recheck also fixed:

- `verify.py` failing on a fresh checkout because its parent output folder did
  not exist. The documented command now creates parent directories.
- Stray pipe separators in Clean education and Clean/Vivid experience when
  neighboring optional fields are empty.
- Generic social-profile destinations potentially pointing to unrelated real
  accounts; sample targets now stay under `example.com`.

Both Python scripts pass Python 3.10 syntax parsing and byte compilation; they
were executed with Python 3.14.5 during verification. Python 3.10 runtime execution
and other operating systems were not separately tested.

Frontend `npm run lint` also passed. The application itself was not changed.

## Limits

- Validated with local pdfLaTeX 2025/2026; the Overleaf service itself was not
  exercised. Set the main document to `main.tex` and use pdfLaTeX. Overleaf
  documents these settings in [Selecting a TeX Live version and LaTeX compiler](https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler).
- This is a visual adaptation with TeX Live fonts and editable LaTeX spacing,
  not a pixel-identical export from Chromium.
- Sample and extended test cases do not guarantee that arbitrary replacement
  content will fit on one page. Long content intentionally paginates.
- PDF text is selectable and extractable. ATS behavior and two-column reading
  order depend on the receiving parser and are not certified here.
- CJK and right-to-left scripts need additional language/font configuration.
- No GitHub repository or Overleaf gallery listing has been published.
