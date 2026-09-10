# Resume Matcher: Clean

A standalone LaTeX adaptation of Resume Matcher's `clean` template.
All example names, employers, achievements, and contact details are fictional.
The sample was written for this template; no uploaded applicant resume was used.
Social/profile links point to `example.com` placeholders. Replace their targets
and labels before using the resume.

## Overleaf

1. Upload this entire folder as a ZIP using **New Project → Upload Project**.
2. Set the main document to `main.tex` and the compiler to **pdfLaTeX**.
3. Edit `resume.tex`, then click **Recompile**.

You need every `.tex` and `.sty` file in this folder. No Resume Matcher
installation, external font files, shell escape, or custom build step is required.
The packages and fonts are supplied by TeX Live on Overleaf.

## Local compilation

With a TeX Live or MiKTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, run `latexmk -pdf main.tex`. The output is `main.pdf`.

## Editing

- `resume.tex`: name, title, contacts, summary, experience, projects, education,
  skills, languages, training, awards, and commented custom-section examples.
- `main.tex`: A4/Letter paper, margins, spacing, name size, icons, accent color,
  and PDF title/author. Update the PDF metadata when replacing the sample name.
- `resume-matcher.sty`: included formatting commands. Usually no edits are needed.

Use `\item` for bullets and `\plainitem` for unbulleted rows inside `highlights`.
Escape special characters: `\&`, `\%`, `\$`, `\#`, `\_`, `\{`, `\}`.
Write backslashes as `\textbackslash{}`, tildes as `\textasciitilde{}`, and
carets as `\textasciicircum{}`. Normal accented Latin letters work with pdfLaTeX;
other scripts need appropriate language/font setup and are not configured here.

Move entire section blocks in `resume.tex` to reorder them. Delete a heading together with its content to hide a section.

Copy a `project` block for publications or research. A `resumesection` followed
by plain text or a `highlights` list creates other custom sections.
Omit optional entry fields by leaving their braces empty, for example `{}`.
To remove a contact, delete its whole `\contact` command and one adjoining
`\contactsep`. To hide location, clear the header location argument and remove
its contact command if present.
Use short display labels with `\href{long URL}{label}` for long contact URLs.

For US Letter, change `a4paper` to `letterpaper` in `main.tex`. To fit more text,
edit the content first, then adjust spacing or margins; avoid making the text
uncomfortably small. Long resumes flow onto additional pages.

This preserves the web template's visual character using TeX Live typefaces;
it is not a pixel-identical browser PDF. PDF text is selectable, but extraction
order in columns varies by parser and no ATS compatibility guarantee is made.

## License and credits

Apache-2.0. Keep `LICENSE` and `NOTICE` when redistributing the template source.
Adapted from [Resume Matcher](https://github.com/srbhr/Resume-Matcher),
release 1.3 Crescendolls (`0932418c`). Font Awesome and TeX Gyre fonts are
provided by the TeX installation under their own licenses; their files are not
redistributed in this project.

[Overleaf upload instructions](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project)
