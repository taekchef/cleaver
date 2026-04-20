"""Read all grading.json files from workspace and generate benchmark.json."""
import json
import os
import glob

WORKSPACE = os.path.expanduser("~/.claude/skills/cleaver-workspace")

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
    "eval-linear": "Linear (Re-eval)",
}

# Dimension short names (first 9 are old, last 3 are new)
DIM_SHORT = {
    "包含产品分析/拆解章节": "Product Analysis",
    "包含多个可用的重建 prompt（≥2）": "Multiple Prompts",
    "包含完成/验收标准": "Done Criteria",
    "包含教学注释（为什么有效）": "Why Annotations",
    "包含 Pro Tips / 实战洞察": "Pro Tips",
    "包含构建顺序建议": "Build Order",
    "使用领域专属分析框架": "Domain Framework",
    "包含 Not-To-Do / 范围限制": "Not-To-Do",
    "捕获了产品的灵魂/核心差异化": "Soul Capture",
    "Prompt 描述目的地而非路线": "Destination Not Route",
    "每个 prompt 可独立使用": "Prompts Standalone",
    "包含 prompt 使用建议": "Usage Guidance",
}


def read_grading(path):
    with open(path) as f:
        return json.load(f)


def main():
    scenarios = {}
    grading_data = {}
    dimension_agg = {}  # dim_name -> {with: [bool], without: [bool]}

    # Pass 1: find latest iteration for each scenario
    latest = {}  # key -> (iter_num, scenario_dir)
    for iteration_dir in sorted(glob.glob(os.path.join(WORKSPACE, "iteration-*"))):
        iter_num = int(os.path.basename(iteration_dir).split("-")[1])
        for scenario_dir in sorted(glob.glob(os.path.join(iteration_dir, "eval-*"))):
            key = os.path.basename(scenario_dir)
            with_path = os.path.join(scenario_dir, "with_skill", "grading.json")
            without_path = os.path.join(scenario_dir, "without_skill", "grading.json")
            if not os.path.exists(with_path) or not os.path.exists(without_path):
                continue
            if key not in latest or iter_num > latest[key][0]:
                latest[key] = (iter_num, scenario_dir)

    # Pass 2: build data from latest iteration only
    for key, (iter_num, scenario_dir) in sorted(latest.items()):
        with_path = os.path.join(scenario_dir, "with_skill", "grading.json")
        without_path = os.path.join(scenario_dir, "without_skill", "grading.json")
        with_grading = read_grading(with_path)
        without_grading = read_grading(without_path)

        grading_data[key] = {
            "with_skill": with_grading["expectations"],
            "without_skill": without_grading["expectations"],
        }

        scenarios[key] = {
            "label": LABELS.get(key, key),
            "iteration": iter_num,
            "dimensions_tested": with_grading["summary"]["total"],
            "with_skill": {
                "passed": with_grading["summary"]["passed"],
                "total": with_grading["summary"]["total"],
                "pass_rate": with_grading["summary"]["pass_rate"],
            },
            "without_skill": {
                "passed": without_grading["summary"]["passed"],
                "total": without_grading["summary"]["total"],
                "pass_rate": without_grading["summary"]["pass_rate"],
            },
        }

        # Aggregate per-dimension
        for mode, data in [("with_skill", with_grading), ("without_skill", without_grading)]:
            for exp in data["expectations"]:
                dim_name = DIM_SHORT.get(exp["text"], exp["text"])
                if dim_name not in dimension_agg:
                    dimension_agg[dim_name] = {"with_skill": [], "without_skill": []}
                dimension_agg[dim_name][mode].append(exp["passed"])

    # Build dimension summary
    dimensions = {}
    for dim_name, results in dimension_agg.items():
        dimensions[dim_name] = {
            "with_skill": {
                "passed": sum(results["with_skill"]),
                "total": len(results["with_skill"]),
            },
            "without_skill": {
                "passed": sum(results["without_skill"]),
                "total": len(results["without_skill"]),
            },
        }

    benchmark = {
        "metadata": {
            "skill_name": "cleaver",
            "version": "0.1.0",
            "date": "2026-04-20",
            "methodology": "Each scenario run with/without skill active, graded by Claude against 12-dimension rubric",
            "grader": "claude-sonnet",
            "scenarios_count": len(scenarios),
            "old_dimensions": 9,
            "new_dimensions": 12,
            "note": "First 13 scenarios (iteration-4) tested on 9 dimensions. Last 3 (iteration-5) tested on all 12.",
        },
        "scenarios": scenarios,
        "dimensions": dimensions,
        "grading": grading_data,
    }

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "benchmark.json")
    with open(out_path, "w") as f:
        json.dump(benchmark, f, indent=2, ensure_ascii=False)
    print(f"Written: {out_path}")
    print(f"Scenarios: {len(scenarios)}")
    print(f"Dimensions: {len(dimensions)}")


if __name__ == "__main__":
    main()
