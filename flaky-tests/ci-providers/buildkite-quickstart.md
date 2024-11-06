---
description: Configure Buildkite jobs to upload test results to Trunk Flaky Tests
---

# Buildkite

### Introduction

Trunk Flaky Tests integrates with your CI by adding an `Upload Test Results` step in each of your testing CI jobs via the [Trunk Uploader CLI](../uploader.md). Just specify file path globs for JUnit XML files, supported by virtually all test frameworks. See the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner.

### Step 1: Store a TRUNK\_TOKEN secret in your CI system

In [app.trunk.io](http://app.trunk.io), navigate to:

**`Settings` -> `Manage Organization` -> `Organization API Token`**

Store your API Token in a CI [secret](https://buildkite.com/docs/pipelines/secrets) named `TRUNK_TOKEN`.

### Step 2: Modify Buildkite test jobs to upload results to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that runs on pull requests, as well as from jobs that run on your main or protected branches (`main`, `master`, `develop`, etc) .

#### Get your Organization Slug

To upload test results to Trunk, you'll need to pass a Trunk Org Slug to the upload command. Replace `TRUNK_ORG_SLUG` in the example workflow below with your  actual Trunk Organization Slug, which you can find in:

&#x20;**`Settings` -> `Manage` -> `Organization` -> `Organization Slug`**

Your Trunk Organization Slug can just be pasted directly into your CI workflow, it's not a secret.

#### Example Buildkite Workflow

The following is an example of a buildkite workflow step to upload test results after your tests run. You must either run `trunk` from the repo root when uploading test results, or supply a `--repo-root` argument.

To find out how to product the JUnit XML files the uploader needs, see instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - trunk flakytests upload --junit-paths "**/junit.xml" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```

See the [uploader.md](../uploader.md "mention") for all available command line arguments and usage.

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live help and support.
