---
description: Enhance CI Autopilot by uploading test results
---

# Upload test results

By default, CI Autopilot analyzes general CI logs to identify failures. Adding structured test results enables more precise, test-level analysis with better root cause identification and more targeted fix recommendations.

### Prerequisites

* GitHub repository with GitHub Action workflows
* [CI Autopilot enabled for your GitHub repository](connect-to-github.md)
* 10-15 minutes for setup

### Step 1 of 3: Configure test framework to generate test reports

{% hint style="info" %}
This setup shares documentation with Trunk's Flaky Tests feature, but you don't need to use Flaky Tests to benefit from enhanced CI Autopilot analysis.
{% endhint %}

Select test framework and follow the instructions to configure test reports: [frameworks](../../../flaky-tests/get-started/frameworks/ "mention")

#### Validating reports (JUnit XML files)

{% include "../../../.gitbook/includes/you-can-validate-your-test-....md" %}

**✅ Success: The test reports pass the validation checks**

### Step 2 of 3: Configure GitHub Actions to upload test results

{% hint style="warning" %}
CI Autopilot currently only supports GitHub Actions.
{% endhint %}

Follow the setup guide to upload test results: [github-actions.md](../../../flaky-tests/get-started/ci-providers/github-actions.md "mention")

**✅ Success: The updated workflow uploads test results successfully**

### Step 3 of 3: Confirm test results are uploaded

{% hint style="info" %}
A new Uploads view for CI Autopilot is currently in progress
{% endhint %}

Currently, the best way to validate test result uploads are successfully processed by Trunk is by looking into the Uploads tab for Flaky Tests.

* Select "Flaky Tests" in the top navigation
* Click on the "Uploads" tab
* Select your repository in the repository selector on the top right

<figure><img src="../../../.gitbook/assets/Screenshot 2025-09-11 at 4.08.51 PM.png" alt="The uploads tab contains results received from past CI jobs."><figcaption><p>The uploads tab contains results received from past CI jobs</p></figcaption></figure>

**✅ Success: The uploaded test results are showing up in the uploads view**
