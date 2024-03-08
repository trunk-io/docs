---
description: A collection of lints to catch common mistakes and improve your Rust code.
title: Trunk | How to run Clippy
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

## Settings

**Clippy** uses the same config files as the
upstream [Clippy](https://doc.rust-lang.org/clippy/) project, so you can continue to use any
existing configuration files (ex: `clippy.toml`, `.clippy.toml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/clippy) if your project does not already have one,
which you can see in our [open source plugins repo]().

Clippy is distributed with rust itself, so specify your rust version for your clippy version (for example `clippy@1.61.0`).





## Links

* [Clippy site](https://doc.rust-lang.org/clippy/)
* Clippy Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/clippy)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
