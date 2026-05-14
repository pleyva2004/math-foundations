"""Generate NOTATION.md and notation.tex from notation.json (single source of truth).

Outputs (both at repo root):
  NOTATION.md   — markdown table grouped by category, with rendered LaTeX columns
  notation.tex  — standalone-compilable LaTeX cheatsheet (pdflatex compatible)

Run:
  python3 generate_notation.py
"""

import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).parent
NOTATION = json.loads((ROOT / "notation.json").read_text())

# Display order for category sections (literal slugs from spec).
CATEGORY_ORDER = [
    "logic",
    "sets",
    "functions",
    "numbers",
    "linear-algebra",
    "analysis",
    "calculus",
    "series-and-limits",
    "probability",
    "distributions",
    "information",
    "stochastic",
    "optimization",
    "geometry",
    "meta",
]

CATEGORY_LABEL = {
    "logic": "Logic",
    "sets": "Sets",
    "functions": "Functions",
    "numbers": "Number systems",
    "linear-algebra": "Linear algebra",
    "analysis": "Analysis",
    "calculus": "Calculus",
    "series-and-limits": "Series and modes of convergence",
    "probability": "Probability",
    "distributions": "Distributions",
    "information": "Information theory",
    "stochastic": "Stochastic calculus",
    "optimization": "Optimisation",
    "geometry": "Information geometry and optimal transport",
    "meta": "Meta-notation",
}


def group_by_category(entries):
    """Return OrderedDict mapping category -> list of entries, in CATEGORY_ORDER."""
    buckets = OrderedDict((cat, []) for cat in CATEGORY_ORDER)
    for e in entries:
        cat = e["category"]
        if cat not in buckets:
            buckets[cat] = []
        buckets[cat].append(e)
    # Drop empty.
    return OrderedDict((k, v) for k, v in buckets.items() if v)


# ---------- Markdown ----------

def md_escape_pipes(s: str) -> str:
    """Escape pipe chars so they don't break the markdown table."""
    return s.replace("|", "\\|")


def render_markdown(entries) -> str:
    grouped = group_by_category(entries)
    lines = [
        "# Math Foundations - Notation Glossary",
        "",
        "> Auto-generated from `notation.json` by `generate_notation.py`. **Do not edit by hand.**",
        "",
        f"This glossary indexes every distinct mathematical symbol used across the {42} concept lessons. "
        "Each row gives the LaTeX symbol, how to read it aloud, a one-line plain-English meaning, "
        "and a link to the concept folder where the symbol is first introduced.",
        "",
        f"**Total entries:** {len(entries)}.  ",
        "**Source of truth:** [`notation.json`](notation.json).  ",
        "**PDF cheatsheet:** [`notation.pdf`](notation.pdf) (compiled in CI from [`notation.tex`](notation.tex)).",
        "",
        "## Contents",
        "",
    ]
    for cat in grouped:
        label = CATEGORY_LABEL.get(cat, cat.title())
        anchor = label.lower().replace(" ", "-").replace("/", "").replace(",", "")
        lines.append(f"- [{label}](#{anchor}) ({len(grouped[cat])} entries)")
    lines.append("")

    for cat, items in grouped.items():
        label = CATEGORY_LABEL.get(cat, cat.title())
        lines.append(f"## {label}")
        lines.append("")
        lines.append("| Symbol | Read aloud as | Meaning | First seen in |")
        lines.append("|--------|---------------|---------|---------------|")
        for e in items:
            sym = "$" + e["latex"] + "$"
            read = '"' + md_escape_pipes(e["read_as"]) + '"'
            meaning = md_escape_pipes(e["plain_english"])
            slug = e["first_seen_in"]
            link = f"[{slug}](concepts/{slug}/README.md)"
            lines.append(f"| {sym} | {read} | {meaning} | {link} |")
        lines.append("")

    return "\n".join(lines) + "\n"


# ---------- LaTeX ----------

