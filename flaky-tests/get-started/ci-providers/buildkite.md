---
description: Configure Buildkite jobs to upload test results to Trunk Flaky Tests
---

# Buildkite

Trunk Flaky Tests integrates with your CI by adding a step in your Buildkite Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your as a new [Buildkite CI secret](https://buildkite.com/docs/pipelines/security/secrets/managing) named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/you-must-upload-tests-from-....md" %}

#### Example Buildkite Pipeline

The following is an example of a Buildkite step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.&#x20;

{% tabs %}
{% tab title="XML" %}
```yaml
steps:
  - label: Run Tests
    command: ...
    key: tests
    
  - label: Upload Test Results to Trunk.io
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
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
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
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
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
    key: upload
    depends_on:
      - tests
```
{% endtab %}
{% endtabs %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.
