---
title: Trunk | How to run djlint
description: djlint is a linter for HTML Templates
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

# djlint

[**djlint**](https://github.com/Riverside-Healthcare/djlint#readme) is a linter for HTML Templates.

You can enable the djlint linter with:

```shell
trunk check enable djlint
```

## Auto Enabling

djlint will be auto-enabled if a `.djlintrc` config file is present.

## Settings

djlint supports the following config files:

* `.djlintrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `.djlintrc` if your project does not already have one.

## Links

* [djlint site](https://github.com/Riverside-Healthcare/djlint#readme)
* djlint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/djlint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
