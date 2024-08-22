---
description: >-
  Bandit is a security linter for Python codebases. Bandit flags problems like
  hard-coded passwords, injection vulnerabilities, and the use of insecure
  libraries.
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

# Bandit

[**Bandit**](https://github.com/PyCQA/bandit) is a linter for Python.

You can enable the Bandit linter with:

```shell
trunk check enable bandit
```

![bandit example output](../../configuration/supported/bandit.gif)

## Auto Enabling

Bandit will be auto-enabled if any _Python_ files are present.

## Settings

Bandit supports the following config files:

* `.bandit`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [Bandit site](https://github.com/PyCQA/bandit)
* Bandit Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/bandit)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
