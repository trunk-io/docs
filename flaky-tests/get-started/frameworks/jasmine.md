---
title: Configuring jasmine
description: Jasmine is a test runner and testing framework for Javascript and Typescript
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

# Jasmine

## How to output test results to upload to Trunk

You can configure Jasmine to produce [JUnit XML](https://github.com/testmoapp/junitxml) that Trunk can ingest by installing the [`jasmine-reporters`](https://www.npmjs.com/package/jasmine-reporters) package:

```shell
npm install --save-dev jasmine-reporters
```

Next, create an instance of a `JUnitXMLReporter` to the top of your test file and add it to your Jasmine environment.

```javascript
import reporters from "jasmine-reporters";

var junitReporter = new reporters.JUnitXmlReporter({
  savePath: "tests/jasmine/reports",
  consolidateAll: false,
});
jasmine.getEnv().addReporter(junitReporter);

describe("HuntingSeason", () => {
  it("Bugs - `Duck Season`", () => {
    const season = new Season();
    expect(season.getCurrent()).toEqual("Duck");
  });

  it("Daffy - `Rabbit Season`", () => {
    const season = new Season();
    expect(season.getCurrent()).toEqual("Rabbit");
  });
});
```

With this configuration, Jasmine will output an xml file in the `tests/jasmine/reports` directory.

## Test Suite Naming

Jasmine will use the test suite names for the file name and xml attributes by combining them with the `JUnitXmlReporter` settings. For example with the `savePath` set to `"tests/jasmine/reports"` the test suite named `"HuntingSeason"` will output to the file `"tests/jasmine/reports/junitresults-HuntingSeason.xml".`

The names of the test suites can be modified by providing a `modifySuiteName()` function. See [the official docs](https://www.npmjs.com/package/jasmine-reporters#multi-capabilities) for details. Unfortunately this reporter does not support adding the `file` attribute to the XML.

See an example of running Jasmine inside of a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/javascript-tests.yaml#L56).

## Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.
