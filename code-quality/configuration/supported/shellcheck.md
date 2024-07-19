---
title: Trunk | How to run ShellCheck
description: >-
  ShellCheck is a static analysis tool designed to identify and report syntax
  errors and potential issues in shell scripts
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

# ShellCheck

[**ShellCheck**](https://www.shellcheck.net/) is a linter for Bash.

You can enable the ShellCheck linter with:

```shell
trunk check enable shellcheck
```

![shellcheck example output](../../../check/configuration/supported/shellcheck.gif)

## Auto Enabling

ShellCheck will be auto-enabled if any _Shell_ files are present.

## Settings

ShellCheck supports the following config files:

* `.shellcheckrc`
* `shellcheckrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](../#moving-linter-configs) for more info. Trunk check provides a default `.shellcheckrc` if your project does not already have one.

## Links

* [ShellCheck site](https://www.shellcheck.net/)
* ShellCheck Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/shellcheck)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
