---
description: perltidy is a linter for Perl
---

**perltidy** is a linter for Perl.

You can enable the perltidy plugin with

```shell
trunk check enable perltidy
```

# Settings

perltidy uses the same config files as the
upstream [perltidy](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy) project, so you can continue to use any
existing configuration files (ex: `.perltidyrc`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/perltidy) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
