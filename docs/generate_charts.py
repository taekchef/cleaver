"""Generate benchmark SVG charts for Cleaver README — 16 scenarios, 12 dimensions."""
import json
import os

# ── Combined data: 13 existing + 3 new ──────────────────────────────────────

COMPARISON = {
    # Existing 13 (9-dim pass rates, will recalculate for 12)
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
    # New 3 (12-dim graded)
    "eval-landing-page":  {"with": 1.00, "without": 0.33},
    "eval-web-app":       {"with": 1.00, "without": 0.33},
    "eval-remix":         {"with": 1.00, "without": 0.42},
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
    "eval-landing-page": "Landing Page",
    "eval-web-app": "Web App",
    "eval-remix": "Remix",
}

# Mark new evals for visual distinction
NEW_EVALS = {"eval-landing-page", "eval-web-app", "eval-remix"}

# Dimension data: old 13 + new 3 = 16 total
DIMENSIONS = {
    "Product Analysis":  {"with": 11+3, "without": 13+3, "total": 16},
    "Multiple Prompts":  {"with": 12+3, "without": 7+3,  "total": 16},
    "Done Criteria":     {"with": 5+3,  "without": 0+0,  "total": 16},
    "Why Annotations":   {"with": 12+3, "without": 0+0,  "total": 16},
    "Pro Tips":          {"with": 9+3,  "without": 3+0,  "total": 16},
    "Build Order":       {"with": 7+3,  "without": 1+0,  "total": 16},
    "Domain Framework":  {"with": 8+3,  "without": 5+1,  "total": 16},
    "Not-To-Do":         {"with": 13+3, "without": 6+0,  "total": 16},
    "Soul Capture":      {"with": 13+3, "without": 4+3,  "total": 16},
    "Destination Not Route": {"with": 0+3, "without": 0+0, "total": 3},
    "Prompts Standalone": {"with": 0+3, "without": 0+3, "total": 3},
    "Usage Guidance":    {"with": 0+3,  "without": 0+0,  "total": 3},
}

# For the new 3 dimensions, we only tested 3 scenarios.
# Show only those 3 for the new dims, all 16 for old dims.
OLD_DIMS = ["Product Analysis", "Multiple Prompts", "Done Criteria", "Why Annotations",
            "Pro Tips", "Build Order", "Domain Framework", "Not-To-Do", "Soul Capture"]
NEW_DIMS = ["Destination Not Route", "Prompts Standalone", "Usage Guidance"]

GREEN = "#10b981"
GRAY = "#94a3b8"
ORANGE = "#f59e0b"
BG = "#ffffff"
TEXT = "#1e293b"
TEXT_LIGHT = "#64748b"


