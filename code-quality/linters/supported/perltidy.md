---
title: Trunk | How to run perltidy
description: perltidy is a linter for Perl
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

# perltidy

[**perltidy**](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy) is a linter for Perl.

You can enable the perltidy linter with:

```shell
trunk check enable perltidy
```

## Auto Enabling

perltidy will be auto-enabled if a `.perltidyrc` config file is present.

## Settings

perltidy supports the following config files:

* `.perltidyrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `.perltidyrc` if your project does not already have one.

## Links

* [perltidy site](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy)
* perltidy Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/perltidy)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
