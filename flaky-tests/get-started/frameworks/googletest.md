---
description: A guide for generating Trunk-compatible test reports for GoogleTest
---

# GoogleTest

You can automatically [detect and manage flaky tests](../../detection/) in your GoogleTest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before you can integrate with Trunk, you need to generate a Trunk-compatible report. For GoogleTest, the built in XML reporter will work. You can use the [`--gtest_output=xml`](https://google.github.io/googletest/advanced.html#generating-an-xml-report) argument when you run your built test project:

```shell
./build/run_test --gtest_output=xml
```

#### Report File Path

By default, the JUnit report will be written to a `test_detail.xml` file.

You can specify a custom directory and filename with:

```bash
--gtest_output=xml:<path/to/file.xml>
```

For example, the following argument writes a JUnit report to `./junit.xml`:

```bash
--gtest_output=xml:junit.xml
```

{% include "../../../.gitbook/includes/retries.md" %}

Omit the[ ](https://docs.pytest.org/en/stable/how-to/cache.html)[`--gtest_repeat`](https://google.github.io/googletest/advanced.html#repeating-the-tests) argument if you've previously configured your CI with these options to disable retries.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
