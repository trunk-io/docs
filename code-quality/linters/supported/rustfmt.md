---
description: Rustfmt is a code formatting tool for Rust that helps ensure your code adheres to the community-driven coding standards and style guidelines.

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

[**rustfmt**](https://github.com/rust-lang/rustfmt) is a formatter for Rust.

You can enable the rustfmt formatter with:

```shell
trunk check enable rustfmt
```

## Auto Enabling

rustfmt will be auto-enabled if any *Rust* files are present.

## Settings

rustfmt supports the following config files:
* `rustfmt.toml`
* `.rustfmt.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.
Trunk Code Quality provides a default `.rustfmt.toml` if your project does not already have one.

## Usage Notes

We currently use the version of `rustfmt` packaged with rust, so for `rustfmt` version, specify your Rust version (for example `rustfmt@1.61.0`).

If you have `edition` in your `cargo.toml`, `rustfmt` also needs the same information in `.rustfmt.toml` in your repo root. For example, your `.rustfmt.toml` might contain:

```toml
edition = "2021"
```


## Links

- [rustfmt site](https://github.com/rust-lang/rustfmt)
- rustfmt Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rustfmt)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
