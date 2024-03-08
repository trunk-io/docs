---
description: Clang Format is a set of tools to format code that is processed by the Clang compiler suite.


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

# ClangFormat

**ClangFormat** is a formatter for Protobuf and C, C++.

You can enable the ClangFormat plugin with

```shell
trunk check enable clang-format
```

## Settings


ClangFormat uses the same config files as the
upstream [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) project, so you can continue to use any
existing configuration files (ex: `.clang-format`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/clang-format) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

By default, Trunk uses Clang-format to additionally format `.proto` files. However, for this to work, you need to have told `clang-format` to do so in your `.clang-format` config file. You can do that by adding the following to the end of your `.clang-format file`:

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
