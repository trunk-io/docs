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

## 1. Generate JUnit

Configure the `maven-surefire-plugin` plugin in your `pom.xml` file:

{% code title="pom.xml" %}
```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>2.22.0</version>
      <dependencies>
        <dependency>
          <groupId>org.apache.maven.surefire</groupId>
          <artifactId>surefire-junit4</artifactId>
          <version>2.22.0</version>
        </dependency>
      </dependencies>
      <configuration>
        <includes>
          <include>**/*.java</include>
        </includes>
      </configuration>
    </plugin>
  </plugins>
</build>
```
{% endcode %}

## 2. Output Location

The JUnit report will be in the `target/surefire-reports` directory.

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

If you're using the Surefire Plugin to retry tests, you can disable it by omitting the `-Dsurefire.rerunFailingTestsCount` option.

## Next Step

JUnit files generated with Maven are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
