#!/usr/bin/env python3
"""Exercise A4, Letter, icons, location edits, Unicode, and multi-page resumes."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import release

parser = argparse.ArgumentParser(description="Compile and inspect all template variants with pdfLaTeX and Poppler.")
parser.add_argument("--engine", default="pdflatex")
parser.add_argument("--output-dir", type=Path, default=ROOT / "_build")
args = parser.parse_args()
engine = shutil.which(args.engine)
if not engine or not shutil.which("pdfinfo") or not shutil.which("pdftotext"):
    parser.error("Install pdfLaTeX and Poppler, or provide --engine /path/to/pdflatex")
release.sync_sources()
results = []
for slug in release.TEMPLATES:
    for variant in ('a4', 'letter', 'icons', 'long', 'omissions', 'edits'):
        folder = args.output_dir / f'{slug}-{variant}'
        folder.mkdir(parents=True, exist_ok=True)
        for name in release.PROJECT_FILES:
            shutil.copyfile(ROOT/'templates'/slug/name, folder/name)
        main = (folder/'main.tex').read_text(encoding="utf-8")
        content = (folder/'resume.tex').read_text(encoding="utf-8")
        expected = ['Sarah Chen', 'Fernway Payments', 'University of Washington', '38%', '2024']
        if variant == 'letter':
            main=main.replace('a4paper','letterpaper')
        if variant == 'icons':
            main=main.replace('\\ResumeIconsfalse','\\ResumeIconstrue')
            content=content.replace('{San Francisco, CA}{','{Pune, India}{',1)
            expected.append('Pune, India')
        if variant == 'long':
            extra = r'''
\resumesection{Additional Work and Publications}
\experience{International Research and Development Collaborative}{Senior Infrastructure and Developer Experience Engineer}{New Delhi, India}{September 2020 -- December 2025}
\begin{highlights}
\item Wrote a technical guide covering reliable APIs, accessible interfaces, and clear documentation for distributed teams.
\plainitem\textit{Plain description: Fran\c{c}ois, Jos\'e, M\"uller; R\&D; 50\%; \$100; \#1; data\_tools.}
\item Maintained developer tools used across product groups and measured improvements in response time.
\end{highlights}
'''
            extra=extra*12+r'\par MAIN-CONTENT-END\par'
            if '\\resumesidebar' in content:
                content=content.replace('\\resumesidebar',extra+'\n\\resumesidebar')
                sidebar=(r'\resumesection{Community Work}\skillgroup{Mentoring}{Workshops on documentation, accessibility, and software testing.}'+'\n')*25+r'\par SIDEBAR-CONTENT-END\par'
                content=content.replace('\\end{resumecolumns}',sidebar+'\n\\end{resumecolumns}')
                expected.append('SIDEBAR-CONTENT-END')
            else:
                content += '\n'+extra
            expected.extend(['MAIN-CONTENT-END','Plain description:', 'François', 'José', 'Müller', 'R&D;', '50%;', '$100;', '#1;', 'data_tools.'])
        if variant == 'omissions':
            content = r'''
\resumeheader{Sarah}{Chen}{}{}{}
\resumesection{Omission Checks}
\education{Optional University}{}{}{2021}
\experience{}{Independent Consultant}{}{2026}
\experience{Example Company}{}{}{}
\education{}{Bachelor of Science}{}{}
\project{Independent Project}{}{}{}
\begin{highlights}
  \item Optional fields can be empty.
\end{highlights}
'''
            expected = ['Sarah Chen', 'Optional University', 'Independent Consultant', 'Example Company', 'Bachelor of Science', 'Independent Project']
        if variant == 'edits':
            content = content.replace(r'\resumeheader{Sarah}{Chen}', r'\resumeheader{Sarah}{Chen García de la Cruz}')
            content += r'''
\resumesection{Résumé and Custom Links}
François, José, and Müller collaborated on R\&D with a \$100 budget.
\href{https://example.com/docs?topic=resume\&lang=en\#sample}{Documentation link}.
'''
            expected[0] = 'Sarah Chen García de la Cruz'
            expected.extend(['François, José, and Müller', 'R&D', '$100', 'Documentation link'])
        (folder/'main.tex').write_text(main, encoding="utf-8")
        (folder/'resume.tex').write_text(content, encoding="utf-8")
        release.compile_project(engine,folder)
        info=release.run(['pdfinfo','main.pdf'],folder)
        page_count=int(next(line.split(':')[1] for line in info.splitlines() if line.startswith('Pages:')))
        text=release.run(['pdftotext','-layout','main.pdf','-'],folder)
        normalized=' '.join(text.split())
        for marker in expected:
            assert marker in normalized, (slug,variant,'missing',marker)
        if variant == 'omissions':
            assert '|' not in normalized, (slug, variant, 'dangling separator')
        if variant == 'edits':
            links = release.run(['pdfinfo', '-url', 'main.pdf'], folder)
            assert 'https://example.com/docs?topic=resume&lang=en#sample' in links, (slug, variant, 'link target changed')
        if variant == 'long':
            assert page_count >= 2, (slug,variant,page_count)
        else:
            assert page_count == 1, (slug,variant,page_count)
        size=next(line for line in info.splitlines() if line.startswith('Page size:'))
        if variant == 'letter':
            assert '612 x 792' in size, size
        results.append({'template':slug,'variant':variant,'pages':page_count,'page_size':size})
        print(slug,variant,page_count,'pages; text and log checks passed',flush=True)
(args.output_dir / 'verification.json').write_text(json.dumps(results,indent=2)+'\n', encoding="utf-8")
