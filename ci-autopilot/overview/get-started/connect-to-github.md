---
description: >-
  Get started with Trunk CI Autopilot to get root cause analysis with fixes for
  CI/test failures.
---

# Connect to GitHub

CI Autopilot automatically investigates CI failures in your pull requests and provides root cause analysis with suggested fixes, saving your team hours of debugging time. The following steps guide you through the onboarding process.

### Prerequisites

* GitHub repository with GitHub Action workflows
* Admin access to your GitHub organization
* [Trunk account](https://app.trunk.io/signup?intent=flaky%20tests)
* 5 minutes for setup

### Step 1 of 3: Open Trunk CI Autopilot

[Open the Trunk app](https://app.trunk.io/) and navigate to the CI Autopilot, which can be found in the top navigation. The following welcome screen will be shown.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-09-11 at 2.35.49 PM.png" alt=""><figcaption><p>CI Autopilot Landing Screen</p></figcaption></figure>

**✅ Success: You see the CI Autopilot welcome screen with an 'Install GitHub App' button**

### Step 2 of 3: Install GitHub App

Click on "Install GitHub App" to get started. A GitHub page to select which organization to enable the app for and what repositories Trunk should have access to will be shown.

{% hint style="info" %}
Trunk's GitHub app requires the following permissions:

* **Read** access to administration, commit statuses, and metadata
* **Read** and **write** access to actions, checks, code, issues, pull requests, and workflows
{% endhint %}

Select your repositories and click Install to return to Trunk's confirmation screen.

**✅ Success: You return to Trunk and see a list of your accessible repositories**

### Step 3 of 3: Enable CI Autopilot

<figure><img src="../../../.gitbook/assets/Screenshot 2025-09-11 at 2.37.58 PM.png" alt="" width="375"><figcaption><p>GitHub App installation confirmation</p></figcaption></figure>

Select the repository you want to enable the CI Autopilot for from the dropdown list and click on "Enable".

A confirmation view will be shown and Trunk will open the activity feed. The CI Autopilot is now running in the background and waiting for the next PR failure to conduct the first failure investigation.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-09-11 at 2.41.58 PM.png" alt=""><figcaption><p>Empty activity feed after CI Autopilot was enabled</p></figcaption></figure>

**✅ Success: The activity feed shows 'CI Autopilot is monitoring this repository' with an empty investigation list.**

### **What's Next?**

CI Autopilot will start investigations whenever a CI workflow fails. Create a failing PR to initiate the first investigation.

In the meantime, learn about how to use the CI Autopilot:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Understanding PR comments</td><td><a href="../use-ci-autopilot/understand-root-cause-analysis.md">understand-root-cause-analysis.md</a></td></tr><tr><td>Requesting fixes</td><td><a href="../use-ci-autopilot/request-fixes-on-prs.md">request-fixes-on-prs.md</a></td></tr><tr><td>Applying fixes locally</td><td><a href="../use-ci-autopilot/apply-fixes-with-mcp.md">apply-fixes-with-mcp.md</a></td></tr></tbody></table>
