---
title: Configuring bazel
description: A guide for generating Trunk-compatible test reports with Bazel
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

## 1. Generate Report&#x20;

Run the `bazel test` command with the options `--nobuild_event_json_file_path_conversion` and `--build_event_json_file=build_events.json`, which should output a JSON serialization of the [build event protocol](https://bazel.build/remote/bep).&#x20;

Trunk will parse this build event JSON file to access your test results.

## 2. Output Location

As specified by the `--build_event_json_file=build_events.json` option added in step 1, the output will be in  `build_events.json` in your current working directory.

When you later [configure your CI ](https://docs.trunk.io/flaky-tests/ci-providers)to upload to Trunk, you'll need to specify the path to your build events file with the `--bazel-bep-path=build_events.json` option instead of the `--junit-paths` for JUnit files.

## Disable Retries

You need to disable automatic retries if you previously enabled them for more accurate detection results.

Disable retries if you're retrying tests using the `--flaky_test_attempts` command line option or retrying in your test runner.

## Next Step

JUnit files generated with Bazel are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
