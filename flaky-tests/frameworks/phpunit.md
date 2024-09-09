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

PHPUnit is a testing framework for Php.

### Enabling XML Output
PHPUnit can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by adding the `--log-junit` argument to your command line.  ex:

```undefined
phpunit --log-junit output.xml
```
will produce XML output in the `output.xml` file.



### Test Suite Naming

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


## Further Information
See an example of PHPUnit invoked from a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/php.yaml).


