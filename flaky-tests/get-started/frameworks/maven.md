---
title: Configuring maven
description: A guide for generating Trunk-compatible test reports for Maven
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

# Maven

You can automatically [detect and manage flaky tests](../../detection.md) in your Maven projects by integrating with Trunk. This document explains how to configure Maven to output JUnit XML reports that can be uploaded to Trunk for analysis.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Maven uses the `maven-surefire-plugin` by default to output JUnit XML reports, which is Trunk compatible. You can configure the plugin in your project's `pom.xml`.&#x20;

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

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests. You should disable retries for accurate detection and use the [Quarantining](../../quarantining.md) feature to stop flaky tests from failing your CI jobs.

Maven uses the `maven-surefire-plugin` to run tests, which allows you to control the test retry behavior. You can disable retries by specifying 0 retries:

```
mvn -Dsurefire.rerunFailingTestsCount=0 test
```

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

