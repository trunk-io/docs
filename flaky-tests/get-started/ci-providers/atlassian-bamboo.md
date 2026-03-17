---
description: Configure Atlassian Bamboo to upload test results to Trunk Flaky Tests
---

# Atlassian Bamboo

Trunk Flaky Tests integrates with your CI by adding a step in your Bamboo Plans to upload tests with the [Trunk Uploader CLI](../../uploader.md).

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

Store the Trunk slug and API token obtained in the previous step as [Bamboo plan variables](https://confluence.atlassian.com/bamboo/bamboo-variables-289277087.html). Name them `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively, and mark `TRUNK_TOKEN` as a **Secret** variable in the Bamboo UI to prevent it from appearing in build logs.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your Bamboo jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Example Bamboo Plan Spec

The following is an example of a [Bamboo Plan Spec](https://confluence.atlassian.com/bamboo/bamboo-specs-894743906.html) that uploads test results after your tests run. The upload step is placed under `final-tasks` so it runs even when tests fail. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

{% tabs %}
{% tab title="XML" %}
```yaml
version: 2
plan:
  project-key: <YOUR_PROJECT_KEY>
  key: <YOUR_PLAN_KEY>
  name: Run Tests and Upload to Trunk.io

Run Tests and Upload to Trunk:
  key: <YOUR_JOB_KEY>
  tasks:
    - checkout:
        description: Checkout Source Code

    - script:
        name: Run Tests
        body: |
          # Your test command here

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --junit-paths "<XML_GLOB_PATH>" \
            --org-url-slug ${bamboo.TRUNK_ORG_SLUG} \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_ORG_SLUG: <YOUR_TRUNK_ORG_SLUG>
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
version: 2
plan:
  project-key: <YOUR_PROJECT_KEY>
  key: <YOUR_PLAN_KEY>
  name: Run Tests and Upload to Trunk.io

Run Tests and Upload to Trunk:
  key: <YOUR_JOB_KEY>
  tasks:
    - checkout:
        description: Checkout Source Code

    - script:
        name: Run Tests
        body: |
          # Your test command here

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --bazel-bep-path <BEP_JSON_PATH> \
            --org-url-slug ${bamboo.TRUNK_ORG_SLUG} \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_ORG_SLUG: <YOUR_TRUNK_ORG_SLUG>
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>
```
{% endtab %}

{% tab title="XCode" %}
```yaml
version: 2
plan:
  project-key: <YOUR_PROJECT_KEY>
  key: <YOUR_PLAN_KEY>
  name: Run Tests and Upload to Trunk.io

Run Tests and Upload to Trunk:
  key: <YOUR_JOB_KEY>
  tasks:
    - checkout:
        description: Checkout Source Code

    - script:
        name: Run Tests
        body: |
          # Your test command here

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --xcresult-path <XCRESULT_PATH> \
            --org-url-slug ${bamboo.TRUNK_ORG_SLUG} \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_ORG_SLUG: <YOUR_TRUNK_ORG_SLUG>
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>
```
{% endtab %}
{% endtabs %}

#### Uploading from Pull Request Builds

To detect flaky tests on pull requests, configure your plan to create [plan branches](https://confluence.atlassian.com/bamboo/using-plan-branches-289276872.html) for pull requests. Add the following to your Plan Spec:

```yaml
branches:
  create:
    for-pull-request:
      accept-fork: false
```

Bamboo automatically sets the `bamboo_repository_pr_key` variable on PR builds, which the Trunk CLI uses to associate uploads with the correct pull request.

{% hint style="info" %}
**PR number not detected?** If your Bamboo setup does not set `bamboo_repository_pr_key`, you can override it by passing the `--pr-number` flag or setting the `TRUNK_PR_NUMBER` environment variable when running the upload command.
{% endhint %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
