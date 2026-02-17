---
description: How Trunk uniquely identifies and tracks test cases across CI runs
---

# How test identification works

Trunk tracks the health of every test case across all your CI runs. To do this, it generates a **unique test ID** for each test based on attributes in your JUnit XML reports. Understanding how test identification works helps you avoid common issues like duplicate tests, missing history, or unexpected "new" test cases appearing in your dashboard.

### What makes a test unique

Trunk identifies each test case using a combination of attributes from your JUnit XML reports:

| Attribute     | JUnit XML field         | Description                                              | Example                              |
| ------------- | ----------------------- | -------------------------------------------------------- | ------------------------------------ |
| **Test name** | `<testcase name="...">` | The name of the individual test                          | `test_user_login`                    |
| **Classname** | `<testcase classname="...">`  | The test class or suite the test belongs to              | `AuthTests`                          |
| **File path** | `<testcase file="...">`       | The file where the test is defined                       | `tests/auth/test_login.py`           |
| **Variant**   | CLI `--variant` flag    | Optional label for environment-specific tracking         | `ios`, `chrome`, `python3.11`        |

These four attributes are combined to create a stable, unique identifier for each test. If any of these values change, Trunk treats it as a **different test case** with its own history.

{% hint style="warning" %}
**Common pitfall:** If you add a `file` attribute to your JUnit XML output (for example, by changing a pytest flag or JUnit reporter configuration), Trunk will see these as new test cases because the unique ID has changed. Your previous test history will not carry over automatically.
{% endhint %}

### Why this matters

Understanding test identification helps you:

* **Avoid duplicates:** If the same test appears with different classnames across CI runs (for example, due to parameterized test names), Trunk will track them as separate tests.
* **Preserve history:** Renaming a test file, moving a test to a different class, or changing the test name will start a new history for that test.
* **Use variants correctly:** If you run the same tests on multiple platforms (e.g., iOS and Android), use the `--variant` flag to track them separately. Without variants, results from different environments are merged into one test, making flake detection less accurate.

### Example: JUnit XML mapping

Here is an example JUnit XML test case and how Trunk maps it:

```xml
<testcase name="test_user_can_login"
          classname="tests.auth.TestLogin"
          file="tests/auth/test_login.py"
          time="1.234">
  <failure message="AssertionError: expected 200, got 401">
    Traceback (most recent call last):
      File "tests/auth/test_login.py", line 42
    AssertionError: expected 200, got 401
  </failure>
</testcase>
```

Trunk generates the unique test ID from:

* **Name:** `test_user_can_login`
* **Classname:** `tests.auth.TestLogin`
* **File:** `tests/auth/test_login.py`
* **Variant:** _(none, unless specified via `--variant`)_

### Using variants for environment-specific tracking

If you run the same test suite across different environments, use the `--variant` flag during upload to keep their histories separate:

```bash
# Upload iOS test results
./trunk-analytics-cli upload \
    --junit-paths "test_output.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_API_TOKEN \
    --variant ios

# Upload Android test results
./trunk-analytics-cli upload \
    --junit-paths "test_output.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_API_TOKEN \
    --variant android
```

Variant names appear in brackets next to test names in your dashboard, making it easy to identify which environment is flaky.

[Learn more about variant-based detection -->](../detection.md#use-variants-to-track-environment-specific-flakes)

### Troubleshooting test identification

<details>
<summary>Tests appear as "new" after a config change</summary>

If you changed your test framework configuration (for example, adding `junit_family=xunit1` to pytest), the JUnit XML output may now include attributes like `file` that were previously absent. This changes the unique test ID, so Trunk treats these as new tests.

**Resolution:** This is expected behavior. The new test cases will build up history from new CI runs. The old test cases will age out naturally.

</details>

<details>
<summary>Duplicate tests in the dashboard</summary>

This typically happens when:
- The same test is uploaded with different classnames across runs (inconsistent test configuration)
- Parameterized tests generate dynamic names that change between runs
- Test files are moved without cleaning up cached results

**Resolution:** Ensure your test framework configuration produces consistent names across runs. Avoid randomized test names or dynamic class generation.

</details>

<details>
<summary>Test history split after a file rename</summary>

Moving a test to a different file or renaming the file changes the `file` attribute in the JUnit XML, which changes the unique test ID.

**Resolution:** This is expected behavior. If you need to preserve continuity, consider whether the rename is necessary or whether you can alias the old path.

</details>

### Next steps

* [Validate your reports locally](../uploader.md#validating-reports-locally) before uploading to catch identification issues early
* [Configure uploads in CI](ci-providers/) to start tracking test health
