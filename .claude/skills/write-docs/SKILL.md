---
name: write-docs
description: Process notes, Slack threads, or trunk2 deploy context into documentation changes. Creates a branch, edits docs, opens a PR, and updates Linear. Use when given a notes file from .claude/drafts/, trunk2 PR numbers, Linear ticket IDs, or a deploy tag to document.
allowed-tools: Bash(git *), Bash(gh pr *), Bash(gh issue *), Bash(gh api *), Read, Write, Edit, Glob, Grep, mcp__claude_ai_Linear__get_issue, mcp__claude_ai_Linear__list_issues, mcp__claude_ai_Linear__list_projects, mcp__claude_ai_Linear__save_issue, mcp__claude_ai_Linear__save_comment, mcp__claude_ai_Linear__create_attachment, mcp__claude_ai_trunk_docs__searchDocumentation, WebFetch
---

Process raw input (notes files, Slack threads, engineer context, trunk2 deploy info) into polished documentation changes with full project tracking.

## Products

Documentation is organized by product:
- **Merge Queue** — `/merge-queue/` in the docs repo
- **Flaky Tests** — `/flaky-tests/` in the docs repo
- **CI Autopilot** — `/ci-autopilot/` in the docs repo
- **Code Quality** — `/code-quality/` in the docs repo
- **Setup & Administration** — `/setup-and-administration/` in the docs repo

## Inputs

The user may provide any combination of:
- **A notes file path** (e.g., `.claude/drafts/my-feature.md`) — the primary input mode. Contains Slack pastes, engineer notes, Linear ticket IDs, context links.
- **trunk2 PR numbers** — PRs from the product repo (`trunk-io/trunk2`) to document
- **Linear ticket IDs** — `TRUNK-NNNNN` references to look up
- **A deploy tag** (e.g., `v126`) — document features shipped in a specific release
- **Context links** — Slack threads, Slite docs, Loom videos, etc.
- **A specific docs page to update** — if the user knows what needs changing

If a notes file is provided, use `.claude/drafts/TEMPLATE.md` as the reference format.

## Steps

### Phase 0: Duplicate and Overlap Check

Before doing any work, check if this draft has already been processed or if another PR already covers the same docs:

#### Step 1: Check for existing PRs/branches from this draft

1. **Determine the expected branch name**: From the draft filename, derive the kebab-case topic (e.g., `flag-as-flaky.md` → `flag-as-flaky`). Run `git config user.name` to get the username prefix. The expected branch pattern is `<git-username>/<topic>` (with possible suffix variations).

2. **Check for existing PRs**: Run `gh pr list --repo trunk-io/docs --state open --head "<branch-pattern>" --json number,title,url,headRefName` to find any open PR from a matching branch. Also search by draft name: `gh pr list --repo trunk-io/docs --state open --json number,title,url,headRefName | jq '.[] | select(.headRefName | contains("<topic>"))'`.

3. **Check for existing local branches**: Run `git branch --list "*<topic>*"` to find local branches matching this draft.

4. **If a match is found**: Stop and show the user:
   - The existing PR number, title, and URL (if any)
   - The existing branch name (if any)
   - Ask: "A PR/branch already exists for this draft. Would you like to: (a) update the existing PR, (b) close it and start fresh, or (c) skip this draft?"
   - Do NOT proceed until the user responds.

#### Step 2: Check for overlapping PRs from other authors

Even if no exact match exists, another PR may already cover the same docs pages.

1. **Read the draft** to identify the target docs files/product area (from the `Target Docs` section or by inferring from the topic — e.g., a "flag as flaky" draft targets `flaky-tests/detection.md`).

2. **List all open PRs**: Run `gh pr list --repo trunk-io/docs --state open --json number,title,headRefName,url --limit 50`.

3. **Check for file overlap**: For any PR that looks potentially related (based on title or branch name matching the same product area), run `gh pr view <number> --repo trunk-io/docs --json files --jq '[.files[].path]'` and compare against the draft's target files.

4. **If overlapping PRs are found**: Stop and show the user:
   - The overlapping PR number, title, URL, and author
   - Which target files overlap
   - Ask: "PR #NNN already touches [overlapping files]. Would you like to: (a) proceed anyway (changes will likely conflict), (b) wait for that PR to merge first, or (c) skip this draft?"
   - Do NOT proceed until the user responds.

5. **If no overlaps found**: Continue to Phase 1.

### Phase 1: Parse and Understand

1. If a notes file was provided, read it completely and extract:
   - Feature/change name
   - Linear ticket IDs (`TRUNK-NNNNN`)
   - GitHub PR URLs or numbers
   - Context links (Slack, Slite, Loom, Google Docs, etc.)
   - Product area
   - Change type (new feature, update, fix, deprecation, explainer)
   - Key details about what changed and why

2. If trunk2 PR numbers or a deploy tag were provided instead:
   - Use `gh pr view <number> --repo trunk-io/trunk2` to get PR details
   - Extract Linear ticket IDs from PR titles and branch names

### Phase 2: Research

3. **Look up Linear tickets**: Use `mcp__claude_ai_Linear__get_issue` for each ticket ID to get descriptions, status, assignee, linked PRs, and related tickets.

4. **Search Linear for related work**: Search by feature name and product area to find engineering tickets that describe the same functionality. Collect related ticket IDs for linking later.

5. **Search existing docs**: Use `mcp__claude_ai_trunk_docs__searchDocumentation` to find published docs on the topic. Also search the local filesystem:
   - Use Glob to find related files by path
   - Use Grep to find references to the feature/topic
   - Read `summary.md` to understand the docs hierarchy

