# TeamCity

Trunk Flaky Tests integrates with your CI by adding a step in your TeamCity Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

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

Store the Trunk slug and API token obtained in the previous step in your TeamCity project by navigating to **Admin > Build > Parameters > Add new parameter** and adding new environment variables as `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Add Uploader to a Build Step

Add the following command as a build step after your test run to upload test results. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

{% tabs %}
{% tab title="XML" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="XCode" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --xcresults-path <XCRESULT_PATH> \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
TRUNK_ORG_URL_SLUG=$TRUNK_ORG_SLUG \
TRUNK_API_TOKEN=$TRUNK_TOKEN \
bundle exec rspec
```
{% endtab %}
{% endtabs %}

In your build step settings under the **Show advanced options** toggle, find the **Execute step settings** and select `Always, even if build stop command was issued` to ensure that the Upload step will still run if tests have failed.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

You can do this in TeamCity by omitting your JUnit XML path in the saved artifacts. [Learn more about artifacts in TeamCity](https://www.jetbrains.com/help/teamcity/cloud/configure-and-run-your-first-build.html#Artifacts).

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
