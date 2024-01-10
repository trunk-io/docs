# GitHub Actions Quickstart

### Configuring the Analytics Uploader Action

The [**Analytics Uploader Action** ](https://github.com/trunk-io/analytics-uploader)uploads test reports to Trunk Analytics from your GitHub workflows. Here are the steps for setting it up:

1. Create a GitHub workflow that runs the tests you want to monitor and produces a test report in [**JUnit XML**](https://www.ibm.com/docs/en/developer-for-zos/14.1?topic=formats-junit-xml-format) format. Be careful that your test invocation doesn't use cached test results, and doesn't automatically retry failing tests.
2. Modify your GitHub workflow to add the [Trunk Analytics Uploader Action](https://github.com/trunk-io/analytics-uploader) as the step after your tests run. Point the uploader to the locations on disk where your test runner outputs Junit XML files:

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

3. To find your organization slug, you can open [app.trunk.io](http://app.trunk.io). Once you are logged in, you should be automatically redirected to a URL like [https://app.trunk.io/**my-org-slug**/repo-owner/repo-name/ci-analytics](https://app.trunk.io/my-org-slug/repo-owner/repo-name/ci-analytics).
4. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View". Provide this token as a [GitHub secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

***

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

&#x20;\
The uploader action uploads the following data from your workflow:

1. All files matching provided glob patterns (absolute or relative to the repository root).
2. Repository info: url, head branch, head commit sha, head commmit time).
3. Github Action environment variables:
   * GITHUB\_BASE\_REF
   * GITHUB\_ACTIONS
   * GITHUB\_ACTOR
   * GITHUB\_HEAD\_REF
   * GITHUB\_REPOSITORY
   * GITHUB\_REF
   * GITHUB\_RUN\_ID
   * GITHUB\_SERVER\_URL
   * GITHUB\_RUN\_NUMBER
   * GITHUB\_WORKFLOW
   * GITHUB\_EVENT\_NAME
   * GITHUB\_RUN\_ATTEMPT
   * GITHUB\_SHA
