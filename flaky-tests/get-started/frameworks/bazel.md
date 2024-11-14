---
title: Configuring bazel
description: A guide for generating JUnit test reports with Bazel
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

# Bazel

## 1. Generate JUnit

The `bazel test` command outputs a JUnit for every test target in a test invocation.

## 2. Output Location

By default the JUnit output will be written to the `bazel-testlogs` output directory. The file containing JUnit is written to a directory with the same path as the test target.&#x20;

For example, a target named `//app/component:test` will generate a JUnit file at `bazel-testlogs/app/component/test.xml`.

## Next Step

JUnit files generated with Bazel are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
