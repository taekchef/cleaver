# Bad Prompt vs Cleaver Prompt — Linear

> Demonstrates the difference between a generic prompt and a Cleaver-generated prompt.

## The Product

[Linear](https://linear.app) — Issue tracking for software teams, known for keyboard-first speed.

## Bad Prompt

```
Make a dashboard like Linear. It should have a sidebar with projects, a main area
showing issues in a list, and the ability to create, edit, and delete issues.
Use a dark theme.
```

### Why it fails

- **Copies surface, misses soul**: The sidebar + list layout is obvious. What makes Linear special is the *speed* — keyboard shortcuts, instant state transitions, no modals blocking flow.
- **No scope boundary**: "Create, edit, delete" is everything and nothing. No prioritization.
- **No "done" condition**: How do you know when it works? When issues render? When the workflow feels fast?
- **No taste**: "Dark theme" is a color choice, not a design philosophy. Linear's design is about *density without clutter*.

The result: a generic issue tracker that looks like Linear but doesn't *feel* like Linear.

---

## Cleaver Prompt

### Prompt 0: Foundation

```
做一个项目管理工具，核心是"不挡路"——打开就用，键盘搞定一切。
React + Tailwind，不要组件库。数据用本地 state 模拟。
不要做用户认证、团队管理、通知、或者任何多人协作功能。
```

### Prompt 1: Core Issue List

```
Build the main issue list view for a keyboard-first issue tracker.
The core promise: nothing slows you down.

First screen: an inbox-like list of issues, sorted by priority.
Each row shows: status icon, issue title (editable inline), assignee avatar, priority indicator.
No modals for viewing — clicking an issue expands it in a side panel.

Keyboard flow:
- C → create new issue (inline, not modal)
- J/K → navigate up/down
- Enter → open issue in side panel
- 1-4 → set priority
- Space → cycle status (Backlog → Todo → In Progress → Done)
- Escape → back to list

Done when a user can create, view, assign, prioritize, and close an issue
without touching the mouse.

Do not add: roadmap view, docs, chat, analytics, or multiple projects yet.
```

### What Cleaver adds

| Aspect | Bad Prompt | Cleaver |
|--------|-----------|---------|
| **Soul** | "Like Linear" (vague reference) | "不挡路" (named principle) |
| **Scope** | Everything (no boundaries) | Explicit not-to-do list |
| **Done condition** | None | "Create, view, assign, prioritize, close without mouse" |
| **Interaction model** | Implied clicks | Explicit keyboard flow |
| **Build order** | None (big bang) | Foundation → Core list → Features |
| **Why it works** | Not explained | Each prompt is self-documenting |

---

## Key Insight

> Cleaver doesn't just make better prompts — it names the product's soul first,
> then builds every prompt to serve that soul. "不挡路" is Linear's soul.
> Every subsequent decision (keyboard-first, no modals, instant state changes)
> follows from that principle.
>
> The bad prompt copies the *form*. Cleaver captures the *feeling*.
