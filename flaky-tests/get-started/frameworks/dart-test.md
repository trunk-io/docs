---
description: A guide for generating Trunk-compatible test reports for Dart tests
---

# Dart Test

## 1. Generate JUnit

Before you can upload to Trunk, you need to convert the reported test results to a Trunk-compatible format. Dart supports JUnit outputs by using the `tojunit` library. You can install the `tojunit` library using the following command:

```sh
dart pub global activate junitreport
```

Then, you can convert test reports to a JUnit format by piping it to `tojunit`and piping the output to a file like this:&#x20;

```sh
dart test <TEST_PATH> --reporter json | tojunit > junit.xml
```

## 2. Output Location

The JUnit report is written to the location specified by `--log-junit`. In the example above, the test results will be written to `./junit.xml`.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Dart `test` doesn't support retries out of the box, but if you implemented retries, remember to disable them.

## Next Step

JUnit test reports for Dart projects are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
