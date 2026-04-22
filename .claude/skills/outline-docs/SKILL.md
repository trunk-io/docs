---
name: outline-docs
description: >-
  Use when starting a new docs page to scaffold a structured outline.
  Prompts for page type (overview, reference, guide), title, and save path,
  then generates a file with section headers and TODO placeholders.
  Prefer this to the write-docs skill when there is not prior specification
  on what the new docs contents should be.
allowed-tools: Write, Bash(trunk fmt)
---

# Outline Docs

Generate a scaffolded outline for a new docs page in the Trunk docs repo. The skill prompts for page type, title, and save path, then creates a file with proper headers and `<!-- TODO -->` placeholders that the engineer fills in with content. Includes a post-checklist with formatting and validation steps.

## Contents

- [Inputs](#inputs)
- [Workflow](#workflow)
  - [Phase 1: Gather inputs](#phase-1-gather-inputs)
  - [Phase 2: Generate preview](#phase-2-generate-preview)
  - [Phase 3: Write file](#phase-3-write-file)
  - [Phase 4: Post-checklist](#phase-4-post-checklist)
- [Templates](#templates)

## Inputs

The user provides:
- **Page type** — one of: Overview, Reference, Guide
- **Page title** — the H1 heading (e.g., "Installing the CLI")
- **Save path** — where to write the file (optional; defaults to `./untitled.md`)

## Workflow

Follow these phases in order.

### Phase 1: Gather inputs

Ask the user these questions sequentially (one per message):

#### Question 1: Page type

Prompt the user to choose a page type. Include definitions and examples for each:

```
What type of page are you creating?

(1) Overview
    High-level introduction to a product, feature, or concept.
    Examples: product README, "What is X?" page, feature landing page.

(2) Reference
    Lookup documentation for config options, CLI flags, API fields,
    or other structured data.
    Examples: configuration reference, command listing, options table.

(3) Guide
    Step-by-step how-to for completing a specific task.
    Examples: "Getting started", setup walkthrough, "How to configure X".

Enter 1, 2, or 3:
```

Store the user's response as `page_type`.

#### Question 2: Page title

```
What is the page title? (This becomes the H1 header)

Examples: "Installing the CLI", "Configuring Linters", "Understanding Test Reports"

Title:
```

Store the user's response as `page_title`.

#### Question 3: Save path

```
Where should I save this file?
(Default: ./untitled.md in the current directory)

Path (or press Enter for default):
```

Store the user's response as `save_path`. If blank, use `./untitled.md`.

### Phase 2: Generate preview

Generate the outline based on the page type and title. Use the appropriate template from the [Templates](#templates) section below, replacing `<title>` with `page_title`.

Display the outline in the terminal:

```
Generated outline:
========================================
[Show full outline markdown here]
========================================

Does this outline look right?
(y = write it / n = start over)
```

- If user enters `y`, proceed to Phase 3
- If user enters `n`, return to Phase 1

### Phase 3: Write file

Call `Write` tool to create the file at `save_path` with the generated outline.

After writing, output:

```
✅ Outline written to: <save_path>

Next steps:
1. Fill in all <!-- TODO --> sections
2. Add a frontmatter description if this is a top-level overview page
3. Verify all links to related pages are correct
4. Run the post-checklist (see below)
```

Then proceed to Phase 4.

### Phase 4: Post-checklist

Print the post-checklist for the user to complete:

```
Post-Checklist:
[ ] Fill in all <!-- TODO --> sections
[ ] Add frontmatter description (if page is a top-level overview)
[ ] Verify all links to related pages are correct
[ ] Run: trunk check
[ ] Use /review-docs skill to review content and get feedback
```

Then, on the user's behalf, automatically run:

```bash
trunk fmt
```

to format the skeleton markdown.

Report the results. If either command reports errors, display them and suggest fixes.

## Templates

Each template uses `<title>` as a placeholder for the page title. Replace it with the actual title from Phase 1, Question 2.

### Overview template

Use this template when the user chooses page type **(1) Overview**.

```markdown
---
description: <!-- TODO: 1-2 sentence description for page preview/SEO -->
---

# <title>

<!-- TODO: 1-2 sentence intro leading with user benefit. Example: "Trunk Code Quality is a metalinter that lets you..." -->

### How it works

<!-- TODO: Explain the core mechanism or value proposition. Consider including a diagram or ASCII art showing the flow. -->

### Key features

<!-- TODO: List 3-5 key features with brief descriptions. Use bold for feature names. -->

### Get started

<!-- TODO: Link to the getting-started page(s) for this feature. For multiple paths, consider a cards table. -->
```

**When to use this template:**
- Product/feature homepage pages
- "What is X?" pages
- Top-level overview pages that introduce a concept
- README files that lead to more detailed pages

---

### Reference template

Use this template when the user chooses page type **(2) Reference**.

```markdown
# <title>

<!-- TODO: 1-2 sentence intro explaining what this reference documents and when to use it. -->

### Quick reference

<!-- TODO: Table of the most common options/fields/commands.
Adjust columns to match what you're referencing.
Examples: Option | Type | Description
          Command | Arguments | Description
          Field | Type | Default | Description -->

| Option | Type | Description |
|--------|------|-------------|
| <!-- TODO --> | | |

### <option or section name>

<!-- TODO: Repeat this H3 block for each major option, field, or subsection.
     Include: full description, code/YAML example, and any caveats or notes. -->

```yaml
<!-- TODO: Example configuration or command usage -->
```

### Examples

<!-- TODO: 1-2 complete, real-world examples showing the reference in practical use. -->
```

**When to use this template:**
- Configuration option references
- CLI command listing pages
- API field documentation
- Setting/option reference pages
- Structured lookup documentation

---

### Guide template

Use this template when the user chooses page type **(3) Guide**.

```markdown
# <title>

<!-- TODO: 1-2 sentences explaining why/when someone would need this guide.
     Lead with the scenario. Example: "If your tests are flaky, you can use..." -->

### Prerequisites

<!-- TODO: List everything needed before starting this guide:
     - Required accounts or permissions
     - Installed tools and minimum versions
     - Prior setup or knowledge -->

- <!-- TODO -->

### Step 1 of N: <!-- TODO: Name of this step -->

<!-- TODO: Brief description of what this step accomplishes and what the user does. -->

```bash
<!-- TODO: Command or action the user takes -->
```

{% hint style="info" %}
<!-- TODO: Optional tip, caveat, or alternate approach for this step. Delete this hint block if not needed. -->
{% endhint %}

**✅ Success:** <!-- TODO: Describe what the user should see or confirm after completing this step. -->

### What's next?

<!-- TODO: Link to the next natural steps in the workflow. Example: "After setup, learn how to use X" with [link to page](page.md). -->
```

**When to use this template:**
- Step-by-step setup guides
- "Getting started" pages
- "How to configure X" pages
- Task-focused how-to articles
- Walkthrough guides with sequential steps

---

## Post-Checklist Guidance

After writing the file, the user should complete these steps:

1. **Fill in all TODO sections** — Replace every `<!-- TODO -->` comment with actual content. Comments explain what goes in each section.

2. **Add frontmatter description** — If the page is a top-level overview (e.g., `README.md` at `/code-quality/overview/README.md`), add a `description:` field in the frontmatter. Example:
   ```yaml
   ---
   description: High-level intro to Trunk Code Quality and how it works.
   ---
   ```

3. **Verify links** — Ensure all cross-references to related pages use correct relative paths and match the actual file locations. GitBook syntax:
   ```markdown
   [Related page](path/to/page.md "mention")
   ```

4. **Run validation** — Execute `trunk check` to check for linting issues.

5. **Review content** — Use the `/review-docs` skill to review the page content and get feedback before merging.

If any tool reports errors or review identifies issues, fix them before merging.
