---
description: >-
  Set up Trunk Flaky Tests by configuring test result output, uploading from
  CI, and enabling flake detection monitors.
---

# Getting Started

Trunk Flaky Tests detects flaky tests by analyzing test results from your CI runs. Setup requires configuring test result output and CI upload integration.

{% hint style="info" %}
**Interactive setup available** — If you have a Trunk account, the [in-app onboarding guide](https://app.trunk.io) walks you through configuration with instructions tailored to your test framework and CI provider.
{% endhint %}

### Prerequisites

* Account at [app.trunk.io](https://app.trunk.io)
* Ability to modify repository CI configuration and add secrets
* Tests running in CI on both PRs and stable branches (e.g., main)

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

Uploads from both PRs and stable branches are required for Trunk Flaky Tests to accurately detect flaky tests.

#### Step 3: Verify integration

1. Push your changes and trigger a CI run
2. Check CI logs for successful upload confirmation
3. Results typically appear within a few minutes. Verify uploads appear at [app.trunk.io](https://app.trunk.io) → your repo → **Flaky Tests > Uploads**

<figure><picture><source srcset="../../.gitbook/assets/Screenshot 2025-11-11 at 3.57.57 PM.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/Screenshot 2025-11-11 at 3.58.16 PM.png" alt=""></picture><figcaption><p>Uploads tab</p></figcaption></figure>

#### Step 4: Configure flake detection

After uploads are flowing, navigate to your repo → **Flaky Tests > Monitors** to set up detection.

**Pass-on-retry** is enabled by default and is the recommended baseline for everyone. It catches the most common flakiness pattern — a test that fails and then passes on retry within the same commit — without any configuration needed.

**Failure rate monitors** let you detect flakiness based on failure rate over a rolling time window. How you configure them depends on your CI setup:

- **If tests must pass before merging to main**, set up a failure rate monitor scoped to `main` to catch an elevated failure rate. For example, if you run tests 5 times per day on `main`, a 24-hour rolling window with a minimum of 4 runs and a failure threshold of 25% is a reasonable starting point. This gives the monitor enough data before flagging anything.
- **If you use a merge queue**, consider a dedicated monitor scoped to your merge queue branches (e.g., `trunk-merge/*` or `gh-readonly-queue/*`). Failures here are especially suspicious since the code has already passed PR checks, so a low threshold is appropriate.

[How failure rate monitors work →](../detection/failure-rate-monitor.md)

#### Quarantining

Quarantining suppresses failures from known flaky tests, preventing them from forcing CI re-runs or blocking your merge queue. Flaky tests continue to run and report results — they just don't cause pipeline failures while your team works on fixes. This is especially valuable for unblocking merge queues and keeping development velocity high.

[Configure Quarantining →](../quarantining.md)
