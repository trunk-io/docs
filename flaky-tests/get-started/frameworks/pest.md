---
description: A guide for generating Trunk-compatible test reports for Pest
---

# Pest

## 1. Generate JUnit

Append `--log-junit junit.xml` to your `pest` test command:

```undefined
./vendor/bin/pest --log-junit junit.xml
```

## 2. Output Location

The JUnit report is written to the location specified by `--log-junit`. In the example above, the test results will be written to `./`junit.xml.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Pest doesn't support retries out of the box, but if you implemented retries, remember to disable them.

## Next Step

JUnit files generated with Pest are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
