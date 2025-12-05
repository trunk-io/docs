---
description: Add Trunk's MCP Server to Claude Code
---

# Claude Code (CLI)

### CLI setup

Run the following command to add the MCP server configuration. If you want to only enable it for yourself, use `--scope user` instead.

```bash
claude mcp add --transport http trunk https://mcp.trunk.io/mcp --scope project
```

Once completed, reopen Claude Code.

### Alternative: Update MCP configuration

Add the following [configuration](https://docs.anthropic.com/en/docs/claude-code/mcp) to your project's `.mcp.json` file.

```json
{
  "mcpServers": {
    "trunk": {
      "url": "https://mcp.trunk.io/mcp",
      "type": "http"
    }
  }
}
```

### Authentication

After the MCP server was added to Claude Code, users need to authorize to communicate with the server. Follow these steps to complete auth.

**Step 1: Start Claude Code CLI**

In your terminal, run `claude` .

**Step 2: Run the mcp command**

Claude Code should recognize that auth is required. Run `/mcp` to authenticate, select trunk, and hit Enter:

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-09-10 at 12.02.48 PM.png" alt="" width="370"><figcaption></figcaption></figure>

**Step 3: Login & authorize**

A new webpage will be opened. Log in with your Trunk account and follow the instructions to authorize Claude Code to communicate with the MCP server.

**Step 4: Confirm**

Follow instructions to get back to Claude Code. A confirmation should be shown:

```
Authentication successful. Connected to trunk.
```

**With auth completed, Claude Code will be able to fetch the tools exposed by Trunk's MCP server.**
