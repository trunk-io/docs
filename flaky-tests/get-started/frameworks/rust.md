---
title: Configuring cargo-nextest
description: A guide for generating JUnit test reports for Rust tests
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Rust

## 1. Generate JUnit

Use `cargo-nextest` to run your Rust tests and output JUnit reports. Add this to your nextest configuration:

```toml
[profile.ci.junit]
path = "junit.xml"
```

Run your tests with `cargo-nextest` specifying  `--profile ci` to generate JUnit test reports.

```
cargo nextest run --profile ci
```

## 2. Output Location

When using a profile with JUnit support configured, a JUnit report will be written out to `target/nextest/ci/junit.xml` within the workspace root.

## Next Step

JUnit files generated with `cargo-nextest` are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.