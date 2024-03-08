---
description: djlint is a linter for HTML Templates
title: Trunk | How to run djlint
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

## Settings

**djlint** uses the same config files as the
upstream [djlint](https://github.com/Riverside-Healthcare/djlint#readme) project, so you can continue to use any
existing configuration files (ex: `.djlintrc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/djlint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [djlint site](https://github.com/Riverside-Healthcare/djlint#readme)
* djlint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/djlint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
