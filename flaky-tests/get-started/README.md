# Getting Started

Trunk Flaky Tests detects flaky tests by analyzing test results from your CI runs. Setup requires configuring test result output and CI upload integration.

### Prerequisites

* Account at [app.trunk.io](https://app.trunk.io)
* Ability to modify repository CI configuration and add secrets
* Tests running in CI on both PRs and stable branches (e.g., main)

{% hint style="info" %}
GitLab and BitBucket support is experimental. [Contact us](mailto:support@trunk.io) if not using GitHub.
{% endhint %}

### Key concepts

Before you begin setup, it helps to understand the core concepts behind Trunk Flaky Tests:

| Concept | What it means |
| --- | --- |
| **JUnit XML** | The standard report format Trunk ingests. Most test frameworks can produce it natively or via a plugin. Trunk also supports Bazel BEP and XCResult formats. |
| **Test identification** | Trunk generates a unique ID for each test from its name, classname, file path, and variant. Changing any of these creates a new test in Trunk. [Learn more -->](test-identification.md) |
| **Stable branches** | Branches like `main` or `master` where tests are expected to pass. Failures on stable branches are the strongest signal for flake detection. |
| **Variants** | Optional labels (e.g., `ios`, `chrome`) that let you track the same test across different environments separately. |
| **Quarantining** | An advanced feature that overrides CI exit codes for known flaky tests, preventing them from blocking your pipelines. |

### Setup steps

#### Step 1: Ensure JUnit XML output

Trunk ingests test results in JUnit XML format. If your CI already generates JUnit XML, note the file paths and skip to Step 2.

If not, configure your test frameworks to output JUnit XML:

* See [**Test Frameworks**](frameworks/) for framework-specific configuration
* Supports multiple frameworks simultaneously

#### Step 2: Get your Trunk organization credentials

Before configuring uploads, obtain your organization slug and API token from [app.trunk.io](https://app.trunk.io):

1. **Organization slug:** **Settings > Organization > General > Organization > Name**
2. **Organization API token:** **Settings > Organization > General > API > API Key**

{% hint style="danger" %}
Use your **Organization API token**, not a repo token. Store both values as secrets in your CI provider.
{% endhint %}

#### Step 3: Configure CI uploads

Add test result uploads to all CI jobs that run tests.

1. See [**CI Providers**](ci-providers/) for integration instructions
2. Configure uploads in jobs that run on:
   * Pull request branches
   * Stable branches (`main`, `master`, `develop`, etc.)
   * Merge queue branches (if applicable)

Uploads from both PRs and stable branches are required for accurate flaky test detection.

{% hint style="info" %}
**Using a custom or self-hosted CI runner?** Even if you use a supported CI provider (like GitHub Actions), you may need to set manual environment variables if your runner does not expose the standard CI environment. See the [environment variables reference](ci-providers/otherci.md#environment-variables) for details.
{% endhint %}

#### Step 4: Verify integration

1. Push your changes and trigger a CI run
2. Check CI logs for successful upload confirmation
3. **Wait 15-30 minutes** for results to process, then verify uploads appear at [app.trunk.io](https://app.trunk.io) -> your repo -> **Flaky Tests > Uploads**

<figure><picture><source srcset="../../.gitbook/assets/Screenshot 2025-11-11 at 3.57.57 PM.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/Screenshot 2025-11-11 at 3.58.16 PM.png" alt=""></picture><figcaption><p>Uploads tab</p></figcaption></figure>

### Detection timeline

Trunk requires **10+ runs per test** to start detecting flaky tests accurately. Depending on your CI velocity, this takes hours to days. High-velocity repos (100+ runs/day) may see first detections within a day.

You'll receive email notification when the first flaky test is detected.

[How Trunk detects flaky tests -->](../detection.md)

### After setup

#### Quarantining

Override exit codes for known flaky test failures, allowing CI jobs to pass while tests continue running and uploading results. Requires both UI configuration and CI job modifications.

**Use case:** Unblock merge queues and critical pipelines without losing test coverage or data.

{% hint style="warning" %}
**Advanced feature:** Enable only after detection is working reliably. Quarantining significantly changes CI behavior.
{% endhint %}

[Configure Quarantining -->](../quarantining.md)

### Troubleshooting

<details>
<summary>Uploads are not appearing in the Uploads tab</summary>

1. Check your CI logs for upload errors. Look for the `trunk-analytics-cli upload` output.
2. Verify you are using the **Organization API token**, not a repo token.
3. Confirm the `--org-url-slug` matches your organization slug exactly.
4. Ensure the JUnit XML file paths in `--junit-paths` match the actual report output locations.
5. Wait at least 30 minutes -- uploads are processed asynchronously.

</details>

<details>
<summary>Tests are not being detected as flaky</summary>

1. Trunk requires **10+ runs per test** before detection starts. Check the Uploads tab to confirm enough data has been received.
2. Verify you are uploading from **stable branches** (e.g., `main`), not just PR branches.
3. Check that test names are consistent across runs. See [How test identification works](test-identification.md) for details.

</details>

<details>
<summary>Using a custom CI runner or non-standard environment</summary>

If your CI environment does not set standard CI provider environment variables (for example, self-hosted GitHub Actions runners, custom Docker-based runners, or orchestration tools like Argo Workflows), you need to manually set environment variables. See the [environment variables reference](ci-providers/otherci.md#environment-variables).

Set `CUSTOM=true` to enable manual configuration, then provide the optional variables like `COMMIT_BRANCH`, `JOB_URL`, and others.

</details>
