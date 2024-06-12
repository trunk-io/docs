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

Cypress is a testing framework for Webapps.

## Enabling XML Output

Cypress can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by adding the [mocha-junit-reporter](https://github.com/michaelleeallen/mocha-junit-reporter) package to your codebase and modify the config file to add it as a reporter.

```shell
npm install --save-dev mocha-junit-reporter
```

`cypress.config.js` or [similar file](https://docs.cypress.io/guides/references/configuration).

```javascript
const { defineConfig } = require('cypress')
module.exports = defineConfig({
  reporter: 'junit',
  reporterOptions: {
    mochaFile: 'results/my-test-output.xml',
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

The `mocha-junit-reporter` will automatically fill in values for the and `name` and `class` attributes.&#x20;

```javascript
describe('addition', () => {
  describe('positive numbers', () => {
    it('should add up', () => {
      expect(1 + 2).toBe(3);
    });
  });
});
```

would produce output that looks like this:

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
