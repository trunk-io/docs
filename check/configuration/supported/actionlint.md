---
description: Explore our guide on Actionlint, the linter for Github Actions. Learn about its features, installation, and configuration.
title: Trunk | How to run Actionlint
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

# Actionlint

[**Actionlint**](https://github.com/rhysd/actionlint) is a linter for GitHub.

You can enable the Actionlint linter with:

```shell
trunk check enable actionlint
```

## Settings

**Actionlint** uses the same config files as the
upstream [Actionlint](https://github.com/rhysd/actionlint) project, so you can continue to use any
existing configuration files (ex: `.github/actionlint.yaml`, `.github/actionlint.yml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/actionlint) if your project does not already have one,
which you can see in our [open source plugins repo]().

**Note** that Actionlint is the **only** linter that  does not support moving the config files to `.trunk/configs`. They **must** be in the `.github` directory.



## Links

* [Actionlint site](https://github.com/rhysd/actionlint)
* Actionlint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/actionlint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
