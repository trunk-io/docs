---
description: 'MCP tool reference: fix-flaky-test'
---

# Get root cause analysis

### Overview

The `fix-flaky-test` tool retrieves insights and historical failure analysis about a flaky test. This tool allows AI assistants to access investigation results and apply fixes directly in your development environment.

\
**Return Type:** Structured analysis data with fix recommendations. Structure: issue, root cause, proposed fix

### Parameters

#### Required Parameters

| Parameter  | Type   | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `repoName` | string | Repository name in `owner/repo` format (e.g., `trunk-io/trunk`) |

#### Optional Parameters

| Parameter | Type   | Description                                                            |
| --------- | ------ | ---------------------------------------------------------------------- |
| `fixId`   | string | Specific fix identifier from CI Autopilot comment (e.g., `FIX-abc123`) |
| `orgSlug` | string | The name of your organization in the Trunk app                         |

### Getting Parameter Values

If your AI assistant doesn't have direct access to Git information, use these commands:

**Get repository name:**

```bash
git remote -v
```

Look for the repository name in the output (e.g., `trunk-io/trunk` from `git@github.com:trunk-io/trunk.git`)

### Usage Examples

#### With Fix ID

```
Fix the flaky test with ID <fix-id>
```

### Sample Response

```
Fix Flaky Tests Insight for <fix-id>

Issue: The CI failure occurred during the "Run Mysql Migrations" step due to a ValidationException from AWS Secrets Manager.

Root Cause: The SECRET_NAME being used to retrieve the secret value is malformed. The grep -oP "adminsecret.*" command is extracting the secret name along with surrounding JSON formatting (like quotes), which creates an invalid secret ID when passed to aws secretsmanager get-secret-value.

Proposed Fix: Replace the problematic grep command with a proper JSON parser:

-        SECRET_NAME=$(aws secretsmanager list-secrets --filters Key=name,Values=adminsecret | grep Name | grep -oP "adminsecret.*")
+        SECRET_NAME=$(aws secretsmanager list-secrets --filters Key=name,Values=adminsecret | jq -r '.SecretList[0].Name')

This fix is located in .github/actions/setup-k8s-and-migrate/action.yml at line 11.
```

### Error Handling

| Error                          | Cause                                         | Resolution                                                |
| ------------------------------ | --------------------------------------------- | --------------------------------------------------------- |
| `Fix {fixId} not found`        | Invalid or non-existent fix ID                | Verify the fix ID from the original CI Autopilot comment  |
| `fixId must be provided`       | Missing required query parameter              | Fix ID is required                                        |
| Repository authorization error | Insufficient permissions or invalid repo name | Verify repository name format and your access permissions |
