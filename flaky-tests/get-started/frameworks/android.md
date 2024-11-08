---
title: Configuring android
description: Android unit test framework with JUnit 4 and Espresso run with Gradle.
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

# Android

## How to output test result to upload to Trunk

Android tests run with Gradle will generate JUnit XML output that Trunk can ingest by default.

There are two output paths depending on the type of tests that are run. Local unit test results will be in `/path_to_your_project/module_name/build/test-results/`and instrumented unit test results will be in `path_to_your_project/module_name/build/test-results/connected/`.

See the [Android Developer Docs](https://developer.android.com/studio/test/command-line) for more info.

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [ci-providers](../ci-providers/ "mention") for instructions to do this for the CI system you use.
