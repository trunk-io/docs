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

### Introduction

Rust has built in support for unit tests using `cargo test`. Unfortunately `cargo test` does not support customizing output formats. Instead we suggest using **cargo-nextest.**

### How to output test results to upload to Trunk

In your `.config/nextest.toml` config file,  we recommend making a `ci` profile and setting the output format to `junit` for only that profile:

```toml
[profile.ci]
fail-fast = false

[profile.ci.junit]
path = "junit.xml"
```

The default profile will use standard text output. See full docs for configuring nextest [here](https://nexte.st/docs/configuration/).

In CI, run tests with the `--profile=ci` argument:

```bash
cargo nextest run --profile=ci
```

### Deficiencies

Currently, nextest does not support filenames and lines for test results. Trunk will show this information when available; however, uploading the nextest results will not contain this information.

### Next Step

Once you've configured your test runner to output JUnit XML, you're ready to modify your CI test jobs to actually upload test results to Trunk. See [ci-providers](../ci-providers/ "mention") for instructions to do this for the CI system you use.
