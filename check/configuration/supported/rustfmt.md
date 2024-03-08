---
description: A tool for formatting Rust code according to style guidelines.
title: Trunk | How to run rustfmt
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

# rustfmt

**rustfmt** is a formatter for Rust.

You can enable the rustfmt plugin with

```shell
trunk check enable rustfmt
```

## Settings


**rustfmt** uses the same config files as the
upstream [rustfmt](https://github.com/rust-lang/rustfmt) project, so you can continue to use any
existing configuration files (ex: `rustfmt.toml`, `.rustfmt.toml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rustfmt) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

We currently use the version of `rustfmt` packaged with rust, so for `rustfmt` version, specify your Rust version (for example `rustfmt@1.61.0`).

If you have `edition` in your `cargo.toml`, `rustfmt` also needs the same information in `.rustfmt.toml` in your repo root. For example, your `.rustfmt.toml` might contain:

```toml
edition = "2021"
```
