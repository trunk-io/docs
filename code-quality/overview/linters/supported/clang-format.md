---
title: Trunk | How to run ClangFormat
description: >-
  Clang Format is a set of tools to format code that is processed by the Clang
  compiler suite.
---

# ClangFormat

[**ClangFormat**](https://clang.llvm.org/docs/ClangFormat.html) is a formatter for Protobuf and C, C++.

You can enable the ClangFormat formatter with:

```shell
trunk check enable clang-format
```

## Auto Enabling

ClangFormat will be auto-enabled if a `.clang-format` config file is present.

## Settings

ClangFormat supports the following config files:

* `.clang-format`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Usage Notes

By default, Trunk uses ClangFormat to additionally format `.proto` files. However, for this to work, you need to have told `clang-format` to do so in your `.clang-format` config file. You can do that by adding the following to the end of your `.clang-format file`:

```yaml
---
Language: Proto
```

For example, you might have this for your entire `.clang-format` file:

```yaml
BasedOnStyle: Google
ColumnLimit: 100
---
Language: Cpp
DerivePointerAlignment: false
---
Language: Proto
```

## Links

* [ClangFormat site](https://clang.llvm.org/docs/ClangFormat.html)
* ClangFormat Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/clang-format)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
