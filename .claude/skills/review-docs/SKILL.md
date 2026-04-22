---
name: review-docs
description: >-
  Use when docs changes are ready to review before opening a PR. Reviews
  git diff for repetition, structural completeness, logic errors, and style
  consistency with related pages. Runs trunk fmt and trunk check.
allowed-tools: Bash(git diff *), Bash(git log *), Bash(trunk fmt), Bash(trunk check), Read, Glob, Grep, Edit
---

# Review Docs

Review docs changes for quality before opening a PR. Checks git diff for unnecessary repetition, structural completeness, logic errors, and style consistency with related pages. Runs `trunk fmt` and `trunk check` and prompts to help fix issues.

## Contents

- [Inputs](#inputs)
- [Workflow](#workflow)
  - [Phase 1: Identify changed files](#phase-1-identify-changed-files)
  - [Phase 2: Run automated checks](#phase-2-run-automated-checks)
  - [Phase 3: Read related pages for style baseline](#phase-3-read-related-pages-for-style-baseline)
  - [Phase 4: Review each changed file](#phase-4-review-each-changed-file)
  - [Phase 5: Generate report](#phase-5-generate-report)
  - [Phase 6: Prompt for fixes](#phase-6-prompt-for-fixes)
- [Review Criteria](#review-criteria)
- [Style Conventions](#style-conventions)

## Inputs

The user provides:
- **Optional file path** — review a specific `.md` file instead of all changed files
- If no path provided, reviews all changed `.md` files in the branch via `git diff main...HEAD`

## Workflow

Follow these phases in order.

### Phase 1: Identify changed files

Run `git diff --name-only main...HEAD` to get all changed files on the current branch.
Filter for `.md` files only.

If a specific file path was provided as an argument, use that single file instead.

If no `.md` files are found, output:
```
ℹ️ No .md files changed in git diff. Nothing to review.
```
and exit.

### Phase 2: Run automated checks

On behalf of the user, run:

```bash
trunk fmt
trunk check
```

Collect the output (success or any issues found). Include this in the final report.

### Phase 3: Read related pages for style baseline

For each changed file, determine its product area from its directory path:

| Path | Product Area |
|------|--------------|
| `merge-queue/` | Merge Queue |
| `flaky-tests/` | Flaky Tests |
| `ci-autopilot/` | CI Autopilot |
| `code-quality/` | Code Quality |
| `setup-and-administration/` | Setup & Admin |

Use `Glob` to find 2 other `.md` files in the same product area directory. Read them to establish a baseline for:
- Tone and voice (formal vs. conversational)
- Terminology and phrasing
- Header structure and naming
- Section flow and organization

Store these as reference for Phase 4 comparisons.

### Phase 4: Review each changed file

Read each changed `.md` file and evaluate it against the four review criteria (see [Review Criteria](#review-criteria) below).

Document findings by criterion. If a file passes a criterion with no issues, no note needed. Only document issues.

### Phase 5: Generate report

Print the review report. Format:

```
Review Report — <filename>
========================================
✅ trunk fmt: passed
✅ trunk check: passed

[Repetition]
- <section/location>: <issue description and suggested fix>

[Structure]
- <issue description>: <suggested fix>

[Logic]
- <issue description>: <suggested fix>

[Style & Consistency]
- <issue description and baseline from related pages>: <suggested fix>

Summary: N issues found across M files.
```

**Report rules:**
- Only print sections with issues. Omit clean categories.
- If a tool (trunk fmt/check) found issues, note them separately and include in report.
- If no issues found across any file and both tools pass, print:
  ```
  ✅ No issues found. All files are ready for a PR.
  ```

### Phase 6: Prompt for fixes

After the report, ask:

```
Would you like help fixing any of these issues? (y/n)
```

If the user answers **no**, exit.

If the user answers **yes**:
1. List all issues from the report
2. Ask which issues to fix (they can choose specific ones or "all")
3. For **clear-cut fixes** (style/repetition/obvious rewording), apply the edits directly using the `Edit` tool
4. For **structural/logic issues**, explain what should be changed and let the user decide whether to apply the fix or manually edit
5. After fixes are applied, suggest running `/review-docs` again to verify

---

## Review Criteria

### 1. No unnecessary repetition

**Check for:**
- Same information stated multiple times within a single page
- Redundant paragraphs or sections that say the same thing
- Concepts explained once, then re-explained a few sentences later

**Example of repetition to flag:**
```markdown
### How it works

Trunk Code Quality is a metalinter. A metalinter lets you lint…

Trunk is a metalinter that…  [← repetitive]
```

**Suggested fix:** Merge or delete the redundant statement. Keep one clear explanation.

---

### 2. Structure completeness

**Check for:**
- Logical flow: Does the page progress from concept to action (or whatever is appropriate)?
- Header hierarchy: H1 title, then H3 sections (no H2). Are sections ordered logically?
- **Guide pages:** Prerequisites → step-by-step → success criteria → what's next all present?
- **Reference pages:** Brief intro → quick reference table → detailed sections → examples all present?
- **Overview pages:** Intro → how it works → key features → get started all present?

**Example of incomplete structure to flag:**
```markdown
# Installing the CLI

### Step 1: Download

[steps…]

### What's next?
[no prerequisites section above—should have been there]
```

**Suggested fix:** Add missing prerequisites before Step 1. Re-order sections for logical flow.

---

### 3. Logic errors

**Check for:**
- Contradictory statements (e.g., "only works on Linux" in one section, "all platforms" in another)
- Steps that reference undefined concepts (e.g., "set the FLAG variable" without explaining what FLAG is)
- Claims inconsistent with the product area or code (e.g., "always runs locally" when it might not)
- Instructions that skip implied prerequisites

**Example of logic error to flag:**
```markdown
### Step 1: Configure the linter

Set the `output_format` flag to `json`.

### Step 2: Run the linter

trunk check [← doesn't mention that output_format was set, but code may require it]
```

**Suggested fix:** Add clarity: "Now when you run `trunk check`, output will be in JSON format."

---

### 4. Style & consistency

**Check for:**
- **Tense:** Present tense throughout ("Click X" not "You will click X" or "You clicked X")
- **Lead:** User benefit first ("Trunk X lets you…"), not implementation detail
- **Terminology:** Matches related pages in the same product area (established in Phase 3)
- **Jargon:** No internal system names (ClickHouse, Prisma, SST, Lambda, etc.)
- **Hint blocks:** Tips/warnings use `{% hint style="info/warning/success" %}` — not plain text callouts
- **Success markers:** Guide steps end with `**✅ Success:**` line

**Example of style issue to flag:**
```markdown
The system will write logs to ClickHouse for analysis.
[← internal jargon; user doesn't care where logs go]
```

**Suggested fix:** Reframe for user benefit: "Trunk analyzes your test results to identify patterns."

---

## Style Conventions

Reference for Phase 4 checks — derived from existing Trunk docs pages:

| Convention | Rule | Example |
|------------|------|---------|
| **Headers** | H3 (`###`) for all sections; no H2 in body | ✅ `### How it works` |
| **Tense** | Present tense | ✅ "Click X to open Y" not "You will click" |
| **User benefit** | Lead with benefit, not implementation | ✅ "Trunk catches errors early" not "uses static analysis" |
| **Hints** | Use GitBook blocks for tips/warnings | ✅ `{% hint style="info" %}` not plain text |
| **Success** | Guide steps end with `**✅ Success:**` | ✅ `**✅ Success:** You see X in the dashboard` |
| **Jargon** | Avoid internal system names | ✅ "analyzes test results" not "ClickHouse stores metrics" |
| **Links** | Relative paths with GitBook mention syntax | ✅ `[page](path/to/page.md "mention")` |

---

## Typical Review Workflow

1. Engineer creates a docs page using `/outline-docs` or writes one manually
2. Engineer runs `/review-docs` — reports any issues found
3. If issues exist, engineer answers `y` to fixes
4. Fixes are applied; engineer can run `/review-docs` again to verify clean
5. Once clean, engineer opens a PR
6. CI `claude-review.yaml` runs final typo/grammar/formatting check on the PR
7. PR is reviewed and merged

The `review-docs` skill bridges the gap between local writing and PR submission, catching quality issues before CI review.
