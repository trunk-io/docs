# Trunk Docs — Claude Code Agents

This directory contains Claude Code subagents for documentation workflows.
When you run `claude` from this repo, these agents are automatically available.

## Prerequisites

You need two MCP servers configured (user scope):

1. **Linear** — for ticket and PR lookup
   ```bash
   claude mcp add linear --scope user -- npx -y @linear/mcp-server
   ```
2. **Trunk Docs (GitBook)** — for searching existing documentation
   ```bash
   claude mcp add trunk-docs --scope user --transport sse https://docs.trunk.io/~gitbook/mcp
   ```

Verify with `claude mcp list` or `/mcp` inside Claude Code.

## Available Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `notes-processor` | Opus | End-to-end pipeline: reads a notes file, researches, drafts docs, creates branch/PR, updates Linear |
| `doc-writer` | Opus | Full documentation drafting with all outputs (doc, PRs, questions, changelog, roadmap) |
| `doc-researcher` | Sonnet | Gathers and organizes context from Linear + existing docs before writing |
| `changelog-writer` | Sonnet | Focused changelog/release note entries |
| `branch-manager` | Sonnet | Creates branches, PRs, and updates/creates Linear tickets for tracking |

## Quick Start: Notes-Based Workflow

The fastest way to turn Slack conversations and engineer notes into docs:

### 1. Create a notes file

Copy the template and fill it in:
```bash
cp .claude/drafts/TEMPLATE.md .claude/drafts/my-feature.md
```

Paste in your Slack messages, engineer notes, Linear ticket IDs — don't
worry about formatting. Raw paste is fine.

### 2. Process the notes

```
Process the notes file at .claude/drafts/my-feature.md
```

The `notes-processor` agent will:
- Parse the notes and extract what changed
- Look up any Linear tickets for additional context
- Search existing docs to find what needs updating
- Draft the documentation changes
- Apply changes to the repo
- Create a branch (`sam/<topic>`), commit, push, and open a PR
- Update or create a Linear ticket with the PR link

### 3. Review and iterate

Check the PR and GitBook preview. The agent will list any open questions
for things it couldn't determine from the notes alone.

### Batch processing

To process multiple notes files:
```
Process all notes files in .claude/drafts/ that haven't been processed yet
```

## Usage Examples

**Process a notes file (recommended):**
```
Process the notes file at .claude/drafts/parallel-queues.md
```

**Write docs for a feature (manual):**
```
Use the doc-writer agent for the parallel queues feature.
Linear tickets: MRG-452, MRG-467
Slack context: [paste relevant messages]
```

**Research before writing:**
```
Use doc-researcher to gather context on tickets MRG-500 through MRG-510,
then use doc-writer to draft docs based on the findings
```

**Just a changelog entry:**
```
Use changelog-writer for the new test quarantine feature. Tickets: FTD-301
```

**Survey the backlog:**
```
Use doc-researcher to survey Linear for all open tickets labeled "docs"
```

## Parallel Workflows

For working on multiple features simultaneously, use [Claude Squad](https://github.com/smtg-ai/claude-squad):
```bash
brew install claude-squad
cs
```
This lets you run multiple Claude Code sessions in parallel, each with its own git worktree.

## Directory Structure

```
.claude/
  agents/
    notes-processor.md   # End-to-end pipeline orchestrator
    doc-writer.md         # Documentation drafting
    doc-researcher.md     # Context gathering
    changelog-writer.md   # Changelog entries
    branch-manager.md     # Git/PR/Linear lifecycle
    README.md             # This file
  drafts/
    TEMPLATE.md           # Notes file template
    *.md                  # Your notes files (gitignored)
```
