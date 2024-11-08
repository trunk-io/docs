---
title: Configuring cypress
description: Cypress is a tool for testing dynamic web front end code.
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

# Cypress

## How to output test results to upload to Trunk

Cypress can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by adding the [mocha-junit-reporter](https://github.com/michaelleeallen/mocha-junit-reporter) package to your codebase and modifying the config file to add it as a reporter.

```shell
npm install --save-dev mocha-junit-reporter
```

Edit `cypress.config.js` or [similar file](https://docs.cypress.io/guides/references/configuration):

```javascript
const { defineConfig } = require('cypress')
module.exports = defineConfig({
  reporter: 'junit',
  reporterOptions: {
    mochaFile: 'report.xml',
  },
})
```

Now you can run Cypress from the command line with

```shell
cypress run
```

And from within your CI system the same way

```shell
cypress run
```

## Test Suite Naming

`mocha-junit-reporter` will automatically fill in values for the `<testcase/>` and `<testsuite/>` `name` and `class` attributes. A test suite like this:

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
              name="addition positive numbers should add up">
    </testcase>
  </testsuite>
</testsuites>
```

The default attributes [can be configured](https://www.npmjs.com/package/mocha-junit-reporter) with the `reporterOptions` argument in the Cypress config.

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.

\


