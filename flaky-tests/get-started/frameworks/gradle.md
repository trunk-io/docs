---
description: A guide for generating Trunk-compatible test reports for Gradle
---

# Gradle

You can automatically [detect and manage flaky tests](../../detection.md) in your Gradle projects by integrating with Trunk. This document explains how to configure Gradle to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Tests run with Gradle will generate JUnit XML reports by default and are compatible with Trunk. You can further [configure reporting behavior](https://docs.gradle.org/8.10.2/userguide/java_testing.html#test_reporting) in your `build.gradle.kts` or `build.gradle`.

#### Report File Path

By default, Android projects will produce a directory with JUnit XML reports under `./app/build/test-results/test`. You can locate these files with the glob `"./app/build/test-results/test/*.xml"`.  &#x20;

If you wish to override the default test result path, you can do so in the `build.gradle.kts` or `build.gradle` files:

{% tabs %}
{% tab title="Groovy" %}
{% code title="build.gradle" %}
```groovy
java.testResultsDir = layout.buildDirectory.dir("junit-reports")
```
{% endcode %}
{% endtab %}

{% tab title="Kotlin" %}
{% code title="build.gradle.kts" %}
```kotlin
java.testResultsDir = layout.buildDirectory.dir("junit-reports")
```
{% endcode %}
{% endtab %}
{% endtabs %}

This example will write report files to `"./app/build/junit-reports/test/*.xml"`

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you've enabled retries using a plugin like the [test-retry-gradle-plugin](https://github.com/gradle/test-retry-gradle-plugin), disable it when running tests for Trunk flaky tests.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./app/build/junit-reports/test/*.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./app/build/junit-reports/test/" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

{% include "../../../.gitbook/includes/you-can-find-your-trunk-org....md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}

