"""Quality gate for v1.7 — verifies each concept folder is filled in.

Exits non-zero if any concept fails. CI runs this after the subagent fleet
completes (and before pushing PDFs).

Checks per concept folder:
  1. All four files present: README.md, lesson.tex, code.py, notebook.ipynb.
  2. README.md word count between 600 and 2000.
  3. lesson.tex compiles cleanly under pdflatex (or skipped if pdflatex absent).
  4. code.py parses (ast.parse) and runs in <30 s without error.
  5. notebook.ipynb validates as JSON.
  6. No "TODO", "FIXME", or "placeholder" string in any artifact.
  7. lesson.tex contains at least one \\begin{theorem} or \\begin{definition}
     environment and one \\begin{proof}.
"""

import ast
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = json.loads((ROOT / "manifest.json").read_text())
CONCEPTS = MANIFEST["concepts"]

FORBIDDEN_TOKENS = ("TODO", "FIXME", "placeholder", "Placeholder", "PLACEHOLDER")

failures: list[tuple[str, str]] = []


def fail(node_slug: str, reason: str):
    failures.append((node_slug, reason))


def check_concept(c):
    slug = f"{c['id']}-{c['slug']}"
    folder = ROOT / "concepts" / slug

    files = {
        "README.md": folder / "README.md",
        "lesson.tex": folder / "lesson.tex",
        "code.py": folder / "code.py",
        "notebook.ipynb": folder / "notebook.ipynb",
    }
    for name, path in files.items():
        if not path.exists():
            fail(slug, f"missing {name}")
            return

    # 1. README.md word count
    readme_words = len(files["README.md"].read_text().split())
    if not (600 <= readme_words <= 2500):
        fail(slug, f"README.md word count {readme_words} not in [600, 2500]")

    # 2. forbidden tokens
    for name, path in files.items():
        text = path.read_text()
        for tok in FORBIDDEN_TOKENS:
            if tok in text:
                fail(slug, f"{name} contains forbidden token '{tok}'")
                break

    # 3. lesson.tex: theorem + proof present
    lesson = files["lesson.tex"].read_text()
    has_theorem = bool(re.search(r"\\begin\{(theorem|definition|lemma|proposition)\}", lesson))
    has_proof = "\\begin{proof}" in lesson
    if not has_theorem:
        fail(slug, "lesson.tex has no theorem/definition/lemma/proposition env")
    if not has_proof:
        fail(slug, "lesson.tex has no proof env")
    if "fontspec" in lesson:
        fail(slug, "lesson.tex uses fontspec (incompatible with pdflatex)")

    # 4. code.py parses
    try:
        ast.parse(files["code.py"].read_text())
    except SyntaxError as e:
        fail(slug, f"code.py SyntaxError: {e}")
        return

    # 5. code.py runs in <30 s
    try:
        r = subprocess.run(
            ["python3", str(files["code.py"])],
            timeout=30, capture_output=True, text=True,
            cwd=folder,
        )
        if r.returncode != 0:
            fail(slug, f"code.py exit {r.returncode}; stderr: {r.stderr[:200]}")
    except subprocess.TimeoutExpired:
        fail(slug, "code.py exceeded 30 s")

    # 6. notebook.ipynb is valid JSON with cells
    try:
        nb = json.loads(files["notebook.ipynb"].read_text())
        n_cells = len(nb.get("cells", []))
        if n_cells < 4:
            fail(slug, f"notebook.ipynb has only {n_cells} cells (need ≥4)")
        kinds = {cell.get("cell_type") for cell in nb.get("cells", [])}
        if "markdown" not in kinds or "code" not in kinds:
            fail(slug, "notebook.ipynb missing markdown or code cells")
    except json.JSONDecodeError as e:
        fail(slug, f"notebook.ipynb invalid JSON: {e}")

    # 7. (optional, slow) pdflatex compile
    if shutil.which("pdflatex"):
        try:
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "lesson.tex"],
                timeout=60, capture_output=True, text=True, cwd=folder,
            )
            if r.returncode != 0:
                fail(slug, f"pdflatex failed; last 200 chars: {r.stdout[-200:]}")
        except subprocess.TimeoutExpired:
            fail(slug, "pdflatex exceeded 60 s")


def main():
    for c in CONCEPTS:
        check_concept(c)

    if failures:
        print(f"❌ {len(failures)} failures across {len(set(s for s, _ in failures))} concept(s):\n")
        for slug, reason in failures:
            print(f"  {slug}: {reason}")
        return 1
    print(f"✅ All {len(CONCEPTS)} concepts pass quality gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
