---
description: Use Trunk's CI Autopilot in pull requests or with MCP
---

# Use CI Autopilot

Once CI Autopilot is set up, it automatically investigates every CI failure in your pull requests and provides detailed root cause analysis with fix recommendations. Here's how to work with CI Autopilot's findings.



### How CI Autopilot works

When your pull request's CI fails, CI Autopilot:

1. **Investigates the failure** within a few minutes
2. **Posts a detailed comment** with root cause analysis and fix suggestions
3. **Groups related failures** to reduce noise and cognitive load
4. **Provides multiple options** for applying fixes



### Understanding CI Autopilot comments

Each investigation comment includes a test summary, affected CI jobs or tests, root-cause and fix recommendations, as well as autofix options.

→ **Learn more:** [**Understanding root cause analysis**](understand-root-cause-analysis.md)



### Applying recommended fixes

#### Request automatic stacked PRs

**Best for:** team workflows and code review processes

Use the slash command in your PR:

```
/trunk stack-fix <fix-id>
```

This creates a separate pull request with the proposed changes, keeping your original PR clean while providing a ready-to-review solution.

**→ Learn more:** [**Request fixes on PRs**](request-fixes-on-prs.md)



#### Apply fixes with AI Assistants (MCP)

**Best for:** solo development and immediate fixes in your IDE

Copy the provided MCP prompt from CI Autopilot's comment and use it with compatible AI applications like Claude Code or Cursor. Your AI assistant will access the root cause analysis and apply fixes directly in your development environment.

**→ Learn more:** [**Apply fixes with MCP**](apply-fixes-with-mcp.md)
