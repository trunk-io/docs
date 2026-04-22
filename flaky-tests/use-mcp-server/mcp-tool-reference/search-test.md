---
description: 'MCP tool reference: search-test'
---

# Search Test

### Overview

The `search-test` tool looks up the ID of a test case given its name.


**Return Type:** Metadata about the test, including its ID.

### Parameters

#### Required Parameters

| Parameter  | Type   | Description                                                     |
| ---------- | ------ | --------------------------------------------------------------- |
| `repoName` | string | Repository name in `owner/repo` format (e.g., `trunk-io/trunk`) |
| `testNameSearch` | string | Search string for the test name. Does not include filepaths |

#### Optional Parameters

| Parameter | Type   | Description                                                            |
| --------- | ------ | ---------------------------------------------------------------------- |
| `orgSlug` | string | The name of your organization in the Trunk app                         |
| `limit`   | number | Return up to 20 search results at a time |

### Getting Parameter Values

If your AI assistant doesn't have direct access to Git information, use these commands:

**Get repository name:**

```bash
git remote -v
```

Look for the repository name in the output (e.g., `trunk-io/trunk` from `git@github.com:trunk-io/trunk.git`)

### Usage Examples

#### Search

```
What's the test case ID for the test "clear all filters button appears in empty state and clears filters"
```

### Error Handling

| Error                          | Cause                                         | Resolution                                                |
| ------------------------------ | --------------------------------------------- | --------------------------------------------------------- |
| `No tests matched {searchString} in repo {repoName}` | No results found | Check your search string and try again |
| Repository authorization error | Insufficient permissions or invalid repo name | Verify repository name format and your access permissions |
