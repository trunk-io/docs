---
description: clang-format is a linter for Protobuf and C, C++
title: Trunk | How to run clang-format
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

# clang-format

[**clang-format**](https://clang.llvm.org/docs/ClangFormat.html) is a linter for Protobuf and C, C++.

You can enable the clang-format linter with:

```shell
trunk check enable clang-format
```

## Auto Enabling

clang-format will be auto-enabled if a `.clang-format` config file is present.

## Settings

clang-format supports the following config files:
* `.clang-format`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [clang-format site](https://clang.llvm.org/docs/ClangFormat.html)
- clang-format Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/clang-format)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
