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

## How to output test results to upload to Trunk

Mocha can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by adding the [`mocha-junit-reporter`](https://www.npmjs.com/package/mocha-junit-reporter) package to your codebase.

```shell
npm install --save-dev mocha-junit-reporter
```

Now run Mocha from the command line or inside your CI system as:

```shell
mocha test --reporter mocha-junit-reporter
```

## Test Suite Naming

The `mocha-junit-reporter` will automatically fill in values for the `<testcase/>` and `<testsuite/>` `name` and `class` attributes. The test:

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

The default attributes [can be configured](https://www.npmjs.com/package/mocha-junit-reporter) with the `reporterOptions` argument in the `.mocharc.js` or [similar config file.](https://mochajs.org/#configuring-mocha-nodejs)

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

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
