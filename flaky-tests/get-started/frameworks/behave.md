---
description: A guide for generating Trunk-compatible test reports for Behave
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Behave

## 1. Generate JUnit

Add the [`--junit`](https://behave.readthedocs.io/en/latest/behave/#cmdoption-junit) option to your `behave` command to generate separate JUnit XML reports for every `.feature` file in your repo:

```shell
behave --junit
```

## 2. Output Location

JUnit reports will be written to a `reports` directory in your project root by default. You can modify this location using the [`--junit-directory`](https://behave.readthedocs.io/en/latest/behave/#cmdoption-junit-directory) option.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

You must remove the [rerun formatter](https://behave.readthedocs.io/en/latest/formatters/#formatters) from your `behave.ini` file if it is being used to automatically rerun failed tests.

## Next Step

JUnit files generated with Behave are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk. Multiple JUnit XML files should be uploaded together using a file glob or comma-separated list.
