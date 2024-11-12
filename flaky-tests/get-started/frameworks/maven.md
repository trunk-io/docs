---
title: Configuring maven
description: A guide for generating JUnit test reports for Maven tests
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

Configure the `maven-surefire-plugin` plugin in your pom.xml file:

<pre class="language-xml" data-title="pom.xml"><code class="lang-xml"><strong>&#x3C;build>
</strong>  &#x3C;plugins>
    &#x3C;plugin>
      &#x3C;groupId>org.apache.maven.plugins&#x3C;/groupId>
      &#x3C;artifactId>maven-surefire-plugin&#x3C;/artifactId>
      &#x3C;version>2.22.0&#x3C;/version>
      &#x3C;dependencies>
        &#x3C;dependency>
          &#x3C;groupId>org.apache.maven.surefire&#x3C;/groupId>
          &#x3C;artifactId>surefire-junit4&#x3C;/artifactId>
          &#x3C;version>2.22.0&#x3C;/version>
        &#x3C;/dependency>
      &#x3C;/dependencies>
      &#x3C;configuration>
        &#x3C;includes>
          &#x3C;include>**/*.java&#x3C;/include>
        &#x3C;/includes>
      &#x3C;/configuration>
    &#x3C;/plugin>
  &#x3C;/plugins>
&#x3C;/build>
</code></pre>

## 2. Output Location

The JUnit report will be in the `target/surefire-reports` directory.

## Next Step

JUnit files generated with Maven are compatible with Trunk Flaky Tests. See [CI Providers](../ci-providers/) for a guide on how to upload test results to Trunk.

