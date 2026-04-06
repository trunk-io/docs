# Automated DevRel Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create two RemoteTrigger scheduled agents that automatically scan trunk2 for merged PRs and deploy tags, then run the full docs/changelog/roadmap pipeline and report results via Slack DM.

**Architecture:** Two RemoteTrigger cron jobs running in Anthropic's cloud. Each gets a fresh git checkout of trunk-io/docs, Bash/Git/gh CLI tools, and MCP connections (Linear, Slack, Slite, trunk docs). Prompts are self-contained since the remote agent has no access to local skill files. State is derived fresh each run (GitHub API for PRs, Linear for existing tickets, git tags for deploys).

**Tech Stack:** RemoteTrigger API, GitHub CLI (`gh`), MCP servers (Linear, Slack, Slite, trunk docs GitBook), Git

---

## File Structure

No new files are created in the repo. The implementation consists of two RemoteTrigger configurations created via the API. The prompts live server-side in the trigger config.

Supporting docs (already created):
- `docs/superpowers/specs/2026-04-06-automated-devrel-pipeline-design.md` -- spec
- `docs/superpowers/specs/2026-04-06-transition-plan.md` -- transition plan

---

## Task 1: Draft and Test the Daily Scanner Prompt

The daily scanner prompt must be self-contained. Before creating the trigger, we need to validate the prompt works by running it manually in a local Claude Code session.

**Files:**
- Create: `docs/superpowers/specs/daily-scanner-prompt.md` (reference copy of the prompt)

- [ ] **Step 1: Write the daily scanner prompt**

The prompt must instruct the remote agent to:
1. Clone trunk-io/trunk2 (or use gh CLI to query PRs without cloning)
2. Find PRs merged in the last 24 hours
3. Classify each as user-facing or internal
4. For user-facing PRs: search existing docs PRs and Linear tickets to avoid duplicates
5. Create draft docs PRs on trunk-io/docs for documentable changes
6. Create Linear changelog tickets for changelog-worthy changes
7. Check the public roadmap and create Linear tickets for newly completed items
8. Send a Slack DM to Sam with the summary (or heartbeat if no changes)

Write the prompt to `docs/superpowers/specs/daily-scanner-prompt.md`:

