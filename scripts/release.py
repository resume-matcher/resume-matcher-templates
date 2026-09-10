#!/usr/bin/env python3
"""Build isolated template projects, render previews, and create release ZIPs."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PROJECT_FILES = ("main.tex", "resume.tex", "resume-matcher.sty", "README.md", "LICENSE", "NOTICE")
TEMPLATES = (
    "swiss-single", "swiss-two-column", "modern", "modern-two-column", "latex", "clean", "vivid"
)


def run(command: list[str], cwd: Path) -> str:
    """Run a build command and preserve diagnostic output on failure."""
    result = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=120)
    if result.returncode:
        raise RuntimeError(f"Command failed: {' '.join(command)}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def sync_sources() -> None:
    """Keep a complete local style package in every independently usable project."""
    for slug in TEMPLATES:
        shutil.copyfile(ROOT / "shared/resume-matcher.sty", ROOT / "templates" / slug / "resume-matcher.sty")


def compile_project(engine: str, folder: Path) -> None:
    """Compile twice, rejecting overflow and missing glyphs as well as TeX errors."""
    for _ in range(2):
        run([engine, "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", "main.tex"], folder)
    log = (folder / "main.log").read_text(encoding="utf-8", errors="replace")
    errors = re.findall(r"^.*(?:Overfull \\[hv]box|Missing character:|LaTeX Font Warning).*$", log, re.MULTILINE)
    if errors:
        raise RuntimeError(f"Layout/font problems in {folder.name}:\n" + "\n".join(errors))


def package_template(slug: str, dist: Path) -> Path:
    """Place main.tex at ZIP root so Overleaf finds it without extra configuration."""
    target = dist / f"resume-matcher-{slug}.zip"
    with ZipFile(target, "w", compression=ZIP_DEFLATED) as archive:
        for name in PROJECT_FILES:
            archive.write(ROOT / "templates" / slug / name, name)
    return target


def verify_archive(archive: Path, engine: str, renderer: str, previews: Path, slug: str) -> None:
    """Build the actual upload ZIP in a fresh directory, without repository inputs."""
    with tempfile.TemporaryDirectory(prefix=f"resume-matcher-{slug}-") as temporary:
        folder = Path(temporary)
        with ZipFile(archive) as project:
            project.extractall(folder)
        compile_project(engine, folder)
        shutil.copyfile(folder / "main.pdf", previews / f"{slug}.pdf")
        run([renderer, "-f", "1", "-singlefile", "-scale-to", "1400", "-png", "main.pdf", str(previews / slug)], folder)


def package_collection(dist: Path) -> Path:
    """Create the repository handoff with upload ZIPs, excluding scratch/self."""
    target = dist / "resume-matcher-templates.zip"
    with ZipFile(target, "w", compression=ZIP_DEFLATED) as archive:
        paths = [ROOT / name for name in ("README.md", "LICENSE", "NOTICE", ".gitignore", "VALIDATION.md")]
        paths += [ROOT / "shared/resume-matcher.sty", ROOT / "scripts/release.py", ROOT / "scripts/verify.py"]
        for slug in TEMPLATES:
            paths += [ROOT / "templates" / slug / name for name in PROJECT_FILES]
            paths += [ROOT / "previews" / f"{slug}.{suffix}" for suffix in ("pdf", "png")]
            paths += [dist / f"resume-matcher-{slug}.zip"]
        for path in sorted(paths):
            relative = path.relative_to(ROOT)
            if not path.is_file():
                raise FileNotFoundError(f"Missing release file: {relative}")
            archive.write(path, Path("resume-matcher-templates") / relative)
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", default="pdflatex", help="pdfLaTeX executable name or absolute path")
    parser.add_argument("--sync-only", action="store_true", help="Copy the shared style to each project without building")
    args = parser.parse_args()
    sync_sources()
    if args.sync_only:
        print("Updated the style package in all seven standalone projects.")
        return
    engine = shutil.which(args.engine)
    renderer = shutil.which("pdftoppm")
    if not engine or not renderer:
        parser.error("Install TeX Live (pdflatex) and Poppler (pdftoppm), or set --engine to the pdfLaTeX path.")
    dist = ROOT / "dist"
    previews = ROOT / "previews"
    dist.mkdir(exist_ok=True)
    previews.mkdir(exist_ok=True)
    for slug in TEMPLATES:
        archive = package_template(slug, dist)
        verify_archive(archive, engine, renderer, previews, slug)
        print(f"Verified {slug}: {archive.relative_to(ROOT)}", flush=True)
    collection = package_collection(dist)
    print(f"Repository handoff: {collection.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
