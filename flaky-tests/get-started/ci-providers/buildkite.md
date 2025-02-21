---
description: Configure Buildkite jobs to upload test results to Trunk Flaky Tests
---

# Buildkite

## Introduction

Trunk Flaky Tests integrates with your CI by adding an `Upload Test Results` step in each of your testing CI jobs via the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

### 1. Store a TRUNK\_TOKEN secret in your CI system

In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization API Token > View Organization API Token > View**

Store your API Token in a [Buildkite CI secret](https://buildkite.com/docs/pipelines/security/secrets/managing) named `TRUNK_TOKEN`. Make sure you are getting your _organization token_, not your project/repo token.

### 2. Grab your Organization Slug

To upload test results to Trunk, you'll need to pass a Trunk Organization Slug to the upload command. To get your organization slug, In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization Name > Slug**

Your Trunk Organization Slug can just be pasted directly into your CI workflow; it's not a secret. In the example workflow in the next step, replace `TRUNK_ORG_SLUG` with your actual organization slug.

### 3. Modify Buildkite jobs to upload test results

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example,`main`, `master`, or `develop`.

#### Example Buildkite Pipeline

The following is an example of a Buildkite step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the JUnit XML files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results to Trunk.io
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --junit-paths "**/junit.xml" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live support.
