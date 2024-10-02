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

Karma is a testing framework for JavaScript.

### Enabling XML Output

Karma can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by adding the [`karma-junit-reporter`](https://www.npmjs.com/package/karma-junit-reporter) package to your codebase.

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

### Test Suite Naming

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
},
```


