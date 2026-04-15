---
description: >-
  Make sure your CI runs whenever Trunk Merge Queue tests a pull request.
---

# Configure CI status checks

This page covers how to make sure your CI checks run on the branches Trunk Merge Queue creates while testing a pull request. What you need to do depends on the testing mode you selected in [Configure branch protection](configure-branch-protection.md):

* **Draft PR mode (default)** — no additional CI configuration is required.
* **Push-Triggered mode** — you need to add a CI workflow that triggers on pushes to `trunk-merge/**`.

### If using Draft PR mode (default) <a href="#if-using-draft-pr-mode-default" id="if-using-draft-pr-mode-default"></a>

Your existing pull request-triggered CI workflows will automatically run when Trunk creates draft pull requests to test changes. **No additional configuration is required.**

See GitHub's documentation for configuring required status checks on your protected branch:

* [Classic branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging)
* [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

**You're done!** Skip to the [Verification](test-your-setup.md) section.

### If using Push-Triggered mode <a href="#if-using-push-triggered-mode" id="if-using-push-triggered-mode"></a>

Set up your CI provider to run status checks whenever Trunk pushes to `trunk-merge/*` branches.

**Example for GitHub Actions:**

```yaml
name: Merge Queue Tests
run-name: Merge Queue Checks for ${{ github.ref_name }}

# Trigger when Trunk Merge Queue tests a pull request
on:
  push:
    branches:
      - trunk-merge/**

jobs:
  unit_tests:
    runs-on: ubuntu-latest
    name: Unit Tests
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run tests
        run: npm test  # Your actual test commands

  integration_tests:
    runs-on: ubuntu-latest
    name: Integration Tests
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run integration tests
        run: npm run test:integration  # Your actual test commands
```

**For other CI providers:** Configure workflows triggered by pushes to branches matching `trunk-merge/**`.

### Choosing which checks gate the queue <a href="#choosing-which-checks-gate-the-queue" id="choosing-which-checks-gate-the-queue"></a>

By default, Merge Queue waits on the same required status checks defined in your GitHub branch protection rules before merging a PR. If you want a different set of checks to gate the queue — for example, because you don't use GitHub branch protection, or because the queue should require different checks than PR review — you can override that in the Trunk UI or in `.trunk/trunk.yaml` (`merge.required_statuses`). Both overrides work in either testing mode.

{% hint style="info" %}
**This controls which checks gate merging while a PR is being tested in the queue. It does not control which PRs are admitted into the queue.**
{% endhint %}

PR admission is governed separately: Trunk waits until GitHub considers the PR mergeable (driven by your [branch protection rules](configure-branch-protection.md#how-branch-protection-affects-the-queue)) before testing begins. If your queue is running in [parallel mode](../optimizations/parallel-queues/README.md), Trunk additionally waits for the PR's [impacted targets](../optimizations/parallel-queues/README.md#what-are-impacted-targets) to be uploaded.

See [Required Status Checks](../administration/advanced-settings.md#required-status-checks) for the full set of gating options.

### Next Steps

→ [**Test your setup**](test-your-setup.md) - Verify everything is configured correctly before using Merge Queue in production.

_Having trouble?_ See our [Troubleshooting guide](../reference/troubleshooting.md) for common installation issues.
