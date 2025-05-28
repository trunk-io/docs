---
description: Configure Flaky Tests using Drone CI
---

# Drone CI

Trunk Flaky Tests integrates with your CI by adding a step in your Drone CI Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

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

### Add the Trunk Token as a Secret

Store your Trunk slug and API token in your Drone CI project settings as new variables named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Add Uploader to Testing Pipelines

The following is an example of a workflow step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

{% tabs %}
{% tab title="XML" %}
```yaml
kind: pipeline
type: docker
name: test

steps:
  - name: Run Tests
    commands: ...

  - name: Upload Test Results to Trunk.io
    environment:
      TRUNK_ORG_SLUG:
        from_secret: TRUNK_ORG_SLUG
      TRUNK_API_TOKEN:
        from_secret: TRUNK_API_TOKEN
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --junit-paths <XML_GLOB_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
kind: pipeline
type: docker
name: test

steps:
  - name: Run Tests
    commands: ...

  - name: Upload Test Results to Trunk.io
    environment:
      TRUNK_ORG_SLUG:
        from_secret: TRUNK_ORG_SLUG
      TRUNK_API_TOKEN:
        from_secret: TRUNK_API_TOKEN
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="XCode" %}
```yaml
kind: pipeline
type: docker
name: test

steps:
  - name: Run Tests
    commands: ...

  - name: Upload Test Results to Trunk.io
    environment:
      TRUNK_ORG_SLUG:
        from_secret: TRUNK_ORG_SLUG
      TRUNK_API_TOKEN:
        from_secret: TRUNK_API_TOKEN
    commands:
      - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      - ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
kind: pipeline
type: docker
name: test

steps:
  - name: Run Tests and Upload Results to Trunk.io
    environment:
      TRUNK_ORG_SLUG:
        from_secret: TRUNK_ORG_SLUG
      TRUNK_TOKEN:
        from_secret: TRUNK_TOKEN
    commands:
      - TRUNK_ORG_URL_SLUG=$TRUNK_ORG_SLUG TRUNK_API_TOKEN=$TRUNK_TOKEN bundle exec rspec
```
{% endtab %}
{% endtabs %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
