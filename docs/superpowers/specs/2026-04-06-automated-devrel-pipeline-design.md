# Automated DevRel Pipeline

**Date:** 2026-04-06
**Author:** Sam Gutentag
**Status:** Approved design, pending implementation
**Linear:** TRUNK-17922 (feature flag monitoring follow-up)

## Problem

Trunk's DevRel docs workflow is reactive. Sam manually monitors Slack threads, trunk2 PRs, and deploy tags to decide what needs docs, changelog entries, or roadmap updates. The skills to do this work already exist (`draft-docs`, `write-docs`, `changelog`, `roadmap`, `release-comms`), but they require manual invocation. Features ship and go undocumented until someone notices.

## Solution

Two scheduled remote agents running in Anthropic's cloud via RemoteTrigger:

1. **Daily Scanner** -- scans trunk2 merged PRs every morning and runs the full docs/changelog/roadmap pipeline for anything user-facing.
2. **Deploy Watcher** -- polls for new deploy tags every 2 hours and runs `release-comms` when a deploy lands.

Both agents post Slack DM summaries. They run remotely with their own git checkout, so no local machine needs to be awake. MCP connections (Linear, Slack, Slite, trunk docs) are attached to each trigger.

## Architecture

### Daily Scanner

**Schedule:** `0 4 * * *` (4:00 AM PT, every day including weekends/holidays)
**Working directory:** `/Users/samgutentag/TRUNK/docs`

**Pipeline:**

1. Fetch trunk2 PRs merged in the last 24 hours (`get-merged-prs.sh`)
2. Check processed PR list (`daily-scan-log.json`) and skip already-handled PRs
3. Classify remaining PRs as user-facing or internal (defer to existing skill classification logic in `draft-docs` and `changelog`)
4. For user-facing PRs (run sequentially to avoid git branch conflicts):
   - Run `draft-docs` with the PR numbers to generate notes files
   - For each notes file produced, run `write-docs` to open a draft PR on trunk-io/docs
   - Run `changelog` to create Linear tickets for changelog-worthy changes
   - Run `roadmap` to check for newly completed roadmap items
5. Update `daily-scan-log.json` with processed PR numbers
6. Compose and send Slack DM summary
7. Append to report.html (local runs only; remote agents skip this)

**Heartbeat:** If no user-facing PRs are found, still send a Slack DM confirming the scan ran with PR count and "no action taken." This runs every day including weekends and holidays so Sam can confirm the automation is alive.

### Deploy Watcher

**Schedule:** `0 */2 * * *` (every 2 hours)
**Working directory:** `/Users/samgutentag/TRUNK/docs`

**Pipeline:**

1. Run `get-deploy-tags.sh --latest` to get the most recent tag
2. Compare against `last-deploy-tag.txt`
3. If new tag found:
   - Update `last-deploy-tag.txt`
   - Run full `release-comms` pipeline (changelog + roadmap + draft-docs)
   - For each notes file produced by draft-docs, run `write-docs` to open draft PRs
   - Compose and send Slack DM with deploy summary
   - Append to `report.html`
4. If no new tag: silent exit (no heartbeat needed, the daily scanner covers liveness)

### State Management

Since agents run remotely with a fresh git checkout each time, there are no persistent local files. State is derived fresh each run:

- **Daily scanner** queries GitHub for trunk2 PRs merged in the last 24 hours. No log of previously processed PRs is needed because the 24-hour window is self-limiting -- each run covers exactly yesterday's work.
- **Deploy watcher** queries the latest deploy tag from trunk2 and searches Linear for an existing `release-comms` ticket with that tag. If one exists, the deploy was already processed. If not, it runs the pipeline.

### Deduplication

Three layers prevent duplicate work:

1. **Time-window:** The daily scanner's 24-hour window means each PR is only in scope for one run.
2. **Docs PR-level:** The agent checks for existing open PRs on trunk-io/docs covering the same topic before creating new ones.
3. **Linear ticket-level:** The agent checks for existing changelog/roadmap tickets before creating new ones. The deploy watcher uses the presence of a Linear ticket tagged with the deploy version as its "already processed" signal.

### Slack Messages

