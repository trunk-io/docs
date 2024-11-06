---
title: Configuring cargo-nextest
description: a test runner for Rust
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

# Cargo-nextest

Cargo-nextest is a testing framework for Rust.

### Enabling XML Output

Rust has built in support for unit tests using `cargo test`.  Unfortunately `cargo test` does not support customizing output formats (though there is [experimental support for JSON output](https://doc.rust-lang.org/beta/test/enum.OutputFormat.html)). Instead we suggest using **cargo-nextest.**

[cargo-nextest](https://nexte.st/) is an alternative test runner for Rust which, among other cool features, supports XML and JSON output. Install **cargo-nextest** as either a [pre-built binary](https://nexte.st/book/installation) like this:

```shell
curl -LsSf https://get.nexte.st/latest/linux | tar zxf - -C ${CARGO_HOME:-~/.cargo}/bin
```
or [install and compile](https://nexte.st/book/installing-from-source) from source.

Next add a `.config/nextest.toml`  config file to tell **cargo-nextest** what output format to use and where the output should be written too, among other settings. Something like this:

```toml
[profile.ci]
fail-fast = false

[profile.ci.junit]
path = "junit.xml"
```
The `default` profile will use standard text output. The `ci` profile will use JUnit XML output.

Now run the tests with: 

```shell
cargo nextest run --profile=ci
```

### Test Suite Naming

You can change the name of the report with the `report-name` option.  Nextest will use the test binary names for the `<testsuite>` and the individual test names for the `<testcase>`. However, Nextest does not currently support adding the filepaths and names.

## Further Information

See an example of **cargo-nextest** invoked form a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/rust-tests.yaml).

[Documentation](https://nexte.st/book/configuration) for the `cargo-nextest` config file.
