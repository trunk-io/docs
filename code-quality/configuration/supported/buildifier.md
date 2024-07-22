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

[**buildifier**](https://github.com/bazelbuild/buildtools/blob/master/buildifier/readme.md) is a linter for Bazel, Starlark.

You can enable the buildifier linter with:

```shell
trunk check enable buildifier
```
![buildifier example output](./buildifier.gif)
## Auto Enabling

buildifier will be auto-enabled if any *Bazel or Starlark* files are present.

## Settings

buildifier supports the following config files:
* `.buildifier.json`
* `.buildifier-tables.json`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [buildifier site](https://github.com/bazelbuild/buildtools/blob/master/buildifier/readme.md)
- buildifier Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buildifier)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
