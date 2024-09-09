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

Android is a testing framework for Android, Kotlin and Java.

### Enabling XML Output
Android tests run with Gradle generate XML output by default.

There are two output paths depending on the type of tests that are run.
Local unit test results will be in `/path_to_your_project/module_name/build/test-results/`and instrumented unit test results will be in `path_to_your_project/module_name/build/test-results/connected/`. 

See the [Android Developer Docs](https://developer.android.com/studio/test/command-line) for more info.



### Test Suite Naming

 







