# .claude — Agents, Skills, and Drafts

This directory contains Claude Code configuration for the Trunk docs repo.

## Directory Structure

```
.claude/
├── agents/                    # Subagent definitions (spawned via Agent tool)
│   └── doc-researcher.md      # Research agent — gathers context before writing
├── skills/                    # User-invoked skills (triggered via /skill-name)
│   ├── write-docs/            # End-to-end docs pipeline
│   │   ├── SKILL.md           # Main workflow (7 phases)
│   │   ├── OVERLAP-CHECK.md   # Phase 0: duplicate/overlap detection
│   │   └── OUTPUTS.md         # Phase 4-6: PR body, Slack post, report formats
│   └── flaky-tests/           # Flaky test diagnosis and remediation
│       ├── SKILL.md           # Entry point and sub-skill index
│       ├── detect-flakiness/  # Diagnose intermittent test failures
│       ├── root-cause-ci/     # Triage CI failures (flake vs regression vs infra)
│       ├── quarantine/        # Isolate flaky tests without disabling them
│       └── write-tests/       # Patterns for writing deterministic tests
├── drafts/                    # Input notes for write-docs skill
│   ├── TEMPLATE.md            # Template for new drafts
│   └── *.md                   # Feature notes (one per topic)
└── tmp/                       # Staged outputs (gitignored)
    ├── <draft-name>/          # Per-draft: sources.md, slack.md
    └── report.html            # Cumulative HTML report
```

## Agents vs. Skills

**Agents** (`agents/`) are autonomous subprocesses spawned by the Agent tool. They run with a specific model and limited toolset, do their work, and return results to the parent conversation. Use agents for parallelizable research tasks.

**Skills** (`skills/`) are user-invoked workflows triggered with `/skill-name`. They run in the main conversation with full tool access and follow a structured multi-phase pipeline. Use skills for end-to-end tasks that produce artifacts (PRs, tickets, reports).

| Type | How to invoke | Runs where | Best for |
|------|--------------|------------|----------|
| Agent | Spawned automatically or via Agent tool | Background subprocess | Research, context gathering, parallel work |
| Skill | `/write-docs`, `/flaky-tests` | Main conversation | Multi-step workflows with user checkpoints |

## Best Practices

### Using the doc-researcher agent

- **Spawn it early** when the scope of a docs task is unclear or when you need to survey multiple Linear tickets, PRs, or existing docs pages before deciding what to write.
- **Run it in parallel** with other research (e.g., Slack/Slite searches) to save time.
- It returns a structured research brief — use its output as input to the write-docs skill or to inform manual writing.
- The agent uses Sonnet for speed. It reads code and tickets but does not write docs or create PRs.

### Using write-docs

- **One draft = one PR.** Each `.claude/drafts/*.md` file produces its own branch, PR, and Linear ticket.
- **Start from a draft file** whenever possible. The template at `.claude/drafts/TEMPLATE.md` ensures all required fields are present.
- **Don't skip Phase 0** (overlap check). It prevents wasted work when someone else already has a PR open for the same topic.
- **Code is law.** When Slite specs, Slack threads, or planning docs conflict with what the code actually does, document the code's behavior and flag the discrepancy as an open question.
- **Engineering authors matter.** The skill identifies who built the feature from trunk2 PRs and includes their GitHub handles in the PR body so they can be tagged for technical accuracy review.
- **Review staged outputs** in `.claude/tmp/<draft-name>/` before posting. The `slack.md` file is meant for direct copy-paste into Slack (uses Slack mrkdwn, not Markdown).

### Using flaky-tests skills

- **Check for Trunk first.** If `trunk` CLI is installed, the `fix-flaky-test` MCP tool at `https://mcp.trunk.io/mcp` replaces most manual investigation steps.
- **Start with detect-flakiness** to confirm a test is actually flaky before quarantining or rewriting it.
- **Quarantine, don't disable.** A quarantined test still runs and collects data. A disabled test is invisible.
- **Always create a tracking ticket** when quarantining. Quarantine without a ticket is how flaky tests stay quarantined forever.
- The write-tests sub-skill is useful both for fixing existing flaky tests and for writing new tests that won't be flaky.

### Running skills on worktrees

When processing multiple drafts, use worktrees to run skills in parallel without branch conflicts:

1. Each worktree gets its own isolated copy of the repo
2. The skill creates its branch and PR within the worktree
3. Worktrees are cleaned up automatically if no changes are made
4. This avoids the stash/restore cycle needed when processing drafts sequentially on a single checkout

### General tips

- **Read before writing.** Always read existing docs pages adjacent to where you're adding content. Match tone, structure, and formatting.
- **Progressive disclosure.** Skills load supporting files (OVERLAP-CHECK.md, OUTPUTS.md) only when they reach the relevant phase to keep context lean.
- **Drafts are input, not output.** Never modify or delete files in `.claude/drafts/`. They're the source of truth for what was requested.
