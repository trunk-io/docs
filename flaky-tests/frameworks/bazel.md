---
title: Configuring bazel
description: Bazel is a scalable build and test system
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Bazel

### How to upload test results to Trunk

By default `bazel test` will output JUnit compatible XML that Trunk can ingest. By default the XML output will go to `./bazel-testlogs/TEST_NAME/test.xml` along with the other test outputs. This cannot be changed.

## Test Suite Naming

By default `bazel test` will produce XML output in a file named `test.xml`. This cannot be customized.

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](https://docs.trunk.io/flaky-tests/ci-providers) for instructions to do this for the CI system you use.

\


