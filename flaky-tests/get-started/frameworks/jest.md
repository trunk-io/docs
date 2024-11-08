---
title: Configuring jest
description: Jest is a Javascript testing framework that can be configured to output XML
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

# Jest

## How to output test results to upload to Trunk

Configure Jest to produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by installing the `jest-junit` module.&#x20;

```bash
npm install --save-dev jest-junit
```

Then update your Jest config (`jest.config.json` or [similar file)](https://jestjs.io/docs/configuration) to add `jest-junit` as a reporter.

`jest.config.json`

```json
{
  "reporters": [ 
    "default", 
    [ 
      "jest-junit", {
        "outputName":"report.xml",
      }
    ]
  ]
}
```

With this configuration, Jest runs will output a `report.xml` file in the working directory. To further configure the reporter, consult the [detailed documentation](https://github.com/jest-community/jest-junit) on GitHub.

## Test Suite Naming

The `jest-junit` reporter will automatically fill in values for the `<testcase/>` and `<testsuite/>` `name` and `class` attributes using the _description_ parameters to the tests. The `testsuites.name` is set to `jest tests` by default.

To make it easier to debug, it is also useful to include the name of the file that the failing test is in. You can do this by setting the `addFileAttribute` flag to true in your `jest.config.json` file.

```json
{
  "reporters": [ 
    "default", 
    [ 
      "jest-junit",
      {
        "outputDirectory":"tests/jest",
        "outputName":"report.xml",
        "addFileAttribute": "true"
      }
    ]
  ]
}
```

With the `addFileAttribute` flag set this test:

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
<testsuites name="jest tests">
  <testsuite name="addition">
    <testcase classname="addition positive numbers should add up" 
              name="addition positive numbers should add up"
              file="src/math.test.js"
              >
    </testcase>
  </testsuite>
</testsuites>
```

The default attributes can be changed using `jest-junit` [configuration settings](https://github.com/jest-community/jest-junit?tab=readme-ov-file#configuration).&#x20;

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
