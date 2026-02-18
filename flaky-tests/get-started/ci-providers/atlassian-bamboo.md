---
description: Configure Flaky Tests using Atlassian Bamboo
---

# Atlassian Bamboo

Trunk Flaky Tests integrates with your CI by adding a step in your Bamboo Plans to upload tests with the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

### Checklist

By the end of this guide, you should achieve the following.

* [ ] Get your Trunk organization slug and token
* [ ] Set your slug and token as a variable in Bamboo
* [ ] Configure your Bamboo Plan to upload to Trunk
* [ ] Validate your uploads in Trunk

After completing these checklist items, you'll be integrated with Trunk.

### Trunk Organization Slug and Token

Before setting up uploads to Trunk, you must sign in to [app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests) and obtain your Trunk organization slug and token.

#### Trunk Slug

You can find your organization slug under **Settings > Organization > Manage > Organization Name > Slug**. You'll save this as a variable in Bamboo in a later step.

#### Trunk Token

You can find your token under **Settings > Organization > Manage > Organization API Token > View Organization API Token > View**. Since this is a secret, do not leak it publicly. Ensure you get your _organization token_, not your project/repo token.

### Add the Trunk Token as a Secret

Store the Trunk API token as a [Bamboo plan variable](https://confluence.atlassian.com/bamboo/bamboo-variables-289277087.html) named `TRUNK_TOKEN`. Mark this variable as **Secret** in the Bamboo UI to prevent it from being exposed in build logs.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your Bamboo jobs that run tests. This should minimally include all jobs that run on pull requests, as well as jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Example Bamboo Plan Spec

The following is an example of a [Bamboo Plan Spec](https://confluence.atlassian.com/bamboo/bamboo-specs-894743906.html) (YAML) that uploads test results after your tests run. The upload step is placed under `final-tasks` so it runs even if your tests fail.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](../frameworks/) docs.

{% tabs %}
{% tab title="JUnit XML" %}
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
          # Your test command here, e.g.:
          # ./gradlew test
          # mvn test
          # npm test

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --junit-paths "**/junit.xml" \
            --org-url-slug <TRUNK_ORG_SLUG> \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>

branches:
  create:
    for-pull-request:
      accept-fork: false
```
{% endtab %}

{% tab title="Bazel BEP JSON" %}
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
          bazel test //... --build_event_json_file=build_events.json

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --bazel-bep-path build_events.json \
            --org-url-slug <TRUNK_ORG_SLUG> \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>

branches:
  create:
    for-pull-request:
      accept-fork: false
```
{% endtab %}

{% tab title="XCResult Path" %}
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
          xcodebuild test \
            -scheme YourScheme \
            -resultBundlePath ./test-results.xcresult

  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --xcresult-path ./test-results.xcresult \
            --org-url-slug <TRUNK_ORG_SLUG> \
            --token ${bamboo.TRUNK_TOKEN}

variables:
  TRUNK_TOKEN: <YOUR_TRUNK_TOKEN>

branches:
  create:
    for-pull-request:
      accept-fork: false
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Why `final-tasks`?** In Bamboo, `final-tasks` always execute regardless of whether previous tasks succeeded or failed. This ensures test results are uploaded even when tests fail, which is essential for accurate flaky test detection.
{% endhint %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

### PR Number Detection

{% hint style="warning" %}
Bamboo may not always expose the pull request number through its environment variables, depending on your plan configuration and how branch builds are triggered.

If Trunk is not detecting PR numbers for your Bamboo builds, you can explicitly pass the PR number using the `--pr-number` flag or the `TRUNK_PR_NUMBER` environment variable.
{% endhint %}

To set the PR number explicitly, add the `--pr-number` flag to your upload command:

```yaml
  final-tasks:
    - script:
        name: Upload Test Results to Trunk.io
        body: |
          curl -fsSLO --retry 3 https://trunk.io/releases/trunk
          chmod +x ./trunk
          ./trunk flakytests upload \
            --junit-paths "**/junit.xml" \
            --org-url-slug <TRUNK_ORG_SLUG> \
            --token ${bamboo.TRUNK_TOKEN} \
            --pr-number ${bamboo.TRUNK_PR_NUMBER}
```

Alternatively, set the `TRUNK_PR_NUMBER` environment variable in your plan, and the CLI will pick it up automatically.

### Bamboo Environment Variables

Trunk automatically detects the following Bamboo environment variables when running in a Bamboo CI environment:

| Variable | Description |
| --- | --- |
| `bamboo_planRepository_branch` | The branch being built |
| `bamboo_planRepository_revision` | The commit SHA |
| `bamboo_planRepository_repositoryUrl` | The repository URL |
| `bamboo_buildNumber` | The build number |
| `bamboo_buildResultKey` | Unique key for the build result |
| `bamboo_buildResultsUrl` | URL to the build results page |
| `bamboo_planKey` | The plan key |
| `bamboo_planName` | The plan name |
| `bamboo_buildTimeStamp` | Timestamp of the build |
| `bamboo_repository_pr_key` | PR number (only available on PR builds) |

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
