---
description:  Learn how to install, configure, and use buildifier effectively for Bazel build scripts.
title: Trunk | How to run Buildifier
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

# Buildifier

[**Buildifier**](https://github.com/rhysd/actionlint) is a linter for Bazel, Starlark.

You can enable the Buildifier linter with:

```shell
trunk check enable buildifier
```
![buildifier example output](/.gitbook/assets/buildifier.gif)
## Auto Enabling

Buildifier will be auto-enabled if any *Bazel or Starlark* files are present.

## Settings

Buildifier supports the following config files:
* `.buildifier.json`
* `.buildifier-tables.json`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [Buildifier site](https://github.com/rhysd/actionlint)
- Buildifier Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/buildifier)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
