---
description: Configure Flaky Tests using GitLab CI
---

# GitLab

## Introduction

Trunk Flaky Tests integrates with your CI by adding an `Upload Test Results` step in each of your testing CI jobs via the [Trunk Uploader CLI](../uploader.md).&#x20;

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

### 1. Store a TRUNK\_TOKEN secret in your CI system

In [app.trunk.io](http://app.trunk.io), navigate to:

**`Settings` -> `Manage Organization` -> `Organization API Token`**

Store your API Token in a [GitLab Variable](https://docs.gitlab.com/ee/ci/variables/index.html#for-a-project) for your `TRUNK_TOKEN` by navigating to your GitLab project's **Settings** > **CI/CD** > **Variables**.&#x20;

### 2. Grab your Organization Slug

To upload test results to Trunk, you'll need to pass a Trunk Org Slug to the upload command. To get your organization slug, in [app.trunk.io](http://app.trunk.io), navigate to:

&#x20;**`Settings` -> `Manage` -> `Organization` -> `Organization Slug`**

Your Trunk Organization Slug can just be pasted directly into your CI workflow; it's not a secret. In the example workflow in the next step, replace `TRUNK_ORG_SLUG` with your actual organization slug.

### 3. Modify GitLab pipelines to upload test results

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or protected branches (`main`, `master`, `develop`, etc) .

#### Example GitLab Pipeline

The following is an example of a GitLab pipeline step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the JUnit XML files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```yaml
image: node:latest

stages:         # List of stages for jobs, and their order of execution
  - test
  - flaky-tests

unit_test_job:   # This job runs the tests
  stage: test    
  script: ...

upload_test_results: # This job uploads tests results run in the last stage
  stage: flaky-tests
  script:
    - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
    - ./trunk flakytests upload --junit-paths "**/report.xml" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```

See the [uploader.md](../uploader.md "mention") for all available command line arguments and usage.

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live support.