```markdown
You are an automated DevRel pipeline agent. Your job is to scan trunk-io/trunk2 for recently merged PRs and produce docs updates, changelog entries, and roadmap status updates.

## Step 1: Gather merged PRs from the last 24 hours

Run this command to get trunk2 PRs merged in the last 24 hours:

gh pr list --repo trunk-io/trunk2 --state merged --search "merged:>=$(date -u -v-1d +%Y-%m-%d)" --limit 100 --json number,title,author,mergedAt,headRefName,body,labels

If the date command fails (Linux vs macOS), try:
gh pr list --repo trunk-io/trunk2 --state merged --search "merged:>=$(date -u -d '1 day ago' +%Y-%m-%d)" --limit 100 --json number,title,author,mergedAt,headRefName,body,labels

Save the count of PRs found. If zero PRs, skip to Step 7 (heartbeat).

## Step 2: Classify PRs

For each PR, determine if it is user-facing. A PR is user-facing if it:
- Changes app UI code, API endpoints, configuration options, or user-visible behavior
- Adds or modifies a feature that customers interact with
- Changes error messages, CLI output, or webhook payloads

A PR is NOT user-facing if it:
- Only touches tests, CI config, internal tooling, or documentation
- Only contains database migrations with no behavior change
- Is a dependency update with no user-visible effect
- Only touches files in docs/prd/, docs/trd/, or internal docs

For borderline cases, err on the side of including the PR. Sam will review the drafts.

Record the classification for each PR: user-facing (docs-worthy, changelog-worthy, roadmap-relevant) or skipped.

## Step 3: Check for duplicates

For each user-facing PR, check if work already exists:
- Search open PRs on trunk-io/docs: gh pr list --repo trunk-io/docs --state open --search "<PR title keywords>" --json number,title
- Search Linear for existing tickets: use mcp__claude_ai_Linear__list_issues with query matching the PR title or feature name, filtered to team "Trunk Engineering" and labels "docs" or "changelog"

Skip any PR that already has a docs PR or Linear ticket covering it.

## Step 4: Create docs draft PRs

For each documentable PR (after dedup):
1. Read the PR diff to understand what changed: gh pr diff <number> --repo trunk-io/trunk2
2. Look up any linked Linear tickets from the PR body
3. Search existing docs for related pages: use mcp__claude_ai_trunk_docs__searchDocumentation
4. Determine what docs changes are needed (new page, update existing page, no change needed)
5. If docs changes are needed:
   - Create a branch on trunk-io/docs: git checkout -b sam-gutentag/<kebab-case-topic>
   - Write or edit the docs files, matching the tone and structure of nearby existing docs
   - Commit with message and Co-Authored-By trailer
   - Push and create a draft PR with structured body (Summary, Linear tickets, Engineering authors, Context links, Files changed, Open questions, Test plan)
   - Return to main branch

## Step 5: Create changelog Linear tickets

For each changelog-worthy PR (after dedup):
1. Determine the product area (Flaky Tests, Merge Queue, CI Autopilot, General)
2. Write a customer-facing changelog entry: what changed, why it matters, how to use it
3. Create a Linear ticket in team "Trunk Engineering" with labels: changelog, <product-label>
4. Attach the trunk2 PR link and any related context

## Step 6: Check roadmap status

1. Fetch the public roadmap: use WebFetch on https://trunk.io/roadmap
2. For each roadmap item, check if recent PRs complete it
3. If a roadmap item is newly complete, create a Linear ticket with labels: roadmap, complete, <product-label>

## Step 7: Send Slack DM summary

Send a Slack DM to Sam Gutentag using mcp__claude_ai_Slack__slack_send_message.

Find Sam's Slack user ID by searching: mcp__claude_ai_Slack__slack_search_users with query "Sam Gutentag"

If user-facing PRs were found, format the message as:

*Daily docs scan -- <today's date>*

Scanned <N> merged PRs on trunk2 (<yesterday's date>, 00:00-23:59 PT).

*Docs PRs opened:*
* <PR URL|#NNN> -- description
[for each docs PR created]

*Changelog tickets created:*
* <Linear URL|TRUNK-XXXXX> -- title (product)
[for each changelog ticket]

*Roadmap updates:*
* <Linear URL|TRUNK-XXXXX> -- item marked complete
[or "No newly completed roadmap items."]

*Skipped (not user-facing):* N PRs (infra, tests, internal tooling)

If NO user-facing PRs were found, send heartbeat:

*Daily docs scan -- <today's date>*

Scanned <N> merged PRs on trunk2 (<yesterday's date>, 00:00-23:59 PT). None were user-facing. No action taken.

Next scan: <tomorrow's date> at 4:00 AM PT.

## Important guidelines

- All docs PRs must be created as drafts (gh pr create --draft)
- PR branch format: sam-gutentag/<kebab-case-topic>
- Commit trailer: Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- Linear team: Trunk Engineering (ID: 16f26d2e-3c38-4c56-869d-9fea8f33321e)
- Sam's Linear user ID: 59254109-3f85-4e5c-afb8-1b17fa4354d3
- Never use em dashes in any writing output. Use periods, commas, or parentheticals instead.
- Write in a direct, technically grounded style. No preamble, no AI-isms.
- Never use: leverage, delve, nuanced, robust, seamlessly, elevate, streamline, supercharge, empower, unlock, comprehensive.
```

- [ ] **Step 2: Save the prompt as a reference doc**

Save to `docs/superpowers/specs/daily-scanner-prompt.md` so it can be maintained alongside the spec.

- [ ] **Step 3: Test the prompt locally**

Run the prompt in the current Claude Code session to validate it works end-to-end. Verify:
- PR fetching works via gh CLI
- Classification logic produces reasonable results
- Dedup checks find existing work
- Slack DM sends correctly

Run: paste the prompt into a Claude Code session and observe the output.
Expected: Slack DM arrives with either a changes summary or heartbeat message.

- [ ] **Step 4: Iterate on the prompt based on test results**

Fix any issues found during testing. Common problems:
- Date command syntax differences (macOS vs Linux in the remote environment)
- GitHub API rate limits on large PR lists
- MCP tool name or parameter mismatches
- Branch conflicts if a previous run left a branch

- [ ] **Step 5: Commit the reference prompt**

