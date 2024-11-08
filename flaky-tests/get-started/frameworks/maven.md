---
title: Configuring maven
description: Maven is a build and testing tool for Java projects
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Maven

## How to output test results to upload to Trunk

When a Maven project is tested with `mvn test` it does not automatically produce [JUnit XML](https://github.com/testmoapp/junitxml) output. You can enable XML output that Trunk can ingest with the [Surefire plugin](https://maven.apache.org/surefire/maven-surefire-plugin/). To enable it, add the following to the `plugins` section of your `pom.xml` file. This process is the same whether you use test using JUnit or TestNG.

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.3.1</version>
</plugin>
```

and then run

```shell
mvn test
```

The output will be in the `target/surefire-reports` directory.

## Test Suite Naming

You can change the output filename with the `<reportsDirectory>` property.

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-report-plugin</artifactId>
  <version>3.3.1</version>
  <configuration>
    <reportsDirectory>coolthing</reportsDirectory>
  </configuration>
</plugin>
```

You can see a full list of configuration options [here](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html#reportsDirectory).

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.

