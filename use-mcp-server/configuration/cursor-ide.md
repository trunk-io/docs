---
description: Add Trunk's MCP Server to Cursor
---

# Cursor (IDE)

### One-click setup

Use the "Add to Cursor" action to add the Trunk MCP server:

<p align="center"><a href="https://cursor.com/en/install-mcp?name=trunk&#x26;config=eyJ1cmwiOiJodHRwczovL21jcC50cnVuay5pby9tY3AifQ%3D%3D"><img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Add trunk MCP server to Cursor"></a></p>



Once clicked, follow instructions to open the MCP configuration in Cursor. A new settings window to confirm the installation of the MCP server will be shown. Click on "Install" to proceed.

<figure><img src="../../.gitbook/assets/Screenshot 2025-09-10 at 11.28.24 AM.png" alt="" width="375"><figcaption></figcaption></figure>

### Alternative: Update MCP configuration

Add the following [configuration](https://docs.cursor.com/en/context/mcp#model-context-protocol-mcp) to your project's `.cursor/mcp.json` file. If you want to enable it only for yourself, add it to `~/.cursor/mcp.json` instead.

```json
{
  "mcpServers": {
    "trunk": {
      "url": "https://mcp.trunk.io/mcp"
    }
  }
}
```



### Authentication

After the MCP server was added to Cursor, users need to authorize Cursor to communicate with the server. Follow these steps to complete auth.



**Step 1: Open MCP Settings**

Run `CMD+Shift+P` to open the command palette and choose `View: Open MCP Settings`

&#x20;

**Step 2: Enable the Trunk MCP server**

A "Needs authentication" status will be shown:

<figure><img src="../../.gitbook/assets/Screenshot 2025-09-10 at 11.28.34 AM.png" alt="" width="375"><figcaption></figcaption></figure>



**Step 3: Login & authorize**

A new webpage will be opened. Login with your Trunk account and follow insturctions to authorize Cursor to communicate with the MCP server.



**Step 4: Confirm**

Follow instructions to get back to Cursor. With auth completed, Cursor will be able to fetch the tools exposed by Trunk's MCP server:

<figure><img src="../../.gitbook/assets/Screenshot 2025-09-10 at 11.29.00 AM.png" alt="" width="375"><figcaption></figcaption></figure>

