# write-docs skill

End-to-end documentation pipeline: raw notes -> reviewed docs PR with Linear tracking.

Invoked as `/write-docs <input>`.

## Directory Structure

```
write-docs/
├── SKILL.md           # Main instructions (~130 lines, loaded when skill triggers)
├── OVERLAP-CHECK.md   # Detailed dupe/overlap check procedure (loaded in Phase 0)
├── OUTPUTS.md         # PR body, Slack post, report format specs (loaded in Phases 4-6)
└── README.md          # This file (human reference only)
```

## How It Works

The skill uses progressive disclosure: Claude loads SKILL.md when triggered, then reads OVERLAP-CHECK.md and OUTPUTS.md only when it reaches the relevant phase. This keeps the context window lean.

### Pipeline

```
Phase 0    Duplicate & overlap check     Stops if a PR/branch already covers this draft
Phase 1    Parse input                   Read notes file, extract tickets, PRs, context links
Phase 2    Research                      Linear tickets, Slite PRDs, Slack channels,
                                         published docs, trunk2 PR diffs, gap analysis
Phase 2.5  Sources                       Write audit trail to .claude/tmp/<draft>/sources.md
Phase 3    Draft                         Edit existing pages or create new docs files
Phase 4    Branch & PR                   Stash → branch → commit → push → gh pr create
Phase 5    Linear                        Create/update ticket, attach links, add relations
Phase 6    Stage                         Write slack.md, append to report.html
Phase 7    Clean up                      Restore original branch and stashed changes
```

### Research Sources (Phase 2)

The skill cross-references five sources to build context before writing anything:

| Source             | What it finds                                                                            | MCP Server            |
| ------------------ | ---------------------------------------------------------------------------------------- | --------------------- |
| **Linear**         | Ticket descriptions, status, assignees, related tickets                                  | `claude.ai Linear`    |
| **Slite**          | PRDs, specs, roadmap items, knowledge base articles                                      | `claude.ai Trunk Slite` |
| **Slack**          | Team discussions, changelogs, feature context from `#team-flaky-tests`, `#team-merge-queue` | `claude.ai Slack`     |
| **Published docs** | Existing documentation pages, hierarchy from `summary.md`                                | `claude.ai trunk docs` |
| **GitHub**         | trunk2 PR diffs, code changes, implementation details                                    | `gh` CLI              |

### Inputs

| Input type        | Example                           | What happens                                                    |
| ----------------- | --------------------------------- | --------------------------------------------------------------- |
| Notes file        | `.claude/drafts/flag-as-flaky.md` | Primary mode. Reads file, extracts metadata, researches, writes |
| trunk2 PR numbers | `3187 3177`                       | Reads PR details via `gh`, extracts Linear IDs                  |
| Linear ticket IDs | `TRUNK-17633`                     | Looks up ticket, finds related PRs and context                  |
| Deploy tag        | `v126`                            | Documents features shipped in a specific release                |

Notes files follow the template at `.claude/drafts/TEMPLATE.md`.

### Outputs

**Committed (the PR):**

- Branch: `<git-username>/<kebab-case-topic>`
- PR title: `[TRUNK-XXXXX] Short descriptive title`
- PR body: summary, Linear links, context links, files changed, open questions, test plan

**Staged (gitignored, under `.claude/tmp/<draft-name>/`):**

- `sources.md` — audit trail for reviewers (every source consulted)
- `slack.md` — copy-pasteable Slack announcement (uses Slack mrkdwn, not Markdown)

**Cumulative (`.claude/tmp/report.html`):**

- HTML card appended per run — PR link, Linear link, changes summary, open questions

**Linear:**

- Ticket created/updated in Docs Maintenance project with `docs` label
- Context links attached (Slack, Slite, Loom, etc.)
- Related engineering tickets linked via `relatedTo`
- Status set to "In Review"

### Prerequisites

The skill requires these MCP servers to be connected. Verify with `claude mcp list`:

- `claude.ai Slack` — for searching team channels
- `claude.ai Trunk Slite` — for PRDs and specs
- `claude.ai trunk docs` — for searching published docs
- `claude.ai Linear` — for ticket management
- GitHub via `gh` CLI (authenticated with access to `trunk-io/trunk2`)

---

## Demo Script

Walkthrough for demoing `/write-docs` at an all-hands or team meeting. Total runtime: ~5 minutes.

### Pre-Demo Setup (10 min before)

#### 1. Clean terminal state

```bash
cd ~/TRUNK/docs
git checkout main
git pull origin main
git status  # should be clean
```

#### 2. Verify no leftover demo artifacts

```bash
git branch --list "*indefinite-monitor-muting*"
gh pr list --repo trunk-io/docs --state open --json number,title,headRefName | jq '.[] | select(.headRefName | contains("indefinite-monitor-muting"))'

# If either returns results, clean up:
# gh pr close <number> --repo trunk-io/docs --delete-branch
# git branch -D sam-gutentag/indefinite-monitor-muting
```

#### 3. Verify draft and clear previous outputs

```bash
cat .claude/drafts/indefinite-monitor-muting.md
rm -rf .claude/tmp/indefinite-monitor-muting/
```

#### 4. Verify MCP servers

```bash
claude mcp list
```

