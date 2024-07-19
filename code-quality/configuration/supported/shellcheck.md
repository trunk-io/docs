---
title: Trunk | How to run ShellCode Quality
description: >-
  ShellCode Quality is a static analysis tool designed to identify and report syntax
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

# ShellCode Quality

[**ShellCode Quality**](https://www.shellcheck.net/) is a linter for Bash.

You can enable the ShellCode Quality linter with:

```shell
trunk check enable shellcheck
```

![shellcheck example output](../../../check/configuration/supported/shellcheck.gif)

## Auto Enabling

ShellCode Quality will be auto-enabled if any _Shell_ files are present.

## Settings

ShellCode Quality supports the following config files:

* `.shellcheckrc`
* `shellcheckrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](../#moving-linter-configs) for more info. Trunk check provides a default `.shellcheckrc` if your project does not already have one.

## Links

* [ShellCheck site](https://www.shellcheck.net/)
* ShellCheck Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/shellcheck)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
