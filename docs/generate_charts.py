"""Generate benchmark SVG charts for Cleaver README."""
import json
import os

# ── Data ──────────────────────────────────────────────────────────────────────

COMPARISON = {
    "eval-ai-product":    {"with": 0.89, "without": 0.33},
    "eval-animation":     {"with": 0.67, "without": 0.22},
    "eval-api-backend":   {"with": 0.78, "without": 0.56},
    "eval-cli-tool":      {"with": 1.00, "without": 0.22},
    "eval-design-system": {"with": 0.89, "without": 0.22},
    "eval-fasttrack-path":{"with": 0.67, "without": 0.22},
    "eval-game":          {"with": 0.89, "without": 0.33},
    "eval-learning-path": {"with": 1.00, "without": 0.78},
    "eval-minimal-path":  {"with": 0.22, "without": 0.22},
    "eval-mobile-app":    {"with": 0.89, "without": 0.33},
    "eval-multi-product": {"with": 0.67, "without": 0.33},
    "eval-service":       {"with": 0.78, "without": 0.33},
    "eval-verbal-only":   {"with": 0.67, "without": 0.22},
}

LABELS = {
    "eval-ai-product": "AI Product",
    "eval-animation": "Animation",
    "eval-api-backend": "API/Backend",
    "eval-cli-tool": "CLI Tool",
    "eval-design-system": "Design System",
    "eval-fasttrack-path": "Fast Track",
    "eval-game": "Game",
    "eval-learning-path": "Learning",
    "eval-minimal-path": "Minimal",
    "eval-mobile-app": "Mobile App",
    "eval-multi-product": "Multi-Product",
    "eval-service": "Service",
    "eval-verbal-only": "Verbal Only",
}

DIMENSIONS = {
    "Product Analysis":  {"with": 11, "without": 13, "total": 13},
    "Multiple Prompts":  {"with": 12, "without": 7,  "total": 13},
    "Done Criteria":     {"with": 5,  "without": 0,  "total": 13},
    "Why Annotations":   {"with": 12, "without": 0,  "total": 13},
    "Pro Tips":          {"with": 9,  "without": 3,  "total": 13},
    "Build Order":       {"with": 7,  "without": 1,  "total": 13},
    "Domain Framework":  {"with": 8,  "without": 5,  "total": 13},
    "Not-To-Do":         {"with": 13, "without": 6,  "total": 13},
    "Soul Capture":      {"with": 13, "without": 4,  "total": 13},
}

GREEN = "#10b981"
GREEN_LIGHT = "#d1fae5"
GRAY = "#94a3b8"
GRAY_LIGHT = "#e2e8f0"
BG = "#ffffff"
TEXT = "#1e293b"
TEXT_LIGHT = "#64748b"

# ── Chart 1: Benchmark comparison ────────────────────────────────────────────

