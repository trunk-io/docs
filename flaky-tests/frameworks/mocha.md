---
title: Configuring mocha
description: Mocha is a Javascript testing framework that can be configured to output XML
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

# Mocha

Mocha is a testing framework for JavaScript and TypeScript.

### Enabling XML Output

Mocha can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by adding the [`mocha-junit-reporter`](https://www.npmjs.com/package/mocha-junit-reporter)  package to your codebase.

```shell
npm install --save-dev mocha-junit-reporter
```
Now run Mocha from the command line or inside your CI system as:

```shell
mocha test --reporter mocha-junit-reporter
```

### Test Suite Naming

The `mocha-junit-reporter` will automatically fill in values for the _<testcase>_ and _<testsuite>_ `name` and `class` attributes. The test:

```javascript
describe('addition', () => {
  describe('positive numbers', () => {
    it('should add up', () => {
      expect(1 + 2).toBe(3);
    });
  });
});
```
will produce output that looks like this:

```xml
<testsuites name="Mocha Tests">
  <testsuite name="addition">
    <testcase classname="addition positive numbers should add up" 
              name="addition positive numbers should add up"
              file="/somepath/tests/mocha/mocha.test.js"
              >
    </testcase>
  </testsuite>
</testsuites>
```
The default attributes [can be configured](https://www.npmjs.com/package/mocha-junit-reporter) with the `reporterOptions` argument in the  `.mocharc.js` or [similar config file.](https://mochajs.org/#configuring-mocha-nodejs)

```javascript
var mocha = new Mocha({
    reporter: 'mocha-junit-reporter',
    reporterOptions: {
        testsuitesTitle: true,
        // suites separator, default is space (' ')
        suiteTitleSeparatedBy: '.' 
    }
});
```
By default Mocha will include the `file` attribute.

## Further Information

See an example of MochaJS invoked form a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/javascript-tests.yaml#L29).
