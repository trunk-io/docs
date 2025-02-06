---
description: A guide for generating Trunk-compatible test reports for Gradle
---

# Gradle

## 1. Generate JUnit

JUnit tests run with Gradle will produce a JUnit XML output by default. However, you need to enable output per test case and merge reruns. Here's an example:

{% code title="build.gradle.kts" %}
```kotlin
tasks.test {
    useJUnitPlatform()
    testLogging {
        events("passed", "skipped", "failed")
    }
    reports {
        junitXml.apply {
            isOutputPerTestCase = true // defaults to false
            mergeReruns = true // defaults to false
            outputLocation = file("output/test-results")
        }
    }
}
```
{% endcode %}

## 2. Output Location

The JUnit report will be in the `output/test-results` directory.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

## Next Step

JUnit files generated with Gradle are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
