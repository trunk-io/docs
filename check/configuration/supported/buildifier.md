---
description: buildifier is a linter for Bazel, Starlark
title: Trunk | How to run buildifier
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

# buildifier

[**buildifier**](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md) is a linter for Bazel, Starlark.

You can enable the buildifier linter with:

```shell
trunk check enable buildifier
```

## Settings

**buildifier** uses the same config files as the
upstream [buildifier](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md) project, so you can continue to use any
existing configuration files (ex: `.buildifier.json`, `.buildifier-tables.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/buildifier) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [buildifier site](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md)
* buildifier Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buildifier)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