```bash
git add docs/superpowers/specs/daily-scanner-prompt.md
git commit -m "docs: add daily scanner prompt for automated DevRel pipeline

Reference copy of the prompt used in the RemoteTrigger configuration.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Create the Daily Scanner Trigger

- [ ] **Step 1: Determine the UTC cron expression**

4:00 AM PST = 4:00 AM America/Los_Angeles. During PDT (current), that's UTC-7, so 11:00 AM UTC. During PST, that's UTC-8, so 12:00 PM UTC.

Since PDT is active now: `57 10 * * *` (10:57 AM UTC = 3:57 AM PDT, slightly offset to avoid the :00 mark).

Note: when clocks fall back to PST in November, this will fire at 2:57 AM PST instead of 3:57 AM. Acceptable drift. Adjust if needed.

- [ ] **Step 2: Generate a UUID for the event**

```bash
python3 -c "import uuid; print(str(uuid.uuid4()))"
```

Save the output for the create call.

- [ ] **Step 3: Create the trigger**

Call RemoteTrigger with action "create" using the body structure from the schedule skill. Include:
- name: "daily-devrel-scanner"
- cron_expression: "57 10 * * *"
- enabled: true
- environment_id: "env_014TsMDQpwWR98RLG2srG4cz"
- model: "claude-sonnet-4-6"
- source repo: https://github.com/trunk-io/docs
- allowed_tools: ["Bash", "Read", "Write", "Edit", "Glob", "Grep"]
- MCP connections: Slack, Linear, Slite, trunk docs
- Event prompt: the full daily scanner prompt from Task 1

- [ ] **Step 4: Verify the trigger was created**

```
RemoteTrigger action: "list"
```

Expected: one trigger named "daily-devrel-scanner" with the correct cron expression.

- [ ] **Step 5: Test-run the trigger**

```
RemoteTrigger action: "run" trigger_id: "<id from step 4>"
```

Expected: Slack DM arrives within a few minutes. Check https://claude.ai/code/scheduled/<trigger_id> for the session log.

---

## Task 3: Draft and Test the Deploy Watcher Prompt

- [ ] **Step 1: Write the deploy watcher prompt**

The deploy watcher prompt must:
1. Check the latest deploy tag on trunk-io/trunk2
2. Search Linear for an existing release-comms ticket with that tag version
3. If no existing ticket: run the full release-comms pipeline
4. Send Slack DM with deploy summary (or stay silent if no new deploy)

Write to `docs/superpowers/specs/deploy-watcher-prompt.md`:

```markdown
You are an automated deploy watcher agent. Your job is to detect new production deploys on trunk-io/trunk2 and run the full release communications pipeline (changelog, roadmap, docs drafts).

## Step 1: Check for the latest deploy tag

Run:
gh release list --repo trunk-io/trunk2 --limit 2 --json tagName,publishedAt,name

This returns the two most recent releases. The first is the latest deploy, the second is the previous one.

Save both tag names and the latest publish date.

## Step 2: Check if this deploy was already processed

Search Linear for an existing ticket that references this deploy tag:
- Use mcp__claude_ai_Linear__list_issues with query matching the tag name (e.g., "v145"), team "Trunk Engineering", and label "changelog"

If a ticket exists with this tag in the title or description, this deploy was already processed. Send no message and exit.

## Step 3: Get PRs in this deploy

Run:
gh pr list --repo trunk-io/trunk2 --state merged --search "merged:<latest_tag_date>..$(date -u +%Y-%m-%dT%H:%M:%SZ)" --limit 100 --json number,title,author,mergedAt,headRefName,body,labels

Or use git log between tags:
gh api repos/trunk-io/trunk2/compare/<previous_tag>...<latest_tag> --jq '.commits | length'

Get the full list of PRs between the two tags.

## Step 4: Classify PRs (same rules as daily scanner)

Classify each PR as user-facing or internal. See the daily scanner prompt for classification rules.

## Step 5: Create docs draft PRs

For each documentable PR (after dedup check against existing trunk-io/docs PRs):
1. Read the PR diff
2. Look up linked Linear tickets
3. Search existing docs
4. Create branch, write docs, commit, push, create draft PR
5. Return to main

## Step 6: Create changelog Linear tickets

For each changelog-worthy PR (after dedup against existing Linear tickets):
1. Determine product area
2. Write customer-facing changelog entry
3. Create Linear ticket with labels: changelog, <product-label>
4. Include the deploy tag in the ticket description

## Step 7: Check roadmap status

1. Fetch public roadmap from https://trunk.io/roadmap
2. Check if any roadmap items are newly completed by PRs in this deploy
3. Create Linear tickets for completed items with labels: roadmap, complete

## Step 8: Send Slack DM

Send a Slack DM to Sam Gutentag.

Find Sam's Slack user ID by searching: mcp__claude_ai_Slack__slack_search_users with query "Sam Gutentag"

Format:

*Deploy detected -- <tag_name>*

Tag <tag_name> pushed at <publish_date>. <N> PRs since <previous_tag>.

