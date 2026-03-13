---
name: write-docs
description: Process notes, Slack threads, Slite docs, or trunk2 deploy context into documentation changes. Creates a branch, edits docs, opens a PR, and updates Linear. Use when given a notes file from .claude/drafts/, trunk2 PR numbers, Linear ticket IDs, a deploy tag, Slite doc links, or when the user says "write docs", "document this", or "process drafts".
allowed-tools: Bash(git *), Bash(gh pr *), Bash(gh issue *), Bash(gh api *), Read, Write, Edit, Glob, Grep, mcp__claude_ai_Linear__get_issue, mcp__claude_ai_Linear__list_issues, mcp__claude_ai_Linear__list_projects, mcp__claude_ai_Linear__save_issue, mcp__claude_ai_Linear__save_comment, mcp__claude_ai_Linear__create_attachment, mcp__claude_ai_trunk_docs__searchDocumentation, mcp__claude_ai_Trunk_Slite__*, mcp__claude_ai_Slack__*, WebFetch
---

# Writing Docs

Turn raw notes, Slack pastes, and PR references into reviewed docs PRs with full Linear tracking.

## Contents

- [Inputs](#inputs)
- [Products](#products)
- [Workflow](#workflow)
- [Guidelines](#guidelines)
- [Batch processing](#batch-processing)

## Inputs

The user provides any combination of:
- **Notes file** (e.g., `.claude/drafts/my-feature.md`) — primary input. Template: `.claude/drafts/TEMPLATE.md`
- **trunk2 PR numbers** — PRs from `trunk-io/trunk2`
- **Linear ticket IDs** — `TRUNK-NNNNN` references
- **Deploy tag** (e.g., `v126`) — features shipped in a release
- **Slite doc links** — PRDs, specs, or knowledge base articles from Slite
- **Context links** — Slack threads, Loom videos, Google Docs, etc.
- **Specific docs page** — if the user knows what needs changing

## Products

Docs are organized by product area:
- **Merge Queue** — `/merge-queue/`
- **Flaky Tests** — `/flaky-tests/`
- **CI Autopilot** — `/ci-autopilot/`
- **Code Quality** — `/code-quality/`
- **Setup & Administration** — `/setup-and-administration/`

## Workflow

Copy this checklist and track progress:

```
Progress:
- [ ] Phase 0: Duplicate & overlap check
- [ ] Phase 1: Parse input
- [ ] Phase 2: Research (Linear, Slite, Slack, docs, PRs)
- [ ] Phase 2.5: Write sources audit file
- [ ] Phase 3: Draft documentation
- [ ] Phase 4: Branch, commit, PR
- [ ] Phase 5: Update Linear
- [ ] Phase 6: Stage outputs (Slack post, report)
- [ ] Phase 7: Clean up and summarize
```

### Phase 0: Duplicate & Overlap Check

Before doing any work, verify no existing PR already covers this draft. See [OVERLAP-CHECK.md](OVERLAP-CHECK.md) for the detailed check procedure.

If a match or overlap is found, stop and ask the user how to proceed before continuing.

### Phase 1: Parse and Understand

1. If a notes file was provided, read it and extract: feature name, Linear ticket IDs, GitHub PR URLs, context links, product area, change type, and key details.
2. If trunk2 PR numbers or a deploy tag were provided instead, use `gh pr view <number> --repo trunk-io/trunk2` to get details and extract Linear ticket IDs.

### Phase 2: Research

**Code is law.** Actual source code and PR diffs are the authoritative source of truth. Slite specs, PRDs, Slack threads, and other planning docs provide context, intent, and examples — but when they conflict with what the code does, the code wins. Only document what is actually implemented.

3. **Linear tickets**: Use `mcp__claude_ai_Linear__get_issue` for each ticket ID. Search by feature name for related engineering tickets.
4. **Slite docs**: Search Slite for PRDs, specs, roadmap items, and knowledge base articles related to the feature. Use feature name and product area as search terms. Retrieve relevant docs for product intent, requirements, and decisions.
5. **Slack channels**: Search relevant Slack channels for recent discussion, changelogs, and context:
   - `#team-flaky-tests` — Flaky Tests product discussions
   - `#team-merge-queue` — Merge Queue product discussions
   - Search by feature name, ticket ID, or key terms from the notes
6. **Existing docs**: Use `mcp__claude_ai_trunk_docs__searchDocumentation`, Glob, and Grep. Read `summary.md` for the docs hierarchy.
7. **trunk2 PR diffs** (if available): `gh pr diff <number> --repo trunk-io/trunk2 --name-only`, then read key files. When possible, also read the current source on `main` via `gh api` to confirm the latest state.
8. **Gap analysis**: Compare existing docs vs. what the code implements. Cross-reference planning docs (Slite, Slack) against code to identify discrepancies — features described in specs but not yet implemented should be flagged as open questions, not documented as existing functionality.

### Phase 2.5: Generate Sources File

9. Write `.claude/tmp/<draft-name>/sources.md` with all Linear tickets, GitHub PRs, Slite docs, Slack threads, existing docs, code references, and context links found during research. This is the reviewer audit trail. Must include:
   - A **"Code-Confirmed Details"** section listing metric names, endpoint paths, auth mechanisms, etc. as they exist in the actual codebase
   - A **"Differences: Code vs. Planning Docs"** table highlighting any discrepancies between what planning docs describe and what the code implements
   - An **"Open Questions"** section for anything that could not be confirmed from code

### Phase 3: Draft Documentation

8. Write or edit documentation:
   - **Match tone and structure** of existing Trunk docs — read nearby files first
   - **New pages**: write full content; **Updates**: edit in place; **Explainers**: add to relevant existing page
   - Update `summary.md` if adding new pages
   - Lead with user benefit, not implementation details
   - Use present tense, include practical examples
   - Don't mention internal systems (ClickHouse, Prisma, SST, Lambda)

### Phase 4: Branch, Commit, and PR

9. **Branch**: From `main`. Name: `<git-username>/<kebab-case-topic>` (username from `git config user.name`, kebab-cased). Stash unrelated changes first.
10. **Commit**: Stage changed files. Include `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`.
11. **Push and PR**: `gh pr create` with structured body. See [OUTPUTS.md](OUTPUTS.md) for PR body format.

### Phase 5: Update Linear

12. Create or update the docs ticket — add PR link, context links, change summary. Set status to "In Review". If no ticket exists, create one in Trunk Engineering with `docs` label.
13. Attach all context links (Slack, Slite, Loom) as attachments with descriptive titles.
14. Add `relatedTo` relations for every related engineering ticket found during research.

### Phase 6: Stage Outputs

15. **Slack post**: Write to `.claude/tmp/<draft-name>/slack.md`. See [OUTPUTS.md](OUTPUTS.md) for Slack formatting rules.
16. **Report**: Append an HTML card to `.claude/tmp/report.html`. See [OUTPUTS.md](OUTPUTS.md) for report format.

### Phase 7: Clean Up

17. Return to original branch, restore stashed changes.
18. Show the user: branch name, PR link, Linear ticket link, files changed, open questions, staged output file paths.

## Guidelines

- **One notes file = one PR.** Flag multi-topic drafts and ask how to split.
- **Preserve the notes file** — never delete or modify it.
- **Ask before guessing** — list specific questions rather than making assumptions.
- **Always include full PR URLs** in Linear comments and descriptions.
- **Match existing style** — read adjacent docs before writing.
- **Prioritize accuracy** — flag inferred vs. confirmed items in open questions.

## Batch Processing

Process each notes file in `.claude/drafts/` one at a time. Each gets its own branch, PR, Linear ticket, and `.claude/tmp/<draft-name>/` directory. The skill handles git stash/restore between runs.