All five should show connected (see [Prerequisites](#prerequisites) above).

#### 5. Start Claude Code

```bash
claude
```

Wait for it to load. Verify `/write-docs` is recognized.

#### 6. Terminal setup

- Font size: 18-20pt for readability
- Terminal width: full screen, max 120 chars
- Dark theme for projector visibility

### The Demo

#### ACT 1: The Problem (30 seconds)

**[Speaking to audience, terminal visible but idle]**

> "Quick show of hands — who's had to write documentation for a feature someone else built? Yeah. It's not the writing that's painful, it's the context-gathering. You're reading Slack threads, digging through PRs, searching Linear, figuring out which docs pages need updating. Then you do the actual writing. Then you create a branch, open a PR, update the ticket, post in Slack. That's 30 minutes for something that should take 5."

> "We built a Claude Code skill that does all of that from a single command. Let me show you."

#### ACT 2: Show the Input (30 seconds)

**[In Claude Code, type:]**

```
cat .claude/drafts/indefinite-monitor-muting.md
```

**[Let the file scroll. Point out key sections:]**

> "This is a notes file — it's what an engineer or PM drops into our drafts folder. It has the feature name, links to the PRs that shipped it, and which docs pages need updating. It's rough and that's fine — it's input, not output."

> "Notice there's no Linear ticket yet, no branch, no PR. Just notes."

#### ACT 3: Run the Skill (2-3 minutes)

**[Type the command:]**

```
/write-docs .claude/drafts/indefinite-monitor-muting.md
```

**[Narrate each phase as it runs. Don't rush — let the audience watch the tool calls.]**

When you see `gh pr list` calls:
> "Phase zero — it's checking whether someone already opened a PR for this, or if another PR touches the same docs files."

When you see `mcp__claude_ai_Linear` calls:
> "Now it's researching. Starts with Linear to get ticket context..."

When you see Slite or Slack MCP calls:
> "It's searching our Slite knowledge base for PRDs and checking the #team-flaky-tests Slack channel for recent discussion. This is context that used to take 10 minutes of manual digging."

When you see `gh pr view` or `gh pr diff` calls:
> "Reading the trunk2 PR to see what code actually shipped."

When you see a file being written to `.claude/tmp/`:
> "That's the sources file — an audit trail so reviewers can trace any claim back to its source."

When you see `Edit` tool calls on docs files:
> "Now it's writing the actual docs. It read the existing pages first to match our tone and structure."

When you see `git` commands:
> "Creating a branch, committing, pushing..."

When you see `gh pr create`:
> "And there's the PR."

When you see Linear calls:
> "Creating a Linear ticket, attaching the PR link, context URLs, and linking related engineering tickets."

#### ACT 4: Show the Outputs (1 minute)

**[Claude will output a summary with links. Click through each one:]**

**GitHub PR** — open in browser:
> "The title has the Linear ticket ID. The body has open questions — things it couldn't confirm from the available context. It flags what needs human verification instead of guessing."

**Linear ticket** — open in browser:
> "Docs Maintenance project, assigned to me, status In Review. It attached the PR link, the Slack threads it found, and any Slite docs it consulted."

**[Show staged outputs:]**

```
cat .claude/tmp/indefinite-monitor-muting/slack.md
cat .claude/tmp/indefinite-monitor-muting/sources.md
```

> "A copy-pasteable Slack post and a full sources audit trail."

#### ACT 5: Wrap Up (30 seconds)

> "From one command and a rough notes file: a docs PR, a Linear ticket, an audit trail, and a team notification. About 3 minutes."

> "The skill searches five systems — Linear, Slite, Slack, our published docs, and GitHub PRs — to build context before writing a single line. Every PR still gets human review."

### Q&A

**"What if the docs it writes are wrong?"**
> "Every PR gets human review. The skill flags open questions explicitly. It's doing the 80%, a human does the last 20%."

**"Can this work for other repos?"**
> "The skill is specific to our docs workflow, but the pattern is portable. You write a SKILL.md describing the pipeline and Claude Code follows it."

**"How long did it take to build?"**
> "About 130 lines of instructions plus two reference files. The iteration was the slow part — maybe 2-3 sessions."

**"What if it creates a PR that conflicts with someone else's work?"**
> "Phase 0 catches that. It checks every open PR for file-level overlap before doing any work."

**"Does it handle new pages or just updates?"**
> "Both. New pages get created and added to summary.md. Updates edit existing files in place."

**"How does it know what's in Slite and Slack?"**
> "We connected them as MCP servers — same protocol as Linear. The skill searches them during research, and knows to check #team-flaky-tests and #team-merge-queue for product context."

### Post-Demo Cleanup

```bash
gh pr close <PR_NUMBER> --repo trunk-io/docs --delete-branch
git checkout main
git branch -D sam-gutentag/indefinite-monitor-muting 2>/dev/null
rm -rf .claude/tmp/indefinite-monitor-muting/
```

### Dry Run Checklist

Do a full dry run the day before. Clean up everything so the live demo starts fresh.

- [ ] Draft file exists at `.claude/drafts/indefinite-monitor-muting.md`
- [ ] No existing branch `sam-gutentag/indefinite-monitor-muting`
- [ ] No existing PR for indefinite-monitor-muting
- [ ] No existing `.claude/tmp/indefinite-monitor-muting/` directory
- [ ] Claude Code starts cleanly and recognizes the skill
- [ ] MCP servers are responding (Linear, GitBook, Slack, Slite)
- [ ] Terminal font size is readable from the back of the room
- [ ] You've timed the run — should be 2-4 minutes
- [ ] You know where to find the PR and Linear links in the output
- [ ] Linear "Docs Maintenance" project view is open in a browser tab
