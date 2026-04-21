---
description: A guide for generating Trunk-compatible test reports for Kotest
---

# Kotest

You can automatically [detect and manage flaky tests](../../detection/) in your Kotest projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Steps for generating JUnit XML reports for Kotest depend on the build system you use for your project:

{% tabs %}
{% tab title="Gradle" %}
Tests run with Gradle will generate Trunk-compatible JUnit XML reports by default. You can further [configure reporting behavior](https://docs.gradle.org/8.10.2/userguide/java_testing.html#test_reporting) in your `build.gradle.kts` or `build.gradle`.
{% endtab %}

{% tab title="Maven" %}
Kotest projects using Maven require the following to be added to a project's `pom.xml` so JUnit XML reports can be generated:

* the `maven-surefire-plugin` must be added to the `plugins` section of `pom.xml`

{% code title="pom.xml" %}
```xml
<project>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.2</version>
            </plugin>
            
            <!-- other plugins -->
        </plugins>
    </build>
</project>
```
{% endcode %}

* the `kotest-extensions-junitxml` must be added to the `dependencies` section of `pom.xml`

{% code title="pom.xml" %}
```xml
<dependencies>
    <dependency>
        <groupId>io.kotest</groupId>
        <artifactId>kotest-extensions-junitxml-jvm</artifactId>
        <version>5.9.0</version>
        <scope>test</scope>
    </dependency>
    
    <!-- other dependencies -->
</dependencies>
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Report File Path

You can configure the path for generated JUnit XML files:

{% tabs %}
{% tab title="Gradle" %}
By default, Kotlin projects will produce a directory with JUnit XML reports under `./app/build/test-results/test`. You can locate these files with the glob `"./app/build/test-results/test/*.xml"`.

If you wish to override the default test result path, you can do so in the `build.gradle.kts` or `build.gradle` files:

{% code title="build.gradle.kts (Kotlin) or build.gradle (Groovy)" %}
```kotlin
java.testResultsDir = layout.buildDirectory.dir("junit-reports")
```
{% endcode %}
{% endtab %}

{% tab title="Maven" %}
You can change the report file path by configuring the `reportsDirectory` in your `maven-surefire-plugin` in your `pom.xml` file:

{% code title="pom.xml" %}
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.2</version>
    <configuration>
        <reportsDirectory>${project.build.directory}/junit/</reportsDirectory>
    </configuration>
</plugin>
```
{% endcode %}

The example above will output JUnit XML reports that can be located with the `/target/junit/*.xml` glob.
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/retries.md" %}

{% tabs %}
{% tab title="Gradle" %}
If you've enabled retries using a plugin like the [test-retry-gradle-plugin](https://github.com/gradle/test-retry-gradle-plugin), disable it when running tests for Trunk Flaky Tests.
{% endtab %}

{% tab title="Maven" %}
Maven uses the `maven-surefire-plugin` to run tests, which allows you to control the test retry behavior. You can disable retries by specifying 0 retries:

```
mvn -Dsurefire.rerunFailingTestsCount=0 test
```
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
