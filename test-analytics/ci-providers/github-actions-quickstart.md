---
description: Configure Test Analytics detection using a GitHub Action
---

# GitHub Actions

### Configuring the Analytics Uploader Action

The [**Analytics Uploader Action** ](https://github.com/trunk-io/analytics-uploader)uploads test reports to Trunk Test Analytics from your GitHub workflows. Here are the steps for setting it up:

* Create a GitHub workflow that runs the tests you want to monitor and produces a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format. Be careful that your test invocation doesn't use cached test results, and doesn't automatically retry failing tests.
* Modify your GitHub workflow to add the [Trunk Analytics Uploader Action](https://github.com/trunk-io/analytics-uploader) as the step after your tests run. Point the uploader to the locations on disk where your test runner outputs Junit XML files:

```yaml
      - name: Upload results
        # Run this step even if the test step ahead fails
        if: "!cancelled()"
        uses: trunk-io/analytics-uploader@main
        with:
          # Path to your test results.
          junit-paths: target/path/**/*_test.xml
          # Provide your Trunk organization slug.
          org-slug: my-trunk-org
          # Provide your Trunk API token as a GitHub secret.
          token: ${{ secrets.TRUNK_API_TOKEN }}
        continue-on-error: true

```

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io).  Once logged in navigate to **Settings** -> **Manage** -> **Organization**.  Copy your organization slug. You can find your Trunk token by navigating to **Settings** → **Manage Organization** → **Organization API Token** and clicking "View." Provide this token as a [GitHub secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).&#x20;

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Sample GitHub Actions workflow file:

```yaml
name: Upload Test Results
on:
  workflow_dispatch: {}
  schedule:
    # run every hour on the hour
    - cron: 0 * * * *

permissions: read-all

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup node
        uses: actions/setup-node@v4

      - name: Install Dependencies
        run: npm ci

      - name: Run Jest Tests
        run: npm test

      - name: Upload Jest Test Results
        uses: trunk-io/analytics-uploader@main
        # Upload the results even if the tests fail
        if: "!cancelled()"
        with:
          junit-paths: junit.xml
          org-slug: matt
          token: ${{ secrets.TRUNK_API_TOKEN }}
        # don't fail this job if the upload fails
        continue-on-error: true

```

\
If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
