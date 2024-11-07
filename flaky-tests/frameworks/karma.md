---
title: Configuring karma
description: Karma is a browser test runner for Javascript
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

# Karma

## How to output test results to upload to Trunk

Karma can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output that Trunk can ingest by adding the [`karma-junit-reporter`](https://www.npmjs.com/package/karma-junit-reporter) package to your codebase.

```shell
npm install --save-dev karma-junit-reporter
```

Also add the `junit` reporter to your karma config file. ex:

```javascript
reporters: ['progress','junit'],
```

Now run Karma from the command line or inside your CI system as:

```shell
karma start <your-config.cjs>
```

## Test Suite Naming

The XML output can be customized by adding a `junitReporter` section to your Karma config file. You can set the name of the test suite using the `suite` attribute. You can customize the output directory and output file name using the `outputDir` and `outputFile` attributes. Names and classnames can be customized by providing formatter functions. Ex:

```javascript
junitReporter:{
  outputDir: 'test-output',
  outputFile:'karma-output.xml',
  suite:'my-test-suite',
  useBrowserName:false,
  // function (browser, result) to customize the name attribute in xml testcase element
  nameFormatter: function(browser, result) { return "cool-name"}, 
  // function (browser, result) to customize the classname attribute in xml testcase element
  // classNameFormatter: undefined,
  classNameFormatter: function(browser,result) { return "cool-class-name" }
}
```

## Next Step <a href="#next-step" id="next-step"></a>

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [CI Providers](../ci-providers/) for instructions to do this for the CI system you use.

\