*Docs drafts opened:*
* <PR URL|#NNN> -- description
[for each docs PR created, or "None needed."]

*Changelog tickets:*
* <Linear URL|TRUNK-XXXXX> -- title (product)
[for each changelog ticket]

*Roadmap:*
* <Linear URL|TRUNK-XXXXX> -- item marked complete
[or "No newly completed roadmap items."]

*Skipped:* N PRs (infra, tests, internal tooling)

## Important guidelines

- All docs PRs must be created as drafts (gh pr create --draft)
- PR branch format: sam-gutentag/<kebab-case-topic>
- Commit trailer: Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- Linear team: Trunk Engineering (ID: 16f26d2e-3c38-4c56-869d-9fea8f33321e)
- Sam's Linear user ID: 59254109-3f85-4e5c-afb8-1b17fa4354d3
- Never use em dashes. Use periods, commas, or parentheticals instead.
- Write in a direct, technically grounded style. No preamble, no AI-isms.
- Never use: leverage, delve, nuanced, robust, seamlessly, elevate, streamline, supercharge, empower, unlock, comprehensive.
- If no new deploy is detected, exit silently. Do NOT send a Slack message.
```

- [ ] **Step 2: Save and commit the reference prompt**

```bash
git add docs/superpowers/specs/deploy-watcher-prompt.md
git commit -m "docs: add deploy watcher prompt for automated DevRel pipeline

Reference copy of the prompt used in the RemoteTrigger configuration.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

- [ ] **Step 3: Test the prompt locally**

Run the prompt in the current Claude Code session. Verify:
- Tag fetching works
- Dedup against Linear works (should find existing tickets for recent deploys)
- If a genuinely new deploy exists, the pipeline runs correctly

---

## Task 4: Create the Deploy Watcher Trigger

- [ ] **Step 1: Determine the UTC cron expression**

Every 2 hours, offset from :00. Use `7 */2 * * *` (7 minutes past every even hour UTC).

- [ ] **Step 2: Generate a UUID**

```bash
python3 -c "import uuid; print(str(uuid.uuid4()))"
```

- [ ] **Step 3: Create the trigger**

Call RemoteTrigger with action "create":
- name: "deploy-watcher"
- cron_expression: "7 */2 * * *"
- enabled: true
- environment_id: "env_014TsMDQpwWR98RLG2srG4cz"
- model: "claude-sonnet-4-6"
- source repo: https://github.com/trunk-io/docs
- allowed_tools: ["Bash", "Read", "Write", "Edit", "Glob", "Grep"]
- MCP connections: Slack, Linear, Slite, trunk docs
- Event prompt: the full deploy watcher prompt from Task 3

- [ ] **Step 4: Verify and test-run**

List triggers to confirm both exist. Run the deploy watcher trigger manually and verify behavior (should either find a new deploy or exit silently).

---

## Task 5: Validate End-to-End and Update Docs

- [ ] **Step 1: Wait for the first scheduled daily scan**

Check Slack the morning after creation. Expected: a Slack DM at ~4:00 AM PT with either changes or heartbeat.

- [ ] **Step 2: Verify the deploy watcher fires on the next deploy**

After the next trunk2 deploy tag is pushed, check Slack within 2 hours. Expected: deploy summary DM.

- [ ] **Step 3: Update the transition plan**

Edit `docs/superpowers/specs/2026-04-06-transition-plan.md` to update the current state log:

```markdown
| 2026-04-07 | Phase 1 | Both triggers created and first daily scan verified |
```

- [ ] **Step 4: Commit all documentation updates**

```bash
git add docs/superpowers/specs/ docs/superpowers/plans/
git commit -m "docs: finalize automated DevRel pipeline setup

Both RemoteTrigger agents created and verified. Daily scanner runs at
4 AM PT, deploy watcher polls every 2 hours.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Self-Review Notes

- **Spec coverage:** All spec requirements covered. Daily scanner (Task 1-2), deploy watcher (Task 3-4), Slack DMs with heartbeat, dedup, end-to-end validation.
- **No placeholders:** All prompts are complete with actual commands and MCP tool names.
- **Date handling:** The remote agent runs on Linux, so `date -d '1 day ago'` syntax is correct. The macOS fallback (`date -v-1d`) is included for local testing.
- **Timezone:** 4 AM PDT = 11 AM UTC. Cron set to 10:57 UTC to avoid :00 mark. Will drift to 2:57 AM PST in winter -- acceptable.
- **Missing from spec:** The spec mentions `report.html` but remote agents can't write local files. Updated spec to note this. Slack DM is the primary output.
