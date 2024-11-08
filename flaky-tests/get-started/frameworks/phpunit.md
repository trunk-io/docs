---
title: Configuring phpunit
description: PHPUnit is a unit testing framework for PHP
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

# PHPUnit

## How to output test results to upload to Trunk

PHPUnit can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by adding the `--log-junit` argument to your command line.

```undefined
phpunit --log-junit report.xml
```

will produce XML output in the `report.xml` file.

## Test Suite Naming

By default PHPUnit use the name of your PHP files as the `name` attribute of the output XML. For example, this test code

```php
final class EmailTest extends TestCase
{
    public function testCanBeCreatedFromValidEmail(): void
    {
        $string = 'user@example.com';
        ...
    }
}
```

will produce XML output that looks like this:

```xml
<testsuites>
  <testsuite tests="2">
    <testsuite name="Project" tests="2"  time="0.000969">
      <testsuite name="EmailTest" file=".../tests/EmailTest.php">
        <testcase name="testCanBeCreatedFromValidEmail" 
          file="...tests/EmailTest.php" 
          line="6" 
          class="EmailTest" 
          classname="EmailTest" 
          assertions="1" 
          time="0.000803"/>
...
```

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
