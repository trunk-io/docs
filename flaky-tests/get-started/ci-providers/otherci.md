---
description: Configure Flaky Tests using any CI Provider
---

# Other CI Providers

Trunk Flaky Tests integrates with your CI provider by adding an upload step in each of your testing CI jobs via the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

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

Store the Trunk slug and API token obtained in the previous step in your CI provider as a secret, environment variable, or an equivalent concept and name them `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example,`main`, `master`, or `develop`.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Example Upload Script

The following is an example of a script to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

<pre class="language-sh"><code class="lang-sh">curl -fsSLO --retry 3 https://trunk.io/releases/trunk &#x26;&#x26; chmod +x trunk
<strong>./trunk flakytests upload --junit-paths "**/report.xml" --org-url-slug &#x3C;TRUNK_ORG_SLUG> --token "${TRUNK_TOKEN}"
</strong></code></pre>

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Environment Variables

Set these environment variables before running `trunk flaky-tests upload` on unsupported CI systems:

{% hint style="info" %}
Config Requirement: `CUSTOM` must be set to `true` for environment varaibles to take effect and override the auto-detection of CI. &#x20;
{% endhint %}

| Environment Variable | Description                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **`CUSTOM=true`**    | Set `CUSTOM` to `true` to indicate this CI system is not one of our first party supported ones |
| **`JOB_URL`**        | Direct link to the CI job/build page                                                           |
| **`JOB_NAME`**       | Name of the CI job or test suite                                                               |
| **`AUTHOR_EMAIL`**   | Email address of the commit author                                                             |
| **`AUTHOR_NAME`**    | Full name of the commit author                                                                 |
| **`COMMIT_BRANCH`**  | Git branch being tested                                                                        |
| **`COMMIT_MESSAGE`** | Commit message for the tested commit                                                           |
| **`PR_NUMBER`**      | Pull request number (if applicable)                                                            |
| **`PR_TITLE`**       | Pull request title (if applicable)                                                             |

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
