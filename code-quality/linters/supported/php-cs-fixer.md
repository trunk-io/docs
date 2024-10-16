---
description: php-cs-fixer is a linter for PHP
title: Trunk | How to run php-cs-fixer
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

# php-cs-fixer

[**php-cs-fixer**](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer) is a linter for PHP.

You can enable the php-cs-fixer linter with:

```shell
trunk check enable php-cs-fixer
```

## Auto Enabling

php-cs-fixer will be auto-enabled if a `.php-cs-fixer.dist.php` config file is present.

## Settings

php-cs-fixer supports the following config files:
* `.php-cs-fixer.dist.php`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [php-cs-fixer site](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer)
- php-cs-fixer Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/php-cs-fixer)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
