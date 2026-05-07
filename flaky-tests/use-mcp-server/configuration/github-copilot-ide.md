---
description: Add Trunk's MCP Server to GitHub Copilot
---

# GitHub Copilot (IDE)

## One-click setup

Use the "Add to VS Code" action to add the Trunk MCP server

<p align="center"><a href="vscode:mcp/install?%7B%22name%22%3A%22trunk%22%2C%22url%22%3A%22https%3A//mcp.trunk.io/mcp%22%7D"><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&#x26;logo=visual-studio-code&#x26;logoColor=white" alt="Add trunk MCP server to VS Code"></a></p>

### Command Palette setup

Run `CMD+Shift+P` to open the Command Palette and choose `MCP: Add Server`. Choose `HTTP` and input `https://mcp.trunk.io/mcp`. Set the name to `trunk`.

A new window will open to confirm the MCP configuration. It should show:

```json
{
	"servers": {
		"trunk": {
			"url": "https://mcp.trunk.io/mcp",
			"type": "http"
		}
	},
	"inputs": []
}
```



### Alternative: Update MCP configuration

Add the following [configuration](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) to your project's `.vscode/mcp.json` file.

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

### Authentication with OAuth (default)

After the MCP server was added, users need to authorize GitHub Copilot to communicate with the server. Follow these steps to complete auth.



**Step 1: Start MCP server**

Run `CMD+Shift+P` to open the Command Palette and choose `MCP: List Servers`. Choose `trunk` and select `Start Server` to authenticate.



**Step 2: Login & authorize**

A new webpage will be opened. Login with your Trunk account and follow instructions to authorize GitHub Copilot to communicate with the MCP server.



**Step 3: Confirm**

Follow instructions to get back to GitHub Copilot. With auth completed, GitHub Copilot will be able to fetch the tools exposed by Trunk's MCP server.

```
2025-09-10 12:49:16.975 [info] Discovered 2 tools
```

### Alternative: Authentication with API token

If you prefer not to use the OAuth flow, you can authenticate with your Trunk organization API token. Find your token under **Settings > API** in the Trunk dashboard.

Add the token to your `.vscode/mcp.json`:

```json
{
  "mcpServers": {
    "trunk": {
      "url": "https://mcp.trunk.io/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer ${env:TRUNK_API_TOKEN}"
      }
    }
  }
}
```

{% hint style="info" %}
VS Code uses `${env:VARIABLE_NAME}` syntax for environment variable interpolation in MCP configuration files, unlike other clients which use `${VARIABLE_NAME}`.
{% endhint %}

