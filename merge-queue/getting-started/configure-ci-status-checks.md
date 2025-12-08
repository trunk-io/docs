# Configure CI status checks

### If using Draft PR mode (Default) <a href="#if-using-draft-pr-mode-default" id="if-using-draft-pr-mode-default"></a>

Your existing pull request-triggered CI workflows will automatically run when Trunk creates draft pull requests to test changes. **No additional configuration is required.**

Trunk will wait for the same required status checks configured in your branch protection rules (either via Classic rules or Rulesets) before merging.

See GitHub's documentation for configuring required status checks:

* [Classic branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging)
* [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

**You're done!** Skip to the Verification section below.

### If using Push-Triggered mode <a href="#if-using-push-triggered-mode" id="if-using-push-triggered-mode"></a>

You need to complete two additional steps:

**Step 1: Configure Push-Triggered CI Workflows**

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

**Step 2: Define Required Status Checks in .trunk/trunk.yaml**

Create or edit your `trunk.yaml` file in a directory named `.trunk` at the root of your repository (so, `.trunk/trunk.yaml`) to specify which status checks Trunk should wait for before merging:

```yaml
version: 0.1
merge:
  required_statuses:
    - Unit Tests
    - Integration Tests
```

**Important:** The status check names in `.trunk/trunk.yaml` must exactly match the job names from your CI workflows.



### Next Steps

→ [**Test your setup**](test-your-setup.md) - Verify everything is configured correctly before using Merge Queue in production.

_Having trouble?_ See our [Troubleshooting guide](../reference/troubleshooting.md) for common installation issues.
