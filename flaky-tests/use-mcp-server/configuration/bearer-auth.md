---
description: Add Trunk's MCP Server via Bearer Authentication
---

# Bearer Authentication

You can leverage Trunk's MCP server for all of your agentic needs. When using the MCP in cloud environments, authenticate using Bearer Authentication.

### API Token

Retrieve your organization's API token from the settings page in the web app, e.g. `https://app.trunk.io/<orgSlug>/settings`.

### Authorization Header

Set the following header when connecting to the MCP `https://mcp.trunk.io/mcp`:

| Header Key | Header Value |
| - | - |
| `Authorization` | `Bearer <token>` |
