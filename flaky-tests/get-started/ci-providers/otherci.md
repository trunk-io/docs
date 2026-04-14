---
description: Configure Flaky Tests using any CI Provider
---

# Other CI Providers

Trunk Flaky Tests integrates with your CI provider by adding an upload step in each of your testing CI jobs via the [Trunk Analytics CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your CI provider as a secret, environment variable, or an equivalent concept and name them `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection/), for example,`main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

#### Example Upload Script

The following is an example of a script to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

You can install the Trunk Analytics CLI locally like this:

{% tabs %}
{% tab title="Linux (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="Linux (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="macOS (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="macOS (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}
{% endtabs %}

Then, you can validate the results using the `trunk-analytics-cli validate` command like this:

```bash
./trunk-analytics-cli validate --junit-paths <PATH_TO_REPORTS>
```

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Environment Variables

Set these environment variables before running `trunk-analytics-cli upload` on unsupported CI systems:

{% hint style="info" %}
**Config Requirement:** `CUSTOM` must be set to `true` for environment varaibles to take effect and override the auto-detection of CI.

All other variables are optional but recommended.
{% endhint %}

| Variable         | Description                                                                                                      | Example                               |
| ---------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `CUSTOM`         | Set to `true` to indicate this CI system is not one of our supported providers                                   | `CUSTOM=true`                         |
| `JOB_URL`        | Direct link to the CI job/build page. This is the link users will click when viewing test failure logs in Trunk. | `https://ci.example.com/builds/12345` |
| `JOB_NAME`       | Name of the CI job or test suite                                                                                 | `unit-tests`                          |
| `AUTHOR_EMAIL`   | Email address of the commit author                                                                               | `dev@example.com`                     |
| `AUTHOR_NAME`    | Full name of the commit author                                                                                   | `Jane Developer`                      |
| `COMMIT_BRANCH`  | Git branch being tested                                                                                          | `main`                                |
| `COMMIT_MESSAGE` | Commit message for the tested commit                                                                             | `Fix authentication bug`              |
| `PR_NUMBER`      | Pull request number (if applicable)                                                                              | `123`                                 |
| `PR_TITLE`       | Pull request title (if applicable)                                                                               | `Add new feature`                     |

#### About JOB\_URL

The `JOB_URL` variable controls where the "Logs" link in Trunk Flaky Tests points to. When users click "Logs" on a test failure, they'll be taken to this URL to view the complete CI job output.

**Best practice:** Provide the most specific link possible:

* ✅ Direct link to the specific job/build where the test ran
* ✅ Link that shows the full logs and test output
* ❌ Link to a dashboard or workflow overview (less helpful for debugging)

{% hint style="info" %}
**For GitHub Actions users:** While GitHub Actions is auto-detected, you can override the default workflow URL with a direct job URL. See [GitHub Actions - Getting Direct Links to Job Logs](github-actions.md#getting-direct-links-to-job-logs) for instructions.
{% endhint %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}
