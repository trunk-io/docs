---
description: A guide for generating Trunk-compatible test reports for Nightwatch
---

# Nightwatch

## 1. Generate JUnit

Nightwatch will report test results in multiple formats automatically. You can configure the output location by updating the `nightwatch.conf.cjs` config file.

```javascript
module.exports = {
  output_folder: 'junit',
  ...
}
```

You can also specify output at runtime with the command line option `--output <OUTPUT_FOLDER>`:

```sh
nightwatch --output ./junit
```

## 2. Output Location

Nightwatch outputs multiple reports for each test suite under the specified output folder.

If you configured your output folder to be `./junit`, the JUnit XML files will be found under `./junit/**`. You can upload multiple JUnit reports by using a glob like \``./junit/**/*.xml`.

{% hint style="warning" %}
**Duplicate Uploads**

When using globs, it's important to clean up old test reports between test runs. If your glob path contains old JUnit files, uploading old test results can cause tests to be mislabeled.
{% endhint %}

## Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.

Nightwatch doesn't implement any form of automatic retry for failed or flaky tests by default. If you have a custom implementation of retries, remember to disable them.

## Next Step

JUnit files generated with Nightwatch are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
