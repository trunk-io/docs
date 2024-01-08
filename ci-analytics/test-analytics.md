---
description: >-
  NOTE: At the moment we only support test analytics for test runners which can
  produce reports in Junit XML format.
---

# Test Analytics

Test Analytics is available by invites only. Please [**contact**](https://trunk.io/about) us if you would like to try the product early.

### Configuring the Analytics Uploader Action

The [**Analytics Uploader Action** ](https://github.com/trunk-io/analytics-uploader)uploads test reports to Trunk Analytics from your Github workflows. Here are the steps for setting it up:

1. Make sure you have a GitHub workflow producing test reports in [**Junit XML**](https://www.ibm.com/docs/en/developer-for-zos/14.1?topic=formats-junit-xml-format) format.
2. Modify your Github workflow to add the [Trunk Analytics Uploader Action](https://github.com/trunk-io/analytics-uploader) as a step after your tests complete. Point the uploader to the locations on disk where your test runner outputs Junit XML files:

```yaml
      - name: Upload results
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
name: Upload Test Results to Trunk
on: 
  workflow_dispatch:

jobs:
  upload-test-results:
    runs-on: ubuntu-latest
    name: Run tests and upload results
    timeout-minutes: 60
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run tests
        # Execute your tests and write XML report to some location. 
        run: mkdir -p target/path && touch target/path/junit_report.xml

      - name: Upload results
        uses: trunk-io/analytics-uploader@main
        with:
          junit-paths: target/path/**/*_test.xml
          org-slug: my-trunk-org
          token: ${{ secrets.TRUNK_API_TOKEN }}
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
