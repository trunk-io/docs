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

## Auto Enabling

rubocop will be auto-enabled if a `.rubocop.yml` config file is present.

## Settings

rubocop supports the following config files:
* `.rubocop.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [rubocop site](https://github.com/rubocop/rubocop#readme)
- rubocop Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/rubocop)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
