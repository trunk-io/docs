---
description: Configure Flaky Tests using Semaphore CI
---

# Semaphore CI

Trunk Flaky Tests integrates with your CI by adding a step in your Semaphore CI Pipeline to upload tests with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your Semaphore CI Pipelines as new secrets named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/you-must-upload-tests-from-....md" %}

#### Example Semaphore CI Workflow

The following is an example of a Semaphore CI workflow step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

{% tabs %}
{% tab title="XML" %}
```yaml
version: v1.0
name: Semaphore JavaScript Example Pipeline
blocks:
  - name: Tests
    task:
      secrets:
        - name: TRUNK_TOKEN
      env_vars:
        - name: NODE_ENV
          value: test
        - name: CI
          value: "true"
      prologue:
        commands:
          - checkout
          - nvm use
          - node --version
          - npm --version
      jobs:
        - name: Run Tests
          commands: ...
      epilogue:
        always:
          commands:
            # Upload results to trunk.io
            - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
            - ./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
version: v1.0
name: Semaphore JavaScript Example Pipeline
blocks:
  - name: Tests
    task:
      secrets:
        - name: TRUNK_TOKEN
      env_vars:
        - name: NODE_ENV
          value: test
        - name: CI
          value: "true"
      prologue:
        commands:
          - checkout
          - nvm use
          - node --version
          - npm --version
      jobs:
        - name: Run Tests
          commands: ...
      epilogue:
        always:
          commands:
            # Upload results to trunk.io
            - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
            - ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}

{% tab title="XCode" %}
```yaml
version: v1.0
name: Semaphore JavaScript Example Pipeline
blocks:
  - name: Tests
    task:
      secrets:
        - name: TRUNK_TOKEN
      env_vars:
        - name: NODE_ENV
          value: test
        - name: CI
          value: "true"
      prologue:
        commands:
          - checkout
          - nvm use
          - node --version
          - npm --version
      jobs:
        - name: Run Tests
          commands: ...
      epilogue:
        always:
          commands:
            # Upload results to trunk.io
            - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
            - ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}
{% endtabs %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.