def gen_benchmark_svg():
    W, H = 1100, 520
    ML, MR, MT, MB = 70, 30, 55, 100
    CW = W - ML - MR
    CH = H - MT - MB

    n = len(COMPARISON)
    gw = CW / n
    bw = 22
    gap = 4
    total_bars = bw * 2 + gap
    bar_offset = (gw - total_bars) / 2

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui,-apple-system,sans-serif">')
    lines.append(f'<rect width="{W}" height="{H}" fill="{BG}" rx="12"/>')
    lines.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="15" font-weight="700" fill="{TEXT}">Cleaver Skill Effectiveness — 16 Scenarios × 12 Quality Dimensions</text>')

    for pct in [0, 25, 50, 75, 100]:
        y = MT + CH * (1 - pct / 100)
        lines.append(f'<line x1="{ML}" y1="{y}" x2="{W-MR}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>')
        lines.append(f'<text x="{ML-8}" y="{y+4}" text-anchor="end" font-size="10" fill="{TEXT_LIGHT}">{pct}%</text>')

    for i, (key, vals) in enumerate(COMPARISON.items()):
        gx = ML + i * gw
        x1 = gx + bar_offset
        x2 = x1 + bw + gap

        fill_color = ORANGE if key in NEW_EVALS else GREEN

        h1 = vals["with"] * CH
        y1 = MT + CH - h1
        lines.append(f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{bw}" height="{h1:.1f}" fill="{fill_color}" rx="3"/>')

        h2 = vals["without"] * CH
        y2 = MT + CH - h2
        lines.append(f'<rect x="{x2:.1f}" y="{y2:.1f}" width="{bw}" height="{h2:.1f}" fill="{GRAY}" rx="3"/>')

        delta = vals["with"] - vals["without"]
        if delta > 0:
            delta_text = f"+{int(delta*100)}"
            lines.append(f'<text x="{gx + gw/2:.1f}" y="{y1-5:.1f}" text-anchor="middle" font-size="8" font-weight="600" fill="{fill_color}">{delta_text}</text>')

        label = LABELS[key]
        cx = gx + gw / 2
        lines.append(f'<text x="{cx:.1f}" y="{MT+CH+16:.1f}" text-anchor="middle" font-size="9" fill="{TEXT}" transform="rotate(40 {cx:.1f} {MT+CH+16:.1f})">{label}</text>')

    # Legend
    lx = W / 2 - 180
    ly = H - 16
    lines.append(f'<rect x="{lx}" y="{ly-10}" width="12" height="12" fill="{GREEN}" rx="2"/>')
    lines.append(f'<text x="{lx+18}" y="{ly}" font-size="10" fill="{TEXT}">with Cleaver (existing)</text>')
    lines.append(f'<rect x="{lx+150}" y="{ly-10}" width="12" height="12" fill="{ORANGE}" rx="2"/>')
    lines.append(f'<text x="{lx+168}" y="{ly}" font-size="10" fill="{TEXT}">with Cleaver (new)</text>')
    lines.append(f'<rect x="{lx+310}" y="{ly-10}" width="12" height="12" fill="{GRAY}" rx="2"/>')
    lines.append(f'<text x="{lx+328}" y="{ly}" font-size="10" fill="{TEXT}">without Cleaver</text>')

    lines.append(f'<line x1="{ML}" y1="{MT+CH}" x2="{W-MR}" y2="{MT+CH}" stroke="{TEXT_LIGHT}" stroke-width="1"/>')
    lines.append('</svg>')
    return '\n'.join(lines)


def gen_dimensions_svg():
    W, H = 850, 500
    ML, MR, MT, MB = 150, 40, 50, 30
    CW = W - ML - MR
    CH = H - MT - MB

    # Combine old + new dimensions
    all_dims = OLD_DIMS + NEW_DIMS
    n = len(all_dims)
    row_h = CH / n
    bar_h = 16
    bar_gap = 2
    total_bar_h = bar_h * 2 + bar_gap
    bar_offset = (row_h - total_bar_h) / 2

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui,-apple-system,sans-serif">')
    lines.append(f'<rect width="{W}" height="{H}" fill="{BG}" rx="12"/>')
    lines.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="15" font-weight="700" fill="{TEXT}">Quality Dimension Coverage — with vs without Cleaver</text>')

    for pct in [0, 25, 50, 75, 100]:
        x = ML + CW * pct / 100
        lines.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+CH}" stroke="#e2e8f0" stroke-width="1"/>')
        lines.append(f'<text x="{x}" y="{MT-8}" text-anchor="middle" font-size="10" fill="{TEXT_LIGHT}">{pct}%</text>')

    for i, name in enumerate(all_dims):
        y_base = MT + i * row_h
        cy = y_base + row_h / 2

        # Label - add asterisk for new dims
        display_name = f"{name} *" if name in NEW_DIMS else name
        lines.append(f'<text x="{ML-10}" y="{cy+4:.1f}" text-anchor="end" font-size="11" fill="{TEXT}">{display_name}</text>')

        vals = DIMENSIONS[name]

        # with_skill bar
        y1 = y_base + bar_offset
        w1 = (vals["with"] / vals["total"]) * CW
        lines.append(f'<rect x="{ML}" y="{y1:.1f}" width="{w1:.1f}" height="{bar_h}" fill="{GREEN}" rx="3"/>')
        lines.append(f'<text x="{ML+w1+5:.1f}" y="{y1+bar_h-2:.1f}" font-size="9" font-weight="600" fill="{GREEN}">{vals["with"]}/{vals["total"]}</text>')

        # without_skill bar
        y2 = y1 + bar_h + bar_gap
        w2 = (vals["without"] / vals["total"]) * CW
        lines.append(f'<rect x="{ML}" y="{y2:.1f}" width="{w2:.1f}" height="{bar_h}" fill="{GRAY}" rx="3"/>')
        if vals["without"] > 0:
            lines.append(f'<text x="{ML+w2+5:.1f}" y="{y2+bar_h-2:.1f}" font-size="9" fill="{TEXT_LIGHT}">{vals["without"]}/{vals["total"]}</text>')
        else:
            lines.append(f'<text x="{ML+5:.1f}" y="{y2+bar_h-2:.1f}" font-size="9" fill="{TEXT_LIGHT}">0/{vals["total"]}</text>')

    # Legend
    lx = W / 2 - 120
    ly = H - 12
    lines.append(f'<rect x="{lx}" y="{ly-10}" width="12" height="12" fill="{GREEN}" rx="2"/>')
    lines.append(f'<text x="{lx+18}" y="{ly}" font-size="10" fill="{TEXT}">with Cleaver</text>')
    lines.append(f'<rect x="{lx+130}" y="{ly-10}" width="12" height="12" fill="{GRAY}" rx="2"/>')
    lines.append(f'<text x="{lx+148}" y="{ly}" font-size="10" fill="{TEXT}">without Cleaver</text>')
    lines.append(f'<text x="{W-MR}" y="{ly}" text-anchor="end" font-size="9" fill="{TEXT_LIGHT}">* tested on 3 new scenarios</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


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
