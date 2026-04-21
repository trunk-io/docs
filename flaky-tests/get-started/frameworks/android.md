---
title: Configuring android
description: A guide for generating Trunk-compatible test reports for Android projects
---

# Android

You can automatically [detect and manage flaky tests](../../detection/) in your Android projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating reports

Android tests run with Gradle, typically using `./gradlew test` in CI. This will generate JUnit XML output by default, which you can further configure in your `build.gradle.kts` or `build.gradle`.

#### Report file path

By default, Android projects will produce a directory with JUnit XML reports under `./app/build/test-results`.

You can customize the report output location in your `build.gradle.kts` or `build.gradle`, for example, writing the reports to `./app/junit-reports`.

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
                    junitXml.outputLocation.set(file("./junit-reports"))
                }
            }
        }
    }
}
```
{% endtab %}
{% endtabs %}

When you configure your CI provider to upload reports in later steps, you will be uploading the reports using a glob such as `./junit-reports/*.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

If you've enabled retries using a plugin like the [test-retry-gradle-plugin](https://github.com/gradle/test-retry-gradle-plugin), disable it when running tests for Trunk Flaky Tests.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
