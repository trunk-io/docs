---
description: 'MCP tool reference: get-root-cause-analysis'
---

# Get root cause analysis

### Overview

The `get-root-cause-analysis` tool retrieves detailed root cause analyses and fix recommendations for CI failures from CI Autopilot. This tool allows AI assistants to access investigation results and apply fixes directly in your development environment.

\
**Return Type:** Structured analysis data with fix recommendations. Structure: issue, root cause, proposed fix



### Parameters

#### Required Parameters

| Parameter  | Type   | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `repoName` | string | Repository name in `owner/repo` format (e.g., `trunk-io/trunk`) |

#### Optional Parameters

| Parameter            | Type   | Description                                                            |
| -------------------- | ------ | ---------------------------------------------------------------------- |
| `fixId`              | string | Specific fix identifier from CI Autopilot comment (e.g., `FIX-abc123`) |
| `prReviewCommentUrl` | string | Direct URL to a specific PR comment containing analysis                |
| `branch`             | string | The Git branch name where the CI failure occurred                      |

### Getting Parameter Values

If your AI assistant doesn't have direct access to Git information, use these commands:

**Get current branch:**

```bash
git rev-parse --abbrev-ref HEAD
```

**Get repository name:**

```bash
git remote -v
```

Look for the repository name in the output (e.g., `trunk-io/trunk` from `git@github.com:trunk-io/trunk.git`)



### Usage Examples

#### With Fix ID

```
Retrieve the root cause analysis for fix <fix-id>
```



**With PR Comment URL**

```
Retrieve the root cause analysis for the following comment: https://github.com/myorg/myapp/pull/42#issuecomment-123456
```



### Sample Response

```
Root Cause Analysis for <fix-id>

Issue: The CI failure occurred during the "Run Mysql Migrations" step due to a ValidationException from AWS Secrets Manager.

Root Cause: The SECRET_NAME being used to retrieve the secret value is malformed. The grep -oP "adminsecret.*" command is extracting the secret name along with surrounding JSON formatting (like quotes), which creates an invalid secret ID when passed to aws secretsmanager get-secret-value.

Proposed Fix: Replace the problematic grep command with a proper JSON parser:

-        SECRET_NAME=$(aws secretsmanager list-secrets --filters Key=name,Values=adminsecret | grep Name | grep -oP "adminsecret.*")
+        SECRET_NAME=$(aws secretsmanager list-secrets --filters Key=name,Values=adminsecret | jq -r '.SecretList[0].Name')

This fix is located in .github/actions/setup-k8s-and-migrate/action.yml at line 11.
```



### Error Handling

| Error                                                          | Cause                                             | Resolution                                                             |
| -------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- |
| `Fix {fixId} not found`                                        | Invalid or non-existent fix ID                    | Verify the fix ID from the original CI Autopilot comment               |
| `Investigation comment {url} not found`                        | Invalid PR comment URL or no analysis at that URL | Check the URL and ensure it points to a CI Autopilot comment           |
| `No failure root causes found for branch {branch}`             | No analyses exist for the specified branch        | Ensure CI has run and failed on this branch, or try a different branch |
| `Either fixId, prReviewCommentUrl, or branch must be provided` | Missing required query parameter                  | Provide at least one of the three query methods                        |
| Repository authorization error                                 | Insufficient permissions or invalid repo name     | Verify repository name format and your access permissions              |
| `No root cause analysis comments found`                        | Query found records but no comment content        | CI Autopilot hasn't completed the root cause analysis yet              |
