# Getting Started

Trunk Flaky Tests detects flaky tests by analyzing test results from your CI runs. Setup requires configuring test result output and CI upload integration.

### Prerequisites

* Account at [app.trunk.io](https://app.trunk.io)
* Ability to modify repository CI configuration and add secrets
* Tests running in CI on both PRs and stable branches (e.g., main)

{% hint style="info" %}
GitLab and BitBucket support is experimental. [Contact us](mailto:support@trunk.io) if not using GitHub.
{% endhint %}

#### Step 1: Ensure JUnit XML output

Trunk ingests test results in JUnit XML format. If your CI already generates JUnit XML, note the file paths and skip to Step 2.

If not, configure your test frameworks to output JUnit XML:

* See [**Test Frameworks**](frameworks/) for framework-specific configuration
* Supports multiple frameworks simultaneously

#### Step 2: Configure CI uploads

Add test result uploads to all CI jobs that run tests.

1. See [**CI Providers**](ci-providers/) for integration instructions
2. Configure uploads in jobs that run on:
   * Pull request branches
   * Stable branches (`main`, `master`, `develop`, etc.)
   * Merge queue branches (if applicable)

Uploads from both PRs and stable branches are required for accurate flaky test detection.

#### Step 3: Verify integration

1. Push your changes and trigger a CI run
2. Check CI logs for successful upload confirmation
3. **Wait 15-30 minutes** for results to process, then verify uploads appear at [app.trunk.io](https://app.trunk.io) → your repo → **Flaky Tests > Uploads**

<figure><picture><source srcset="../../.gitbook/assets/Screenshot 2025-11-11 at 3.57.57 PM.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/Screenshot 2025-11-11 at 3.58.16 PM.png" alt=""></picture><figcaption><p>Uploads tab</p></figcaption></figure>

#### Detection timeline

Trunk requires **10+ runs per test** to start detecting flaky tests accurately. Depending on your CI velocity, this takes hours to days. High-velocity repos (100+ runs/day) may see first detections within a day.

You'll receive email notification when the first flaky test is detected.

[How Trunk detects flaky tests →](../detection.md)

#### Quarantining

Override exit codes for known flaky test failures, allowing CI jobs to pass while tests continue running and uploading results. Requires both UI configuration and CI job modifications.

**Use case:** Unblock merge queues and critical pipelines without losing test coverage or data.

{% hint style="warning" %}
**Advanced feature:** Enable only after detection is working reliably. Quarantining significantly changes CI behavior.
{% endhint %}

[Configure Quarantining →](../quarantining.md)
