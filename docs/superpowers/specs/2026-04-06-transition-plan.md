# Transition Plan: Automated DevRel Pipeline

**Date:** 2026-04-06
**Status:** Phase 1 (local crontab on Sam's Mac)

## Phases

### Phase 1: RemoteTrigger on Anthropic Cloud (current)

Both agents run as RemoteTrigger scheduled sessions in Anthropic's cloud infrastructure. Each trigger gets a fresh git checkout, Bash/Git/gh tools, and MCP connections (Linear, Slack, Slite, trunk docs).

**Pros:** No local machine needs to be awake. Server-side persistence (no 7-day expiry). MCP connections managed via claude.ai settings. Zero infrastructure to maintain.

**Cons:** Remote agent can't access local skill files -- prompts must be self-contained. Can't run local scripts (shared scripts logic must be inlined or replicated via gh CLI). Limited to tools declared in the trigger config.

**Monitoring:**
- Slack heartbeat messages confirm the daily scanner ran (even on days with no changes)
- Silence = trigger didn't fire, check https://claude.ai/code/scheduled
- Manual catch-up: run the trigger immediately via RemoteTrigger `run` action

**Exit criteria for Phase 2:** Need for local file access, custom tooling, or workflows that exceed what RemoteTrigger supports.

### Phase 2: Dedicated Runner (future, if needed)

Move to a Raspberry Pi or cloud VM running Claude Code CLI with full local access.

**When to consider:**
- Workflows need access to local files or custom scripts
- MCP connection issues with RemoteTrigger that don't affect local sessions
- Need for multi-repo orchestration that requires local git state
- Token/cost constraints on RemoteTrigger usage

**Setup requirements (if needed):**
- [ ] Claude Code CLI installed and authenticated
- [ ] GitHub CLI (`gh`) authenticated with access to trunk-io/docs and trunk-io/trunk2
- [ ] MCP server connections configured
- [ ] Git configured with Sam's user identity
- [ ] Skills directory synced
- [ ] Cron or systemd timer to keep Claude Code session alive

### Phase 3: Feature Flag Monitoring Agent (follow-up)

Add a third trigger that monitors for LaunchDarkly feature flag changes. Tracked as TRUNK-17922. Build after Phase 1 is stable for at least a week.

## Current State Log

| Date | Phase | Notes |
|------|-------|-------|
| 2026-04-06 | Design | Architecture approved. Discovered RemoteTrigger, pivoted from local Mac to cloud-hosted. |
| 2026-04-06 | Phase 1 | RemoteTrigger tested but MCP connections unavailable in CCR environment. Pivoted to local crontab. |
| 2026-04-06 | Phase 1 | Daily scanner validated end-to-end locally (2 docs PRs, 5 changelog tickets, Slack DM). Crontab installed. |
| 2026-04-06 | Phase 1 | Deploy watcher prompt updated for macOS/gh. Heartbeat added. Crontab installed. Remote triggers disabled (preserved). |
