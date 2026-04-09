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

The Trunk MCP server supports two authentication methods:

**OAuth (default)** — Recommended for interactive use. The MCP client opens a browser window to authenticate with your Trunk account. Supported by Cursor, Claude Code, GitHub Copilot, and Gemini CLI.

**API token** — For CI environments, headless setups, or MCP clients that don't support OAuth. Pass your Trunk organization API token as a bearer token in the request header:

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

Find your API token in your organization settings at [app.trunk.io](https://app.trunk.io) under **Settings → Organization → General**.

### Get started

**To get started, configure your AI application to communicate with Trunk's MCP server:**

* [Cursor](configuration/cursor-ide.md)
* [GitHub Copilot](configuration/github-copilot-ide.md)
* [Claude Code CLI](configuration/claude-code-cli.md)
* [Gemini CLI](configuration/gemini-cli.md)
