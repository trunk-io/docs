---
description: perlcritic is a linter for Perl
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

# perlcritic

**perlcritic** is a linter for Perl.

You can enable the perlcritic plugin with

```shell
trunk check enable perlcritic
```

## Settings


perlcritic uses the same config files as the
upstream [perlcritic](https://metacpan.org/pod/Perl::Critic) project, so you can continue to use any
existing configuration files (ex: `.perlcriticrc`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/perlcritic) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
