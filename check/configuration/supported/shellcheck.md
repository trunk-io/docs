---
description: ShellCheck is a static analysis tool designed to identify and report syntax errors and potential issues in shell scripts
title: Trunk | How to run ShellCheck
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

## Settings

**ShellCheck** uses the same config files as the
upstream [ShellCheck](https://www.shellcheck.net/) project, so you can continue to use any
existing configuration files (ex: `.shellcheckrc`, `shellcheckrc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/shellcheck) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [ShellCheck site](https://www.shellcheck.net/)
* ShellCheck Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/shellcheck)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
