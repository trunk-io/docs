---
description: >-
  Leverage the power of CI Autopilot from your IDE, or the AI application of
  your choosing
---

# Use MCP Server

CI Autopilot comes with a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server. AI applications like Claude Code or Cursor can use MCP servers to connect to data sources, tools, and workflows - enabling them to access key information and perform tasks.

### Supported AI applications

The following applications are currently supported: Cursor, Claude Code, Gemini CLI, and GitHub Copilot.

{% hint style="info" %}
Gemini Code Assist and Windsurf are not supported due to their limited support for MCP servers
{% endhint %}

### API

Our MCP server is available at `https://mcp.trunk.io/mcp` and exposes the following tools:

<table><thead><tr><th width="265.30859375">Tool</th><th>Capability</th></tr></thead><tbody><tr><td><a href="mcp-tool-reference/get-root-cause-analysis.md"><code>fix-flaky-test</code></a></td><td>Experimental: Retrieve insights around a failing/flaky test</td></tr><tr><td><a href="mcp-tool-reference/set-up-test-uploads.md"><code>setup-trunk-uploads</code></a></td><td>Experimental: Create a setup plan to upload test results</td></tr></tbody></table>

### Authorization

The Trunk MCP server supports two authentication methods.

**OAuth (default)**

OAuth 2.0 + OpenID Connect is the default. MCP clients that support the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) will initiate the OAuth flow automatically. Most interactive clients (Cursor, Claude Code, GitHub Copilot) use this path.

**API token**

As an alternative, you can authenticate with your Trunk organization API token. This is useful for MCP clients that do not support OAuth, CI/headless environments, or quick manual setup.

Find your token under **Settings > API** in the Trunk dashboard. Pass it as a Bearer token in the `Authorization` header:

```json
{
  "mcpServers": {
    "trunk": {
      "url": "https://mcp.trunk.io/mcp",
      "headers": {
        "Authorization": "Bearer <your-trunk-api-token>"
      }
    }
  }
}
```

API token auth is org-level — all requests are attributed to the organization rather than to a specific user. OAuth remains the preferred method for interactive use because it provides user-level identity.

### Get started

**To get started, configure your AI application to communicate with Trunk's MCP server:**

* [Cursor](configuration/cursor-ide.md)
* [GitHub Copilot](configuration/github-copilot-ide.md)
* [Claude Code CLI](configuration/claude-code-cli.md)
* [Gemini CLI](configuration/gemini-cli.md)
