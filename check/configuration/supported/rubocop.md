---
description: rubocop is a linter for Ruby
title: Trunk | How to run rubocop
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

# rubocop

[**rubocop**](https://github.com/rubocop/rubocop#readme) is a linter for Ruby.

You can enable the rubocop linter with:

```shell
trunk check enable rubocop
```

## Settings

**rubocop** uses the same config files as the
upstream [rubocop](https://github.com/rubocop/rubocop#readme) project, so you can continue to use any
existing configuration files (ex: `.rubocop.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rubocop) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [rubocop site](https://github.com/rubocop/rubocop#readme)
* rubocop Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rubocop)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
