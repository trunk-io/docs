---
title: Configuring maven
description: A guide for generating Trunk-compatible test reports for Maven
---

# Maven

You can automatically [detect and manage flaky tests](../../detection/) in your Maven projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Maven uses the `maven-surefire-plugin` by default to output JUnit XML reports, which is Trunk compatible. You can configure the plugin in your project's `pom.xml`.

#### Report File Path

You can change the report file path by configuring the `maven-surefire-plugin` plugin in your `pom.xml` file:

{% code title="pom.xml" %}
```xml
<project>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.2</version>
                <configuration>
                    <reportsDirectory>${project.build.directory}/junit/</reportsDirectory>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

The example above will output JUnit XML reports that can be located with the `/target/junit/*.xml` glob.

#### Using Kotlin and Kotest

If you have a Kotlin project and are using the Kotest test framework, you also need to include `kotest-extensions-junitxml` in your project's `pom.xml`. This allows Kotest to generate JUnit XML reports.

{% code title="pom.xml" %}
```xml
<dependency>
    <groupId>io.kotest</groupId>
    <artifactId>kotest-extensions-junitxml-jvm</artifactId>
    <version>5.9.0</version>
    <scope>test</scope>
</dependency>
```
{% endcode %}

{% include "../../../.gitbook/includes/retries.md" %}

Maven uses the `maven-surefire-plugin` to run tests, which allows you to control the test retry behavior. You can disable retries by specifying 0 retries:

```
mvn -Dsurefire.rerunFailingTestsCount=0 test
```

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
