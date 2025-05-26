---
description: Configure Flaky Tests detection using a GitHub Action
---

# GitHub Actions

Before you start these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing Trunk-compatible reports for your test runner.

Trunk Flaky Tests integrates with your CI by adding a step in your GitHub Action workflow to upload tests with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

### Checklist

By the end of this guide, you should achieve the following.

* [ ] Get your Trunk organization slug and token
* [ ] Set your slug and token as secrets in GitHub Actions
* [ ] Configure GitHub Actions to upload to Trunk
* [ ] Validate your uploads in Trunk

After completing these checklist items, you'll be integrated with Trunk.&#x20;

### Trunk Organization Slug and Token

Before setting up uploads to Trunk, you must sign in to [app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests) and obtain your Trunk organization slug and token.

#### Trunk Slug

You can find your organization slug under **Settings > Organization > Manage > Organization Name > Slug**. You'll save this as a variable in CI in a later step.

#### Trunk Token

You can find your token under **Settings > Organization > Manage > Organization API Token > View Organization API Token > View**. Since this is a secret, do not leak it publicly. Ensure you get your _organization token_, not your project/repo token.

### Add Your Trunk Token and Organization Slug as Secrets

Store the Trunk slug and API token obtained in the previous step in your repo as [GitHub secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) named `TRUNK_ORG_URL_SLUG` and `TRUNK_API_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should minimally include all jobs that run on pull requests, as well as jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Example GitHub Actions Workflow

The following is an example of a GitHub Actions workflow step to upload test results after your tests using Trunk's [**Analytics Uploader Action**](https://github.com/trunk-io/analytics-uploader).

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [**Test Frameworks**](../frameworks/) docs.

{% tabs %}
{% tab title="JUnit XML" %}
```yaml
jobs:
  test:
    name: Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests
        run: ...

      - name: Upload Test Results to Trunk.io
        if: "!cancelled()" # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          junit-paths: "**/junit.xml"        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}

```
{% endtab %}

{% tab title="XCResults Path" %}
```yaml
jobs:
  test:
    name: Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests
        run: ...

      - name: Upload Test Results to Trunk.io
        if: "!cancelled()" # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          xcresult-path: "./test-results.xcresult"        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}
```
{% endtab %}

{% tab title="Bazel BEP JSON" %}
```yaml
jobs:
  test:
    name: Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests
        run: ...

      - name: Upload Test Results to Trunk.io
        if: "!cancelled()" # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          bazel-bep-path: "./build_events.json"        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}
```
{% endtab %}
{% endtabs %}

See the [GitHub Actions Reference page](https://github.com/trunk-io/analytics-uploader) for all available CLI arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
