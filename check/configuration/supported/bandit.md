---
description: Bandit is a security linter for Python codebases. Bandit flags problems like hard-coded passwords, injection vulnerabilities, and the use of insecure libraries.
title: Trunk | How to run Bandit
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

## Settings

**Bandit** uses the same config files as the
upstream [Bandit](https://github.com/PyCQA/bandit) project, so you can continue to use any
existing configuration files (ex: `.bandit`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/bandit) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [Bandit site](https://github.com/PyCQA/bandit)
* Bandit Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/bandit)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
