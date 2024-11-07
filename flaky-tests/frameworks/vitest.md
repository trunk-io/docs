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

## How to output test results to upload to Trunk

Vitest can produce JUnit XML output that Trunk can ingest using the built in `junit` reporter command line option.

```shell
vitest --reporter=junit --outputFile=report.xml
```

Typically you will do this in the package.json script that runs your tests, like this:

```json
"scripts": {
  "vitest": "vitest run --dir test --reporter=junit --outputFile=./report.xml",
}
```

For more details see the [Vitest reporter docs](https://vitest.dev/guide/reporters).

## Test Suite Naming

The generated XML contains nested `testsuites` and `testcase` tags. You can use the environment variables `VITEST_JUNIT_SUITE_NAME` and `VITEST_JUNIT_CLASSNAME` to configure their `name` and `classname` attributes, respectively. These can also be customized via reporter options:

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

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
