---
description: phpstan is a linter for PHP
title: Trunk | How to run phpstan
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

# phpstan

[**phpstan**](https://phpstan.org/) is a linter for PHP.

You can enable the phpstan linter with:

```shell
trunk check enable phpstan
```

## Auto Enabling

phpstan will never be auto-enabled. It must be enabled manually.

## Settings

phpstan supports the following config files:
* `phpstan.neon`
* `phpstan.neon.dist`
* `phpstan.dist.neon`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [phpstan site](https://phpstan.org/)
- phpstan Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/phpstan)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
