---
description: >-
  Prevent false flaky test detections during CI outages and infrastructure
  failures.
---

# Infrastructure Failure Protection

When infrastructure issues like database outages, network problems, or CI runner failures cause a large number of tests to fail simultaneously, retrying those tests can trigger mass false flaky detections. Infrastructure Failure Protection identifies these scenarios and excludes them from flakiness detection.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### How it works

Trunk monitors the failure rate of each test upload. If the percentage of failing tests exceeds your configured threshold, that upload is flagged as an infrastructure failure and excluded from flaky test detection.

For example, if your threshold is set to 80% and a CI run has 85% of tests failing (this could be due to a database being unavailable or similar infrastructure issue, etc) that entire run will be excluded from flaky test detection. This prevents tests from being incorrectly marked as flaky when they're retried and pass.

{% hint style="info" %}
Uploads excluded due to infrastructure failure protection will appear in the **Uploads** tab with the status **"Upload Skipped Due to Infrastructure Error."**
{% endhint %}

### Configuring Infrastructure Failure Protection

Administrators can enable this feature in repository settings:

1. Click on your profile and open **Settings**
2. Select your repository from the left navigation
3. Locate **Infrastructure Failure Protection** under Flaky Tests
4. Toggle **Enable Protection** to on
5. Set your **Failure Threshold** percentage (default: 80%)

The threshold determines what percentage of test failures triggers infrastructure failure detection. A threshold of 80% is a reasonable starting point for most repositories—adjust based on your test suite size and typical failure patterns.

### Trade-offs

When a test upload is excluded due to infrastructure failure protection:

**Uploads are still recorded:**

* The upload appears in the Uploads tab with "Upload Skipped Due to Infrastructure Error" status

**Failures are excluded from analysis:**

* Failures do not impact flakiness detection
* Failures do not contribute to failure rate metrics
* Stack traces from that run are not visible in test case history

This is generally an acceptable trade-off since infrastructure failures don't reflect the actual behavior of individual test cases.

### When to use this

Enable Infrastructure Failure Protection if you experience:

* Database or service outages that cause mass test failures
* CI runner infrastructure issues
* Network failures during test runs
* Any scenario where a large percentage of tests fail for reasons unrelated to code changes

If you're using test quarantine, this feature is especially important to prevent infrastructure issues from automatically quarantining large numbers of tests.

### Next steps

* Learn more about how Trunk [detects flaky tests](detection.md)
* View excluded uploads in the Uploads tab
* Configure [test quarantine](quarantining.md#enable-quarantining) to automatically skip flaky tests

