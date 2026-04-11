---
description: >-
  Use the Analysis tab on a test detail page to view AI-generated investigation
  results, trigger new investigations, and get fix recommendations.
---

# AI Investigation

Trunk Flaky Tests can automatically investigate a flaky test and surface root cause findings directly in the Trunk web app. The **Analysis** tab on a test detail page shows the latest investigation results, lets you trigger a new investigation, apply a fix, or browse past investigations.

{% hint style="info" %}
The Analysis tab requires a GitHub app installation for the repository. If your repo does not have the Trunk GitHub app installed, the Analyze button will be disabled.
{% endhint %}

## Open the Analysis tab

1. Navigate to **Flaky Tests** in the Trunk web app.
2. Click a test case to open the test detail page.
3. Select the **Analysis** tab.

If no investigation has run for this test yet, the tab shows an empty state with an **Analyze** button.

## Understanding investigation results

When an investigation is available, the Analysis tab shows:

### Latest Analysis header

At the top, you will see:

- The **overall confidence score** (color-coded green for 80%+, yellow for 50%+, orange below 50%)
- A relative timestamp for when the investigation ran
- An **Analyze** button to trigger a new investigation
- A **History** button to view past investigations
- An **Apply Fix** button if the investigation produced actionable findings

### Key Findings

The Key Findings section lists the top three findings ordered by impact. Each finding shows:

| Field | Description |
|---|---|
| Fact type badge | The analysis source that produced the finding |
| Confidence percentage | How confident the AI is in this specific finding |
| Finding content | A summary with links to relevant code, CI logs, or commits |

A collapsible **Other Findings** section holds any additional findings beyond the top three.

### Fact types

Each finding is labeled with the analysis source used to produce it:

| Fact type | What it analyzes |
|---|---|
| **CI Logs** | Supplements test failure outputs with CI workflow logs |
| **Git Blame** | Recent code changes that may have introduced flakiness |
| **Failure Mode** | Patterns in error outputs and failure metadata |
| **Test Purpose** | What the test covers and how it has drifted from its intent |
| **Environment** | Environmental factors such as resource constraints or timing |
| **Co-failure** | Other tests that fail at the same time, pointing to shared causes |
| **File Co-change** | Related files that have changed alongside the failing test |

## Trigger a new investigation

Click **Analyze** to open the Trigger Analysis modal. Click **Run Analysis** to kick off a fresh investigation. Trunk will analyze the test using the latest CI logs, git history, and failure data.

Investigations run automatically when a test first becomes flaky (if the GitHub app is installed). You can trigger additional investigations manually at any time.

## Apply a fix

Click **Apply Fix** to open the Apply Fix modal. Trunk surfaces the fix options available for the current investigation:

- **Copy Prompt** — copies a prompt you can paste into an AI coding assistant to guide it toward the fix
- **Fix with MCP** — connects directly to the Trunk MCP server to apply the fix (requires the MCP server to be configured)
- **Automate with Webhooks** — links to the webhooks configuration to automate fix workflows

See [Use MCP Server](use-mcp-server/README.md) for information on setting up the MCP integration.

## View investigation history

Click **History** to open the Analysis History modal. This shows past investigations for the test case, each with:

- A confidence badge
- A findings count
- A timestamp

Click any past investigation to expand its details.

## Related

- [Get root cause analysis (MCP)](use-mcp-server/mcp-tool-reference/get-root-cause-analysis.md)
- [Webhooks](webhooks/README.md)
- [Managing detected flaky tests](managing-detected-flaky-tests.md)
