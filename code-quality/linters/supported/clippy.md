---
description: A collection of lints to catch common mistakes and improve your Rust code.
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

# Clippy

[**Clippy**](https://doc.rust-lang.org/clippy/) is a linter for Rust.

You can enable the Clippy linter with:

```shell
trunk check enable clippy
```

## Auto Enabling

Clippy will be auto-enabled if any _Rust_ files are present.

## Settings

Clippy supports the following config files:

* `clippy.toml`
* `.clippy.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Usage Notes

Clippy is distributed with rust itself, so specify your rust version for your clippy version (for example `clippy@1.61.0`).

## Links

* [Clippy site](https://doc.rust-lang.org/clippy/)
* Clippy Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/clippy)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
