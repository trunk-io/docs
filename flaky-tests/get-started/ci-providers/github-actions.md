---
description: Configure Flaky Tests detection using a GitHub Action
---

# GitHub Actions

## Introduction

Trunk Flaky Tests integrates with your CI by adding an `Upload Test Results` step in each of your GitHub workflows via the [Trunk Analytics Uploader Action](https://github.com/trunk-io/analytics-uploader).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

### 1. Store a TRUNK\_TOKEN secret in your CI system

In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization API Token > View Organization API Token > View**

Store your API Token in a [GitHub secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) named `TRUNK_TOKEN`. Make sure you are getting your _organization token_, not your project/repo token.

### 2. Grab your Organization Slug

To upload test results to Trunk, you'll need to pass a Trunk Organization Slug to the upload command. To get your organization slug, In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization Name > Slug**

Your Trunk Organization Slug can just be pasted directly into your CI workflow; it's not a secret. In the example workflow in the next step, replace `TRUNK_ORG_SLUG` with your actual organization slug.

### 3. Modify GitHub Actions workflow file to upload test results

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example: `main`, `master`, or `develop`.

#### Example GitHub Actions Workflow

The following is an example of a GitHub Actions workflow step to upload test results after your tests using Trunk's [**Analytics Uploader Action**](https://github.com/trunk-io/analytics-uploader).

To find out how to produce the JUnit XML files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```yaml
jobs:
  test:
    name: Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests
        run: ...

      - name: Upload Test Results to Trunk
        if: "!cancelled()" # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@main
        with:
          junit-paths: "**/junit.xml"        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}

```

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live support.
