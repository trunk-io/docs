---
description: Configure Flaky Tests detection using a GitHub Action
---

# GitHub Actions

Before you start these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing Trunk-compatible reports for your test runner.

Trunk Flaky Tests integrates with your CI by adding a step in your GitHub Action workflow to upload tests with the [Trunk Analytics CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add Your Trunk Token and Organization Slug as Secrets

Store the Trunk slug and API token obtained in the previous step in your repo as [GitHub secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) named `TRUNK_ORG_URL_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should minimally include all jobs that run on pull requests, as well as jobs that run on your main or [stable branches](../../detection/), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

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
        if: ${{ !cancelled() }} # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          junit-paths: **/junit.xml        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}
```
{% endtab %}

{% tab title="XCResult Path" %}
```yaml
jobs:
  test:
    name: Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests
        run: ...

      - name: Upload Test Results to Trunk.io
        if: ${{ !cancelled() }} # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          xcresult-path: ./test-results.xcresult        
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
        if: ${{ !cancelled() }} # Upload the results even if the tests fail
        continue-on-error: true # don't fail this job if the upload fails
        uses: trunk-io/analytics-uploader@v1
        with:
          bazel-bep-path: ./build_events.json        
          org-slug: <TRUNK_ORG_SLUG>
          token: ${{ secrets.TRUNK_TOKEN }}
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
jobs:
  test:
    name: Run and Upload Tests
    runs-on: ubuntu-latest

    steps:
      - name: Run Tests and Upload Results to Trunk.io
        run: TRUNK_ORG_URL_SLUG=${{ secrets.TRUNK_ORG_SLUG }} TRUNK_API_TOKEN=${{ secrets.TRUNK_TOKEN }} bundle exec rspec

```
{% endtab %}
{% endtabs %}

See the [GitHub Actions Reference page](https://github.com/trunk-io/analytics-uploader) for all available CLI arguments and usage.

#### Enable quarantining

You can quarantine flaky tests by wrapping the test command or as a follow-up step.

{% tabs %}
{% tab title="GitHub Actions Workflow" %}
{% hint style="warning" %}
Using the Trunk Analytics Uploader Action in your GitHub Actions Workflow files, may need modifications to your workflow files to support quarantining.

If you upload your test results as a second step after you run your tests, **you need to add** `continue-on-error: true` **on your test step so your CI** job will continue even on failures.
{% endhint %}

Here's an example file.

<pre class="language-yaml" data-line-numbers><code class="lang-yaml">name: Run Tests And Upload Results
on:
  workflow_dispatch:
jobs:
  upload-test-results:
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:   
    - name: Run Tests
      id: unit_tests
      shell: bash
<strong>      run: &#x3C;COMMAND TO RUN TESTS> # command to run tests goes here
</strong><strong>      continue-on-error: true # allow CI job to continue to upload step on errors
</strong>        
    - name: Upload test results
      if: always()
      uses: trunk-io/analytics-uploader@v1
      with:
        junit-paths: &#x3C;TEST OUTPUT PATH>
        org-slug: my-trunk-org-slug
        token: ${{ secrets.TRUNK_TOKEN }}
</code></pre>

If you want to run the test command and upload in a single step, the test command must be **run via the Analytics Uploader** through the `run: <COMMAND TO RUN TESTS>` parameter.

This will override the response code of the test command. Make sure to set `continue-on-error: false` so un-quarantined tests are blocking.

<pre class="language-yaml" data-line-numbers><code class="lang-yaml">name: Run Tests And Upload Results
on:
  workflow_dispatch:
jobs:
  upload-test-results:
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run tests and upload results
        uses: trunk-io/analytics-uploader@v1
        with:
          junit-paths: &#x3C;TEST OUTPUT PATH>
<strong>          run: &#x3C;COMMAND TO RUN TESTS> # command to run tests goes here
</strong>          org-slug: my-trunk-org-slug
          token: ${{ secrets.TRUNK_TOKEN }}
</code></pre>
{% endtab %}

{% tab title="Using The Trunk Analytics CLI Directly" %}
**Using Flaky Tests as a separate step**

{% hint style="warning" %}
If you upload your test results as a second step after you run your tests, you need to make sure your test step **continues on errors** so the upload step that's run after can quarantine failed tests.&#x20;

When quarantining is enabled, the `trunk-analytics-cli upload` command will **return an error** if there are unquarantined failures and return a status code 0 if all tests are quarantined.
{% endhint %}

<pre class="language-bash"><code class="lang-bash"><strong>&#x3C;run my tests> || true # doesn't fail job on failure
</strong>|
    ./trunk-analytics-cli upload \
        --org-url-slug $TRUNK_ORG_SLUG \
        --token $TRUNK_TOKEN \
        --junit-paths $JUNIT_PATH
</code></pre>

**Using Flaky Tests as a single step**

You can also wrap the test command with the Trunk Analytics CLI. When wrapping the command with the Trunk Analytics CLI, if there are unquarantined tests, the command will return an error. If there are no unquarantined tests, the command will return a status code `0`.

{% code overflow="wrap" %}
```bash
./trunk-analytics-cli test \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN \
    --junit-paths $JUNIT_PATH \
    --allow-empty-test-results \
    <Test Command>
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

### Getting Direct Links to Job Logs

{% hint style="info" %}
**Direct Links to Job Logs is an optional configuration, and relies on a** [**third-party actions dependency**](https://github.com/marketplace/actions/get-action-job-id)**.**
{% endhint %}

By default, Trunk Flaky Tests links to your overall workflow run when you click "Logs" on a test failure. However, GitHub Actions makes it difficult to get a direct link to the specific job where the test ran.

If you want **direct links to individual job logs** instead of the workflow run, you can manually set the `JOB_URL` environment variable using a third-party action to extract the job ID.

#### Setup

1. **Add the job ID extraction step** to your workflow using a community action:

<pre class="language-yaml"><code class="lang-yaml">jobs:  
  run_tests:
    runs-on: ubuntu-latest
    name: Run Tests  # This name is important - use it in the next step
    steps:
      - name: Checkout
        uses: actions/checkout@v3

<strong>      # Extract the job ID
</strong><strong>      - name: Get Job ID
</strong><strong>        id: get-job-id
</strong><strong>        uses: ayachensiyuan/get-action-job-id@v1.6
</strong><strong>        env:
</strong><strong>          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
</strong><strong>        with:
</strong><strong>          job-name: Run Tests  # Must match the job 'name' above
</strong></code></pre>

2. **Pass the job URL** when uploading test results:

<pre class="language-yaml"><code class="lang-yaml">      - name: Run Tests
        id: unit_tests
        run: &#x3C;COMMAND TO RUN TESTS>
        continue-on-error: true
        
      - name: Upload test results
        if: always()
        uses: trunk-io/analytics-uploader@v1
        with:
          junit-paths: &#x3C;TEST OUTPUT PATH>
          org-slug: my-trunk-org-slug
          token: ${{ secrets.TRUNK_TOKEN }}
<strong>        env:
</strong><strong>          JOB_URL: https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}/job/${{ steps.get-job-id.outputs.jobId }}
</strong></code></pre>

#### Complete Example

Here's a full workflow example with direct job linking:

```yaml
name: Run Tests And Upload Results
on:
  push:
  pull_request:

jobs:  
  test-suite:
    runs-on: ubuntu-latest
    name: Test Suite
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Get Job ID
        id: get-job-id
        uses: ayachensiyuan/get-action-job-id@v1.6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          job-name: Test Suite
        
      - name: Run Tests
        run: npm test
        continue-on-error: true
        
      - name: Upload test results
        if: always()
        uses: trunk-io/analytics-uploader@v1
        with:
          junit-paths: junit.xml
          org-slug: my-trunk-org-slug
          token: ${{ secrets.TRUNK_TOKEN }}
        env:
          JOB_URL: https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}/job/${{ steps.get-job-id.outputs.jobId }}
```

#### How It Works

* The `ayachensiyuan/get-action-job-id` [action](https://github.com/marketplace/actions/get-action-job-id) extracts the GitHub Actions job ID
* We construct the full job URL using: `https://github.com/{repo}/actions/runs/{run_id}/job/{job_id}`
* This URL is passed to Trunk via the `JOB_URL` environment variable
* When you click "Logs" on a test failure in Trunk, you'll go directly to that job's logs instead of the workflow overview

#### Notes

* The `job-name` parameter must **exactly match** your job's `name` field
* The `GITHUB_TOKEN` must have appropriate permissions to read workflow job information
* If the job ID extraction fails, Trunk will fall back to linking to the workflow run
