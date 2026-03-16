---
description: >-
  Learn how Trunk identifies repositories and how to track tests across forks
  and multiple repositories without mixing results.
---

# Multiple Repositories and Forks

Trunk Flaky Tests identifies repositories by their **git remote URL**, not by the API token. You can safely use the same organization API token across multiple repositories, including forks, without mixing test results.

### How Repository Identification Works

When the Trunk Analytics CLI uploads test results, it reads the git remote URL from your CI environment and parses it into three components:

* **Host**: `github.com`, `gitlab.com`, or your self-hosted instance
* **Owner**: The organization or user (e.g., `your-company`)
* **Name**: The repository name (e.g., `your-repo`)

These three components together uniquely identify the repository in Trunk. The API token determines which _organization_ the upload belongs to, but does not affect which _repository_ the results are associated with.

### Using Trunk with Forks

If you run tests from a fork, Trunk automatically keeps test results separate based on the fork's remote URL.

For example, if your company forks `metabase/metabase` to `your-company/metabase-fork`:

| Repository  | Remote URL                                | Trunk Repo ID              |
| ----------- | ----------------------------------------- | -------------------------- |
| Original    | `github.com/metabase/metabase`            | `metabase/metabase`        |
| Your fork   | `github.com/your-company/metabase-fork`   | `your-company/metabase-fork` |

You can use the same organization API token for both repositories. Trunk creates separate repo entries and keeps all test data isolated.

{% hint style="info" %}
No special configuration is needed for forks. As long as your fork has a different remote URL (which it does by default), Trunk keeps the data separate automatically.
{% endhint %}

### Verifying Your Remote URL

Before setting up uploads, verify your CI job is using the correct remote URL:

```bash
git remote -v
# origin  git@github.com:your-company/metabase-fork.git (fetch)
# origin  git@github.com:your-company/metabase-fork.git (push)
```

{% hint style="warning" %}
Some CI providers set environment variables like `GITHUB_REPOSITORY` that may differ from your git remote. The CLI reads the git remote URL by default. If your CI environment modifies the remote, use the `--repo-url` flag to override repository detection.
{% endhint %}

### Overriding Repository Detection

In some CI environments, you may need to manually specify the repository URL:

* The git remote is not available or is incorrect
* You are uploading results from a build artifact without a git checkout
* A shallow clone has modified remotes

Override the repository URL with the `--repo-url` flag:

```bash
./trunk-analytics-cli upload \
  --junit-paths "test_output.xml" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN \
  --repo-url "https://github.com/your-company/your-repo.git"
```

You can also set the repository URL via the `TRUNK_REPO_URL` environment variable:

```bash
export TRUNK_REPO_URL="https://github.com/your-company/your-repo.git"
./trunk-analytics-cli upload \
  --junit-paths "test_output.xml" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN
```

See the [Trunk Analytics CLI](../../uploader.md) reference for the full list of override flags.

### Monorepo with Multiple Test Suites

To track different test suites within the same repository separately, use the `--variant` flag:

```bash
# Frontend tests
./trunk-analytics-cli upload \
  --junit-paths "frontend/test_output.xml" \
  --variant "frontend" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN

# Backend tests
./trunk-analytics-cli upload \
  --junit-paths "backend/test_output.xml" \
  --variant "backend" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN
```

### Troubleshooting

#### Test results appearing in wrong repository

1. **Check your git remote**: Run `git remote -v` in your CI job to verify the URL.
2. **Check CI environment variables**: Some CI providers override git configuration.
3. **Use explicit override**: Set `--repo-url` to force the correct repository.

#### Duplicate repositories in dashboard

This can happen if the same repository is uploaded with different URL formats (e.g., HTTPS vs SSH). To resolve:

1. Standardize the remote URL format across all CI jobs.
2. Use `--repo-url` to set a consistent URL.
3. Contact [support@trunk.io](mailto:support@trunk.io) to merge duplicate repository entries.

### FAQ

| Question                                       | Answer                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| Can I use the same API token for multiple repos? | Yes. The token is org-scoped, not repo-scoped.                        |
| Will fork test results mix with upstream?       | No. Repos are identified by remote URL, not by token.                 |
| Do I need separate tokens for forks?            | No. The same token works for all repos in your organization.          |
| Can I override the detected repository?         | Yes. Use `--repo-url` or the `TRUNK_REPO_URL` environment variable.  |
