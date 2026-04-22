---
name: outline-docs
description: >-
  Use when starting a new docs page to scaffold a structured outline.
  Extracts page type, title, and context from your message, asks only for
  missing information, then generates a file with sections pre-filled with
  initial content (1-2 sentences) and focused TODO comments for expansion.
  Prefer this to the write-docs skill when there is no prior specification.
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
  - [Phase 4: Docs organization](#phase-4-docs-organization)
  - [Phase 5: Post-checklist](#phase-5-post-checklist)
- [Templates](#templates)

## Inputs

The user may provide upfront context:
- **Page type** — one of: Overview, Reference, Guide
- **Page title** — the H1 heading (e.g., "Installing the CLI")
- **Save path** — where to write the file (optional; defaults to `./untitled.md`)
- **Topic description** — what the page should cover (e.g., "walkthrough of investigating and fixing flaky tests")
- **Key prerequisites** — required setup, permissions, or tools mentioned

## Workflow

Follow these phases in order.

### Phase 0: Extract upfront context

Before asking any questions, scan the user's message for:
- **Page type hints** — words like "guide", "overview", "reference", "how-to", "walkthrough"
- **Page title hints** — capitalized phrases, quoted strings, or suggested topics
- **Path hints** — directory structures, URLs, or path suggestions
- **Topic details** — what the page should document or teach
- **Prerequisites** — requirements, access levels, tools, or setup mentioned

Store any detected values. Only ask for information that's missing or ambiguous.

### Phase 1: Gather missing inputs

Ask only for inputs not extracted from upfront context (ask one question per message):

**If page type is unknown:**

#### Question: Page type

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

**If page title is unknown:**

#### Question: Page title

```
What is the page title? (This becomes the H1 header)

Examples: "Installing the CLI", "Configuring Linters", "Understanding Test Reports"

Title:
```

Store the user's response as `page_title`.

**If save path is unknown:**

#### Question: Save path

```
Where should I save this file?
(Default: ./untitled.md in the current directory)

Path (or press Enter for default):
```

Store the user's response as `save_path`. If blank, use `./untitled.md`.

**After gathering missing inputs:**

Confirm extracted + provided values to the user:
```
Using:
- Page type: [page_type]
- Title: [page_title]
- Path: [save_path]
- Topic: [topic_description if provided]

Ready to generate outline.
```

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

Generate the outline based on the page type, title, and any topic context provided. Use the appropriate template from the [Templates](#templates) section below, replacing `<title>` with `page_title`.

**Pre-fill strategy:**
- Replace obvious `<!-- TODO -->` comments with 1-2 sentences of initial content from Claude based on topic/context
- Keep `<!-- TODO: ... -->` comments for sections that need user expansion or details Claude can't infer
- Example: Instead of `<!-- TODO: Explain prerequisites -->`, write: "This guide requires beta access and the Investigate Flaky Tests setting enabled. <!-- TODO: Add specific account requirements or version constraints -->"

Display the outline in the terminal:

```
Generated outline:
========================================
[Show full outline markdown here, with Claude pre-fill + remaining TODOs]
========================================

Does this outline look right?
(y = write it / n = start over)
```

- If user enters `y`, proceed to Phase 3
- If user enters `n`, return to Phase 1 to gather new inputs

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

### Phase 4: Docs Organization

Add the new page and its appropriate title to the `summary.md` file at the root of the repo.

Then proceed to Phase 5.

### Phase 5: Post-checklist

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
description: [Claude generates 1-2 sentences summarizing the feature/product for SEO. TODO: Refine if needed.]
---

# <title>

[Claude writes 1-2 sentences explaining what this feature is and the primary user benefit. TODO: Add specific use cases or scenarios if needed.]

### How it works

[Claude provides a high-level explanation of the mechanism or value proposition based on topic context. TODO: Add diagrams, ASCII art, or deeper technical detail if appropriate.]

### Key features

[Claude lists 3-5 key features with brief descriptions. TODO: Expand with additional features or rearrange by priority.]

### Get started

[Claude provides a link or brief guidance pointing to the getting-started page(s) for this feature. TODO: Add alternatives or decision tree if multiple paths exist.]
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

[Claude writes 1-2 sentences explaining what this reference documents and when to use it. TODO: Add details about scope or version constraints if needed.]

### Quick reference

[Claude creates a table of the most common options/fields/commands with appropriate columns. TODO: Add or remove rows based on actual options to document.]

| Option | Type | Description |
|--------|------|-------------|
| [Claude populates 1-2 examples] | | [Brief description] |
| <!-- TODO: Add additional rows --> | | |

### [Option or section name from topic]

[Claude provides a high-level description of this option. TODO: Add detailed explanation, code example, and caveats specific to your use case.]

```yaml
# [Claude provides a basic example structure. TODO: Expand with complete configuration or command usage.]
```

### Examples

[Claude provides 1-2 real-world examples of how to use this reference. TODO: Add domain-specific examples or alternative approaches if applicable.]
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

[Claude writes a direct, feature-focused intro (1-2 sentences). Example: "You can configure Trunk to automatically analyze your flaky tests and raise fix PRs." TODO: Adjust the capability description if needed.]

### Prerequisites

[Claude lists essential requirements based on workflow context (access, tools, setup, knowledge). TODO: Add or remove prerequisites specific to your implementation.]

- Beta access via waitlist (request at https://slack.trunk.io)
- The "Investigate Flaky Tests" setting enabled
- <!-- TODO: Add other prerequisites if applicable -->

### Step 1: [Claude names step based on workflow]

[Claude provides a brief description of what this step accomplishes and what the user does. TODO: Add more detail or clarifications.]

```bash
# [Claude provides example command or action. TODO: Add actual command with parameters for your use case.]
```

{% hint style="info" %}
[Claude adds a relevant tip or caveat if appropriate. Delete this hint block if not needed. TODO: Customize guidance if needed.]
{% endhint %}

**✅ Success:** [Claude describes expected outcome or confirmation. TODO: Specify success criteria if different.]

### Step 2: [Claude names next step]

[Claude provides description. TODO: Fill in step details.]

<!-- Repeat Step N blocks as needed -->

### What's next?

[Claude suggests next logical steps or links to related documentation. TODO: Add links to follow-on guides or references.]
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
