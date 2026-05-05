---
description: >-
  Use the Trunk MCP server from your IDE or AI application to access flaky test
  insights and configure test uploads
---

# Use MCP Server

Trunk Flaky Tests includes a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server. AI applications like Claude Code or Cursor can use MCP servers to connect to data sources, tools, and workflows, enabling them to access key information and perform tasks.

### Supported AI applications

The following applications are currently supported: Cursor, Claude Code, Gemini CLI, and GitHub Copilot.

{% hint style="info" %}
Gemini Code Assist and Windsurf are not supported due to their limited support for MCP servers
{% endhint %}

### API

The Trunk MCP server is available at `https://mcp.trunk.io/mcp` and exposes the following tools:

<table><thead><tr><th width="265.30859375">Tool</th><th>Capability</th></tr></thead><tbody><tr><td><a href="mcp-tool-reference/search-test.md"><code>search-test</code></a></td><td>Experimental: Lookup the id of a test case</td></tr><tr><td><a href="mcp-tool-reference/fix-flaky-test.md"><code>fix-flaky-test</code></a></td><td>Experimental: Retrieve insights around a failing/flaky test</td></tr><tr><td><a href="mcp-tool-reference/investigate-ci-failure.md"><code>investigate-ci-failure</code></a></td><td>Experimental: Retrieve failing test logs from a CI run</td></tr><tr><td><a href="mcp-tool-reference/set-up-test-uploads.md"><code>setup-trunk-uploads</code></a></td><td>Create a setup plan to upload test results</td></tr></tbody></table>

### Authorization

The Trunk MCP server supports the OAuth 2.0 + OpenID Connect standard for MCP authorization.

### Get started

**To get started, configure your AI application to communicate with Trunk's MCP server:**

* [Cursor](configuration/cursor-ide.md)
* [GitHub Copilot](configuration/github-copilot-ide.md)
* [Claude Code CLI](configuration/claude-code-cli.md)
* [Gemini CLI](configuration/gemini-cli.md)