6. **Read trunk2 PR diffs** (if PR numbers available): Use `gh pr diff <number> --repo trunk-io/trunk2 --name-only` to understand what code changed, then read key files for context.

7. **Identify gaps**: Compare what exists in the docs vs. what the notes/PRs describe. Determine:
   - Does a page need updating, or does a new page need creating?
   - What sections are affected?
   - What's accurate vs. outdated?

### Phase 2.5: Generate Sources File

8. Determine the output directory from the draft filename (e.g., `.claude/drafts/flag-as-flaky.md` → `.claude/tmp/flag-as-flaky/`). All staged outputs for this run go under this directory.

   Write a sources audit trail to `.claude/tmp/<draft-name>/sources.md`. This lets reviewers verify accuracy. Include:
   - All Linear tickets found (with clickable links)
   - All GitHub PRs (with links, status, key changes)
   - Existing docs files relevant to this change
   - Key code references from PRs
   - All context links from the notes
   - Related Linear tickets discovered via search

### Phase 3: Draft Documentation

9. Write or edit documentation:
   - **Match the tone and structure of existing Trunk docs** — read nearby files for reference
   - For **new pages**: write the full page content
   - For **updates**: edit the existing file(s) in place
   - For **explainers**: add examples and scenarios to the relevant existing page. Use collapsible `<details>` blocks for edge cases. Keep happy-path guides clean.
   - Update `summary.md` if adding new pages

   Writing guidelines:
   - Lead with the user benefit, not implementation details
   - Use present tense ("Merge Queue now supports...")
   - Include practical examples and code snippets where relevant
   - Don't mention internal systems (ClickHouse, Prisma, SST, Lambda)
   - Use the customer's vocabulary, not engineering jargon

### Phase 4: Create Branch, Commit, and PR

10. **Branch**: Create a branch from `main`. Determine the git username by running `git config user.name` and converting it to kebab-case (e.g., "Sam Gutentag" → `sam-gutentag`). Name the branch `<git-username>/<kebab-case-topic>`.
    - Stash any unrelated working tree changes first
    - Apply only the files relevant to this change

11. **Commit**: Stage the changed files and commit with a clear message. Include `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`

12. **Push and PR**: Push to origin and create a PR via `gh pr create` with:
    - **Title format:** `[TRUNK-XXXXX] Short descriptive title` (prefix with Linear ticket ID if one exists)
    - Body containing:
      - **Summary** — bullet list of changes
      - **Linear tickets** — clickable links to all related tickets
      - **Context links** — all Slack, Slite, Loom links from the notes
      - **Files changed** — list of files created/modified
      - **Open questions** — things that couldn't be confirmed from available context
      - **Test plan** — checklist for reviewer (e.g., "check GitBook preview", "verify code example works")

### Phase 5: Update Linear

13. **Create or update the docs ticket**:
    - If a ticket exists: update description with PR link, context links, summary of changes. Add a comment with the PR link. Update status to "In Review".
    - If no ticket exists: create one in Trunk Engineering team with `docs` label, assigned to "me". Include PR link and full context.

14. **Attach context links**: For every URL from the notes (Slack, Slite, Loom, etc.), add it as an attachment on the Linear ticket with a descriptive title (e.g., `"Slack: #channel — topic"`).

15. **Link related tickets**: For every related engineering ticket discovered during research, add a `relatedTo` relation on the docs ticket.

### Phase 6: Stage Outputs

16. **Slack post**: Write to `.claude/tmp/<draft-name>/slack.md`. This file must be directly copy-pasteable into Slack with correct formatting. Use Slack's mrkdwn syntax (not Markdown):
    - Bold: `*text*` (single asterisks, not double)
    - Links: `<URL|display text>`
    - Bullets: `•` (bullet character, not `-`)
    - No Markdown-style headers (`##`), links (`[text](url)`), or bold (`**text**`)

    Format:
    ```
    *[Feature Name] — docs update ready for review*

    [1-2 sentence summary of what changed in the docs.]

    • PR: <GitHub PR URL|#NNN>
    • Linear: <Linear ticket URL|TRUNK-XXXXX>

    *Open questions for the team:*
    • [list any items needing eng confirmation]
    ```

17. **Review report**: Append an HTML card to `.claude/tmp/report.html` with PR link, Linear link, changes summary, review focus areas, and open questions. If the file doesn't exist, create it with basic HTML styling.

### Phase 7: Clean Up

19. Return to the original branch and restore any stashed changes.

20. **Output summary**: Show the user:
    - Branch name and PR link
    - Linear ticket link
    - Files changed (list)
    - Open questions (numbered)
    - Staged output files (slack, sources)

## Guidelines

- **One notes file = one PR.** If a notes file describes multiple unrelated changes, flag this and ask how to split.
- **Preserve the notes file** — don't delete or modify it. It's the audit trail.
- **Ask before guessing** — if the notes are too ambiguous, output your best interpretation and list specific questions rather than making assumptions.
- **Always include PR links** in Linear comments and descriptions.
- **Match existing style** — read adjacent doc files before writing. Don't introduce new formatting conventions.
- **Keep happy paths clean** — add examples in dedicated sections, not inline with workflow steps.
- **Prioritize accuracy** — flag anything you inferred vs. confirmed in the open questions.

## Batch Processing

To process multiple notes files:
```
Process each notes file in .claude/drafts/ one at a time.
For each: research, draft, apply, branch/PR, update Linear, then move to the next.
```

Each file gets its own branch (`<git-username>/<topic>`), PR, Linear ticket, and output directory under `.claude/tmp/`. Process one at a time to avoid git conflicts.
