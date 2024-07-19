---
title: Trunk | How to run buildifier
description: buildifier is a linter for Bazel, Starlark
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

![buildifier example output](../../../check/configuration/supported/buildifier.gif)

## Auto Enabling

buildifier will be auto-enabled if any _Bazel or Starlark_ files are present.

## Settings

buildifier supports the following config files:

* `.buildifier.json`
* `.buildifier-tables.json`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](../#moving-linter-configs) for more info.

## Links

* [buildifier site](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md)
* buildifier Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buildifier)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
