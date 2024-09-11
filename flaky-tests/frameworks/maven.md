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

Maven is a testing framework for Java.

### Enabling XML Output

When a Maven project is tested with `mvn test` it does not automatically produce [JUnit XML](https://github.com/testmoapp/junitxml) output. You can enable XML output with the [Surefire plugin](https://maven.apache.org/surefire/maven-surefire-plugin/).  To enable it, add the following to the `plugins` section of your `pom.xml` file.

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

### Test Suite Naming

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

## Further Information

See an example of running Maven inside of a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/java-tests.yaml#L34).
