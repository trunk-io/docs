---
description: A collection of lints to catch common mistakes and improve your Rust code.
---

**Clippy** is a linter for Rust.

You can enable the Clippy plugin with

```shell
trunk check enable clippy
```

# Settings

Clippy uses the same config files as the 
upstream [Clippy](https://doc.rust-lang.org/clippy/) project, so you can continue to use any
existing configuration files (ex: `clippy.toml`, `.clippy.toml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/clippy) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
Clippy is distributed with rust itself, so specify your rust version for your clippy version (for example `clippy@1.61.0`).



