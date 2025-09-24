---
description: Add Trunk's MCP Server to Github Copilot
---

# GitHub Copilot (IDE)

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

### Authentication

After the MCP server was added to Cursor, users need to authorize Cursor to communicate with the server. Follow these steps to complete auth.



**Step 1: Start MCP server**

Run `CMD+Shift+P` to open the Command Palette and choose `MCP: List Servers`. Choose `trunk` and select `Start Server` to authenticate.



**Step 2: Login & authorize**

A new webpage will be opened. Login with your Trunk account and follow insturctions to authorize GitHub Copilot to communicate with the MCP server.



**Step 3: Confirm**

Follow instructions to get back to GitHub Copilot. With auth completed, GitHub Copilot will be able to fetch the tools exposed by Trunk's MCP server.

```
2025-09-10 12:49:16.975 [info] Discovered 2 tools
```