Sent via `mcp__claude_ai_Slack__slack_send_message` to Sam's DM. Format uses Slack mrkdwn (not Markdown).

**Daily Scanner (changes found):**
```
*Daily docs scan -- April 7, 2026*

Scanned 12 merged PRs on trunk2 (April 6, 00:00-23:59 PT).

*Docs PRs opened:*
* <https://github.com/trunk-io/docs/pull/531|#531> -- Description
* <https://github.com/trunk-io/docs/pull/532|#532> -- Description

*Changelog tickets created:*
* <https://linear.app/trunk/issue/TRUNK-XXXXX|TRUNK-XXXXX> -- Title (Product)

*Roadmap updates:*
* <https://linear.app/trunk/issue/TRUNK-XXXXX|TRUNK-XXXXX> -- Item marked complete

*Skipped (not user-facing):* N PRs (infra, tests, internal tooling)

Full report: ~/.claude/tmp/report.html
```

**Daily Scanner (no changes):**
```
*Daily docs scan -- April 7, 2026*

Scanned 3 merged PRs on trunk2 (April 6, 00:00-23:59 PT). None were user-facing. No action taken.

Next scan: April 8 at 4:00 AM PT.
```

**Deploy Watcher (new deploy):**
```
*Deploy detected -- v145*

Tag v145 pushed at April 6, 8:42 PM PT. 14 PRs since v144.

*Docs drafts opened:*
* <https://github.com/trunk-io/docs/pull/533|#533> -- Description

*Changelog tickets:*
* <https://linear.app/trunk/issue/TRUNK-XXXXX|TRUNK-XXXXX> -- Title (Product)

*Roadmap:*
* No newly completed roadmap items.

*Skipped:* N PRs (infra, tests, internal tooling)

Full report: ~/.claude/tmp/report.html
```

### Failure Handling

- If a skill fails mid-run (GitHub API rate limit, MCP timeout, etc.), the agent logs the error in report.html and includes it in the Slack DM
- Partial success is acceptable: if changelog succeeds but draft-docs fails, report what worked and flag what didn't
- Silence (no Slack DM at all) means the agent didn't run (machine was asleep, Claude Code not active), which is a clear signal to investigate

### Existing Skills Used

| Skill | Used by | Purpose |
|-------|---------|---------|
| `draft-docs` | Daily Scanner | Generate notes files from trunk2 PRs |
| `write-docs` | Both | Turn notes files into docs PRs |
| `changelog` | Both | Create Linear tickets for changelog entries |
| `roadmap` | Both | Check for newly completed roadmap items |
| `release-comms` | Deploy Watcher | Orchestrate all three workflows for a deploy |
| `sam-style` | Both (via other skills) | Ensure consistent writing voice |

### Shared Scripts Used

| Script | Purpose |
|--------|---------|
| `get-merged-prs.sh` | Fetch trunk2 PRs merged in a date range |
| `get-deploy-tags.sh` | Find production deploy tags |
| `get-linear-projects.sh` | Extract Linear ticket IDs from PRs |

## Out of Scope (v1)

- **Feature flag monitoring** -- tracked as TRUNK-17922, will be a third agent added after v1 is stable
- **Auto-merging docs PRs** -- all PRs are created as drafts, Sam reviews manually
- **Slack channel posts** -- DMs only for now, could expand to #team-docs later
- **PR threading** -- each scan is independent, no cross-run context

## Success Criteria

- Daily scanner runs every morning at 4 AM PT, including weekends
- Sam receives a Slack DM every morning (heartbeat or changes summary)
- User-facing trunk2 PRs result in draft docs PRs within 24 hours of merge
- Deploys result in full release-comms output within 2 hours
- No duplicate docs PRs, changelog tickets, or roadmap tickets
- Sam spends less time hunting for what needs documenting and more time reviewing drafts

## Implementation Plan

Implemented as two RemoteTrigger configurations with self-contained prompts. Each trigger gets its own remote session with a fresh git checkout of trunk-io/docs, access to MCP servers (Linear, Slack, Slite, trunk docs), and Bash/Git/gh CLI tools. The prompts must be fully self-contained since the remote agent has no access to local skill files.

See `docs/superpowers/plans/2026-04-06-automated-devrel-pipeline.md` for the implementation plan.
