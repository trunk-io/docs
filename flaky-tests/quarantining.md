# Quarantining

Quarantining lets you isolate failures for known flaky tests so they don't fail your CI jobs, while still continuing to run them. Quarantining flaky tests lets you mitigate the negative effects of flaky tests without disabling any tests. Quarantined failures will still be uploaded to Trunk Flaky Tests and displayed in PRs through[ Universal Test Reports](https://app.gitbook.com/s/HGOcicyppLcsuUEwz9hd/flaky-tests/github-pull-request-comments), allowing you to easily triage failures and identify real issues surfaced by flaky tests.

### Prerequisites of Quarantining

Before a test can be quarantined, the test must be marked as flaky by Trunk Flaky Tests. You can tell if a test is flaky by the ⚠️ label or by checking its Status History.

<figure><img src="../.gitbook/assets/labelled as flaky.png" alt=""><figcaption></figcaption></figure>

A test's status history shows it labeled as flaky.

### Quarantining Modes

Quarantining operates in one of three modes, disabled, enabled, and preview. If you’re trying quarantining for the first time in a project, you can enable the preview mode, which will show you what could be quarantined but will not affect your CI job results.

<table data-header-hidden><thead><tr><th width="167"></th><th></th></tr></thead><tbody><tr><td>Mode</td><td>Behavior</td></tr><tr><td>Disabled</td><td>No tests will be quarantined.</td></tr><tr><td>Enabled</td><td>If CI jobs use the<a href="https://open.gitbook.com/~space/HGOcicyppLcsuUEwz9hd/~changes/kktdUpvJkOC1F16Yh1ml/~gitbook/pdf?back=false&#x26;only=yes&#x26;page=ypJ8CSYxGsp7J1Eev0JW#pdf-page-ypJ8CSYxGsp7J1Eev0JW-update-ci-jobs"> Analytics Uploader with Quarantining enabled</a>, failed flaky tests will be quarantined. If all failed tests are quarantined, the CI job result will be overridden as a pass.</td></tr><tr><td>Preview</td><td>If CI jobs use the<a href="https://open.gitbook.com/~space/HGOcicyppLcsuUEwz9hd/~changes/kktdUpvJkOC1F16Yh1ml/~gitbook/pdf?back=false&#x26;only=yes&#x26;page=ypJ8CSYxGsp7J1Eev0JW#pdf-page-ypJ8CSYxGsp7J1Eev0JW-update-ci-jobs"> Analytics Uploader with Quarantining enabled</a>, failed flaky tests will be displayed as quarantined in the Flaky Test web app, but the CI jobs will not be overridden as a pass.</td></tr></tbody></table>

#### Enable Quarantining

You can enable quarantining by navigating to **Settings** > **Repositories** > **Flaky Tests** > **Quarantine Flaky Tests** and selecting enabled in the drop-down.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3-J-EA1yJ9kRz7_vdu23CtvZNh4nR03u7SRgciS_piqb2KYVvgNQI3ymXSwW8UOfl4eFOBoslB_3Br855qxIyLiUZkQ71THDiYz0nzSxxfSIiv1WR1ibdfh4g8oyd6kyN7vyJeNlON8pr5ke6aErKZ0Sw?key=X3VGLphhBSvJq7pfJ6AeNA" alt=""><figcaption></figcaption></figure>

After enabling quarantining on Trunk Flaky Tests, future CI jobs with quarantining enabled on the Analytics Uploader will begin quarantining failed flaky tests.

**Update CI Jobs**

Before tests can be quarantined on a CI job, the test command needs to be run via the Analytics Uploader through the `run: <COMMAND TO RUN TESTS>` parameter and have `quarantine: true`passed to the Analytics Uploader to enable quarantining.

With quarantining enabled, the Analytics Uploader will compare failed test cases against known flaky tests. If a test is known to be flaky, it will be quarantined. If all failed tests are flaky then the exit code of the test command will be overridden to return 0 which means the CI job will pass.

Here is an example of a GitHub workflow:

```yaml
name: Upload Test Results to Trunk
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
        continue-on-error: true
        quarantine: true
        run: <COMMAND TO RUN TESTS>
        env:
          token: ${{ secrets.TRUNK_API_TOKEN }}
          org-slug: my-trunk-org-slug
        with:
          junit-paths: <TEST OUTPUT PATH>

      - name: Upload results
        uses: trunk-io/analytics-uploader@main
        if: "!cancelled()"
```

#### Overriding Individual Tests

If you have tests that should never be quarantined or should always be quarantined regardless of their current health status, you can do this through overriding individual tests.

<figure><img src="../.gitbook/assets/Enable Override Quarantining (1).png" alt=""><figcaption></figcaption></figure>

You can update the overriding settings on each test by navigating to the details page for a specific test and clicking the Quarantining (Repo Default) selector in the top left corner.&#x20;

You can choose between one of three override settings:

<table data-header-hidden><thead><tr><th width="244"></th><th></th></tr></thead><tbody><tr><td>Setting</td><td>Behavior</td></tr><tr><td>Repo Default</td><td>Quarantining behavior follows the repository settings. <br><br><a href="quarantining.md#quarantining-modes">Learn more about quarantining modes</a></td></tr><tr><td>Always Quarantine </td><td>Quarantine a test failure even if the health status is healthy or broken.</td></tr><tr><td>Never Quarantine</td><td>Never quarantine failures, even if the health status is flaky and quarantining is enabled for the repo.</td></tr></tbody></table>

#### Audit Logs

Trunk provides audit logs for all setting changes and overwrites for individual tests. You can access the audit log by navigating to **Settings** > **Repositories** > **Flaky Tests** > **Quarantine Flaky Tests** > **Audit logs**.

<figure><img src="../.gitbook/assets/Audit log (2).png" alt=""><figcaption></figcaption></figure>
