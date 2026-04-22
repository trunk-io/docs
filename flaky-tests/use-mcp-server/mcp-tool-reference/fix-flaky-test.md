---
description: 'MCP tool reference: fix-flaky-test'
---

# Fix Flaky Test

### Overview

The `fix-flaky-test` tool retrieves insights and historical failure analysis about a flaky test. This tool allows AI assistants to access investigation results and apply fixes directly in your development environment. For more information, see [Autofix Flaky Tests](../../autofix-flaky-tests.md).


**Return Type:** Structured analysis data with fix recommendations. Structure: metadata, summary, facts

### Parameters

#### Required Parameters

| Parameter  | Type   | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `repoName` | string | Repository name in `owner/repo` format (e.g., `trunk-io/trunk`) |
| `testCaseId` | string | UUID of the test case to retrieve investigations for |

#### Optional Parameters

| Parameter | Type   | Description                                                            |
| --------- | ------ | ---------------------------------------------------------------------- |
| `orgSlug` | string | The name of your organization in the Trunk app                         |
| `investigationId`   | string | Specific fix identifier from previous investigation queries |
| `createNewInvestigation`   | boolean | Whether or not to trigger a new investigation (may take up to 1 minute) |

### Getting Parameter Values

If your AI assistant doesn't have direct access to Git information, use these commands:

**Get repository name:**

```bash
git remote -v
```

Look for the repository name in the output (e.g., `trunk-io/trunk` from `git@github.com:trunk-io/trunk.git`)

### Usage Examples

#### With Test ID

```
Fix the flaky test with ID <testCaseId>
```

#### Create New Investigation

```
Run a new analysis to help me fix flaky test with ID <testCaseId>
```

#### With Existing Investigation

```
Retrieve the investigation for test <testCaseId> with investigationId <investigationId>
```

### Error Handling

| Error                          | Cause                                         | Resolution                                                |
| ------------------------------ | --------------------------------------------- | --------------------------------------------------------- |
| `Investigation {investigationId} not found`        | Invalid or non-existent fix ID                | Verify the investigationId from the previous query |
| `testCaseId must be provided`       | Missing required query parameter              | Test ID is required                                        |
| `This investigation was skipped before producing a completed summary.` | Investigation was skipped | The setting may be disabled, revisit prerequisites in [Autofix Flaky Tests](../../autofix-flaky-tests.md) |
| `This investigation failed before producing a completed summary. Please contact Trunk support.` | Investigation error | This feature is still in Beta, please contact support |
| Repository authorization error | Insufficient permissions or invalid repo name | Verify repository name format and your access permissions |
