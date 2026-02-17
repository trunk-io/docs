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
| `doc-writer` | Opus | Full documentation drafting with all outputs (doc, PRs, questions, changelog, roadmap) |
| `doc-researcher` | Sonnet | Gathers and organizes context from Linear + existing docs before writing |
| `changelog-writer` | Sonnet | Focused changelog/release note entries |

## Usage Examples

**Write docs for a feature:**
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

**Chain agents:**
```
First use doc-researcher to survey all open tickets labeled "needs-docs",
then use doc-writer for each feature identified
```

## Parallel Workflows

For working on multiple features simultaneously, use [Claude Squad](https://github.com/smtg-ai/claude-squad):
```bash
brew install claude-squad
cs
```
This lets you run multiple Claude Code sessions in parallel, each with its own git worktree.