def gen_benchmark_svg():
    W, H = 960, 500
    ML, MR, MT, MB = 70, 30, 55, 95  # margins
    CW = W - ML - MR   # chart width
    CH = H - MT - MB    # chart height

    n = len(COMPARISON)
    gw = CW / n         # group width
    bw = 22             # bar width
    gap = 4             # gap between bars
    total_bars = bw * 2 + gap
    bar_offset = (gw - total_bars) / 2

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui,-apple-system,sans-serif">')

    # Background
    lines.append(f'<rect width="{W}" height="{H}" fill="{BG}" rx="12"/>')

    # Title
    lines.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="{TEXT}">Cleaver Skill Effectiveness — 13 Scenarios × 9 Quality Dimensions</text>')

    # Grid lines
    for pct in [0, 25, 50, 75, 100]:
        y = MT + CH * (1 - pct / 100)
        lines.append(f'<line x1="{ML}" y1="{y}" x2="{W-MR}" y2="{y}" stroke="{GRAY_LIGHT}" stroke-width="1"/>')
        lines.append(f'<text x="{ML-8}" y="{y+4}" text-anchor="end" font-size="11" fill="{TEXT_LIGHT}">{pct}%</text>')

    # Bars
    for i, (key, vals) in enumerate(COMPARISON.items()):
        gx = ML + i * gw
        x1 = gx + bar_offset
        x2 = x1 + bw + gap

        # with_skill bar
        h1 = vals["with"] * CH
        y1 = MT + CH - h1
        lines.append(f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{bw}" height="{h1:.1f}" fill="{GREEN}" rx="3"/>')

        # without_skill bar
        h2 = vals["without"] * CH
        y2 = MT + CH - h2
        lines.append(f'<rect x="{x2:.1f}" y="{y2:.1f}" width="{bw}" height="{h2:.1f}" fill="{GRAY}" rx="3"/>')

        # Delta label (on top of with_skill bar)
        delta = vals["with"] - vals["without"]
        if delta > 0:
            delta_text = f"+{int(delta*100)}"
            lines.append(f'<text x="{gx + gw/2:.1f}" y="{y1-6:.1f}" text-anchor="middle" font-size="9" font-weight="600" fill="{GREEN}">{delta_text}</text>')

        # X label
        label = LABELS[key]
        cx = gx + gw / 2
        lines.append(f'<text x="{cx:.1f}" y="{MT+CH+18:.1f}" text-anchor="middle" font-size="10" fill="{TEXT}" transform="rotate(35 {cx:.1f} {MT+CH+18:.1f})">{label}</text>')

    # Legend
    lx = W / 2 - 120
    ly = H - 18
    lines.append(f'<rect x="{lx}" y="{ly-10}" width="12" height="12" fill="{GREEN}" rx="2"/>')
    lines.append(f'<text x="{lx+18}" y="{ly}" font-size="11" fill="{TEXT}">with Cleaver</text>')
    lines.append(f'<rect x="{lx+130}" y="{ly-10}" width="12" height="12" fill="{GRAY}" rx="2"/>')
    lines.append(f'<text x="{lx+148}" y="{ly}" font-size="11" fill="{TEXT}">without Cleaver</text>')

    # Bottom axis line
    lines.append(f'<line x1="{ML}" y1="{MT+CH}" x2="{W-MR}" y2="{MT+CH}" stroke="{TEXT_LIGHT}" stroke-width="1"/>')

    lines.append('</svg>')
    return '\n'.join(lines)


# ── Chart 2: Dimension coverage ──────────────────────────────────────────────

def gen_dimensions_svg():
    W, H = 800, 420
    ML, MR, MT, MB = 130, 40, 50, 30
    CW = W - ML - MR
    CH = H - MT - MB

    dims = list(DIMENSIONS.items())
    n = len(dims)
    row_h = CH / n
    bar_h = 18
    bar_gap = 3
    total_bar_h = bar_h * 2 + bar_gap
    bar_offset = (row_h - total_bar_h) / 2

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui,-apple-system,sans-serif">')

    # Background
    lines.append(f'<rect width="{W}" height="{H}" fill="{BG}" rx="12"/>')

    # Title
    lines.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="{TEXT}">Quality Dimension Coverage — with vs without Cleaver</text>')

    # Grid lines
    for pct in [0, 25, 50, 75, 100]:
        x = ML + CW * pct / 100
        lines.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+CH}" stroke="{GRAY_LIGHT}" stroke-width="1"/>')
        lines.append(f'<text x="{x}" y="{MT-8}" text-anchor="middle" font-size="10" fill="{TEXT_LIGHT}">{pct}%</text>')

    for i, (name, vals) in enumerate(dims):
        y_base = MT + i * row_h

        # Label
        cy = y_base + row_h / 2
        lines.append(f'<text x="{ML-10}" y="{cy+4:.1f}" text-anchor="end" font-size="12" fill="{TEXT}">{name}</text>')

        # with_skill bar
        y1 = y_base + bar_offset
        w1 = (vals["with"] / vals["total"]) * CW
        pct1 = int(vals["with"] / vals["total"] * 100)
        lines.append(f'<rect x="{ML}" y="{y1:.1f}" width="{w1:.1f}" height="{bar_h}" fill="{GREEN}" rx="3"/>')
        lines.append(f'<text x="{ML+w1+6:.1f}" y="{y1+bar_h-3:.1f}" font-size="10" font-weight="600" fill="{GREEN}">{vals["with"]}/{vals["total"]}</text>')

        # without_skill bar
        y2 = y1 + bar_h + bar_gap
        w2 = (vals["without"] / vals["total"]) * CW
        lines.append(f'<rect x="{ML}" y="{y2:.1f}" width="{w2:.1f}" height="{bar_h}" fill="{GRAY}" rx="3"/>')
        if vals["without"] > 0:
            lines.append(f'<text x="{ML+w2+6:.1f}" y="{y2+bar_h-3:.1f}" font-size="10" fill="{TEXT_LIGHT}">{vals["without"]}/{vals["total"]}</text>')
        else:
            lines.append(f'<text x="{ML+6:.1f}" y="{y2+bar_h-3:.1f}" font-size="10" fill="{TEXT_LIGHT}">0/13</text>')

    # Legend
    lx = W / 2 - 120
    ly = H - 12
    lines.append(f'<rect x="{lx}" y="{ly-10}" width="12" height="12" fill="{GREEN}" rx="2"/>')
    lines.append(f'<text x="{lx+18}" y="{ly}" font-size="11" fill="{TEXT}">with Cleaver</text>')
    lines.append(f'<rect x="{lx+130}" y="{ly-10}" width="12" height="12" fill="{GRAY}" rx="2"/>')
    lines.append(f'<text x="{lx+148}" y="{ly}" font-size="11" fill="{TEXT}">without Cleaver</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))

    svg1 = gen_benchmark_svg()
    path1 = os.path.join(out_dir, "benchmark.svg")
    with open(path1, "w") as f:
        f.write(svg1)
    print(f"Written: {path1}")

    svg2 = gen_dimensions_svg()
    path2 = os.path.join(out_dir, "dimensions.svg")
    with open(path2, "w") as f:
        f.write(svg2)
    print(f"Written: {path2}")
