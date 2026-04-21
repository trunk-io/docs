---
description: Configure Buildkite jobs to upload test results to Trunk Flaky Tests
---

# Buildkite

Trunk Flaky Tests integrates with your CI by adding a step in your Buildkite Pipelines to upload tests with the [Trunk Analytics CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step as a new [Buildkite CI secret](https://buildkite.com/docs/pipelines/security/secrets/managing) named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection/), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

#### Example Buildkite Pipeline

The following is an example of a Buildkite step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/) docs.

{% tabs %}
{% tab title="XML" %}
```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results to Trunk.io
    commands:
      - curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
      - ./trunk-analytics-cli upload --junit-paths "<XML_GLOB_PATH>" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results to Trunk.io
    commands:
      - curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
      - ./trunk-analytics-cli upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endtab %}

{% tab title="XCode" %}
```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results to Trunk.io
    commands:
      - curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli
      - ./trunk-analytics-cli upload --xcresult-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
steps:
  - label: Run Tests and Upload Results to Trunk.io
    command: TRUNK_ORG_URL_SLUG=$TRUNK_ORG_SLUG TRUNK_API_TOKEN=$TRUNK_TOKEN bundle exec rspec
    key: tests
```
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/platform-hint.md" %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}
