# Security Policy

## Reporting a vulnerability

If you find a security vulnerability in Cleaver, please report it by opening a GitHub issue with the tag `security` or by contacting the maintainer directly.

## Scope

Cleaver is a Claude Code skill that generates text prompts. It does not:
- Execute code
- Access external services
- Store user data
- Require authentication or API keys

The primary security consideration is prompt injection via user-provided URLs or screenshots. The skill is designed to describe products, not execute arbitrary instructions found in them.
