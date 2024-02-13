---
description: How to generate JUnit Reports for common test runners
---

# Generating JUnit Reports

## Jest

1. Install [`jest-junit`](https://github.com/jest-community/jest-junit).

```bash
$ npm install jest-junit --save-dev
```

2. Update your Jest config to use the `jest-junit` reporter.

```json
{
  "reporters": [ "default", "jest-junit" ]
}
```

With this configuration, Jest runs will by default output a `junit.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/jest-community/jest-junit?tab=readme-ov-file#jest-junit).

## Mocha

1. Install [`mocha-junit-reporter`](https://www.npmjs.com/package/mocha-junit-reporter).

```bash
$ npm install mocha-junit-reporter --save-dev
```

2. Run your tests.

```bash
$ mocha test --reporter mocha-junit-reporter
```

This will output a `test-results.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/michaelleeallen/mocha-junit-reporter?tab=readme-ov-file#usage).

## Playwright

Run the tests as follows:

```bash
$ PLAYWRIGHT_JUNIT_OUTPUT_NAME=test-results.xml npx playwright test --reporter=junit
```

This will output a `test-results.xml` file in the working directory. To further configure the reporter, consult the [Playwright documentation](https://playwright.dev/docs/test-reporters#junit-reporter).

## pytest

Run your tests as follows:

```bash
$ pytest --junitxml=junit_report.xml
```

This will output a `junit_report.xml` file in the working directory. To further configure the reporter, consult the [pytest documentation](https://docs.pytest.org/en/7.2.x/how-to/output.html#creating-junitxml-format-files).

## RSpec

1. Install [`rspec_junit_formatter`](https://rubygems.org/gems/rspec_junit_formatter/versions/0.2.3).

```bash
$ gem install rspec_junit_formatter
```

2. Run your tests.

```bash
$ rspec --format RspecJunitFormatter --out junit_report.xml
```

This will by output a `junit_report.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/sj26/rspec_junit_formatter?tab=readme-ov-file#usage).

## Cargo

1. Install [`cargo2junit`](https://crates.io/crates/cargo2junit).

```bash
$ cargo install cargo2junit
```

2. Run your tests.

```bash
$ cargo test -q -- -Z unstable-options --format json --report-time | cargo2junit > junit_report.xml
```

This will by output a `junit_report.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/johnterickson/cargo2junit).

## CTest

Run the tests as follows (CMake >= v3.21):

```bash
$ ctest --output-junit junit_report.xml
```

This will output a `junit_report.xml` file in the working directory. To further configure the reporter, consult the [CMake documentation](https://cmake.org/cmake/help/v3.21/manual/ctest.1.html).

## GTest

Run the tests with the following flag: `--gtest_output xml`

This will output a `test_detail.xml` file in the working directory. To further configure the reporter, consult the [GoogleTest documentation](https://google.github.io/googletest/advanced.html#generating-an-xml-report).
