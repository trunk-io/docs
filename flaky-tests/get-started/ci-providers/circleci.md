---
description: Configure CircleCI jobs to upload test results to Trunk Flaky Tests
---

# CircleCI

Trunk Flaky Tests integrates with your CI by adding a step in your CircleCI Pipelines to upload tests with the [Trunk Analytics CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store your Trunk slug and API token in your CircleCI project settings under **Environment Variables** as new variables named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection/), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

#### Example CircleCI workflow

The following is an example of a workflow step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

{% tabs %}
{% tab title="XML" %}
```yaml
jobs:
  test-node:
    # Install node dependencies and run tests
    executor: node/default
    steps:
      - run:
          name: Run Tests
          command: ...

      - run:
          name: Upload Test Results to Trunk.io
          command: |
            curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
            ./trunk-analytics-cli upload --junit-paths "**/junit.xml" --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
jobs:
  test-node:
    # Install node dependencies and run tests
    executor: node/default
    steps:
      - run:
          name: Run Tests
          command: ...

      - run:
          name: Upload Test Results to Trunk.io
          command: |
            curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
            ./trunk-analytics-cli upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}

{% tab title="XCode" %}
```yaml
jobs:
  test-node:
    # Install node dependencies and run tests
    executor: node/default
    steps:
      - run:
          name: Run Tests
          command: ...

      - run:
          name: Upload Test Results to Trunk.io
          command: |
            curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
            ./trunk-analytics-cli upload --xcresult-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
jobs:
  test-node:
    # Install node dependencies and run tests
    executor: node/default
    steps:
      - run:
          name: Run Tests and Upload Results to Trunk.io
          command: TRUNK_ORG_URL_SLUG=${TRUNK_ORG_SLUG} TRUNK_API_TOKEN=${TRUNK_TOKEN} bundle exec rspec
```
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/platform-hint.md" %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}
