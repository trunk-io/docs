---
title: Configuring android
description: A guide for generating Trunk-compatible test reports for Android projects
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

You can automatically [detect and manage flaky tests](../../detection.md) in your Android projects by integrating with Trunk. This document explains how to configure Android to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Android tests run with Gradle, typically using  `./gradlew test` in CI. This will generate JUnit XML output by default, which you can further configure in your `build.gradle.kts` or `build.gradle`.

#### Report File Path

By default, Android projects will produce a directory with JUnit XML reports under `./app/build/test-results`.&#x20;

You can customize the report output location in your `build.gradle.kts` or `build.gradle`, for example, writing the reports to `./app/junit-reports`.&#x20;

{% tabs %}
{% tab title="Groovy" %}
```groovy
android {
    testOptions {
        unitTests {
            all {
                reports {
                    junitXml {
                        outputLocation = file("./junit-reports")
                    }
                }
            }
        }
    }
}
```
{% endtab %}

{% tab title="Kotlin" %}
```kotlin
android {
    testOptions {
        unitTests {
            all {
                reports {
                    junitXml.outputLocation.set(file(./junit-reports"))
                }
            }
        }
    }
}
```
{% endtab %}
{% endtabs %}

When you configure your CI provider to upload reports in later steps, you will be uploading the reports using a glob such as `./junit-reports/*.xml`.

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

If you've enabled retries using a plugin like the [test-retry-gradle-plugin](https://github.com/gradle/test-retry-gradle-plugin), disable it when running tests for Trunk flaky tests.

### Try It Locally

#### The Validate Command

You can validate your test reports using the [Trunk CLI](../../uploader.md). If you don't have it installed already, you can install and run the `validate` command like this:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests validate --junit-paths "./app/junit-reports/*.xml"
```

**This will not upload anything to Trunk**. To improve detection accuracy, you should **address all errors and warnings** before proceeding to the next steps.

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
./trunk flakytests upload --junit-paths "./app/junit-reports/*.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token <TRUNK_ORG_TOKEN>
```

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../.gitbook/includes/ci-providers.md" %}



