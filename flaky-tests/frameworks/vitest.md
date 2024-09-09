---
title: Configuring vitest
description: Vitest is a testing framework for JavaScript and TypeScript applications
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

# Vitest

Vitest is a testing framework for JavaScript.

### Enabling XML Output

Configure Vitest to produce JUnit XML output using the built in `junit` reporter command line option.

```shell
vitest --reporter=junit --outputFile=test-output.xml
```
Typically you will do this in the package.json script that runs your tests, like this:

```json
"scripts": {
  "vitest": "vitest run --dir test --reporter=junit --outputFile=./test-output.xml",
}
```
For more details see the [Vitest reporter docs](https://vitest.dev/guide/reporters).



### Test Suite Naming

The generated XML contains nested `testsuites` and `testcase` tags. You can use the environment variables `VITEST_JUNIT_SUITE_NAME` and `VITEST_JUNIT_CLASSNAME` to configure their `name` and `classname` attributes, respectively. These can also be customized via reporter options:

```typescript
export default defineConfig({
  test: {
    reporters: [
      ['junit', { suiteName: 'custom suite name', classname: 'custom-classname' }]
    ]
  },
})
```
For more details see the [Vitest JUnit Reporter docs](https://vitest.dev/guide/reporters#junit-reporter).