LATEX_PREAMBLE = r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{longtable,booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\usepackage{microtype}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\renewcommand{\arraystretch}{1.25}

\title{Math Foundations --- Notation Glossary}
\author{}
\date{}

\begin{document}
\maketitle
\thispagestyle{empty}

\noindent
This is the canonical notation glossary for the
\href{https://github.com/pleyva2004/math-foundations}{math-foundations} repository.
Every symbol used across the \textbf{42 concept lessons} is listed below, grouped by category,
with how to read it aloud, a plain-English meaning, and a link to the concept folder where it
first appears. Auto-generated from \texttt{notation.json}; do not edit by hand.
"""

LATEX_POSTAMBLE = r"""
\end{document}
"""


# Map unicode math glyphs that may appear in human-prose fields
# (read_as, plain_english) to LaTeX-safe equivalents. Avoids the need
# for inputenc / fontspec while keeping pdflatex happy.
UNICODE_TO_TEX = {
    "∀": r"$\forall$",
    "∃": r"$\exists$",
    "∈": r"$\in$",
    "∉": r"$\notin$",
    "⊂": r"$\subset$",
    "⊆": r"$\subseteq$",
    "⊃": r"$\supset$",
    "⊇": r"$\supseteq$",
    "∪": r"$\cup$",
    "∩": r"$\cap$",
    "∅": r"$\emptyset$",
    "∖": r"$\setminus$",
    "×": r"$\times$",
    "→": r"$\to$",
    "↦": r"$\mapsto$",
    "∘": r"$\circ$",
    "∧": r"$\wedge$",
    "∨": r"$\vee$",
    "¬": r"$\neg$",
    "⇒": r"$\Rightarrow$",
    "⇔": r"$\Leftrightarrow$",
    "≡": r"$\equiv$",
    "≠": r"$\neq$",
    "≤": r"$\leq$",
    "≥": r"$\geq$",
    "≈": r"$\approx$",
    "∝": r"$\propto$",
    "≅": r"$\cong$",
    "∞": r"$\infty$",
    "∑": r"$\sum$",
    "∏": r"$\prod$",
    "∫": r"$\int$",
    "∂": r"$\partial$",
    "∇": r"$\nabla$",
    "∴": r"$\therefore$",
    "∵": r"$\because$",
    "⊢": r"$\vdash$",
    "⊨": r"$\vDash$",
    "□": r"$\square$",
    "ℕ": r"$\mathbb{N}$",
    "ℤ": r"$\mathbb{Z}$",
    "ℚ": r"$\mathbb{Q}$",
    "ℝ": r"$\mathbb{R}$",
    "ℂ": r"$\mathbb{C}$",
    "𝔽": r"$\mathbb{F}$",
    "ℱ": r"$\mathcal{F}$",
    "ℒ": r"$\mathcal{L}$",
    "𝒫": r"$\mathcal{P}$",
    "𝒩": r"$\mathcal{N}$",
    "𝟙": r"$\mathbf{1}$",
    "𝔼": r"$\mathbb{E}$",
    "Ω": r"$\Omega$",
    "Σ": r"$\Sigma$",
    "Γ": r"$\Gamma$",
    "α": r"$\alpha$",
    "β": r"$\beta$",
    "γ": r"$\gamma$",
    "δ": r"$\delta$",
    "ε": r"$\varepsilon$",
    "η": r"$\eta$",
    "θ": r"$\theta$",
    "λ": r"$\lambda$",
    "μ": r"$\mu$",
    "ν": r"$\nu$",
    "π": r"$\pi$",
    "σ": r"$\sigma$",
    "τ": r"$\tau$",
    "φ": r"$\varphi$",
    "ω": r"$\omega$",
    "²": r"$^{2}$",
    "³": r"$^{3}$",
    "ⁿ": r"$^{n}$",
    "₀": r"$_{0}$",
    "₁": r"$_{1}$",
    "₂": r"$_{2}$",
    "ᵢ": r"$_{i}$",
    "ⱼ": r"$_{j}$",
    "ₜ": r"$_{t}$",
    "·": r"$\cdot$",
    "‖": r"$\|$",
    "⁻": r"$^{-}$",
    "¹": r"$^{1}$",
    "−": r"$-$",
    "…": r"\ldots{}",
    "ô": r"\^{o}",
    "Θ": r"$\Theta$",
    "⟨": r"$\langle$",
    "⟩": r"$\rangle$",
    "⊗": r"$\otimes$",
    "⫫": r"$\perp\!\!\!\perp$",
    "—": r"---",
    "–": r"--",
    "“": r"``",
    "”": r"''",
    "’": r"'",
    "‘": r"`",
    "′": r"$'$",
}


def _sub_unicode(s: str) -> str:
    out = []
    for ch in s:
        if ch in UNICODE_TO_TEX:
            out.append(UNICODE_TO_TEX[ch])
        else:
            out.append(ch)
    return "".join(out)


def tex_escape_text(s: str) -> str:
    """Escape user text for LaTeX (Meaning column). Symbols stay raw via \\(...\\)."""
    # First handle LaTeX-special ASCII characters.
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    out = []
    for ch in s:
        out.append(repl.get(ch, ch))
    escaped = "".join(out)
    # Now replace unicode math glyphs with LaTeX commands.
    return _sub_unicode(escaped)


def tex_anchor(slug: str) -> str:
    """GitHub URL of the concept folder."""
    return f"https://github.com/pleyva2004/math-foundations/tree/main/concepts/{slug}"


def render_latex(entries) -> str:
    grouped = group_by_category(entries)
    chunks = [LATEX_PREAMBLE]
    for cat, items in grouped.items():
        label = CATEGORY_LABEL.get(cat, cat.title())
        chunks.append("")
        chunks.append(r"\section*{" + tex_escape_text(label) + "}")
        chunks.append(
            r"\begin{longtable}{@{} >{$}c<{$} l p{6.5cm} l @{}}"
        )
        chunks.append(r"\toprule")
        chunks.append(
            r"\textnormal{Symbol} & Read aloud as & Meaning & First seen in \\"
        )
        chunks.append(r"\midrule")
        chunks.append(r"\endfirsthead")
        chunks.append(r"\toprule")
        chunks.append(
            r"\textnormal{Symbol} & Read aloud as & Meaning & First seen in \\"
        )
        chunks.append(r"\midrule")
        chunks.append(r"\endhead")
        chunks.append(r"\bottomrule")
        chunks.append(r"\endfoot")
        for e in items:
            sym = e["latex"]  # rendered in math mode (column 1 wraps in $...$).
            # Guard against TeX swallowing a leading "[" as an optional arg.
            if sym.lstrip().startswith("["):
                sym = "{}" + sym
            read = tex_escape_text(e["read_as"])
            meaning = tex_escape_text(e["plain_english"])
            slug = e["first_seen_in"]
            link = (
                r"\href{"
                + tex_anchor(slug)
                + "}{"
                + tex_escape_text(slug)
                + "}"
            )
            chunks.append(f"{sym} & {read} & {meaning} & {link} \\\\")
        chunks.append(r"\end{longtable}")
    chunks.append(LATEX_POSTAMBLE)
    return "\n".join(chunks)


def main():
    md = render_markdown(NOTATION)
    tex = render_latex(NOTATION)
    (ROOT / "NOTATION.md").write_text(md)
    (ROOT / "notation.tex").write_text(tex)
    print(f"Wrote NOTATION.md ({len(NOTATION)} entries) and notation.tex.")


if __name__ == "__main__":
    main()
