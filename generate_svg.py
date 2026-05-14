"""Generate a clickable SVG dependency graph from manifest.json.

Outputs `html/graph.svg` — a layered DAG with `<a xlink:href>` anchors per
node so the SVG is fully interactive when viewed as a standalone file
(e.g. via GitHub Pages at https://<user>.github.io/math-foundations/graph.svg).

Layout: 5-band horizontal layout, one band per skill level, nodes spread
across each band. Edges drawn as straight lines.

Re-run `python generate_svg.py` after modifying manifest.json. The output
is deterministic.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = json.loads((ROOT / "manifest.json").read_text())
CONCEPTS = MANIFEST["concepts"]
LEVELS = MANIFEST["levels"]

# GitHub blob URL prefix — anchors point here (markdown renders nicely)
BLOB_BASE = "https://github.com/pleyva2004/math-foundations/blob/main/concepts"

# Layout constants
WIDTH = 1400
LEVEL_HEIGHT = 140
TOP_PAD = 80
BOTTOM_PAD = 60
NODE_R = 22
H_PAD = 60


def main():
    # Group concepts by level (preserving manifest order within each level).
    by_level = {}
    for c in CONCEPTS:
        by_level.setdefault(c["level"], []).append(c)

    # Sort levels by their declared order.
    level_names = sorted(LEVELS.keys(), key=lambda n: LEVELS[n]["order"])
    n_levels = len(level_names)
    height = TOP_PAD + n_levels * LEVEL_HEIGHT + BOTTOM_PAD

    # Compute (x, y) for each node.
    pos = {}
    for li, level_name in enumerate(level_names):
        nodes_in_level = by_level.get(level_name, [])
        n = len(nodes_in_level)
        if n == 0:
            continue
        usable = WIDTH - 2 * H_PAD
        spacing = usable / max(n, 1)
        y = TOP_PAD + li * LEVEL_HEIGHT + LEVEL_HEIGHT / 2
        for i, c in enumerate(nodes_in_level):
            x = H_PAD + spacing * (i + 0.5)
            pos[c["id"]] = (x, y)

    # Build SVG.
    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 {WIDTH} {height}" '
        f'font-family="-apple-system, BlinkMacSystemFont, sans-serif" '
        f'role="img" aria-label="math-foundations dependency graph">'
    )

    # Defs: arrowhead.
    svg.append(
        '<defs>'
        '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto">'
        '<path d="M0,0 L10,5 L0,10 Z" fill="#888"/>'
        '</marker>'
        '</defs>'
    )

    # Background + title.
    svg.append(f'<rect width="{WIDTH}" height="{height}" fill="white"/>')
    svg.append(
        f'<text x="{WIDTH/2}" y="36" text-anchor="middle" '
        f'font-size="22" font-weight="bold" fill="#222">'
        f'math-foundations — concept dependency graph (click a node)'
        f'</text>'
    )

    # Level labels (left margin).
    for li, level_name in enumerate(level_names):
        y = TOP_PAD + li * LEVEL_HEIGHT + LEVEL_HEIGHT / 2
        svg.append(
            f'<text x="10" y="{y - 28}" font-size="11" fill="#666" '
            f'font-style="italic">{LEVELS[level_name]["label"]}</text>'
        )
        # Soft horizontal band background.
        band_color = LEVELS[level_name]["color"]
        svg.append(
            f'<rect x="0" y="{y - LEVEL_HEIGHT/2 + 8}" width="{WIDTH}" '
            f'height="{LEVEL_HEIGHT - 16}" fill="{band_color}" opacity="0.15"/>'
        )

    # Edges (drawn before nodes so nodes overlay).
    for c in CONCEPTS:
        if c["id"] not in pos:
            continue
        x2, y2 = pos[c["id"]]
        for prereq in c["prereqs"]:
            prereq_id = prereq.split("-")[0]
            if prereq_id not in pos:
                continue
            x1, y1 = pos[prereq_id]
            svg.append(
                f'<line x1="{x1:.1f}" y1="{y1 + NODE_R:.1f}" '
                f'x2="{x2:.1f}" y2="{y2 - NODE_R:.1f}" '
                f'stroke="#aaa" stroke-width="1.2" opacity="0.55" '
                f'marker-end="url(#arrow)"/>'
            )

    # Nodes (with anchor wrappers — interactive when SVG is the top-level doc).
    for c in CONCEPTS:
        if c["id"] not in pos:
            continue
        x, y = pos[c["id"]]
        slug = f"{c['id']}-{c['slug']}"
        url = f"{BLOB_BASE}/{slug}/README.md"
        color = LEVELS[c["level"]]["color"]
        # Title (tooltip on hover).
        title = c["title"].replace('"', "'")
        summary = c["summary"].replace('"', "'")[:120]

        svg.append(
            f'<a xlink:href="{url}" target="_blank">'
            f'<title>{c["id"]}: {title}\n{summary}</title>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NODE_R}" '
            f'fill="{color}" stroke="#333" stroke-width="1.5"/>'
            f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" '
            f'font-size="12" font-weight="bold" fill="#222" '
            f'pointer-events="none">{c["id"]}</text>'
            f'</a>'
        )

    # Legend in bottom-right.
    legend_x = WIDTH - 220
    legend_y = height - 110
    svg.append(
        f'<rect x="{legend_x - 10}" y="{legend_y - 18}" width="220" '
        f'height="{18 + len(level_names) * 18 + 8}" '
        f'fill="white" stroke="#ccc" stroke-width="1" rx="4"/>'
    )
    svg.append(
        f'<text x="{legend_x}" y="{legend_y - 4}" font-size="11" '
        f'font-weight="bold" fill="#222">Skill levels</text>'
    )
    for li, level_name in enumerate(level_names):
        ly = legend_y + 12 + li * 18
        svg.append(
            f'<rect x="{legend_x}" y="{ly - 9}" width="14" height="14" '
            f'fill="{LEVELS[level_name]["color"]}" stroke="#333" stroke-width="1"/>'
        )
        svg.append(
            f'<text x="{legend_x + 22}" y="{ly + 2}" font-size="11" fill="#333">'
            f'{LEVELS[level_name]["label"]}</text>'
        )

    svg.append('</svg>')

    out = ROOT / "html" / "graph.svg"
    out.write_text("\n".join(svg))
    print(f"Wrote {out} ({len(CONCEPTS)} nodes, {sum(len(c['prereqs']) for c in CONCEPTS)} edges)")


if __name__ == "__main__":
    main()
