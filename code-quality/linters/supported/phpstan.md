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

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [phpstan site](https://phpstan.org/)
- phpstan Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/phpstan)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
