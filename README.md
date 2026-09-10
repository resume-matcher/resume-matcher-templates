# Resume Matcher Templates

Seven standalone, editable LaTeX resume templates adapted from
[Resume Matcher](https://github.com/srbhr/Resume-Matcher). Upload one template ZIP
to Overleaf, edit the sample content, and compile with **pdfLaTeX**.

Each project includes its own styling files. There are no dependencies on the
Resume Matcher app, no external font downloads, and no shell-escape requirement.
All names, employers, accomplishments, and contact details in the samples are fictional.
The resume content was written as demonstration data, not copied from an uploaded
resume or the application database. PDF author/title fields also use the sample
name. Social/profile links deliberately point to `example.com` placeholders;
replace both their labels and destinations before using the resume. Real place
names and technology names are used for context. Project attribution links refer
to the actual Resume Matcher repository.

## Start here

Each template is an independent project. Its ZIP includes `main.tex`,
`resume.tex`, and the custom `.sty` file it needs. Keep those files together.
You do not need the Resume Matcher application, Python, or the other templates
when editing and compiling a single resume.

- **Use Overleaf:** choose a preview below, upload the matching ZIP from `dist/`,
  and follow [Use on Overleaf](#use-on-overleaf).
- **Work locally:** open a folder such as `templates/clean/`, edit `resume.tex`,
  and follow [Compile locally](#compile-locally).
- **Customize the appearance:** edit `main.tex` using the [settings reference](#customize).
- **Maintain this collection:** see [Maintain and release the collection](#maintain-and-release-the-collection).

```text
resume-matcher-templates/
├── README.md             Start here: usage and customization
├── templates/            Seven independent, editable LaTeX projects
├── dist/                 Individual Overleaf ZIPs and the complete collection ZIP
├── previews/             Sample PDF and PNG for every design
├── shared/               Maintained source of the common styling package
├── scripts/              Optional release and verification tools for maintainers
├── VALIDATION.md         Compatibility checks and known limitations
├── LICENSE               Apache-2.0 license
└── NOTICE                Attribution
```

The PDFs in `previews/` are examples. Compile your edited source to produce your
own resume. All supplied applicant details are dummy data.

## Choose a template

| Template            | Layout and character                                               | Overleaf project                                          | Preview                               |
| ------------------- | ------------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------- |
| Swiss Single Column | Centered serif name, black ruled headings, sans serif body         | [Download ZIP](dist/resume-matcher-swiss-single.zip)      | [PDF](previews/swiss-single.pdf)      |
| Swiss Two Column    | Centered header, 65/35 columns, subtle vertical divider            | [Download ZIP](dist/resume-matcher-swiss-two-column.zip)  | [PDF](previews/swiss-two-column.pdf)  |
| Modern              | Centered name with accent underline, colored ruled headings        | [Download ZIP](dist/resume-matcher-modern.zip)            | [PDF](previews/modern.pdf)            |
| Modern Two Column   | Left-aligned header, 65/35 columns, accent divider                 | [Download ZIP](dist/resume-matcher-modern-two-column.zip) | [PDF](previews/modern-two-column.pdf) |
| LaTeX Classic       | Serif type, small-caps name, company-first entries                 | [Download ZIP](dist/resume-matcher-latex.zip)             | [PDF](previews/latex.pdf)             |
| Clean               | Sans serif type, light name, gray uppercase headings               | [Download ZIP](dist/resume-matcher-clean.zip)             | [PDF](previews/clean.pdf)             |
| Vivid               | Two-tone name, 63/37 columns, colored small caps and arrow bullets | [Download ZIP](dist/resume-matcher-vivid.zip)             | [PDF](previews/vivid.pdf)             |

<table>
  <tr>
    <td><a href="previews/swiss-single.pdf"><img src="previews/swiss-single.png" width="240" alt="Swiss Single Column preview"></a></td>
    <td><a href="previews/swiss-two-column.pdf"><img src="previews/swiss-two-column.png" width="240" alt="Swiss Two Column preview"></a></td>
    <td><a href="previews/modern.pdf"><img src="previews/modern.png" width="240" alt="Modern preview"></a></td>
  </tr>
  <tr>
    <td><a href="previews/modern-two-column.pdf"><img src="previews/modern-two-column.png" width="240" alt="Modern Two Column preview"></a></td>
    <td><a href="previews/latex.pdf"><img src="previews/latex.png" width="240" alt="LaTeX Classic preview"></a></td>
    <td><a href="previews/clean.pdf"><img src="previews/clean.png" width="240" alt="Clean preview"></a></td>
  </tr>
  <tr>
    <td><a href="previews/vivid.pdf"><img src="previews/vivid.png" width="240" alt="Vivid preview"></a></td>
  </tr>
</table>

## Use on Overleaf

1. Download the ZIP for **one template** from the table above. On GitHub, open
   the ZIP's file page and use **Download raw file**.
2. In Overleaf, select **New Project → Upload Project** and upload that ZIP.
3. Set **Main document** to `main.tex` and **Compiler** to **pdfLaTeX**.
4. Open `resume.tex` and replace the fictional name, experience, education,
   skills, and contact details. Update both the display text and destination of
   each link, including the `example.com` social-profile placeholders.
5. In `main.tex`, change the `pdftitle` and `pdfauthor` values in `\hypersetup`.
   Adjust the paper size and other formatting settings if needed.
6. Select **Recompile**, inspect every page, and use **Download PDF** to save
   your finished resume.

Use TeX Live 2025 or 2026 with **pdfLaTeX**; both versions passed the local
compatibility checks. The Overleaf service itself has not been exercised.

Overleaf documents this workflow in
[Uploading a project](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project).
The individual template ZIPs contain `main.tex` at the root so there is one clear
main document. The collection ZIP is intended for the GitHub repository handoff;
upload a single template ZIP to Overleaf.

## What's in each project

```text
main.tex             Paper size, spacing, colors, icons, PDF metadata
resume.tex           Your resume content and custom-section examples
resume-matcher.sty   All template formatting commands, included locally
README.md            Editing and compilation instructions
LICENSE              Apache-2.0 license
NOTICE               Source attribution and adaptation notice
```

Start with the supplied examples. Move complete section blocks to reorder them,
or delete a heading with its content to hide a section. The two-column projects
place main content before `\resumesidebar` and supporting content after it.
Columns can continue onto additional pages. Entries reserve space for headings
and initial content, while long bullet lists may continue on the next page.

## Customize

| Setting              | Where to edit                                                                       |
| -------------------- | ----------------------------------------------------------------------------------- |
| A4 or US Letter      | `a4paper` / `letterpaper` in `main.tex`                                             |
| Body size            | `10pt`, `11pt`, or `12pt` in `\documentclass`                                       |
| Margins              | `\geometry{top=12mm,bottom=12mm,left=12mm,right=12mm}`                              |
| Section/item spacing | `\ResumeSectionGap` / `\ResumeItemGap`                                              |
| Line spacing         | `\ResumeLineSpread`                                                                 |
| Name size            | `\ResumeNameSize`                                                                   |
| Accent               | `\definecolor{ResumeAccent}{HTML}{1D4ED8}`; Modern and Vivid designs                |
| Contact icons        | `\ResumeIconstrue` / `\ResumeIconsfalse`                                            |
| Column split         | `\ResumeColumnRatio`; 0.65 normally, 0.63 for Vivid                                 |
| Heading font         | `\renewcommand{\ResumeHeadingFont}{\rmfamily}` (serif), `\sffamily`, or `\ttfamily` |
| Body font            | `\renewcommand{\familydefault}{\rmdefault}`, `\sfdefault`, or `\ttdefault`          |

For compact spacing, reduce the two gap lengths and line spread. The samples use
12 mm margins for comfortable editing; the app's browser defaults are denser.
TeX Gyre Termes, Heros, and Cursor replace the browser's serif, sans serif, and
monospace font stacks. The designs preserve their visual character, not exact
browser line breaks. The Modern Two Column name underline is a solid accent rule
instead of a CSS gradient. Icons are off by default, as in the app.

### Content commands

```tex
\resumesection{Experience}
\experience{Company}{Role}{Location}{2023 -- Present}
\begin{highlights}
  \item Improved reliability by \textbf{35\%}.
  \plainitem\textit{An unbulleted description or continuation line.}
\end{highlights}

\project{Project name}{Role or technologies}{2024}{https://example.com}
\education{University}{Degree}{City}{2017 -- 2021}
\skillgroup{Languages}{Python, TypeScript, SQL}
```

Custom sections support paragraphs, entry lists (publications, research), or bullet
lists. Commented examples are included in every `resume.tex`.
Leave optional entry arguments empty with `{}`. To remove a contact, delete its
whole `\contact` command and one adjoining `\contactsep`. To hide the location,
clear the header's location argument and remove its contact command if present.
Rename headings directly to translate them.
The style also includes `\skilltag{Python}` for short boxed skill labels.

Escape `&`, `%`, `$`, `#`, `_`, `{`, and `}` as `\&`, `\%`, `\$`, `\#`, `\_`,
`\{`, and `\}`. Use `\textbackslash{}`, `\textasciitilde{}`, and
`\textasciicircum{}` for the other special characters. Use `\url{...}` for URLs
or `\href{...}{short label}` for readable links. Accented Latin text is supported
by the supplied pdfLaTeX setup. CJK, Arabic, and other scripts require additional
language/font configuration; this collection does not promise automatic multilingual
conversion from the app.

The PDF contains selectable text and real hyperlinks. Two-column extraction order
depends on the reader/parser; test with your target system. No ATS score or universal
parsing compatibility is implied.

## Compile locally

Install TeX Live or MiKTeX. From this collection's root, choose a template:

```sh
cd templates/clean
```

Replace `clean` with `swiss-single`, `swiss-two-column`, `modern`,
`modern-two-column`, `latex`, or `vivid` as desired. Edit `resume.tex` and the
PDF metadata in `main.tex`, then compile from that same template folder:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The resulting file is `main.pdf` in that template folder. Re-run these commands
after editing. Alternatively, run `latexmk -pdf main.tex`.

Standard TeX Live packages used here include
`lm` (Latin Modern math), `tex-gyre`, `geometry`, `xcolor`, `tools` (tabularx), `enumitem`, `needspace`,
`paracol`, `microtype`, `fontawesome5`, `xurl`, `hyperref`, and `iftex`.
Minimal TeX installations may need these installed with their package manager.
Overleaf supplies these packages. Once installed, compilation needs no network access.

## Troubleshooting

| Problem                                        | What to do                                                                                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `resume-matcher.sty` or `resume.tex` not found | Upload the complete individual template ZIP, or compile from the folder containing all three source files.                      |
| Overleaf compiles the wrong document           | Set **Main document** to `main.tex`; upload one template ZIP, not the whole collection ZIP.                                     |
| A standard package is missing locally          | Install the packages listed above using your TeX distribution's package manager, or use Overleaf.                               |
| Errors after pasting text                      | Check special characters such as `%`, `&`, `_`, and `$`; use the escaping examples in [Customize](#customize).                  |
| A contact still opens an example page          | Replace the URL argument as well as the visible contact label in `resume.tex`.                                                  |
| PDF properties still say Alex Morgan           | Update `pdftitle` and `pdfauthor` in `main.tex`, then recompile.                                                                |
| Content runs onto another page                 | Shorten the content or adjust spacing/margins in `main.tex`. Multi-page resumes are supported.                                  |
| Non-Latin characters fail to compile           | The included setup supports accented Latin text. CJK and right-to-left scripts need additional language and font configuration. |

## Maintain and release the collection

This `resume-matcher-templates` directory is ready to use as the repository root
under the [resume-matcher organization](https://github.com/resume-matcher).
Keep its `.gitignore`, license, notices, and complete directory structure.
No repository name is hard-coded into download links. GitHub and Overleaf gallery
publication are separate later steps; these files have not been published.

The copy in `shared/resume-matcher.sty` is the maintained source. Each template
has a checked-in copy so it works independently. Edit the shared version and run:

```sh
python3 scripts/release.py --sync-only
```

To rebuild previews and release ZIPs, install Python 3.10+, pdfLaTeX, and Poppler,
then run:

```sh
python3 scripts/release.py
```

For the wider compilation checks (A4, Letter, contact icons, location editing,
accented text, empty optional fields, longer names, URL query/fragment targets,
and multi-page content in all seven styles), run:

```sh
python3 scripts/verify.py
```

This uses Poppler's `pdfinfo` and `pdftotext` as well as pdfLaTeX. Scratch files
and a machine-readable report go into the ignored `_build/` directory.
Use `--engine /path/to/pdflatex --output-dir /path/to/test-output` to test a
different TeX Live installation without overwriting another test run.
See [VALIDATION.md](VALIDATION.md) for the delivered version's results and limits.

The release script copies the styling into all projects, creates seven upload ZIPs,
extracts each ZIP to a fresh temporary directory, compiles it twice with shell
escape disabled, rejects overflow/missing-glyph/font warnings, and renders preview
images. It also creates `dist/resume-matcher-templates.zip` containing the
repository sources, previews, and all seven individual Overleaf ZIPs. The handoff
archive excludes itself and local build scratch files. Its download and preview
links work immediately after the contents are copied into a new repository.

## Origin and license

Adapted from the seven templates under
`apps/frontend/components/resume/` in Resume Matcher, release **1.3 Crescendolls**,
commit `0932418c`. The template IDs remain the same as the app's IDs.

Apache License 2.0, matching the upstream repository. The included notices identify
these files as LaTeX adaptations. Vivid follows Resume Matcher's existing visual
design; no Awesome-CV class or source code is included. TeX Gyre and Font Awesome
are dependencies supplied by TeX Live and retain their own licenses.
