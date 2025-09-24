---
description: Learn about how to apply fix recommendations with MCP
---

# Apply fixes with MCP

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) allows AI applications like Claude Code, Cursor, or other AI coding assistants to directly access CI Autopilot's analysis and apply fixes to your code. Instead of manually implementing suggested changes, your AI assistant can understand the root cause and apply the fix automatically.



[CI Autopilot's MCP server](../use-mcp-server/) exposes a tool called `get-root-cause-analysis`. This tool retrieves root cause analyses and fix recommendations for CI failures.



### Why use MCP instead of stacked PRs?

* Your AI assistant applies fixes directly in your preferred development environment
* No need to review and merge separate pull requests
* Fixes are applied with full context of your existing code
* Works with your existing AI coding workflow



### Prerequisites

* [CI Autopilot enabled for your GitHub repository](../ci-autopilot/get-started/)
* CI Autopilot provided a root cause analysis on your pull request
* Completed the [MCP server configuration](../use-mcp-server/configuration/) with your preferred AI application



{% hint style="info" %}
The following AI applications are currently supported: Cursor, Claude Code, Gemini CLI, and GitHub Copilot.
{% endhint %}



### Complete workflow

When using Trunk's MCP to apply fixes you will go through the following steps:



* [ ] Copy MCP prompt from CI Autopilot's comment
* [ ] Switch to the pull request branch
* [ ] Paste the MCP prompt to apply fix



### Step 1 of 3: Copy the MCP prompt from the PR comment

Every pull request comment from the CI Autopilot will include instructions on how to request a fix.

<figure><img src="../.gitbook/assets/Screenshot 2025-09-12 at 10.32.44 AM.png" alt=""><figcaption><p>Autofix Options section of the CI Autopilot comment</p></figcaption></figure>

In this example, the following MCP prompt is suggested. `duhe5h21` represents the ID of the fix recommendation.

```
Help me fix CI failures from duhe5c21
```

Users can prompt their AI application in different ways. It is important that the application has access to Trunk's MCP and is authorized to make calls.

{% hint style="info" %}
In some environments, the AI application might have other MCP servers configured with similar tools. It is important to disambiguate which tools should be used to complete the fix. You can try adding the tool name: `Trunk's MCP agent "get-root-cause-analysis"`.
{% endhint %}

### Step 2 of 3: Switch to the pull request base branch

In your terminal or IDE, ensure you are on the base branch of the pull request.



### Step 3 of 3: Prompt your AI application to apply the fix

Paste the copied prompt and follow the instructions/steps to apply and verify the fix. Once verified, push the changes to your base pull request.

