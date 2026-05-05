---
description: 'MCP tool reference: investigate-ci-failure'
---

# Investigate CI Failure

### Overview

The `investigate-ci-failure` tool investigates a failing CI run by fetching structured test failure data from Trunk. Given a GitHub Actions workflow URL, this tool looks up test result bundles, parses them to extract test names and error messages, filters out quarantined (known-flaky) tests, and returns structured failure details the agent can act on. For more information, see [Autofix CI Failures](../../autofix-ci-failures.md).

**Return Type:** Structured failure details with test names, error messages, stdout, and stderr. If the CI job failed before tests ran (build or compilation failure), the tool suggests pulling raw logs from the workflow URL as a fallback.

### Prerequisites

- Your repository must be set up to [upload test results to Trunk](../../get-started/README.md)
- For best results, [enable quarantining](../../quarantining.md) so known-flaky tests are filtered out automatically

### Parameters

#### Required Parameters

| Parameter  | Type   | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `workflowUrl` | string | The GitHub Actions workflow URL, e.g. `https://github.com/{owner}/{repo}/actions/runs/{runId}` |

#### Optional Parameters

| Parameter | Type   | Description                                                            |
| --------- | ------ | ---------------------------------------------------------------------- |
| `orgSlug` | string | The Trunk organization slug (used to disambiguate if you belong to multiple orgs) |

### Getting Parameter Values

**Get workflow URL:**

Navigate to your GitHub Actions run and copy the full URL from your browser's address bar. It follows the pattern:

```
https://github.com/{owner}/{repo}/actions/runs/{runId}
```

### Usage Examples

#### Investigate a workflow failure

```
Investigate the CI failure at https://github.com/trunk-io/trunk/actions/runs/12345678
```

### What the tool does

- Looks up test result uploads Trunk has received for that run
- Parses the test runs to extract test names, error messages, stdout and stderr
- Filters out quarantined (known-flaky) tests so you only see real failures
- Returns structured failure details you can act on

**When tests didn't run:** If the CI job failed before any tests ran (e.g., a build or compilation failure), the tool will tell you so and suggest pulling raw CI logs directly from the workflow URL as a fallback.

### Error Handling

| Error                          | Cause                                         | Resolution                                                |
| ------------------------------ | --------------------------------------------- | --------------------------------------------------------- |
| `Invalid workflow URL`         | Malformed or incorrect workflow URL           | Verify the URL follows the pattern `https://github.com/{owner}/{repo}/actions/runs/{runId}` |
| `No test results were uploaded for this CI run`           | No test run uploads were uploaded from the provided workflow | Check that the workflow run URL is correct and that it is uploading test results. Compilation and build failures will not upload test results |
| `No test uploads found for this repository` | Repo hasn't configured Trunk test result uploads | Follow setup instructions to [upload test results](../../get-started/README.md) |
