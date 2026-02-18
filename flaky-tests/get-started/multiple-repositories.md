---
description: Learn how Trunk identifies repositories and how to use Trunk Flaky Tests with forks or multiple related repositories.
---

# Multiple Repositories and Forks

Trunk Flaky Tests identifies repositories by their **git remote URL**, not by the API token. You can safely use the same organization API token across multiple repositories -- including forks -- without mixing test results.

## How Repository Identification Works

When the Trunk Analytics CLI uploads test results, it reads the git remote URL from your local git configuration:

```bash
git config remote.origin.url
# Example: git@github.com:your-company/your-repo.git
```

The CLI parses the URL into three components that uniquely identify the repository:

| Component | Example             |
| --------- | ------------------- |
| **Host**  | `github.com`        |
| **Owner** | `your-company`      |
| **Name**  | `your-repo`         |

The API token determines which **organization** the upload belongs to. The **repository** is determined entirely by the git remote URL.

## Using Trunk with Forks

If you run tests from a fork, Trunk automatically keeps results separate based on the fork's remote URL. No special configuration is needed.

### Example: Forking an Open Source Project

Suppose your company forks `metabase/metabase` to `your-company/metabase-fork`:

| Repository  | Remote URL                                   | Trunk Repo ID                  |
| ----------- | -------------------------------------------- | ------------------------------ |
| Original    | `github.com/metabase/metabase`               | `metabase/metabase`            |
| Your fork   | `github.com/your-company/metabase-fork`      | `your-company/metabase-fork`   |

Both repositories can use the **same organization API token**. Trunk creates separate repo entries and keeps all test data isolated.

### Verify Your Remote URL

Before setting up uploads, verify your CI job uses the correct remote:

```bash
git remote -v
# origin  git@github.com:your-company/metabase-fork.git (fetch)
# origin  git@github.com:your-company/metabase-fork.git (push)
```

{% hint style="info" %}
Some CI providers set environment variables like `GITHUB_REPOSITORY` that may differ from your git remote. The CLI prioritizes the git remote URL by default.
{% endhint %}

## Overriding Repository Detection

In some cases you may need to manually specify the repository URL:

* CI environments where the git remote is not available or is incorrect
* Uploading results from a build artifact without a git checkout
* Shallow clones with modified remotes

### Using the `--repo-url` Flag

```bash
./trunk-analytics-cli upload \
  --junit-paths "test_output.xml" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN \
  --repo-url "https://github.com/your-company/your-repo.git"
```

You can also set this via environment variable:

```bash
export TRUNK_REPO_URL="https://github.com/your-company/your-repo.git"
```

### Uploading Without a Git Checkout

For CI environments where you download build artifacts instead of checking out the repository, use the `--use-uncloned-repo` flag along with the required metadata:

```bash
./trunk-analytics-cli upload \
  --junit-paths "test_output.xml" \
  --org-url-slug <TRUNK_ORG_SLUG> \
  --token $TRUNK_API_TOKEN \
  --use-uncloned-repo \
  --repo-url "https://github.com/your-company/your-repo.git" \
  --repo-head-sha "abc123def456" \
  --repo-head-branch "main" \
  --repo-head-author-name "CI Bot"
```

{% hint style="info" %}
For the full list of CLI flags and environment variables, see the [Trunk Analytics CLI](../uploader.md#full-command-reference) reference.
{% endhint %}

## Common Scenarios

### Private Fork of a Public Repository

**Goal:** Track flaky tests in your private fork separately from the upstream project.

**Solution:** No special configuration needed. Your fork has a different remote URL by default, so Trunk automatically keeps the data separate. Use your existing organization API token.

### Multiple Forks in the Same Organization

**Goal:** Track tests from multiple forks (for example, `your-company/fork-a` and `your-company/fork-b`) using the same Trunk organization.

**Solution:** Use the same API token for all forks. Each fork appears as a separate repository in Trunk based on its remote URL.

### Monorepo with Multiple Test Suites

**Goal:** Track different test suites within the same repository separately.

**Solution:** Use the `--variant` flag to group test results by suite:

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

## Troubleshooting

### Test Results Appearing in the Wrong Repository

1. **Check your git remote:** Run `git remote -v` in your CI job to verify the URL matches the expected repository.
2. **Check CI environment variables:** Some CI providers override git configuration. See your [CI provider's guide](ci-providers/) for details.
3. **Use an explicit override:** Set `--repo-url` to force the correct repository.

### Duplicate Repositories in the Dashboard

This can happen if the same repository is uploaded with different URL formats (for example, HTTPS vs SSH). Trunk normalizes most formats, but if you see duplicates:

1. Standardize the remote URL format across all CI jobs.
2. Use `--repo-url` to set a consistent URL explicitly.
3. Contact [support@trunk.io](mailto:support@trunk.io) to merge duplicate repository entries.
