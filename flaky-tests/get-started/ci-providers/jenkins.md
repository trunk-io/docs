---
description: Configure Flaky Tests using Jenkins
---

# Jenkins

## Introduction

Trunk Flaky Tests integrates with your CI by adding an `Upload Test Results` step in each of your testing Jenkins pipelines via the [Trunk Uploader CLI](../../uploader.md).&#x20;

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

### 1. Store a TRUNK\_TOKEN credential in your CI system

In [app.trunk.io](http://app.trunk.io), navigate to:

**`Settings` -> `Manage Organization` -> `Organization API Token`**

From your Jenkins dashboard, store your API Token in a credential named `TRUNK_TOKEN`.&#x20;

### 2. Grab your Organization Slug

To upload test results to Trunk, you'll need to pass a Trunk Org Slug to the upload command. To get your organization slug, in [app.trunk.io](http://app.trunk.io), navigate to:

&#x20;**`Settings` -> `Manage` -> `Organization` -> `Organization Slug`**

Your Trunk Organization Slug can just be pasted directly into your CI workflow; it's not a secret. In the example workflow in the next step, replace `TRUNK_ORG_SLUG` with your actual organization slug.

### 3. Modify Jenkins pipeline to upload test results

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or protected branches (`main`, `master`, `develop`, etc) .

#### Example Jenkins Pipeline

The following is an example of a Jenkins pipeline step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the JUnit XML files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```groovy
pipeline {
  environment {
    TRUNK_TOKEN = credentials('TRUNK_TOKEN')
  }
  stages {
    stage('Run Tests'){
      ...
    }
    stage('Upload Test Results'){
      sh 'curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk'
      sh './trunk flakytests upload --junit-paths "**/report.xml" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN'
    }
  }
}
```

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live support.