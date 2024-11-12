---
title: Configuring android
description: A guide for generating JUnit test reports for Android projects
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

# Android

## 1. Generate JUnit

All Android tests run with `./gradlew` will generate JUnit XML output.

## 2. Output Location

### ./gradlew test

Output from `./gradlew test` will be written to

`path_to_your_project/module_name/build/test-results/`

### ./gradlew connectedAndroidTest

Output from `./gradlew connectedAndroidTest` will be written to

`path_to_your_project/module_name/build/test-results/connected/`

## Next Step

JUnit test reports for Android projects are compatible with Trunk Flaky Tests. See [[ci-providers](../ci-providers/ "mention")](../ci-providers/) for instructions to upload them to Trunk.
