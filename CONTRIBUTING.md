# Contributing

Cleaver is an open-source Claude Code skill. Contributions are welcome.

## How to contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `python3 evals/build_benchmark.py && python3 docs/generate_charts.py` if you changed eval data
5. Ensure `git diff --exit-code evals/benchmark.json docs/benchmark.svg docs/dimensions.svg` passes
6. Open a pull request

## What to contribute

- **New domain examples**: Real product teardowns following the existing format
- **Reference improvements**: Better strategies for existing domains, or new domains
- **Bug fixes**: SKILL.md behavior that produces inconsistent or poor output
- **Eval improvements**: Better rubric dimensions, new test scenarios

## What NOT to contribute

- Proprietary product internals or leaked information
- Brand impersonation or identity copying
- Over-engineering: Cleaver's strength is its compactness

## Style

- Keep SKILL.md under 250 lines
- Reference files should be 100-300 lines each
- Examples should demonstrate one path clearly, not try to cover everything
