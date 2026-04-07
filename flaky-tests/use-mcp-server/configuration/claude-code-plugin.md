---
description: Install the Trunk plugin for Claude Code
---

# Claude Code Plugin

The Trunk plugin for Claude Code bundles the MCP server connection, slash commands, and skills into a single install. This is the recommended way to connect Trunk to Claude Code.

## Install the Plugin

Run this in Claude Code:

```
/plugin install trunk@claude-plugin-directory
```

This installs the Trunk plugin from the [Claude community plugins directory](https://github.com/anthropics/claude-plugins-community), giving you access to the MCP server connection, slash commands, and skills that activate automatically.

<details>

<summary>Alternative: install directly from GitHub</summary>

You can also install from the plugin repository URL:

```
/plugin install trunk@https://github.com/trunk-io/claude-code-plugin
```

This is useful if you want to pin to a specific version or test changes before they land in the community directory.

</details>

## Authentication

After installing, Claude Code will prompt you to authenticate with Trunk on first use.

1. Run any Trunk command (e.g., `/trunk:fix-flaky`) or trigger an MCP tool call
2. Claude Code will open a browser window for OAuth login
3. Log in with your Trunk account and authorize the connection
4. You'll see `Authentication successful. Connected to trunk.` back in the terminal

## Slash Commands

| Command | What it does |
|---|---|
| `/trunk:fix-flaky <test_name>` | Retrieves root cause analysis for a flaky test and offers to apply the fix |
| `/trunk:why-flaky <test_name>` | Explains why a test is flaky without making changes — good for triage |
| `/trunk:setup-uploads` | Detects your test framework and CI provider, then generates the upload configuration |

### Fix a flaky test

```
/trunk:fix-flaky test_user_login
```

Trunk analyzes the test, explains the root cause (race condition, shared state, time dependency, etc.), and shows a proposed fix with a diff. Confirm to apply the changes directly.

### Understand why a test is flaky

```
/trunk:why-flaky test_payment_processing
```

Same analysis as `fix-flaky`, but read-only. Useful when you want to understand the problem before deciding how to handle it — especially for tests you didn't write.

### Set up test uploads

```
/trunk:setup-uploads
```

Walks through configuring your repo to upload test results to Trunk. The plugin detects your CI provider and test framework automatically, then generates ready-to-paste config snippets.

## Skills

The plugin includes two skills that activate automatically based on context:

**Flaky test patterns** — activates when you're debugging or writing tests. Provides common flaky test patterns and proven fixes so Claude Code can reference them without you asking.

**Trunk CI setup** — activates when you're editing CI configuration files (`.github/workflows/`, `.circleci/config.yml`, etc.). Provides best practices for test upload configuration.

## Also Available For

- [Cursor](cursor-ide.md) (one-click install)
- [GitHub Copilot](github-copilot-ide.md) (one-click install)
- [Gemini CLI](gemini-cli.md)
- [Any MCP client](https://github.com/trunk-io/mcp-server) — manual configuration
