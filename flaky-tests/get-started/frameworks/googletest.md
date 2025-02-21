---
description: A guide for generating Trunk-compatible test reports for GoogleTest
---

# GoogleTest

## 1. Generate JUnit

Use the [`--gtest_output=xml`](https://google.github.io/googletest/advanced.html#generating-an-xml-report) argument when you run your built test project:

```shell
./build/run_test --gtest_output=xml
```

## 2. Output Location

By default, the JUnit report will be written to a `test_detail.xml` file.

You can specify a custom directory and filename with:

```bash
--gtest_output=xml:<path/to/file.xml>
```

For example, the following argument writes a JUnit report to `test_output/junit.xml`:

```bash
--gtest_output=xml:test_output/junit.xml
```

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit the[ ](https://docs.pytest.org/en/stable/how-to/cache.html)[`--gtest_repeat`](https://google.github.io/googletest/advanced.html#repeating-the-tests) argument if you've previously configured your CI with these options to disable retries.

## Next Step

JUnit files generated with GoogleTest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
