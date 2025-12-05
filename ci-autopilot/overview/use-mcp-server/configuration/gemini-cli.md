---
description: Add Trunk's MCP Server to Gemini
---

# Gemini (CLI)

### CLI setup

Run the following command to add the MCP server configuration. If you want to only enable it for yourself, use `--scope user` instead.

```bash
gemini mcp add --transport http trunk https://mcp.trunk.io/mcp --scope project
```

Once completed, reopen Gemini.



### Alternative: Update MCP configuration

Add the following [configuration](https://github.com/google-gemini/gemini-cli/blob/v0.1.19/docs/tools/mcp-server.md#oauth-support-for-remote-mcp-servers) to your project's `.gemini/settings.json` file.

```json
{
  "mcpServers": {
    "trunk": {
      "httpUrl": "https://mcp.trunk.io/mcp"
    }
  }
}
```



### Authentication

After the MCP server was added to Gemini, users need to authorize to communicate with the server. Follow these steps to complete auth.



**Step 1: Start Gemini CLI**&#x20;

In your terminal, run `gemini` .



**Step 2: Run the mcp auth command**

Run `/mcp auth trunk` to initiate the authentication and authorization flow.

&#x20;

**Step 3: Login & authorize**

A new webpage will be opened. Log in with your Trunk account and follow the instructions to authorize Gemini to communicate with the MCP server.



**Step 4: Confirm**

Follow instructions to get back to Gemini. A confirmation should be shown:

```
ℹ✅ Successfully authenticated with MCP server 'trunk'!
 

ℹRe-discovering tools from 'trunk'...
 

ℹSuccessfully authenticated and refreshed tools for 'trunk'.
```

**With auth completed, Gemini will be able to fetch the tools exposed by Trunk's MCP server.**
