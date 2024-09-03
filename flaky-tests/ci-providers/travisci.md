---
description: Configure Flaky Tests using Travis CI
---

# Travis CI

## Getting Started

You can use the Flaky Tests CLI within your [Travis CI](https://www.travis-ci.com/) workflows to upload and analyze your test results.

{% hint style="info" %}
The Trunk Flaky Tests CLI currently only supports x86_64 and arm64 for both Linux and macOS. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation does not use cached test results and does not automatically retry failing tests.
{% endhint %}

### Create a Travis CI Workflow

Create a Travis CI workflow (or modify an existing one) to run the tests that you want to monitor. The workflow should produce a test report in [**JUnit XML**](https://github.com/testmoapp/junitxml) format. Most testing frameworks support XML output. See [Testing Framework Configuration](../frameworks/) for guides for common testing frameworks. Make sure that your test invocation doesn't use cached test results, and doesn't automatically retry failing tests.

### Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to **Settings -> Manage -> Organization**. Copy your organization slug. You can find your Trunk token by navigating to **Settings → Manage Organization → Organization API** Token and clicking "View." Copy this token. Make sure you are getting your _organization token_, not your project/repo token.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

### Set Project Environment Variables

In your Travis CI project settings under **Environment Variables**, create new variables for your Trunk org as `TRUNK_ORG_SLUG` and the api token as `TRUNK_API_TOKEN`.

[//]: # (<figure><img src="../../.gitbook/assets/CircleCI-env-var-settings-screenshot.png" alt=""><figcaption><p>CircleCI Project Settings</p></figcaption></figure>)

### Add Uploader to Testing Workflow

Now update your Travis CI workflow to download and run the test uploader binary after you've run your tests. Here is an example of a NodeJS project using Vitest tests.

You can upload test results to Flaky Tests with the [`trunk-analytics-cli`](https://github.com/trunk-io/analytics-cli) by running
it in a stage after your tests are complete. There are four different OS/arch builds of the CLI in the latest release. Pick the
one you need for your testing platform and be sure to download the release on every CI run. **Do not bake the CLI into a
container or VM.** This ensures your CI runs are always using the latest build.



{% tabs %}


{% tab title="Linux x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - echo "starting to build"
  - npm install
  - npm run clean
  - npm run vitest
  - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
  - ./trunk-analytics-cli upload --junit-paths "test-output.xml" --org-url-slug $TRUNK_ORG_SLUG --token $TRUNK_API_TOKEN
```
{% endcode %}
{% endtab %}

{% tab title="Linux arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - echo "starting to build"
  - npm install
  - npm run clean
  - npm run vitest
  - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-unknown-linux.tar.gz" | tar -xvz > ./trunk-analytics-cli
  - ./trunk-analytics-cli upload --junit-paths "test-output.xml" --org-url-slug $TRUNK_ORG_SLUG --token $TRUNK_API_TOKEN
```
{% endcode %}
{% endtab %}

{% tab title="macOS x86_64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - echo "starting to build"
  - npm install
  - npm run clean
  - npm run vitest
  - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
  - ./trunk-analytics-cli upload --junit-paths "test-output.xml" --org-url-slug $TRUNK_ORG_SLUG --token $TRUNK_API_TOKEN
```
{% endcode %}
{% endtab %}

{% tab title="macOS arm64" %}
{% code title="upload.yaml" overflow="wrap" lineNumbers="true" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - echo "starting to build"
  - npm install
  - npm run clean
  - npm run vitest
  - curl -fsSL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-apple-darwin.tar.gz" | tar -xvz > ./trunk-analytics-cli
  - ./trunk-analytics-cli upload --junit-paths "test-output.xml" --org-url-slug $TRUNK_ORG_SLUG --token $TRUNK_API_TOKEN
```
{% endcode %}
{% endtab %}

{% endtabs %}



In the config about we have added two additional commands to download the latest release of the `trunk-analytics-cli` and 
then run it to upload the test output xml file. The TRUNK\_ORG\_SLUG and TRUNK\_API\_TOKEN variables are filled in at runtime by 
the Travis CI environment variables set earlier.

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).
