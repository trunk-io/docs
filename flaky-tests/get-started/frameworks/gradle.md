---
description: A guide for generating Trunk-compatible test reports for Gradle
---

# Gradle

You can automatically [detect and manage flaky tests](../../detection/) in your Gradle projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Tests run with Gradle will generate JUnit XML reports by default and are compatible with Trunk. You can further [configure reporting behavior](https://docs.gradle.org/8.10.2/userguide/java_testing.html#test_reporting) in your `build.gradle.kts` or `build.gradle`.

#### Report File Path

By default, Android projects will produce a directory with JUnit XML reports under `./app/build/test-results/test`. You can locate these files with the glob `"./app/build/test-results/test/*.xml"`.

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

{% include "../../../.gitbook/includes/retries.md" %}

If you've enabled retries using a plugin like the [test-retry-gradle-plugin](https://github.com/gradle/test-retry-gradle-plugin), disable it when running tests for Trunk Flaky Tests.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
