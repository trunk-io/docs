---
description: Configure CircleCI jobs to upload test results to Trunk Flaky Tests
---

# CircleCI

Trunk Flaky Tests integrates with your CI by adding a step in your CircleCI Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

### Checklist

By the end of this guide, you should achieve the following.

* [ ] Get your Trunk organization slug and token
* [ ] Set your slug and token as a variable in CI
* [ ] Configure your CI to upload to Trunk
* [ ] Validate your uploads in Trunk

After completing these checklist items, you'll be integrated with Trunk.&#x20;

### Trunk Organization Slug and Token

Before setting up uploads to Trunk, you must sign in to [app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests) and obtain your Trunk organization slug and token.

#### Trunk Slug

You can find your organization slug under **Settings > Organization > Manage > Organization Name > Slug**. You'll save this as a variable in CI in a later step.

#### Trunk Token

You can find your token under **Settings > Organization > Manage > Organization API Token > View Organization API Token > View**. Since this is a secret, do not leak it publicly. Ensure you get your _organization token_, not your project/repo token.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

### Add the Trunk Token as a Secret

Store your Trunk slug and API token in your CircleCI project settings under **Environment Variables** as new variables named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
You must upload tests from both PR and [**stable branches**](https://docs.trunk.io/flaky-tests/detection#stable-branches), such as `main`, `master`, or `develop` in CI for Trunk to detect flaky tests. Trunk will not detect flaky tests without uploads from both PR and stable branches.&#x20;

[Learn more about detection](../../detection.md)
{% endhint %}

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
            curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
            ./trunk flakytests upload --junit-paths "**/junit.xml" --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
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
            curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
            ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
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
            curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
            ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token ${TRUNK_TOKEN}
```
{% endtab %}
{% endtabs %}

See the [Uploader CLI Reference](https://docs.trunk.io/flaky-tests/uploader) for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
