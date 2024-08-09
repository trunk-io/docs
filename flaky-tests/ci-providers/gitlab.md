---
description: Configure Flaky Tests using GitLab CI
---

# GitLab

## Getting Started

You can use the analytics test uploader within your [GitLab Pipelines](https://docs.gitlab.com/ee/ci/pipelines/) to upload your test results.

{% hint style="info" %}
The Trunk Flaky Tests Uploader currently only supports Linux x64 and macOS for Intel and Arm. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

### Create workflow

Create a GitLab pipeline that runs the tests you want to monitor. In order for us to use the results, these tests **must** produces a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format.

## Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to **Settings** -> **Manage** -> **Organization**.  Copy your organization slug. You can find your Trunk token by navigating to **Settings** → **Manage Organization** → **Organization API Token** and clicking "View."  Copy this token.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Create GitLab CI/CD Pipeline Variables

[Create a GitLab Variable](https://docs.gitlab.com/ee/ci/variables/index.html#for-a-project) for your `TRUNK_API_TOKEN` by navigating to your GitLab project's **Settings** > **CI/CD** > **Variables**. You will use this variable in the next steps to upload test results to Flaky Tests.

### Add Uploader to Testing Workflow

{% include "./uploader-instructions.md" %}

```yaml
image: node:latest

stages:          # List of stages for jobs, and their order of execution
  - test
  - flaky-tests

unit-test-job:   # This job runs the tests
  stage: test    
  script:
    - npm install 
    - npm test --config=javascript/tests/jest/jest.config.json javascript/tests/jest/**/*.js

upload_test_results: # This job uploads tests results run in the last stage
  stage: flaky-tests
  script:
    - curl -fsSL --retry 3 "UPLOADER_LINK" -o ./trunk-analytics-uploader
    - chmod +x ./trunk-analytics-uploader
    - ./trunk-analytics-uploader upload --junit-paths "tests/jest/jest_junit_test.xml" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_API_TOKEN
      
```

The `trunk-analytics-uploader` tool has several important arguments;

* `--junit-paths`is a comma separated list of paths.
* `--org-url-slug` is an identifier for the Trunk account you are using. This is the Organization Slug you copied from your Trunk settings above set as a GitLab Variable.
* `--token` is the Trunk API token you added as a GitLab Variable above.

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
