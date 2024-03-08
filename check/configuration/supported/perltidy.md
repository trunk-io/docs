---
description: perltidy is a linter for Perl
title: Trunk | How to run perltidy
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

## Settings

**perltidy** uses the same config files as the
upstream [perltidy](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy) project, so you can continue to use any
existing configuration files (ex: `.perltidyrc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/perltidy) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [perltidy site](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy)
* perltidy Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/perltidy)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
